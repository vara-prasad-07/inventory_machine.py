from tkinter import *
from tkinter import messagebox
import random
import os,tempfile

product_stock = {
    "Bath Soap": 10,
    "Face Cream": 20,
    "Face Wash": 15,
    "Hair Spray": 8,
    "Hair Gel": 5,
    "Body Lotion": 12,
    "Rice": 30,
    "Daal": 25,
    "Oil": 10,
    "Sugar": 20,
    "Tea": 15,
    "Wheat": 18,
    "Maaza": 12,
    "Pepsi": 15,
    "Sprite": 10,
    "Dew": 7,
    "Frooti": 15,
    "Coca Cola": 8,
}

def clear():
    bathsoapEntry.delete(0,END)
    facecreamEntry.delete(0,END)
    hairsprayEntry.delete(0,END)
    hairgelEntry.delete(0,END)
    bodylotionEntry.delete(0,END)
    facewashEntry.delete(0,END)

    daalEntry.delete(0,END)
    wheatEntry.delete(0,END)
    riceEntry.delete(0,END)
    oilEntry.delete(0,END)
    teaEntry.delete(0,END)
    sugarEntry.delete(0,END)

    pepsiEntry.delete(0,END)
    maazaEntry.delete(0,END)
    dewEntry.delete(0,END)
    cocacolaEntry.delete(0,END)
    frootiEntry.delete(0,END)
    spriteEntry.delete(0,END)

    bathsoapEntry.insert(0,0)
    facecreamEntry.insert(0,0)
    hairsprayEntry.insert(0,0)
    hairgelEntry.insert(0,0)
    bodylotionEntry.insert(0,0)
    facewashEntry.insert(0,0)

    daalEntry.insert(0,0)
    wheatEntry.insert(0,0)
    riceEntry.insert(0,0)
    oilEntry.insert(0,0)
    teaEntry.insert(0,0)
    sugarEntry.insert(0,0)

    pepsiEntry.insert(0,0)
    maazaEntry.insert(0,0)
    dewEntry.insert(0,0)
    cocacolaEntry.insert(0,0)
    frootiEntry.insert(0,0)
    spriteEntry.insert(0,0)

    cosmetictaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    colddrinktaxEntry.delet(0,END)

    cosmeticpriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    colddrinkpriceEntry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)

    textarea.delete(1.0,END)


def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')


def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billnumberEntry.get():
            f=open(f'bills/{i}','r')
            textarea.delete('1.0',END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break 
        #else:
            #messagebox.showerror('Error','Invalid Bill Number')

if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumber
    result=messagebox.askyesno('Confire','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/ {billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill Number {billnumber} is saved successfully')
        billnumber=random.randint(500,1000)

billnumber=random.randint(500,1000)

def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details Are Required')
    elif cosmeticpriceEntry.get()=='' or grocerypriceEntry.get()==''or colddrinkpriceEntry.get()=='':
        messagebox.showerror('Error','No products are selected')
    elif cosmeticpriceEntry.get()=='0 Rs' and grocerypriceEntry.get()=='0 Rs' and colddrinkpriceEntry.get()=='0 Rs':
        messagebox.showerror('Error','No products are selected')
    else:
        textarea.delete(1.0,END)
    
        textarea.insert(END,'\t\t**Welcome Customer**\n')
        textarea.insert(END,f'\nBillNumber: {billnumber}\n')
        textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}\n')
        textarea.insert(END,f'\nCustomer Phone Number: {phoneEntry.get()}\n')
        textarea.insert(END,'\n=======================================================')
        textarea.insert(END,'Product\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END,'\n=======================================================')
        if bathsoapEntry.get()!='0':
            textarea.insert(END,f'\nBath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs')
        if hairsprayEntry.get()!='0':
            textarea.insert(END,f'\nHair Spray Soap\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs')
        if facewashEntry.get()!='0':
            textarea.insert(END,f'\nFace Wash Soap\t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs')
        if facecreamEntry.get()!='0':
            textarea.insert(END,f'\nFace Cream Soap\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs')
        if hairgelEntry.get()!='0':
            textarea.insert(END,f'\nHair Gel Soap\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs')
        if bodylotionEntry.get()!='0':
            textarea.insert(END,f'\nBody Lotion Soap\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Rs')
    
        if riceEntry.get()!='0':
            textarea.insert(END,f'\nRice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs')
        if daalEntry.get()!='0':
           textarea.insert(END,f'\ndaal\t\t\t{daalEntry.get()}\t\t\t{daalprice} Rs')
        if oilEntry.get()!='0':
            textarea.insert(END,f'\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs')
        if sugarEntry.get()!='0':
            textarea.insert(END,f'\nSugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Rs')
        if teaEntry.get()!='0':
            textarea.insert(END,f'\nTea\t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs')
        if wheatEntry.get()!='0':
            textarea.insert(END,f'\nWheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rs')

        if maazaEntry.get()!='0':
            textarea.insert(END,f'\nMaaza\t\t\t{maazaEntry.get()}\t\t\t{maazaprice} Rs')
        if frootiEntry.get()!='0':
            textarea.insert(END,f'\nFrooti\t\t\t{frootiEntry.get()}\t\t\t{frootiprice} Rs')
        if dewEntry.get()!='0':
            textarea.insert(END,f'\nDew\t\t\t{dewEntry.get()}\t\t\t{dewprice} Rs')
        if pepsiEntry.get()!='0':
            textarea.insert(END,f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Rs')
        if spriteEntry.get()!='0':
            textarea.insert(END,f'\nSprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice} Rs')
        if cocacolaEntry.get()!='0':
            textarea.insert(END,f'\nCoca cola\t\t\t{cocacolaEntry.get()}\t\t\t{cocacolaprice} Rs')
        textarea.insert(END,'\n-------------------------------------------------------')

        if cosmetictaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nCosmetic Tax\t\t\t\t {cosmetictaxEntry.get()}')
        if grocerytaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nGrocery Tax\t\t\t\t {grocerytaxEntry.get()}')
        if colddrinktaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nCold Drink Tax\t\t\t\t {colddrinktaxEntry.get()}')
        textarea.insert(END,f'\n\nTotal Bill \t\t\t\t {totalbill}')
        textarea.insert(END,'\n-------------------------------------------------------')
        save_bill()

def total():
    global soapprice,hairsprayprice,facewashprice,facecreamprice,hairgelprice,bodylotionprice
    global riceprice,daalprice,oilprice,sugarprice,teaprice,wheatprice
    global maazaprice,frootiprice,dewprice,pepsiprice,spriteprice,cocacolaprice
    global totalbill

    soapprice=int(bathsoapEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*50
    facewashprice=int(facewashEntry.get())*100
    hairsprayprice=int(hairsprayEntry.get())*150
    hairgelprice=int(hairgelEntry.get())*80
    bodylotionprice=int(bodylotionEntry.get())*60

    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,f'{totalcosmeticprice}'+' Rs')
    cosmetictax=totalcosmeticprice*0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,str(cosmetictax)+' Rs')
                              
    riceprice=int(riceEntry.get())*30
    daalprice=int(daalEntry.get())*100
    oilprice=int(oilEntry.get())*120
    sugarprice=int(sugarEntry.get())*50
    teaprice=int(teaEntry.get())*140
    wheatprice=int(wheatEntry.get())*80

    totalgroceryprice=riceprice+daalprice+oilprice+sugarprice+teaprice+wheatprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,f'{totalgroceryprice}'+' Rs')
    grocerytax=totalgroceryprice*0.12
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,str(grocerytax)+' Rs')

    maazaprice=int(maazaEntry.get())*50
    frootiprice=int(frootiEntry.get())*20
    dewprice=int(dewEntry.get())*30
    pepsiprice=int(pepsiEntry.get())*20
    spriteprice=int(spriteEntry.get())*45
    cocacolaprice=int(cocacolaEntry.get())*90

    totalcolddrinkprice=maazaprice+frootiprice+dewprice+pepsiprice+spriteprice+cocacolaprice
    colddrinkpriceEntry.delete(0,END)
    colddrinkpriceEntry.insert(0,f'{totalcolddrinkprice}'+' Rs')
    colddrinktax=totalcolddrinkprice*0.12
    colddrinktaxEntry.delete(0,END)
    colddrinktaxEntry.insert(0,str(colddrinktax)+' Rs')

    totalbill=totalcosmeticprice+totalgroceryprice+totalcolddrinkprice+cosmetictax+grocerytax+colddrinktax


#gui
root = Tk()
root.title('Retail Billing System')
root.geometry('1270x685')

headingLabel=Label(root,text='Inventory Management System',font=('times new roman',30,'bold'),bg='slate gray',fg='black',bd=12,relief=FLAT)
headingLabel.pack(fill=X)
customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),fg='black',bd=8,relief=GROOVE,bg='slate gray')
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='slate gray',fg='black')
nameLabel.grid(row=0,column=0,padx=20,pady=2)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18,)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='slate gray',fg='black')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18,)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='slate gray',fg='black')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10,command=search_bill())
searchButton.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack()

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),fg='black',bd=8,relief=GROOVE,bg='brown2')
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel=Label(cosmeticsFrame,text='Bath Soap',font=('times new roman',14,'bold'),bg='brown2',fg='black')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10,sticky='w')
bathsoapEntry.insert(0,0)

facecreamLabel=Label(cosmeticsFrame,text='Face Cream',font=('times new roman',15,'bold'),bg='brown2',fg='black')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',14,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')
facecreamEntry.insert(0,0)


facewashLabel=Label(cosmeticsFrame,text='Face Wash',font=('times new roman',15,'bold'),bg='brown2',fg='black')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

facewashEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')
facewashEntry.insert(0,0)


hairsprayLabel=Label(cosmeticsFrame,text='Hair Spray',font=('times new roman',15,'bold'),bg='brown2',fg='black')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

hairsprayEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10,sticky='w')
hairsprayEntry.insert(0,0)


hairgelLabel=Label(cosmeticsFrame,text='Hair Gel',font=('times new roman',15,'bold'),bg='brown2',fg='black')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

hairgelEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10,sticky='w')
hairgelEntry.insert(0,0)


bodylotionLabel=Label(cosmeticsFrame,text='Body Lotion',font=('times new roman',15,'bold'),bg='brown2',fg='black')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10,sticky='w')
bodylotionEntry.insert(0,0)


groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),fg='black',bd=8,relief=GROOVE,bg='gold')
groceryFrame.grid(row=0,column=1)

riceLabel=Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),bg='gold',fg='black')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

riceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10,sticky='w')
riceEntry.insert(0,0)


oilLabel=Label(groceryFrame,text='Oil',font=('times new roman',15,'bold'),bg='gold',fg='black')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

oilEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')
oilEntry.insert(0,0)


daalLabel=Label(groceryFrame,text='Daal',font=('times new roman',15,'bold'),bg='gold',fg='black')
daalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

daalEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
daalEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')
daalEntry.insert(0,0)


wheatLabel=Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold'),bg='gold',fg='black')
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

wheatEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
wheatEntry.grid(row=3,column=1,pady=9,padx=10,sticky='w')
wheatEntry.insert(0,0)


sugarLabel=Label(groceryFrame,text='Sugar',font=('times new roman',15,'bold'),bg='gold',fg='black')
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

sugarEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sugarEntry.grid(row=4,column=1,pady=9,padx=10,sticky='w')
sugarEntry.insert(0,0)


teaLabel=Label(groceryFrame,text='Tea',font=('times new roman',15,'bold'),bg='gold',fg='black')
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

teaEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
teaEntry.grid(row=5,column=1,pady=9,padx=10,sticky='w')
teaEntry.insert(0,0)

colddrinkFrame=LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',15,'bold'),fg='black',bd=8,relief=GROOVE,bg='cyan4')
colddrinkFrame.grid(row=0,column=2)

maazaLabel=Label(colddrinkFrame,text='Maaza',font=('times new roman',15,'bold'),bg='cyan4',fg='black')
maazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

maazaEntry=Entry(colddrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
maazaEntry.grid(row=0,column=1,pady=9,padx=10,sticky='w')
maazaEntry.insert(0,0)

pepsiLabel=Label(colddrinkFrame,text='Pepsi',font=('times new roman',15,'bold'),bg='cyan4',fg='black')
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

pepsiEntry=Entry(colddrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')
pepsiEntry.insert(0,0)


spriteLabel=Label(colddrinkFrame,text='Sprite',font=('times new roman',15,'bold'),bg='cyan4',fg='black')
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

spriteEntry=Entry(colddrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')
spriteEntry.insert(0,0)


dewLabel=Label(colddrinkFrame,text='Dew',font=('times new roman',15,'bold'),bg='cyan4',fg='black')
dewLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

dewEntry=Entry(colddrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
dewEntry.grid(row=3,column=1,pady=9,padx=10,sticky='w')
dewEntry.insert(0,0)


frootiLabel=Label(colddrinkFrame,text='Frooti',font=('times new roman',15,'bold'),bg='cyan4',fg='black')
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

frootiEntry=Entry(colddrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
frootiEntry.grid(row=4,column=1,pady=9,padx=10,sticky='w')
frootiEntry.insert(0,0)


cocacolaLabel=Label(colddrinkFrame,text='Coca Cola',font=('times new roman',15,'bold'),bg='cyan4',fg='black')
cocacolaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

cocacolaEntry=Entry(colddrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cocacolaEntry.grid(row=5,column=1,pady=9,padx=10,sticky='w')
cocacolaEntry.insert(0,0)


billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

scrollbar  =Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
textarea=Text(billframe, height=18, width=55, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Customer Details',font=('times new roman',16,'bold'),fg='black',bd=8,relief=GROOVE,bg='dark slate gray')
billmenuFrame.pack()

cosmeticpriceLabel=Label(billmenuFrame,text='Cosmetics Price',font=('times new roman',16,'bold'),bg='dark slate gray',fg='black')
cosmeticpriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')

cosmeticpriceEntry=Entry(billmenuFrame,font=('times new roman',16,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=6,padx=10,sticky='w')

grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=('times new roman',16,'bold'),bg='dark slate gray',fg='black')
grocerypriceLabel.grid(row=1,column=0,pady=6,padx=10,sticky='w')

grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',16,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10,sticky='w')

colddrinkpriceLabel=Label(billmenuFrame,text='Cold Drink Price',font=('times new roman',16,'bold'),bg='dark slate gray',fg='black')
colddrinkpriceLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

colddrinkpriceEntry=Entry(billmenuFrame,font=('times new roman',16,'bold'),width=10,bd=5)
colddrinkpriceEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')

cosmetictaxLabel=Label(billmenuFrame,text='Cosmetics Tax',font=('times new roman',16,'bold'),bg='dark slate gray',fg='black')
cosmetictaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')

cosmetictaxEntry=Entry(billmenuFrame,font=('times new roman',16,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=6,padx=10,sticky='w')

grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax',font=('times new roman',16,'bold'),bg='dark slate gray',fg='black')
grocerytaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')

grocerytaxEntry=Entry(billmenuFrame,font=('times new roman',16,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10,sticky='w')

colddrinktaxLabel=Label(billmenuFrame,text='Cold Drink Tax',font=('times new roman',16,'bold'),bg='dark slate gray',fg='black')
colddrinktaxLabel.grid(row=2,column=2,pady=9,padx=10,sticky='w')

colddrinktaxEntry=Entry(billmenuFrame,font=('times new roman',16,'bold'),width=10,bd=5)
colddrinktaxEntry.grid(row=2,column=3,pady=9,padx=10,sticky='w')

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4)

totalButton=Button(buttonFrame,text='Total',font=('arial',14,'bold'),bg='dark slate gray',fg='black',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text='Bill',font=('arial',14,'bold'),bg='dark slate gray',fg='black',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',font=('arial',14,'bold'),bg='dark slate gray',fg='black',bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text='Clear',font=('arial',14,'bold'),bg='dark slate gray',fg='black',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)



root.mainloop()