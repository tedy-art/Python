db = {
    101:{'name':'Jay', 'marks': 88, 'roll': 101, 'fees':20000},
    102:{'name':'Tom', 'marks': 80, 'roll': 102, 'fees':15000},
    103:{'name':'Devid', 'marks': 77, 'roll': 103, 'fees':25000},
    104:{'name':'Abhi', 'marks': 83, 'roll': 104, 'fees':28000},
    105:{'name':'Chandu', 'marks': 84, 'roll': 105, 'fees':20000}
}

def dashboard():
    print('Welcome to student Management system by batch 459')
    print("""
                        menu
                        1) Create student Record
                        2) Read Student Record
                        3) Update student record
                        4) Delete student record
                        5) Display student record
                        6) Display student record
    """)

def create_student():
    u_name = input('Enter student name : ')
    u_roll = eval(input('Enter student roll number : '))
    u_marks = eval(input('Enter student marks : '))
    u_fees = eval(input('Enter student fees paid : '))

    chotu_dict = {}

    chotu_dict['name'] = u_name
    chotu_dict['roll'] = u_roll
    chotu_dict['marks'] = u_marks
    chotu_dict['fees'] = u_fees

    db[u_roll] = chotu_dict
    print(f"Student {u_name} added successfully in db...")
    print('*'*65)
    print()

def read_student():
    print('-'*65)
    print("|{r:^15}|{n:^15}|{m:^15}|{f:^15}|".format(r = 'roll number', n ='Name', m = 'Marks', f='fees'))
    print('-'*65)
    for i in db:
        print("|{r:^15}|{n:^15}|{m:^15}|{f:^15}|".format(r = db[i]['roll'], n =db[i]['name'], m = db[i]['marks'], f=db[i]['fees']))
        print('-'*65)

def update_student():
    u_roll = eval(input('Enter student roll to update : '))
    if u_roll in db:
        u_name = input('Enter student name : ')
        u_marks = eval(input('Enter student marks : '))
        u_fees = eval(input('Enter student fees paid : '))

        db[u_roll]['name'] = u_name
        db[u_roll]['marks'] = u_marks
        db[u_roll]['fees'] = u_fees

        print(f"Student {db[u_roll]['name']} updated successfully in db....")
        print('*'*65)
        print()


def delete_student():
    u_roll = eval(input("Enter student roll to delete : "))
    if u_roll in db:
        n = db[u_roll]['name']
        del db[u_roll]
        print(f"Student {n} deleted successfully from database...")
    else:
        print("Invalid student roll number...")

def read_student_fees():
    u_fees = eval(input("Enter student paid fees ammount to display : "))
    print('-'*65)

    print("|{r:^15}|{n:^15}|{m:^15}|{f:^15}|".format(r = 'roll number', n ='Name', m = 'Marks', f='fees'))
    print('-'*65)
    
    for i in db:
        if db[i]['fees'] >= u_fees:
            print("|{r:^15}|{n:^15}|{m:^15}|{f:^15}|".format(r = db[i]['roll'], n =db[i]['name'], m = db[i]['marks'], f=db[i]['fees']))
            print('-'*65)

def read_student_marks():
    u_marks = eval(input("Enter student marks to display : "))
    print("|{r:^15}|{n:^15}|{m:^15}|{f:^15}|".format(r = 'roll number', n ='Name', m = 'Marks', f='fees'))
    print('-'*65)

    for i in db:
        if db[i]['marks'] >= u_marks:
            print("|{r:^15}|{n:^15}|{m:^15}|{f:^15}|".format(r = db[i]['roll'], n =db[i]['name'], m = db[i]['marks'], f=db[i]['fees']))
            print('-'*65)

while True:
    dashboard()
    choice = eval(input("Enter your choice [1, 2, 3, 4, 5] : "))

    if choice == 1:
        create_student()

    elif choice == 2:
        if len(db) == 0:
            print("Database is empty...")
        else:
            read_student()


    elif choice == 3:
        if len(db) == 0:
            print("No student to update in database....")
        else:
            update_student()
    
    elif choice == 4:
        if len(db) == 0:
            print('No student to delete in database...')
        else:
            delete_student()

    elif choice == 5:
        if len(db) == 0:
            print('No student to display in database : ')
        else:
            read_student_fees()

    elif choice == 6:
        if len(db) == 0:
            print('No student to display in database : ')
        else:
            read_student_marks()

    else:
        print("Invalid choice...")

    ch = input('Do you want to continue [y/n] : ')
    if ch.lower() != 'y':
        # print(db)
        break