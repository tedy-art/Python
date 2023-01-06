db = []

print("\t welcome to student mangement system")
print("""
            Manu:
            1) Add student record
            2) Display(Read) student record
            3) Update student record
            4) Delete student record

""")

class student:
    def __init__(self, nm, rl, addr, marks, fees, dept):
        self.name = nm
        self.roll = rl
        self.address = addr
        self.marks = marks
        self.fees = fees
        self.department = dept
    
    def add_student(self):
        pass

    def display_student(self):
        pass

    def updated_student(self):
        pass

    def delete_student(self):
        pass

    def __str__(self):
        return self.name
    
# Create Dummy object for database (list)
dummy_obj = student('', 0, 0, '', 0, 0, '')
e1 = student(nm = 'jay', rl= 101, addr= 'Karvenagar', marks= '82', fees= 30000, dept= 'MCA')
db.append(e1)