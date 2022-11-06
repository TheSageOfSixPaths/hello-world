import pickle
import os
import datetime
choice='y'

try:               #checks for username and password
    checker=0
    uu=open('user','rb')
    zz=[]
    while True:
        try:
            zz.append(pickle.load(uu))
        except EOFError:
            break
    pp=input('Enter Username: ')
    for i in zz:
        if pp==i[0]:
            qq= input('Enter Password: ')
            if qq==i[1]:
                print()
                print('Access Granted')
                print()
                checker=1
                break
            else:
                print('Incorrect Password')
                checker=2
                break
    if checker==0:
        print('Incorrect Username')
    uu.close()
    
    if checker==1:                              #printing the menu if user is found
        while choice=='y' or choice=='Y':
            n=int(input('''*************MAIN MENU*************
        Choose an option:
            (1)Read
            (2)Write
            (3)Append
            (4)Update
            (5)Search
            (6)Delete
            (7)Exit
            Option number: '''))
            
            def read():
                info=[]
                print()
                print('*************READ*************')
                y=int(input('''What do you want to display?
            (1)All Data
            (2)Cust. ID
            (3)Names
            (4)Adresses
            (5)Phone numbers
            (6)Date of Visit
            Option number: '''))
                f=open('file','rb')
                while True:
                    try:      
                        info.append(pickle.load(f))
                    except(EOFError):
                        break
                print()
                
                max=[0,0,0,0,0]             #list for checking length of all records in a column
                sum=0
                h=['Cust.ID','Name','Address','Phone No.','Date of visit']             #adding the length of column headings in the 'max' list
                for i in range(len(info)):
                    for j in range(len(info[i])):
                        if len(str(info[i][j]))>max[j]:
                            max[j]=len(str(info[i][j]))
                for i in range(len(max)):
                    if len(str(h[i]))>max[i]:
                        max[i]=len(str(h[i]))
                    
                if y not in [1,2,3,4,5,6]:
                    print('Invalid Option!')             
                elif y==1:         #printing all data
                    for i in max:
                        sum+=i
                    print('+','-'*(sum+8),'+',sep='')
                    print('|''Cust.ID',' '*(max[0]-len('Cust.ID')),'|'*2,'Name',' '*(max[1]-len('Name')),'|'*2,'Address',' '*(max[2]-len('Address')),'|'*2,'Phone No.',' '*(max[3]-len('Phone No.')),'|'*2,'Date of visit',' '*(max[4]-len('Date of visit')),'|',sep='')
                    print('+','-'*(sum+8),'+',sep='')
                    for i in range(len(info)):                     #data stored as individual lists in 'info'
                        for j in range(len(info[i])):
                            print('|',info[i][j],' '*(max[j]-(len(str(info[i][j])))),'|',end='',sep='')      #printing each record column wise spaces multiplied by the difference of length of the maximum record in that column and the lenght of that record     
                        print()
                    print('+','-'*(sum+8),'+',sep='')
                elif y==2:                                             #printing customer id
                    sum=max[0]
                    print('+','-'*(sum),'+',sep='')
                    print('|''Cust.ID',' '*(max[0]-len('Cust.ID')),'|',sep='')
                    print('+','-'*(sum),'+',sep='')
                    for i in range(len(info)):
                        j=0
                        print('|',info[i][j],' '*(max[j]-len(str(info[i][j]))),'|',end='',sep='')
                        print()
                    print('+','-'*(sum),'+',sep='')         
                elif y==3:                                           #printing names
                    sum=max[1]
                    print('+','-'*(sum),'+',sep='')
                    print('|''Name',' '*(max[1]-len('Name')),'|',sep='')
                    print('+','-'*(sum),'+',sep='')
                    for i in range(len(info)):
                        j=1
                        print('|',info[i][j],' '*(max[j]-len(str(info[i][j]))),'|',end='',sep='')
                        print()
                    print('+','-'*(sum),'+',sep='')
                elif y==4:                                            #printing addresses
                    sum=max[2]
                    print('+','-'*(sum),'+',sep='')
                    print('|''Address',' '*(max[2]-len('Address')),'|',sep='')
                    print('+','-'*(sum),'+',sep='')
                    for i in range(len(info)):
                        j=2
                        print('|',info[i][j],' '*(max[j]-len(str(info[i][j]))),'|',end='',sep='')
                        print()
                    print('+','-'*(sum),'+',sep='')            
                elif y==5:                                          #printing phone numbers
                    sum=max[3] 
                    print('+','-'*(sum),'+',sep='')
                    print('|''Phone No.',' '*(max[3]-len('Phone No.')),'|',sep='')
                    print('+','-'*(sum),'+',sep='')
                    for i in range(len(info)):
                        j=3
                        print('|',info[i][j],' '*(max[j]-len(str(info[i][j]))),'|',end='',sep='')
                        print()
                    print('+','-'*(sum),'+',sep='')           
                elif y==6:                                           #printing dates of visit
                    sum=max[4]
                    print('+','-'*(sum),'+',sep='')
                    print('|''Date of Visit',' '*(max[4]-len('Date of Visit')),'|',sep='')
                    print('+','-'*(sum),'+',sep='')
                    for i in range(len(info)):
                        j=4
                        print('|',info[i][j],' '*(max[j]-len(str(info[i][j]))),'|',end='',sep='')
                        print()
                    print('+','-'*(sum),'+',sep='')
              
            def write():
                print()
                print('*************WRITE*************')
                f=open('file','wb')
                n=int(input('How many customers do you want to write: '))
                for i in range(n):
                    l=[]
                    print()
                    a=input('Cust. ID: ')
                    b=input('Name: ')
                    c=input('Address: ')
                    d=int(input('Phone: '))
                    while True:
                        if len(str(d))!=10:
                            print('Please Enter a 10 Digit No. Only!')
                            print()
                            d=int(input('Phone: '))
                            continue
                        else:
                            break
                    while True:
                        e=input('Date of visit(YYYY/MM/DD): ')
                        try:
                            Y,M,D=map(int,e.split('/'))
                        except ValueError or TypeError:
                            print('Invalid Data Type or Format!')
                            print()
                            continue
                        today=datetime.date.today()
                        try:
                            date1=datetime.date(Y,M,D)                                 #will check if the date is impossible(like >31 is not possible)
                        except:
                            print('Invalid date')
                            continue
                        if date1>today:                                                         #checking that the date dosen't exeed today
                            print('Please Input a Valid Date!')
                            print()
                            continue
                        else:
                            break
                    l.extend([a,b,c,d,e])
                    pickle.dump(l,f)
                print('Records Added')
                f.close()

            def append():
                cust_id=[]
                f=open('file','rb')
                while True:
                    try:      
                        info=pickle.load(f)
                        cust_id.append(info[0])
                    except(EOFError):
                        break
                f.close()
                print()
                print('*************APPEND*************')
                f=open('file','ab')
                m=int(input('How many customers do you want to append: '))
                for i in range(m):
                    l=[]
                    print()
                    a=input('Cust. ID: ')
                    if a in cust_id:                            #'cust_id' contains all the customer id's 
                        print('ID aready exists!')
                        continue
                    b=input('Name: ')
                    c=input('Address: ')
                    d=int(input('Phone: '))
                    while True:
                        if len(str(d))!=10:                        #checking that the number entered is 10 digit
                            print('Please Enter a 10 Digit No. Only!')
                            print()
                            d=int(input('Phone: '))
                        else:
                            break
                    while True:                                      #checking that the date dosen't exeed today
                        e=input('Date of visit(YYYY/MM/DD): ')
                        try:
                            Y,M,D=map(int,e.split('/'))
                        except ValueError or TypeError:
                            print('Invalid Data Type or Format!')
                            print()
                            continue
                        today=datetime.date.today()
                        try:
                            date1=datetime.date(Y,M,D)                                  #will check if the date is impossible(like >31 is not possible)
                        except:
                            print('Invalid date')
                            continue
                        if date1>today:
                            print('Please Input a Valid Date!')
                            print()
                            continue
                        else:
                            break
                    l.extend([a,b,c,d,e]) 
                    pickle.dump(l,f)
                    print('Records Added')
                f.close()
                        
            def update():
                cust_id=[]
                print()
                print('*************UPDATE*************')
                check=0    
                d=[]
                f=open('file','rb')
                while True:
                    try:      
                        inf=pickle.load(f)
                        d.append(inf)
                        cust_id.append(inf[0])
                    except(EOFError):
                        break
                f.close()
                g=open('updatefile','wb')
                x=input('Customer ID: ')
                if x in cust_id:        
                    y=int(input('''What do you want to update:
            (1)Customer ID
            (2)Name
            (3)Address
            (4)Phone no.
            (5)Date of visit
            Option number: '''))
                    if y not in [1,2,3,4,5]:
                        print('Invalid option!')
                    else:
                        for i in d:
                            z=[]
                            if i[0]==x:
                                if y==1:
                                    new=input('Enter new ID: ')
                                    if new in cust_id:                            #checking for repetition in customer id
                                        print('ID aready exists!')
                                        continue
                                    i[0]=new
                                    z.append(i)
                                elif y==2:
                                    new=input('Enter new Name: ')
                                    i[1]=new
                                    z.append(i)
                                elif y==3:
                                    new=input('Enter new Adress: ')
                                    i[2]=new
                                    z.append(i)
                                elif y==4:
                                    new=int(input('Enter new Phone: '))                   #checking that the number entered is 10 digit
                                    while True:
                                        if len(str(new))!=10:
                                            print('Please Enter a 10 Digit No. Only!')
                                            print()
                                            new=int(input('Enter new Phone: '))
                                        else:
                                            break
                                    i[3]=new
                                    z.append(i)
                                elif y==5:
                                    while True:
                                        new=input('Enter new Date of visit(YYYY/MM/DD): ')                    #checking that the date dosen't exeed today
                                        try:
                                            Y,M,D=map(int,new.split('/'))
                                        except ValueError or TypeError:
                                            print('Invalid Data Type or Format!')
                                            print()
                                            continue
                                        today=datetime.date.today()
                                        try:
                                            date1=datetime.date(Y,M,D)                                       #will check if the date is impossible(like >31 is not possible)
                                        except:
                                            print('Invalid date')
                                            continue
                                        if date1>today:
                                            print('Please Input a Valid Date!')
                                            print()
                                            continue
                                        else:
                                            break
                                    i[4]=new
                                    z.append(i)
                                for e in z:
                                    pickle.dump(e,g)
                                check=1
                            else:
                                pickle.dump(i,g)
                    if check==1:        
                        print("File has been updated")
                    g.close()
                    os.remove('file')
                    os.rename('updatefile','file')
                else:
                    print("ID you entered dosen't exist")
                g.close()

            
            def search():
                print()
                print('*************SEARCH*************')
                f=open('file','rb')
                info=[]
                d=[]
                while True:
                    try:      
                        info.append(pickle.load(f))
                    except(EOFError):
                        break
                f.close()
                x=int(input('''Choose criteria:
            (1)Cust. ID
            (2)Name
            (3)Address
            (4)Phone
            (5)Date of visit
            Option number: '''))
                check=1
                if x not in [1,2,3,4,5]:
                    print('Invalid Option!')
                elif x==1:
                    y=input('Enter ID to search for: ')
                    for i in info:
                        if i[0]==y:
                            check=0
                            d.append(i)
                    if check==1:
                        print("ID you entered dosen't exist")
                elif x==2:
                    y=input('Enter Name to search for: ')
                    for i in info:
                        if i[1]==y:
                            check=0
                            d.extend([i])
                    if check==1:
                        print("Name you entered dosen't exist")
                elif x==3:
                    y=input('Enter Address to search for: ')
                    for i in info:
                        if i[2]==y:
                            check=0
                            d.append(i)
                    if check==1:
                        print("Address you entered dosen't exist")
                elif x==4:
                    y=int(input('Enter Phone number to search for: '))
                    while True:                                                                                   #checking that the number entered is 10 digit
                        if len(str(y))!=10:
                            print('Please Enter a 10 Digit No. Only!')
                            print()
                            y=int(input('Enter Phone number to search for: '))
                        else:
                            break
                    for i in info:
                        if i[3]==y:
                            check=0
                            d.append(i)
                    if check==1:
                        print("Phone number you entered dosen't exist")
                elif x==5:
                    while True:
                        y=input('Enter Date of visit to search for(YYYY/MM/DD): ')                     #checking that the date dosen't exeed today
                        try:
                            Y,M,D=map(int,y.split('/'))
                        except ValueError or TypeError:
                            print('Invalid Data Type or Format!')
                            print()
                            continue
                        today=datetime.date.today()
                        try:
                            date1=datetime.date(Y,M,D)                                       #will check if the date is impossible(like >31 is not possible)
                        except:
                            print('Invalid date')
                            continue
                        if date1>today:
                            print('Please Input a Valid Date!')
                            print()
                            continue
                        else:
                            break
                    for i in info:
                        if i[4]==y:
                            check=0
                            d.append(i)
                    if check==1:
                        print("Date of visit you entered dosen't exist")
                else:
                    print('Invalid option!')
                if check==0:
                    max=[0,0,0,0,0]
                    sum=0
                    h=['Cust.ID','Name','Address','Phone No.','Date of visit']
                    for i in range(len(d)):
                        for j in range(len(d[i])):
                            if len(str(d[i][j]))>max[j]:
                                max[j]=len(str(d[i][j]))
                    for i in range(len(max)):
                        if len(str(h[i]))>max[i]:
                            max[i]=len(str(h[i]))
                    for i in max:
                        sum+=i
                    print('+','-'*(sum+8),'+',sep='')
                    print('|''Cust.ID',' '*(max[0]-len('Cust.ID')),'|'*2,'Name',' '*(max[1]-len('Name')),'|'*2,'Address',' '*(max[2]-len('Address')),'|'*2,'Phone No.',' '*(max[3]-len('Phone No.')),'|'*2,'Date of visit',' '*(max[4]-len('Date of visit')),'|',sep='')
                    print('+','-'*(sum+8),'+',sep='')
                    for i in range(len(d)):
                        for j in range(len(d[i])):
                            print('|',d[i][j],' '*(max[j]-len(str(d[i][j]))),'|',end='',sep='')
                        print()
                    print('+','-'*(sum+8),'+',sep='')
                                        
            def delete():
                print()
                print('*************DELETE*************')
                f=open('file','rb')
                g=open('updatedfile','wb')
                info=[]
                while True:
                    try:      
                        info.append(pickle.load(f))
                    except(EOFError):
                        break
                f.close()
                x=int(input('''Choose criteria:
            (1)Cust. ID
            (2)Name
            (3)Address
            (4)Phone
            (5)Date of visit
            Option number: '''))
                check=1
                if x not in [1,2,3,4,5]:
                    print('Invalid Option!')
                elif x==1:
                    y=input('Enter ID to delete record: ')
                    for i in info:
                        if i[0]==y:
                            check=0
                        else:
                            pickle.dump(i,g)
                    if check==1:
                        print("ID you entered dosen't exist")
                elif x==2:
                    y=input('Enter Name to delete record: ')
                    for i in info:
                        if i[1]==y:
                            check=0
                        else:
                            pickle.dump(i,g)
                    if check==1:
                        print("Name you entered dosen't exist")
                elif x==3:
                    y=input('Enter Address to delete record: ')
                    for i in info:
                        if i[2]==y:
                            check=0
                        else:
                            pickle.dump(i,g)
                    if check==1:
                        print("Address you entered dosen't exist")
                elif x==4:
                    y=int(input('Enter Phone number to delete record: '))
                    while True:                                                                                   #checking that the number entered is 10 digit
                        if len(str(y))!=10:
                            print('Please Enter a 10 Digit No. Only!')
                            print()
                            y=int(input('Enter Phone number to search for: '))
                        else:
                            break
                    for i in info:
                        if i[3]==y:
                            check=0
                        else:
                            pickle.dump(i,g)
                    if check==1:
                        print("Phone number you entered dosen't exist")
                elif x==5:
                    while True:
                        y=input('Enter Date of visit to delete record(YYYY/MM/DD): ')                             #checking that the date entered dosen't exeed today
                        try:
                            Y,M,D=map(int,y.split('/'))
                        except ValueError or TypeError:
                            print('Invalid Data Type or Format')
                            print()
                            continue
                        today=datetime.date.today()
                        try:
                            date1=datetime.date(Y,M,D)                                       #will check if the date is impossible(like >31 is not possible)
                        except:
                            print('Invalid date')
                            continue
                        if date1>today:
                            print('Please Input a Valid Date')
                            print()
                            continue
                        else:
                            break
                    for i in info:
                        if i[4]==y:
                            check=0
                        else:
                            pickle.dump(i,g)
                    if check==1:
                        print("Date of visit you entered dosen't exist")
                else:
                    print('Invalid option!')
                g.close()
                os.remove('file')
                os.rename('updatedfile','file')
                if check==0:
                    print('Record Deleted')
                      
            if n==1:
                read()
            elif n==2:
                write()
            elif n==3:
                append()
            elif n==4:
                update()
            elif n==5:
                search()
            elif n==6:
                delete()
            elif n==7:
                print('EXITING')
                break
            else:
                print('PLEASE CHOOSE A VALID OPTION!')
            print() 
            choice=input('Do you want to continue?(y/n)')
            print()
            
except ValueError or TypeError:
    print('Invalid Data Type!')
    print()