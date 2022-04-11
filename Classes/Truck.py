class Truck:
    def __init__(self, truckID, currentBranch, numConsignmentsHandled, status, usage):
        self.truckID = truckID
        self.currentBranch = currentBranch
        self.numConsignmentsHandled = numConsignmentsHandled
        self.status = status
        self.usage = usage
    
    def getTruckID(self):
        return self.truckID
    def setTruckID(self, truckID):
        self.truckID = truckID
    def getCurrentBranch(self):
        return self.currentBranch
    def setCurrentBranch(self, currentBranch):
        self.currentBranch = currentBranch
    def getNumConsignmentsHandled(self):
        return self.numConsignmentsHandled
    def setNumConsignmentsHandled(self, numConsignmentsHandled):
        self.numConsignmentsHandled = numConsignmentsHandled
    def getStatus(self):
        return self.status
    def setStatus(self, status):
        self.status = status
    def getUsage(self):
        return self.usage
    def setUsage(self, usage):
        self.usage = usage
    def __str__(self):
        return "Truck [truckID=" + self.truckID + ", currentBranch=" + self.currentBranch + ", numConsignmentsHandled=" + self.numConsignmentsHandled \
                + ", status=" + self.status + ", usage=" + self.usage + "]"