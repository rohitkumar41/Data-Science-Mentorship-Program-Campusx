# login program and identation
# email -> nitish.campusx@gmail.com
# password -> 1234

email = input("Enter email")
password = input("Enter password")

if email == 'nitish.campusx@gmail.com' and password == '1234':
    print('Welcome')
elif email == 'nitish.campusx@gmail.com' and password != '1234':
    print("Incorrect Password")
    password = input("enter password again")
    if password == '1234':
        print('Welcome,finally')
    else:
        print('Beta Tumse nhi hoga')
else:
    print("Not correct")