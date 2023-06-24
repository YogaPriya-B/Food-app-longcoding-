import time

from datetime import datetime

class FoodApp:
    def __init__(self,userid:int,userpassword:str,username:str,useremail:str,userphn:str):
        self.userid=userid
        self.userpassword=userpassword
        self.username=username
        self.useremail=useremail
        self.userphn=userphn 
        
class login(FoodApp):
    def __init__(self,userid=None,userpassword=None,username=None,useremail=None,userphn=None):
        FoodApp.__init__(self,userid,userpassword,username,useremail,userphn)
        
    def validate(self):
        
        self.userid=int(input())
        self.userpassword=input()
        self.c=userdetails[self.userid]
        if(self.userpassword==self.c[0]):
             self.validation=1
             return True
        else:
            print("Enter correct details !!!")
            self.validate()
            
    def welcomeuser(self):
            self.username=self.c[1]
            self.useremail=self.c[2]
            self.userphn=self.c[3]
            print("login Successful !!")
            print("Welcome user !!",self.username)
            time.sleep(2)

class Signup(FoodApp):
    
    def __init__(self,userid,userpassword,username,useremail,userphn):
        FoodApp.__init__(self,userid,userpassword,username,useremail,userphn)
        l=[]
        l=[self.userpassword,self.username,self.useremail,self.userphn]
        userdetails[self.userid]=l 
    def welcomeuser(self):
        print(self.userid)
        print(" Sigin Successful !!!\n","Welcome user",self.username)
        time.sleep(2)     
        
class restaurants:
    
    def __init__(self,resid=None,resname=None,restype=None,availablefoods=None,ratings=None):
        self.resid=resid
        self.resname=resname
        self.restype=restype
        self.availablefoods=availablefoods
        self.ratings=ratings

    def vegres(self):
        self.l=[]
        res1=restaurants(1,'AB restaurants','Veg',{1:{'Food':'Idli','Price':15},2:{'Food':'Dosa','Price':20}},'* * * *')
        res2=restaurants(2,'ABC restaurants','Veg',{1:{'Food':'Idli','Price':25},2:{'Food':'Dosa','Price':30}},'* * * * *')
        self.l.append(res1)
        self.l.append(res2)
        
        
    def showvegmenu(self):
        for i in self.l:
            print('-------------------------------------------------------')
            print("Restaurant id :",i.resid,"\nRestaurant name :",i.resname)
            print("Ratings :",i.ratings)
            for j in i.availablefoods:
                print('Food id :',j)
                print(i.availablefoods[j]['Food'],"    Rs:",i.availablefoods[j]['Price'])
                time.sleep(2)
            
    def nonvegres(self):
        self.l1=[]
        res1=restaurants(1,'ABD restaurants','Non Veg',{1:{'Food':'Mutton','Price':150},2:{'Food':'Chicken','Price':200}},'* * * *')
        res2=restaurants(2,'ABDR restaurants','Non Veg',{1:{'Food':'Chicken','Price':225},2:{'Food':'Pizza','Price':300}},'* * * * *')
        self.l1.append(res1)
        self.l1.append(res2)
        
    def shownonvegmenu(self):
        for i in self.l1:
            print('-------------------------------------------------------')
            print("Restaurant id :",i.resid,"\nRestaurant name :",i.resname)
            for j in i.availablefoods:
                print('Food id :',j)
                print(i.availablefoods[j]['Food'],"    Rs:",i.availablefoods[j]['Price'])
                time.sleep(2)
class placeorder(restaurants):
    
    def addcart(self):
        self.vegres()
        self.l
        print(self.l)
        c=1
        while c:
            m=int(input("Select the Restaurant id"))
            h=int(input("Enter the foodid"))
            for items in self.l:
                if(items.resid==m):
                    for fooditems in items.availablefoods:
                        if(h==fooditems):
                            cart.append(items.availablefoods[h]['Food'])
                            price.append(items.availablefoods[h]['Price'])
                    
                    
                            
            place=input("ADD items ? y/ Place order p")
            if(place=='y'):
                    c=1
                                        
            elif(place=='p'):
                    c=0
                    self.placeorders()
            else:
                c=0
                        
    def placeorders(self):
        self.s=""
        print("cart",cart)
        print("Price",sum(price))
        self.o=[]
        self.o.append(cart)
        today = datetime.today()
        print(today)
        time=datetime.now()
        self.s+=str(today)
        self.s+=','
        self.s+=str(time)
        history.append(self.s)
        payment=int(input("Choose a payment option"))
        if(payment==1):
            print("Upi transaction Successful")
        elif(payment==2):
            print("G pay Successful")
            
    def bookinghistory(self):
        if len(history)==0:
            print("Booking history is empty")
        else:
            print(history)
            for rt in history:
                history.pop()        
class cartt(placeorder):
    def showcart(self):
        if(len(cart)==0):
            print("Your cart is empty !!")
        else:
            print('Cart',cart)
            print('Do you want to place your order ')
            choice=int(input("Add items -1,Place order-2"))
            if(choice==1):
                self.addcart()
            elif(choice==2):
                self.placeorder()
            else:
                pass

if __name__=='__main__':
    cart=[]
    price=[]
    history=[]
    userdetails={1:['123**','Yoga','yoga@gmail.com',986754321],2:['456','Bharath','bharath@gmail.com',9876466669]}
    n=int(input("Already have an account-1 / Create new account-2: "))
    if(n==1):
        app=login()
        app.validate()
        if(app.validation):
            app.welcomeuser()
    else:
        app=Signup(3,'234**','Saci','Saci@gmail.com',9786453201)
        app.welcomeuser()
    customer=1
    while(customer):
            
            print('-------------------------')
            print('1. Show restaurants ')
            print('2. Order ')
            print('3. Cart')
            print('4. Booking history')
            print('5. Logout')
            time.sleep(2)
            n=int(input("enter the choice"))
            show=restaurants()
            carts=cartt()
            orders=placeorder()
            if(n==1):
                show.vegres()
                show.showvegmenu()
            elif(n==3):
                  carts.showcart()
            elif(n==2):
                 show.vegres()
                 orders.addcart()     
            elif(n==4):
                orders.bookinghistory()
            else:
                customer=0
                
        
    
    
        
    
        
