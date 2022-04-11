from Employee import Employee


class Manager(Employee):
    def __init__(self, name, address, phoneNumber, email, branchID, passwd, isManager):
        super().__init__(name, address, phoneNumber, email, branchID, passwd, isManager)
        self.isManager = True

    def __str__(self):
        return "Manager [name=" + self.name + ", address=" + self.address + ", phoneNumber=" + self.phoneNumber + ", email=" + self.email \
                + ", branchID=" + self.branchID + ", passwd=" + self.passwd + "]"
