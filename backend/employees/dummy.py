class EmployeeCreate(BaseModel):
    employeeCode: str
    firstName: str
    middleName: Optional[str] = None
    lastName: str
    fatherName: Optional[str] = None
    motherName: Optional[str] = None
    dob: Optional[str] = None
    gender: Optional[str] = None
    maritalStatus: Optional[str] = None
    spouseName: Optional[str] = None
    email: str
    phone: str
    mobileHome: Optional[str] = None
    position: str
    department: str
    hireDate: str
    salary: float
    status: str = "active"
    certifications: Optional[str] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    bloodGroup: Optional[str] = None
    identificationMark: Optional[str] = None
    shirtSize: Optional[str] = None
    trouserSize: Optional[float] = None
    shoeSize: Optional[float] = None
    presentStreet: Optional[str] = None
    presentState: Optional[str] = None
    presentCity: Optional[str] = None
    presentZip: Optional[str] = None
    permanentStreet: Optional[str] = None
    permanentState: Optional[str] = None
    permanentCity: Optional[str] = None
    permanentZip: Optional[str] = None
    bankAccountNumber: Optional[str] = None
    bankName: Optional[str] = None
    branchName: Optional[str] = None
    ifscCode: Optional[str] = None
    aadharNumber: Optional[str] = None
    panNumber: Optional[str] = None
    uanNumber: Optional[str] = None
    esicIPNumber: Optional[str] = None
    
    pfNumber: Optional[str] = None
    salaryDetails: Optional[str] = None
    documents: Optional[str] = None


class EmployeeUpdate(BaseModel):
    employeeCode: Optional[str] = None
    firstName: Optional[str] = None
    middleName: Optional[str] = None
    lastName: Optional[str] = None
    fatherName: Optional[str] = None
    motherName: Optional[str] = None
    dob: Optional[str] = None
    gender: Optional[str] = None
    maritalStatus: Optional[str] = None
    spouseName: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    mobileHome: Optional[str] = None
    position: Optional[str] = None
    department: Optional[str] = None
    hireDate: Optional[str] = None
    salary: Optional[float] = None
    status: Optional[str] = None
    certifications: Optional[str] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    bloodGroup: Optional[str] = None
    identificationMark: Optional[str] = None
    shirtSize: Optional[str] = None
    trouserSize: Optional[float] = None
    shoeSize: Optional[float] = None
    presentStreet: Optional[str] = None
    presentState: Optional[str] = None
    presentCity: Optional[str] = None
    presentZip: Optional[str] = None
    permanentStreet: Optional[str] = None
    permanentState: Optional[str] = None
    permanentCity: Optional[str] = None
    permanentZip: Optional[str] = None
    bankAccountNumber: Optional[str] = None
    bankName: Optional[str] = None
    branchName: Optional[str] = None
    ifscCode: Optional[str] = None
    aadharNumber: Optional[str] = None
    panNumber: Optional[str] = None
    uanNumber: Optional[str] = None
    esicIPNumber: Optional[str] = None
    pfNumber: Optional[str] = None
    salaryDetails: Optional[str] = None
    documents: Optional[str] = None