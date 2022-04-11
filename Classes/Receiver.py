from Customer import Customer
class Sender(Customer):

    recvStatus = False
    
    def __init__(self, name, address, phoneNumber, email, customerID, consignmentID):
        super().__init__(name, address, phoneNumber, email, customerID, consignmentID)
    
    def getDespatchStatus(self):
        return self.recvStatus
    def setDespatchStatus(self, recvStatus):
        self.recvStatus = recvStatus
    def __str__(self):
        return "Receiver [name=" + self.name + ", address=" + self.address + ", phoneNumber=" + self.phoneNumber + ", email=" + self.email \
                + ", customerID=" + self.customerID + ", consignmentID=" + self.consignmentID + "]"