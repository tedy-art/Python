def create_email(fname, lname, cname):
    email = fname.lower() + lname.lower() + '@' + cname.lower() + '.com'
    print(email)

fn = input("Enter first name of Employee : ")
ln = input("Enter last name of Employee : ")
cn = input("Enter company name of Employee : ")

create_email(fname=fn, lname=ln, cname=cn)