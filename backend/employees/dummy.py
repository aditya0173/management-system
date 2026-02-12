# ──────────────────────────────────── Unit ──────────────────────────────────────────────────────────────────────
class UnitCreate(BaseModel):
    unitName: str
    unitCode: str
    clientName: str
    stateOffice: Optional[str] = None
    billingGstin: Optional[str] = None
    placeOfSupply: Optional[str] = None

    # Basic Details
    country: Optional[str] = None
    siteAt: Optional[str] = None
    phone: Optional[str] = None
    noOfEmp: Optional[int] = None
    workStartDate: Optional[str] = None
    agrExpDate: Optional[str] = None
    openingBalance: Optional[float] = None
    panCardNo: Optional[str] = None
    roc: Optional[str] = None
    controller: Optional[str] = None
    # Status
    status: str = "active"
    statusReason: Optional[str] = None
    # Configuration
    executiveKds: Optional[str] = None
    employeeMinAge: Optional[int] = None
    employeeMaxAge: Optional[int] = None
    leaveOpening: Optional[int] = None
    showLeaveOnPaySlip: Optional[bool] = None
    foUsers: Optional[str] = None
    # Additional Details
    oldUnitCode: Optional[str] = None
    attention: Optional[str] = None
    addressShippedTo: Optional[str] = None
    billingToState: Optional[str] = None
    district: Optional[str] = None
    placeOfSupplyAddress: Optional[str] = None
    fieldArea: Optional[str] = None
    fax: Optional[str] = None
    workOrderNo: Optional[str] = None
    agrNo: Optional[str] = None
    contactName: Optional[str] = None
    email: Optional[str] = None
    serviceTaxNo: Optional[str] = None
    tinNo: Optional[str] = None
    wagesRevision: Optional[str] = None
    salaryTransferredBy: Optional[str] = None
    # Toggles (stored as JSON strings if complex, or simple types)
    clientService: Optional[str] = None # JSON string
    isTenderUnit: Optional[bool] = None
    isEventUnit: Optional[bool] = None
    bonusPaidInMonth: Optional[str] = None
    gstCategory: Optional[str] = None
    vendorCode: Optional[str] = None
    # Billing Details
    printNameBilledTo: Optional[str] = None
    printAddressBilledTo: Optional[str] = None
    state: Optional[str] = None
    billingFromState: Optional[str] = None
    pinCode: Optional[str] = None
    workOrderDate: Optional[str] = None
    agrDate: Optional[str] = None
    # Contact Persons (stored as JSON string)
    accountsOfficer: Optional[str] = None 
    operationDept: Optional[str] = None
    # Bill Terms
    billType: Optional[str] = None
    billGenerateType: Optional[str] = None
    printFormat: Optional[str] = None
    bank: Optional[str] = None
    billNotCreateForThisUnit: Optional[bool] = None
    gstApplicable: Optional[bool] = None
    igstApplicable: Optional[bool] = None
    unionTerritory: Optional[bool] = None
    systemBilling: Optional[bool] = None
    isBillingInDecimal: Optional[bool] = None
    contractPeriodShown: Optional[str] = None
    # Codes
    pfCode: Optional[str] = None
    esicCode: Optional[str] = None
    supplyTypeCode: Optional[str] = None
class UnitUpdate(BaseModel):
    unitCode: Optional[str] = None
    unitName: Optional[str] = None
    clientName: Optional[str] = None
    # Basic Details
    stateOffice: Optional[str] = None
    country: Optional[str] = None
    billingGstin: Optional[str] = None
    placeOfSupply: Optional[str] = None
    siteAt: Optional[str] = None
    phone: Optional[str] = None
    noOfEmp: Optional[int] = None
    workStartDate: Optional[str] = None
    agrExpDate: Optional[str] = None
    openingBalance: Optional[float] = None
    panCardNo: Optional[str] = None
    roc: Optional[str] = None
    controller: Optional[str] = None
    # Status
    status: Optional[str] = None
    statusReason: Optional[str] = None
    # Configuration
    executiveKds: Optional[str] = None
    employeeMinAge: Optional[int] = None
    employeeMaxAge: Optional[int] = None
    leaveOpening: Optional[int] = None
    showLeaveOnPaySlip: Optional[bool] = None
    foUsers: Optional[str] = None
    # Additional Details
    oldUnitCode: Optional[str] = None
    attention: Optional[str] = None
    addressShippedTo: Optional[str] = None
    billingToState: Optional[str] = None
    district: Optional[str] = None
    placeOfSupplyAddress: Optional[str] = None
    fieldArea: Optional[str] = None
    fax: Optional[str] = None
    workOrderNo: Optional[str] = None
    agrNo: Optional[str] = None
    contactName: Optional[str] = None
    email: Optional[str] = None
    serviceTaxNo: Optional[str] = None
    tinNo: Optional[str] = None
    wagesRevision: Optional[str] = None
    salaryTransferredBy: Optional[str] = None
    # Toggles
    clientService: Optional[str] = None
    isTenderUnit: Optional[bool] = None
    isEventUnit: Optional[bool] = None
    bonusPaidInMonth: Optional[str] = None
    gstCategory: Optional[str] = None
    vendorCode: Optional[str] = None
    # Billing Details
    printNameBilledTo: Optional[str] = None
    printAddressBilledTo: Optional[str] = None
    state: Optional[str] = None
    billingFromState: Optional[str] = None
    pinCode: Optional[str] = None
    workOrderDate: Optional[str] = None
    agrDate: Optional[str] = None
    # Contact Persons
    accountsOfficer: Optional[str] = None 
    operationDept: Optional[str] = None
    # Bill Terms
    billType: Optional[str] = None
    billGenerateType: Optional[str] = None
    printFormat: Optional[str] = None
    bank: Optional[str] = None
    billNotCreateForThisUnit: Optional[bool] = None
    gstApplicable: Optional[bool] = None
    igstApplicable: Optional[bool] = None
    unionTerritory: Optional[bool] = None
    systemBilling: Optional[bool] = None
    isBillingInDecimal: Optional[bool] = None
    contractPeriodShown: Optional[str] = None
    # Codes
    pfCode: Optional[str] = None
    esicCode: Optional[str] = None
    supplyTypeCode: Optional[str] = None
# ─── BillReport ────────────────────────────────────────────────────────────────
# ─── Bill Rate ────────────────────────────────────────────────────────────────
class BillRateCreate(BaseModel):
    # Header Details
    branch: Optional[str] = None
    clientId: str
    unitId: str
    nos: Optional[int] = None 
    monthDays: Optional[int] = None
    month: str
    year: int
    # Bill BreakUp
    basic: float = 0
    da: float = 0
    hra: float = 0
    conveyance: float = 0
    uniformAllowance: float = 0
    roomRent: float = 0
    # Bill Terms (Percentages)
    epfPercentage: float = 0
    esiPercentage: float = 0
    holidayPercentage: float = 0
    bonusPercentage: float = 0
    leviPercentage: float = 0
    serviceChargesPercentage: float = 0
    relievingChargesPercentage: float = 0
    # Meta
    status: str = "pending"
    description: Optional[str] = None
class BillRateUpdate(BaseModel):
    branch: Optional[str] = None
    clientId: Optional[str] = None
    unitId: Optional[str] = None
    nos: Optional[int] = None
    monthDays: Optional[int] = None
    month: Optional[str] = None
    year: Optional[int] = None
    basic: Optional[float] = None
    da: Optional[float] = None
    hra: Optional[float] = None
    conveyance: Optional[float] = None
    uniformAllowance: Optional[float] = None
    roomRent: Optional[float] = None
    epfPercentage: Optional[float] = None
    esiPercentage: Optional[float] = None
    holidayPercentage: Optional[float] = None
    bonusPercentage: Optional[float] = None
    leviPercentage: Optional[float] = None
    serviceChargesPercentage: Optional[float] = None
    status: Optional[str] = None
    description: Optional[str] = None

# ─── Branches ────────────────────────────────────────────────────────

class BranchCreate(BaseModel):
    branchId: str
    stateOfficeName: str
    stateOfficeAddress: str
    state: str
    district: str
    status: str = "active"
class BranchUpdate(BaseModel):
    branchId: Optional[str] = None
    stateOfficeName: Optional[str] = None
    stateOfficeAddress: Optional[str] = None
    state: Optional[str] = None
    district: Optional[str] = None
    status: Optional[str] = None