class student:
    def __init__(self, nm, rl, mk):
        self.name = nm
        self.roll = rl
        self.marks = mk

    def print_deti(self):
        print(f"Student name is {self.name}, roll number is {self.roll} and marks are {self.marks}.")

s1 = student('xyz', 11, 84)
s1.print_deti()

s2 = student('pqr', 12, 85)
s2.print_deti()