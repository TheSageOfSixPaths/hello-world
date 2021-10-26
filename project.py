import pickle
import os
import sys

dict = {}
newdict = {}

#Accepting records#

def create_data():
    print("=======================VACCINE REGISTRATION=======================")
    f = open('vaccine.dat','ab')
    count = 0
    while True:
        name = input("Enter the name of person: ")
        age = int(input("Enter the age of person: ",))
        if age >= 18:
            pass
        else:
            print("You are not eligible for getting a vaccine: ")
            break
        vaccine = input("Enter the vaccine name: ")
        adhaar = input("Enter your Aadhar card number: ")
        dict["Name"] = name
        dict["Age"] = age
        dict["Vaccine"] = vaccine
        dict["Aadhar no."] = adhaar
        pickle.dump(dict,f)
        choice = input("Do you want to add more records? Y/N: ")
        if choice.lower() == "y":
            count = count + 1
        else:
            break 
    
    f.close() 

#Displaying records#

def display():
    f = open("vaccine.dat",'rb')
    while True:
        try:
            rec = pickle.load(f)
            print(rec)
        except EOFError:
            break
    f.close()

#Searcing#

def search():
    f = open('vaccine.dat','rb')
    a = input("Enter the name or Aadhar number: ")
    found = 0
    while True:
        try:
            rec = pickle.load(f)
            if rec["Name"] == a or rec["Aadhar no."] == a:
                found = 1
                print("Record found")
                print("Name: ",rec["Name"])
                print("Age: ",rec["Age"])
                print("Aadhar no.: ",rec["Aadhar no."])
                print("Vaccine: ",rec["Vaccine"])
            elif found == 0:
                print("Record does not exist")
        except EOFError:
            break
    
    f.close()

#Modification#

def update():
    reclst = []
    found = 0
    f = open("vaccine.dat",'rb')
    while True:
        try:
            rec = pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()

    r = input("Enter name person whose record you wanna update: ")
    for i in range(len(reclst)):
        if reclst[i]['Name'] == r:
            found = 1
            print("Record found.")
            m = input("Which detail do you wanna modify? \n1. AGE  2. VACCINE 3. AADHAAR NUMBER: ")
            if m.lower() == "age":
                a = int(input("Enter the new age: "))
                file = open("temp.dat","wb")
                var = reclst[i]["Age"] = a
                for x in reclst:
                    pickle.dump(x,file)
                file.close()
                os.remove("vaccine.dat")
                os.rename("temp.dat",'vaccine.dat')
                print("Following is the modified record.")
                f = open("vaccine.dat",'rb')
                while True:
                    try:
                        r = pickle.load(f)
                        print(r)
                    except EOFError:
                        break
                f.close()

            elif m.lower() == "vaccine":
                print("We have 2 different vaccines available at the moment: \n1. Sputnik v  2. mRNA-1273")
                v = input("Enter your choice? ")
                f = open("vaccine.dat", 'rb')
                file = open("temp.dat",'wb')
                bar = reclst[i]["Vaccine"] = v
                for y in reclst:
                    pickle.dump(y, file)
                f.close()
                file.close()
                os.remove("vaccine.dat")
                os.rename("temp.dat","vaccine.dat")
                print("Following is the modified record.")
                f = open("vaccine.dat",'rb')
                while True:
                    try:
                        r = pickle.load(f)
                        print(r)
                    except EOFError:
                        break
                f.close()
                
                        
            elif m.lower() == "aadhar number":
                aadhar = int(input("Enter the new aadhar number: "))
                f = open("vaccine.dat",'wb')
                file = open("temp.dat",'wb')
                car = reclst[i]["Aadhar no."] == aadhar
                for z in reclst:
                    pickle.dump(z ,file)
                f.close()
                file.close()
                os.remove("vaccine.dat")
                os.rename("temp.dat","vaccine.dat")
                print("Following is the modified record..")
                x = open("vaccine.dat",'rb')
                while True:
                    try:
                        r = pickle.load(x)
                        print(r)
                    except EOFError:
                        break
                x.close()
        elif found == 0:
                print("This record doesn't exist.")
                

#Deleting a record#

def delete():
    found = 0
    reclst = []
    ch = input("Enter the Name of person you want to delete: ")
    f = open("vaccine.dat",'rb')
    while True:
        try:
            rec = pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()
    file = open("temp.dat",'ab')
    for x in reclst:
        if x["Name"] == ch:
            continue
        pickle.dump(x,file)
    print("Record deleted") 
    print("This is the remaining record:")
    file.close()
    os.remove("vaccine.dat")
    os.rename("temp.dat",'vaccine.dat')
    f = open("vaccine.dat",'rb')
    while True:
        try:
            rec = pickle.load(f)
            print(rec)
        except EOFError:
            break
    for x in reclst:
        if x["Name"] != ch:
            print("Record not found,Please try again")
    
    f.close()

#Main#

def main():
    while True:
        print("===================MAIN MENU===================")
        print("Type 1 to insert records:")
        print("Type 2 to display records:")
        print("Type 3 to search records:")
        print("Type 4 to modify a record:")
        print("Type 5 to delete a record:")
        print("Type 6 to exit.")
        print("Enter your choice:")
        ch = int(input('-> '))
        if ch == 1:
            create_data()
        elif ch == 2:
            display()
        elif ch == 3:
            search()
        elif ch == 5:
            delete()
        elif ch == 4:
            update()
        elif ch == 6:
            break
        
                

    
#registering#

def reg():
    print("==============REGISTRATION============")
    f = open("userdetails.dat",'wb')
    count = 0
    while True:
        x = input("Enter the username: ")
        y = input("Enter the password: ")
        z = input("Enter password again: ")
        if y == z:
            list = [x,z]
            pickle.dump(list,f)
            print("Account successfully registered")
            main()
            break
        else:
            print("Passwords do not match,please try again")
            userin = input("Do you want to try again? Y/N: ")
            if userin.lower() == "y":
                count = count + 1
            else:
                break


#Loggingin#

def log():
    user = input("Do you want to login or register: ")
    if user.lower() == "login":
        f = open("userdetails.dat",'rb')
        while True:
            try:
                rec = pickle.load(f)
                log = input("Enter username: ")
                word = input("Enter password: ")
                if word in rec:
                    print("Access granted.")
                    main()
                    break
                else:
                    print("Access denied, Try again.")
                    
            except EOFError:
                break

    elif user.lower() == "register":
        reg()

log()