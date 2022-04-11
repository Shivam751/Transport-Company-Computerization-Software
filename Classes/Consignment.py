class Consignment:
    def __init__(self, volume, sender, receiver, revenue, isTruckAllotted, truckAssigned, dispatched, sourceOffice, destinationOffice, consignmentID):
        self.volume = volume
        self.sender = sender
        self.receiver = receiver
        self.revenue = revenue
        self.isTruckAllotted = isTruckAllotted
        self.truckAssigned = truckAssigned
        self.dispatched = dispatched
        self.sourceOffice = sourceOffice
        self.destinationOffice = destinationOffice
        self.consignmentID = consignmentID
    
    def getVolume(self):
        return self.volume
    def setVolume(self, volume):
        self.volume = volume
    def getSender(self):
        return self.sender
    def setSender(self, sender):
        self.sender = sender
    def getReceiver(self):
        return self.receiver
    def setReceiver(self, receiver):
        self.receiver = receiver
    def getRevenue(self):
        return self.revenue
    def setRevenue(self, revenue):
        self.revenue = revenue
    def getIsTruckAllotted(self):
        return self.isTruckAllotted
    def setIsTruckAllotted(self, isTruckAllotted):
        self.isTruckAllotted = isTruckAllotted
    def getTruckAssigned(self):
        return self.truckAssigned
    def setTruckAssigned(self, truckAssigned):
        self.truckAssigned = truckAssigned
    def getDispatched(self):
        return self.dispatched
    def setDispatched(self, dispatched):
        self.dispatched = dispatched
    def getSourceOffice(self):
        return self.sourceOffice
    def setSourceOffice(self, sourceOffice):
        self.sourceOffice = sourceOffice
    def getDestinationOffice(self):
        return self.destinationOffice
    def setDestinationOffice(self, destinationOffice):
        self.destinationOffice = destinationOffice
    def getConsignmentID(self):
        return self.consignmentID
    
    def __str__(self):
        return "Consignment [volume=" + self.volume + ", sender=" + self.sender + ", receiver=" + self.receiver + ", revenueGenerated=" \
				+ self.revenue + ", isTruckAssigned=" + self.isTruckAllotted + ", truckAssigned=" + self.truckAssigned \
				+ ", dispatechedAndReceived=" + self.dispatched + ", sourcebranch=" + self.sourceOffice \
				+ ", destinationBranch=" + self.destinationOffice + ", consignmentId=" + self.consignmentID + "]" 