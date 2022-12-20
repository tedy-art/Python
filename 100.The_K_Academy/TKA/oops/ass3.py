class school:
    def __init__(self, nm, addr, section):
        self.name = nm
        self.address = addr
        self.section = section

    def display(self):
        print("School name is {self.name}, address is {self.address} and subjects are {self.section}.")

s1 = school("new arts", "nagar", "MCA")
s1.display()

s2 = school("IBI", "Nagar", "BCA")
s2.display()