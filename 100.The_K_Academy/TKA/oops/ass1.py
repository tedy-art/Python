class employee():
    def __init__(self, nm, id, salary):
        self.name = nm
        self.id = id
        self.salary = salary

    def get_details(self):
        print(f"Emplyoee name is {self.name}, id is {self.id} and address is {self.salary}.")


e1 = employee('pqr', 1, 254000)
e1.get_details()

e2 = employee('xyz', 2, 450000)
e2.get_details()