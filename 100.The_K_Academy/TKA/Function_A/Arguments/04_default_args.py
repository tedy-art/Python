def create_email(fname, lname, cname = "JBK"):
    email = fname.lower() + lname.lower() + '@' + cname.lower() + '.com'
    print(email)

fn = input("Enter first name of Employee : ")
ln = input("Enter last name of Employee : ")

create_email(fname=fn, lname=ln, cname='TCS')

create_email(lname=ln, fname=fn)