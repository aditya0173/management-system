from rest_framework import serializers
from .models import Client, ClientUnit, DepartmentContact



class DepartmentContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentContact
        fields = "__all__"


class ClientUnitSerializer(serializers.ModelSerializer):
    accounts_officer = DepartmentContactSerializer(required=False, allow_null=True)
    operation_department = DepartmentContactSerializer(required=False, allow_null=True)

    class Meta:
        model = ClientUnit
        exclude = ("client",)

    def create(self, validated_data):
        accounts_data = validated_data.pop("accounts_officer", None)
        operation_data = validated_data.pop("operation_department", None)

        accounts = (
            DepartmentContact.objects.create(**accounts_data)
            if accounts_data else None
        )
        operations = (
            DepartmentContact.objects.create(**operation_data)
            if operation_data else None
        )

        return ClientUnit.objects.create(
            accounts_officer=accounts,
            operation_department=operations,
            **validated_data
        )

    def update(self, instance, validated_data):
        for contact_field in ["accounts_officer", "operation_department"]:
            contact_data = validated_data.pop(contact_field, None)
            contact_instance = getattr(instance, contact_field)

            if contact_data:
                if contact_instance:
                    for attr, value in contact_data.items():
                        setattr(contact_instance, attr, value)
                    contact_instance.save()
                else:
                    setattr(
                        instance,
                        contact_field,
                        DepartmentContact.objects.create(**contact_data)
                    )

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance



class ClientSerializer(serializers.ModelSerializer):
    units = ClientUnitSerializer(many=True)

    class Meta:
        model = Client
        fields = "__all__"

    def create(self, validated_data):
        units_data = validated_data.pop("units", [])

        client = Client.objects.create(**validated_data)

        for unit_data in units_data:
            serializer = ClientUnitSerializer(data=unit_data)
            serializer.is_valid(raise_exception=True)
            serializer.save(client=client)

        return client

    def update(self, instance, validated_data):
        units_data = validated_data.pop("units", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if units_data is not None:
            instance.units.all().delete()
            for unit_data in units_data:
                serializer = ClientUnitSerializer(data=unit_data)
                serializer.is_valid(raise_exception=True)
                serializer.save(client=instance)

        return instance
