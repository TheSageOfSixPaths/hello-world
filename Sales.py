import pickle
from datetime import date
def createFiles():
    f=open("items.dat","wb")
    f.close()
    f=open("sales.dat","wb")
    f.close()
def addItems():
    codes=[]
    with open("items.dat","rb") as f:
        while True:
            try:
                rec=pickle.load(f)
                codes.append(rec[0])
            except:
                break
    data=[]
    more='y'
    while more in 'yY':
        while True:
            code=input("Enter item code(4 character alphanumeric): ")
            if code in codes:
                print("That code already exists")
            elif len(code) != 4 or  not(code.isalnum()):
                print('Invalid code')
            else: break            
        desc=input("Enter item description (maximum 20 characters) : ")
        desc=desc[:20]    
        price=float(input("Enter selling price: "))
        disc=float(input("Enter discount percent: "))
        qty=float(input("Enter balance quantity: "))
        reLevel=float(input("Enter reorder level: "))
        reQty=float(input("Enter reorder quantity: "))
        rec=[code,desc,price,disc,qty,reLevel,reQty]
        data.append(rec)
        more=input("More data (y/n)? ")
    with open("items.dat","ab") as f:
        for rec in data:
            pickle.dump(rec,f)

def deleteItems():
    codes=[]
    data=[]
    with open("items.dat","rb") as f:
        while True:
            try:
                rec=pickle.load(f)
                data.append(rec)
                codes.append(rec[0])
            except:
                break
    more='y'
    while more in 'yY':
        while True:
            code=input("Enter item code to delete: ")
            if code in codes:
                index=codes.index(code)
                data.pop(index)
                codes.pop(index)
                break
            else: print("That code does not exist, please re-enter")
        more=input("More to delete (y/n)? ")
        
    with open("item.dat","wb") as f:
        for rec in data:
            pickle.dump(rec,f)

def purchaseItems():
    codes=[]
    data=[]
    with open("items.dat","rb") as f:
        while True:
            try:
                rec=pickle.load(f)
                data.append(rec)
                codes.append(rec[0])
            except:
                break
    data=[]
    more='y'
    while more in 'yY':
        while True:
            code=input("Enter item code: ")
            if code in codes:
                index=codes.index(code)
                break
            else: print("That code does not exist, please re-enter")
        qty=float(input("Enter quantity purchased: "))
        data[index][4]+=qty
        more=input("More purchase (y/n)? ")
        
    with open("item.dat","wb") as f:
        for rec in data:
            pickle.dump(rec,f)
            
def updateItems():
    codes=[]
    data=[]
    with open("items.dat","rb") as f:
        while True:
            try:
                rec=pickle.load(f)
                data.append(rec)
                codes.append(rec[0])
            except:
                break
    data=[]
    more='y'
    while more in 'yY':
        while True:
            code=input("Enter item code: ")
            if code in codes:
                index=codes.index(code)
                break
            else: print("That code does not exist, please re-enter")
        print("To update a value, enter new value. To not update it, just press Enter")
        desc=input("Item description (Press Enter to skip) : ")
        if desc=='':
            pass
        else: data[index][1]=desc[:20]    
        price=input("Selling price (Enter to skip): ")
        if price=='':
            pass
        else: data[index][2]=float(price)
        disc=float(input("Discount percent (Enter to skip): "))
        if disc=='':
            pass
        else: data[index][3]=float(disc)
        qty=input("Quantity (Press Enter to skip): ")
        if qty=='':
            pass
        else: data[index][4]=float(qty)
        reLevel=input("Reorder Level (Press Enter to skip): ")
        if reLevel=='':
            pass
        else: data[index][5]=float(reLevel)
        reQty=input("Reorder Quantity (Press Enter to skip): ")
        if reQty=='':
            pass
        else: data[index][6]=float(reQty)
        more=input("More updates (y/n)? ")
        
    with open("item.dat","wb") as f:
        for rec in data:
            pickle.dump(rec,f)

def inventoryReport():    
    '''
XYZ Enterprises ->Center
Inventory Report ->Center
    ============================================================================
    CODE  DESC                  Balance      Unit      Stock   Reorder   Reorder
                                Quantity    Price      Value     Level  Quantity
    1234  12345678901234567890  12345.78  1234.67  123456.89  12345.78  12345.78
    ----------------------------------------------------------------------------
                             Total Stock Value: 123456789.01
    '''
    heading='''============================================================================
CODE  DESC                  Balance      Unit      Stock   Reorder   Reorder
                            Quantity    Price      Value     Level  Quantity
----------------------------------------------------------------------------'''
    gap=' '*2
    today=date.today()
    today = today.strftime("%d/%m/%Y")    
    totalValue=0
    print(f'{"XYZ Enterprises":^76s}')
    print(f'{"Inventory Report":^76s}')
    print(f'{today:>76}')
    print(heading)
    with open("items.dat","rb") as f:
        while True:
            try:
                rec=pickle.load(f)
                value=rec[2]*rec[4]
                totalValue+=value
                rec=f'{rec[0]:4}{gap}{rec[1]:20}{gap}{rec[4]:8.2f}{gap}{rec[2]:7.2f}{gap}\
{value:9.2f}{gap}{rec[5]:8.2f}{gap}{rec[6]:8.2f}'
                print(rec)
            except:
                print('-'*76)
                break
    lastLine=f'{"Total Stock Value:":>46s} {totalValue:9.2f}'
    print(lastLine)
def printBill(salesData):
    today=date.today()
    today = today.strftime("%d/%m/%Y")    
    totalValue=0
    '''
XYZ Enterprises ->Center
Bill ->Center
Date -> Right
    ======================================================================
    SNo.  CODE  DESC                  Quantity    Price     Disc    Amount
    1234  1234  12345678901234567890  12345.78  1234.67  1234.67  12345.78
    ----------------------------------------------------------------------
                                                         Total:12345678.01
    -You are our valued customer. Please visit again
    -No return, No refund
    -Please check your bill and amount before leaving the counter
    '''
    heading='''======================================================================
SNo.  CODE  DESC                  Quantity    Price     Disc    Amount
----------------------------------------------------------------------'''
    gap=' '*2
    print(f'{"XYZ Enterprises":^70s}')
    print(f'{"BILL":^70s}')
    print(f'{today:>70}')
    print(heading)
    sNo=1
    for rec in salesData:
        qty=rec[3]
        price=rec[4]
        discPer=rec[5]
        discVal=price*discPer/100
        value=(price-discVal)*qty
        totalValue+=value
        rec=f'{sNo:4}{gap}{rec[1]:4}{gap}{rec[2 ]:20}{gap}{qty:8.2f}{gap}{price:7.2f}\
{gap}{discVal:7.2f}{gap}{value:8.2f}'
        print(rec)
    print('-'*70)
    lastLine=f'{"Bill total":>59}{totalValue:11.2f}'
    print(lastLine)
    trailer='''-You are our valued customer. Please visit again
-No return, No refund
-Please check your bill and amount before leaving the counter'''
    print(trailer)
    input("Press Enter to continue")
def sale():
    codes=[]
    itemsData=[]
    today=date.today()
    today = today.strftime("%d/%m/%Y")    
    totalValue=0
    with open("items.dat","rb") as f:
        while True:
            try:
                rec=pickle.load(f)
                itemsData.append(rec)
                codes.append(rec[0])
            except:
                break
    salesData=[]
    more='y'
    while more in 'yY':
        while True:
            code=input("Enter item code (Press Enter to terminate): ")
            if code=='':
                break
            if code in codes:
                index=codes.index(code)
                break
            else: print("That code does not exist, please re-enter")
        if code=='':
            break
        desc=itemsData[index][1]
        price=itemsData[index][2]
        discPer=itemsData[index][3]
        discVal=round(price*discPer/100,2)
        sp=price-discVal
        print(f'{desc}-{price}-{discVal}({discPer}%)-{sp}')
        qty=float(input("Enter quantity: "))
        value=qty*sp
        print(value)
        confirm=input("OK (y/n)? ")
        if confirm in 'yY':
            totalValue+=value
            print("Bill Total: ",totalValue)
            rec=[today,code,desc,qty,price,discPer]
            salesData.append(rec)
        print('-'*25)
    printBill(salesData)
    with open("sales.dat","ab") as f:
        for rec in salesData:
            pickle.dump(rec,f)
            

createFiles()
addItems()
inventoryReport()
sale()

    
