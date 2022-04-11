class Customer:
    def __init__(self, name, address, phoneNumber, email, customerID, consignmentID):
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber
        self.email = email
        self.customerID = customerID
        self.consignmentID = consignmentID
    
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
    def getCustomerID(self):
        return self.customerID
    def setCustomerID(self, customerID):
        self.customerID = customerID
    def getConsignmentID(self):
        return self.consignmentID
    def setConsignmentID(self, consignmentID):
        self.consignmentID = consignmentID
    
    def __str__(self):
        return "Customer [name=" + self.name + ", address=" + self.address + ", phoneNumber=" + self.phoneNumber + ", email=" + self.email \
                + ", customerID=" + self.customerID + ", consignmentID=" + self.consignmentID + "]"
