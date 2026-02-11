from django.db import models
from django.utils.text import slugify
# Create your models here.
class Client(models.Model):
    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]

    company_name = models.CharField(max_length=255)
    client_code = models.CharField(max_length=100, unique=True)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True, null=True)

    # Address
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    gstin = models.CharField(max_length=50, blank=True, null=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="Active"
    )

    contractStartDate = models.DateTimeField(blank=True, null=True) 
    contractEndDate = models.DateTimeField(blank=True, null=True) 

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} ({self.client_code})"


class DepartmentContact(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name or "Department Contact"


class ClientUnit(models.Model):
    client = models.ForeignKey(
        Client,
        related_name="units",
        on_delete=models.CASCADE
    )

    # Identification
    unit_name = models.CharField(max_length=255)
    unit_code = models.CharField(max_length=100)
    old_unit_code = models.CharField(max_length=100, blank=True, null=True)
    print_name = models.CharField(max_length=255, blank=True, null=True)
    billing_name = models.CharField(max_length=255, blank=True, null=True)

    # Addresses
    shipping_address = models.TextField(blank=True, null=True)
    billing_address = models.TextField(blank=True, null=True)
    billing_from_state = models.CharField(max_length=100, blank=True, null=True)
    billing_to_state = models.CharField(max_length=100, blank=True, null=True)
    place_of_supply = models.CharField(max_length=255, blank=True, null=True)
    place_of_supply_address = models.TextField(blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    pin_code = models.CharField(max_length=20, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    gstin = models.CharField(max_length=50, blank=True, null=True)
    state_office = models.CharField(max_length=255, blank=True, null=True)
    field_area = models.CharField(max_length=255, blank=True, null=True)

    # Contact & Communication
    attention = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    # Agreement & Work Order
    work_order_no = models.CharField(max_length=100, blank=True, null=True)
    work_order_date = models.DateField(blank=True, null=True)
    work_start_date = models.DateField(blank=True, null=True)
    work_completion_date = models.DateField(blank=True, null=True)
    agreement_no = models.CharField(max_length=100, blank=True, null=True)
    agreement_date = models.DateField(blank=True, null=True)
    agreement_exp_date = models.DateField(blank=True, null=True)
    renewal_letter_date = models.DateField(blank=True, null=True)

    # Employee Setup
    no_of_employees = models.IntegerField(blank=True, null=True)
    min_age = models.IntegerField(blank=True, null=True)
    max_age = models.IntegerField(blank=True, null=True)
    leave_opening = models.IntegerField(blank=True, null=True)
    show_leave_on_pay_slip = models.BooleanField(default=False)
    is_uniform_free = models.BooleanField(default=False)
    bonus_paid_in_month = models.CharField(max_length=50, blank=True, null=True)

    # Department Contacts
    accounts_officer = models.OneToOneField(
        DepartmentContact,
        related_name="accounts_for",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    operation_department = models.OneToOneField(
        DepartmentContact,
        related_name="operations_for",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    # Statutory & Compliance
    pan_card_no = models.CharField(max_length=50, blank=True, null=True)
    tan_no = models.CharField(max_length=50, blank=True, null=True)
    tin_no = models.CharField(max_length=50, blank=True, null=True)
    service_tax_no = models.CharField(max_length=50, blank=True, null=True)
    pf_code = models.CharField(max_length=50, blank=True, null=True)
    esic_code = models.CharField(max_length=50, blank=True, null=True)
    professional_tax_reg_no = models.CharField(max_length=50, blank=True, null=True)
    roc = models.CharField(max_length=100, blank=True, null=True)
    wages_revision = models.CharField(max_length=100, blank=True, null=True)
    controller = models.CharField(max_length=100, blank=True, null=True)
    salary_transferred_by = models.CharField(max_length=100, blank=True, null=True)
    gst_category = models.CharField(max_length=100, blank=True, null=True)
    vendor_code = models.CharField(max_length=100, blank=True, null=True)

    # Billing Configuration
    bill_type = models.CharField(max_length=50, blank=True, null=True)
    bill_generate_type = models.CharField(max_length=50, blank=True, null=True)
    print_format = models.CharField(max_length=50, blank=True, null=True)
    bank = models.CharField(max_length=255, blank=True, null=True)
    is_gst_applicable = models.BooleanField(default=True)
    is_igst_applicable = models.BooleanField(default=False)
    is_union_territory = models.BooleanField(default=False)
    system_billing = models.BooleanField(default=False)
    billing_in_decimal = models.BooleanField(default=False)
    contract_period_shown = models.CharField(max_length=100, blank=True, null=True)

    # Misc
    remarks = models.TextField(blank=True, null=True)
    nature_of_service = models.CharField(max_length=255, blank=True, null=True)
    rate_structure = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        # First save to generate ID (only for new objects)
        super().save(*args, **kwargs)

        new_code = f"{self.client.client_code}-{slugify(self.unit_name)}-{self.id}".upper()

        # If updating and code changed → store old code
        if not is_new:
            old_obj = ClientUnit.objects.get(pk=self.pk)
            if old_obj.unit_code and old_obj.unit_code != new_code:
                self.old_unit_code = old_obj.unit_code

        # Update only if changed (avoid infinite loop)
        if self.unit_code != new_code:
            self.unit_code = new_code
            super().save(update_fields=["unit_code", "old_unit_code"])
    def __str__(self):
        return f"{self.unit_name} ({self.unit_code})"