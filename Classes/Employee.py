class Employee:
    def __init__(self, name, address, phoneNumber, email, branchID, passwd, isManager):
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber
        self.email = email
        self.branchID = branchID
        self.passwd = passwd
        self.isManager = isManager
    
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getAddress(self):
        return self.address
    def setAddress(self, address):
        self.address = address
    def getPhoneNumber(self):
        return self.phoneNumber
    def setPhoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber
    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email = email
    def getBranchID(self):
        return self.branchID
    def setBranchID(self, branchID):
        self.branchID = branchID
    def getPasswd(self):
        return self.passwd
    def setPasswd(self, passwd):
        self.passwd = passwd
    def getIsManager(self):
        return self.isManager
    def setIsManager(self, isManager):
        self.isManager = isManager
    
    def __str__(self):
        return "Employee [name=" + self.name + ", address=" + self.address + ", phoneNumber=" + self.phoneNumber + ", email=" + self.email \
                + ", branchID=" + self.branchID + ", passwd=" + self.passwd + "]"
        
