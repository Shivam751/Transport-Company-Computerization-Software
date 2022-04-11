from Customer import Customer
class Sender(Customer):

    dispatchStatus = False
    
    def __init__(self, name, address, phoneNumber, email, customerID, consignmentID):
        super().__init__(name, address, phoneNumber, email, customerID, consignmentID)
    
    def getDispatchStatus(self):
        return self.dispatchStatus
    def setDispatchStatus(self, dispatchStatus):
        self.dispatchStatus = dispatchStatus
    def __str__(self):
        return "Sender [name=" + self.name + ", address=" + self.address + ", phoneNumber=" + self.phoneNumber + ", email=" + self.email \
                + ", customerID=" + self.customerID + ", consignmentID=" + self.consignmentID + "]"