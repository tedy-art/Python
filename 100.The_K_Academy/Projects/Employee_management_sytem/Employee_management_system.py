db = {101:{'name':'Jay', 'address': 'Talegoan', 'id': 101, 'salary':20000}}

def dashboard():
    print("\t\t Welcome to Employee Management System")
    print("""
                Manu
                1) Create new Employee record
                2) Read Employee record
                3) update employee reocrd
                4) Delete employee record
    """)

def create_emp():
    u_name = input("Enter employee name : ")
    u_address = input("Enter user's address : ")
    u_id = eval(input("Enter employee id : "))
    u_salary = eval(input("Enter employee payment : "))

    new_dict ={}

    new_dict['name'] = u_name
    new_dict['id'] = u_id
    new_dict['address'] = u_address
    new_dict['salary'] = u_salary

    db[u_id] =  new_dict
    print(f"Employee {u_name} added successfully in db...")
    print('*'* 65)
    print()

def read_emp():
    print('-'*65)
    print("|{emp_id:^15}|{n:^15}|{addr:^15}|{emp_sal:^15}|".format(emp_id = "Employee id", n = 'name', addr = "address", emp_sal = "salary"))
    print('-'*65)

    for i in db:
        print("|{emp_id:^15}|{n:^15}|{addr:^15}|{emp_sal:^15}|".format(emp_id = db[i]['id'], n = db[i]['name'], addr = db[i]['address'], emp_sal = db[i]['salary']))
        print('-'*65)

def update_emp():
    u_id = eval(input("Enter employee id for Update : "))
    if u_id in db:
        u_name = input("Enter employee name for update : ")
        u_address = input("Enter emplyee address for update : ")
        u_salary = eval(input("Enter employee salary for update : "))

        db[u_id]['name'] = u_name
        db[u_id]['address'] = u_address
        db[u_id]['salary'] = u_salary
        print(f"Employee {db[u_id]['name']} updated successfully in db...")
        print('*'*65)
        print()

def delete_emp():
    u_id = eval(input("Enter student roll to delete : "))

    if u_id in db:
        n = db[u_id]['name']
        del db[u_id]
        print(f"Employee {n} deleted successfully from database...")
    else:
        print("Invalid employee id number...")

while True:
    dashboard()
    chioce = eval(input("Enter your choice[1 2 3 4] : "))
    if chioce == 1:
        create_emp()

    if chioce == 2:
        if len(db) == 0:
            print("Database is empty...")
        else:
            read_emp()

    if chioce == 3:
        if len(db) == 0:
            print("Database is empty...")
        else:
            update_emp()

    if chioce == 4:
        if len(db) == 0:
            print("Database is empty...")
        else:
            delete_emp()


    ch = input("Do you want continue [y/n] : ")
    if ch.lower() != 'y':
        break