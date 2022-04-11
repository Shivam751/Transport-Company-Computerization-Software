class Office:
    def __init__(self, ID, address, phoneNumber, email, managerID, numTrucks, numEmplyees, volumeHandled, revenue, IdleWaitingTime, rate):
        self.ID = ID
        self.address = address
        self.phoneNumber = phoneNumber
        self.email = email
        self.managerID = managerID
        self.numTrucks = numTrucks
        self.numEmplyees = numEmplyees
        self.volumeHandled = volumeHandled
        self.revenue = revenue
        self.IdleWaitingTime = IdleWaitingTime
        self.rate = rate
    
    def getID(self):
        return self.ID
    def setID(self, ID):
        self.ID = ID
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
    def getManagerID(self):
        return self.managerID
    def setManagerID(self, managerID):
        self.managerID = managerID
    def getNumTrucks(self):
        return self.numTrucks
    def setNumTrucks(self, numTrucks):
        self.numTrucks = numTrucks
    def getNumEmplyees(self):
        return self.numEmplyees
    def setNumEmplyees(self, numEmplyees):
        self.numEmplyees = numEmplyees
    def getVolumeHandled(self):
        return self.volumeHandled
    def setVolumeHandled(self, volumeHandled):
        self.volumeHandled = volumeHandled
    def getRevenue(self):
        return self.revenue
    def setRevenue(self, revenue):
        self.revenue = revenue
    def getIdleWaitingTime(self):
        return self.IdleWaitingTime
    def setIdleWaitingTime(self, IdleWaitingTime):
        self.IdleWaitingTime = IdleWaitingTime
    def getRate(self):
        return self.rate
    def setRate(self, rate):
        self.rate = rate

    def __str__(self):
        return "Office [ID=" + self.ID + ", address=" + self.address + ", phoneNumber=" + self.phoneNumber + ", email=" + self.email \
                + ", managerID=" + self.managerID + ", numTrucks=" + self.numTrucks + ", numEmplyees=" + self.numEmplyees \
                + ", volumeHandled=" + self.volumeHandled + ", revenue=" + self.revenue + ", IdleWaitingTime=" + self.IdleWaitingTime \
                + ", rate=" + self.rate + "]"
