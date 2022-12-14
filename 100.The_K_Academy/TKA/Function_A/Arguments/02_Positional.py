def create_email(fname, lname, cname):
    email = fname.lower() + lname.lower() + '@'+ cname.lower() + '.com'
    print(email)

fn = input("Enter first name of employee : ")
ln = input("Enter last name of employee : ")
cn = input("Enter company name of employee : ")

create_email(fn, ln, cn)