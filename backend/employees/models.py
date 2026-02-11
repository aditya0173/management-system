from django.db import models

class Gender(models.TextChoices):
    MALE="Male"
    FEMALE="Female"
    OTHERS="Others"

# Create your models here.
class Employees(models.Model):
    employeeCode = models.CharField(max_length=250)

    # Personal Details 
    firstName = models.CharField(max_length=250)
    middleName = models.CharField(max_length=250, null=True, blank=True)
    lastName = models.CharField(max_length=250)
    fatherName = models.CharField(max_length=250, null=True, blank=True)
    motherName = models.CharField(max_length=250, null=True, blank=True)
    dob = models.DateTimeField()
    gender = models.CharField(choices=Gender,)
    maritalStatus = models.BooleanField(default=True)
    spouseName = models.CharField(max_length=250, null=True, blank=True)

    # Contacts Details
    email = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50)
    mobileHome = models.CharField(max_length=50, null=True, blank=True)

    # Employeement Details
    position = models.CharField(max_length=250, null=True, blank=True)
    department = models.CharField(max_length=250, null=True, blank=True)
    hireDate = models.DateField()
    salary = models.DecimalField(max_digits=10,decimal_places=2)

    # Models Property Feilds
    is_active = models.BooleanField(default=True)

    # Physical Details
    height = models.CharField(max_length=250, null=True, blank=True)
    weight = models.CharField(max_length=250, null=True, blank=True)
    bloodGroup = models.CharField(max_length=250, null=True, blank=True)
    identificationMark = models.CharField(max_length=250, null=True, blank=True)
    shirtSize = models.CharField(max_length=250, null=True, blank=True)
    trouserSize = models.CharField(max_length=250, null=True, blank=True)
    shoeSize = models.CharField(max_length=250, null=True, blank=True)

    # Present Address
    presentStreet = models.CharField(max_length=250, null=True, blank=True)
    presentState = models.CharField(max_length=250, null=True, blank=True)
    presentCity = models.CharField(max_length=250, null=True, blank=True)
    presentCity = models.CharField(max_length=250, null=True, blank=True)
    # Permanent Address
    permanentStreet = models.CharField(max_length=250, null=True, blank=True)
    permanentState = models.CharField(max_length=250, null=True, blank=True)
    permanentCity = models.CharField(max_length=250, null=True, blank=True)
    permanentCity = models.CharField(max_length=250, null=True, blank=True)
    
    # Documnets Fields
    certifications = models.CharField(max_length=250, null=True, blank=True)
    bankAccountNumber = models.CharField(max_length=250, null=True, blank=True)
    branchName = models.CharField(max_length=250, null=True, blank=True)
    ifscCode = models.CharField(max_length=250, null=True, blank=True)
    aadharNumber = models.CharField(max_length=250, null=True, blank=True)
    panNumber = models.CharField(max_length=250, null=True, blank=True)
    uanNumber = models.CharField(max_length=250, null=True, blank=True)
    esicIPNumber = models.CharField(max_length=250, null=True, blank=True)
    pfNumbe = models.CharField(max_length=250, null=True, blank=True)
    salaryDetails = models.CharField(max_length=250, null=True, blank=True)
    documents = models.CharField(max_length=250, null=True, blank=True)



