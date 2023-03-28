from tkinter import*
from datetime import date
from random import *
from turtle import *

#Creating welcome window
root = Tk()
root.geometry("1500x800+0+0")
root.configure(bg='light blue')
root.title("RESTAURANT MANAGEMENT SYSTEM")

d = []
today = date.today()

#Specifying the font 
Font_tuple1 = ("Times New Roman", 40, "bold")

#Creating a label to display welcome 
label1 = Label(root, text = "Welcome to Quattro", bg = "light blue", fg = "black")
label1.place(relx = 0.5, rely = 0.5, anchor = 'center')
label1.configure(font = Font_tuple1)
check = False
#Defining function to book a table
def book_table():
    root1 = Tk()
    root1.geometry("1500x800+0+0")
    root1.configure(bg='light blue')
    root1.title("TABLE BOOKING")
    label = Label(root1, text = ' ' , bg = 'light blue').grid(row = 0, column = 0)
    label = Label(root1, text = ' ' , bg = 'light blue').grid(row = 1, column = 1)
    label = Label(root1, text = ' ' , bg = 'light blue').grid(row = 2, column = 2)
    label = Label(root1, text = ' ' , bg = 'light blue').grid(row = 3, column = 3)
    label2 = Label(root1, text = "Please enter the number of seats you want to book: " , bg = "dark blue", font = ("Times New Roman",20,"bold"))
    label2.grid(row = 4, column = 4)
    entry1 = Entry(root1, width = 50 , highlightbackground="light blue")
    entry1.grid(row = 4, column = 5)
    entry1.insert(0,'Maximum number of people allowed is 25')
    button3 = Button(root1, text = 'Click here to view the menu' , command = soups_salads, highlightbackground = "dark blue", font = ("Times New Roman",25,"bold"))
    button3.place(rely = 1.0, relx = 1.0, x = 0, y = 0, anchor = SE)
#Defining function to confirm the table
    def welcome():
        a = int(entry1.get())
        if a<=25:
            message1 = "Your table for " + entry1.get() + " people has been booked"
            label3 = Label(root1, text = message1 , bg = "dark blue", fg = "black", font = ("Times New Roman",20,"bold"))
            label3.place(relx = 0.5 , rely = 0.5 , anchor = 'center')
        else:
            message2 = "Sorry, your table for " + entry1.get() + " people cannot be booked. The maximum number of people allowed is 25"
            label4 = Label(root1, text = message2, bg = "dark blue", fg = "black", font = ("Times New Roman",20,"bold"))
            label4.place(relx = 0.5 , rely = 0.5 , anchor = 'center')
    label = Label(root1, text = ' ' , bg = 'light blue').grid(row = 5, column = 5)
    button2 = Button(root1, width = 25, text = 'Click here to enter', command = welcome, highlightbackground="dark blue", font = ("Times New Roman",16,"bold"))
    button2.grid(row = 6, column = 5)

#Creating button to book table 
button1 = Button(root, text='Click here to book a table', command = book_table, highlightbackground = "dark blue", font = ("Times New Roman",25,"bold"))
button1.place(rely = 1.0, relx = 1.0, x = 0, y = 0, anchor = SE)

#Creating window to display menu
#Soups and Salads
def soups_salads():
    root2 = Tk()
    root2.geometry("1500x800+0+0")
    root2.configure(bg='light blue')
    root2.title("MENU")
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 0, column = 0)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 0, column = 1)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 0, column = 2)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 0, column = 3)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 0, column = 4)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 0, column = 5)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 0, column = 6)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 0, column = 7)
    label5 = Label(root2, text = "SOUPS & SALADS", bg = 'dark blue',font = ("Times New Roman",27,"bold"))
    label5.grid(row = 0, column = 8)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 1, column = 8)
    label6 = Label(root2, text = 'Tomato Soup', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 5, column = 8)
    label7 = Label(root2, text = 'Manchow Soup', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 6, column = 8)
    label8 = Label(root2, text = 'Cream of Mushroom', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 7, column = 8)
    label9 = Label(root2, text = 'Cream of Chicken', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 8, column = 8)
    label10 = Label(root2, text = 'Hot and Sour Soup', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 9, column = 8)
    label11 = Label(root2, text = 'Clear Soup', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 10, column = 8)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 11, column = 8)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 12, column = 8)
    label12 = Label(root2, text = 'Pasta Salad', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 13, column = 8)
    label13 = Label(root2, text = 'Caesar Salad', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 14, column = 8)
    label14 = Label(root2, text = 'Russian Salad', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 15, column = 8)
    label15 = Label(root2, text = 'Greek Salad', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 16, column = 8)
    label16 = Label(root2, text = 'Crunchy Chicken Salad', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 17, column = 8)
    label17 = Label(root2, text = 'Mexican Nachos Grande', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 18, column = 8)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 19, column = 8)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 20, column = 8)
    label18 = Label(root2, text = "EGGS TO ORDER", bg = 'dark blue',font = ("Times New Roman",27,"bold")).grid(row = 21, column = 8)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 22, column = 8)
    label19 = Label(root2, text = 'Omlette(Served with toast)', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 24, column = 8)
    label20 = Label(root2, text = 'Scrambled Eggs', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 25, column = 8)
    label21 = Label(root2, text = 'Fried Eggs', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 26, column = 8)
    label22 = Label(root2, text = 'French Toast(Served with Maple Syrup)', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 27, column = 8)
    
    #Prices
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 0, column = 9)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 1, column = 10)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 2, column = 11)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 2, column = 12)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 2, column = 13)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 2, column = 14)
    label23 = Label(root2, text = "PRICES", bg = 'dark blue',font = ("Times New Roman",27,"bold"))
    label23.grid(row = 0, column = 15)
    label24 = Label(root2, text = '140', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 5, column = 15)
    label25 = Label(root2, text = '140', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 6, column = 15)
    label26 = Label(root2, text = '150', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 7, column = 15)
    label27 = Label(root2, text = '150', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 8, column = 15)
    label28 = Label(root2, text = '140', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 9, column = 15)
    label29 = Label(root2, text = '120', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 10, column = 15)
    label30 = Label(root2, text = '160', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 13, column = 15)
    label31 = Label(root2, text = '160', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 14, column = 15)
    label32 = Label(root2, text = '140', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 15, column = 15)
    label33 = Label(root2, text = '160', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 16, column = 15)
    label34 = Label(root2, text = '210', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 17, column = 15)
    label35 = Label(root2, text = '210', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 18, column = 15)
    label36 = Label(root2, text = '130', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 24, column = 15)
    label37 = Label(root2, text = '110', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 25, column = 15)
    label38 = Label(root2, text = '110', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 26, column = 15)
    label39 = Label(root2, text = '100', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 27, column = 15)
    button4 = Button(root2, text = 'Click here to view further' , command = appetizers, highlightbackground = "dark blue", font = ("Times New Roman",25,"bold"))
    button4.place(rely = 1.0, relx = 1.0, x = 0, y = 0, anchor = SE)

    #Order
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 0, column = 16)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 1, column = 17)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 2, column = 18)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 2, column = 19)
    b1 = Button(root2, text = '0rder ' , command = lambda:bill('Tomato Soup', 140) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 5, column = 22)
    b2 = Button(root2, text = '0rder ' , command = lambda:bill('Manchow Soup', 140), highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 6, column = 22)
    b3 = Button(root2, text = '0rder ' , command = lambda:bill('Cream of Mushroom', 150) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 7, column = 22)
    b4 = Button(root2, text = '0rder ' , command = lambda:bill('Cream of Chicken', 150) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 8, column = 22)
    b5 = Button(root2, text = '0rder ' , command = lambda:bill('Hot and Sour Soup', 140) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 9, column = 22)
    b6 = Button(root2, text = '0rder ' , command = lambda:bill('Clear Soup', 120) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 10, column = 22)
    b7 = Button(root2, text = '0rder ' , command = lambda:bill('Pasta Salad', 160) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 13, column = 22)
    b8 = Button(root2, text = '0rder ' , command = lambda:bill('Caesar Salad', 160) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 14, column = 22)
    b9 = Button(root2, text = '0rder ' , command = lambda:bill('Russian Salad', 140) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 15, column = 22)
    b10 = Button(root2, text = '0rder ' , command = lambda:bill('Greek Salad', 160) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 16, column = 22)
    b11 = Button(root2, text = '0rder ' , command = lambda:bill('Crunchy Chicken Salad', 210) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 17, column = 22)
    b12 = Button(root2, text = '0rder ' , command = lambda:bill('Mexican Nachos Grande', 210) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 18, column = 22)
    b13 = Button(root2, text = '0rder ' , command = lambda:bill('Omlette(Served with toast)', 130) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 24, column = 22)
    b14 = Button(root2, text = '0rder ' , command = lambda:bill('Scrambled Eggs', 110) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 25, column = 22)
    b15 = Button(root2, text = '0rder ' , command = lambda:bill('Fried Eggs', 110) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 26, column = 22)
    b16 = Button(root2, text = '0rder ' , command = lambda:bill('French Toast(Served with Maple Syrup)', 100) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 27, column = 22)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 2, column = 23)
    label = Label(root2, text = ' ' , bg = 'light blue').grid(row = 2, column = 24)
#Cancel
    b1 = Button(root2, text = 'Cancel ' , command = lambda:cancel('Tomato Soup', 140) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 5, column = 25)
    b2 = Button(root2, text = 'Cancel ' , command = lambda:cancel('Manchow Soup', 140), highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 6, column = 25)
    b3 = Button(root2, text = 'Cancel ' , command = lambda:cancel('Cream of Mushroom', 150) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 7, column = 25)
    b4 = Button(root2, text = 'Cancel ' , command = lambda:cancel('Cream of Chicken', 150) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 8, column = 25)
    b5 = Button(root2, text = 'Cancel ' , command = lambda:cancel('Hot and Sour Soup', 140) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 9, column = 25)
    b6 = Button(root2, text = 'Cancel ' , command = lambda:cancel('Clear Soup', 120) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 10, column = 25)
    b7 = Button(root2, text = 'Cancel ' , command = lambda:cancel('Pasta Salad', 160) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 13, column = 25)
    b8 = Button(root2, text = 'Cancel ' , command = lambda:cancel('Caesar Salad', 160) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 14, column = 25)
    b9 = Button(root2, text = 'Cancel ' , command = lambda:cancel('Russian Salad', 140) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 15, column = 25)
    b10 = Button(root2, text = 'Cancel ' , command = lambda:cancel('Greek Salad', 160) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 16, column = 25)
    b11 = Button(root2, text = 'Cancel ' , command = lambda:cancel('Crunchy Chicken Salad', 210) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 17, column = 25)
    b12 = Button(root2, text = 'Cancel ' , command = lambda:cancel('Mexican Nachos Grande', 210) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 18, column = 25)
    b13 = Button(root2, text = 'Cancel ' , command = lambda:cancel('Omlette(Served with toast)', 130) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 24, column = 25)
    b14 = Button(root2, text = 'Cancel ' , command = lambda:cancel('Scrambled Eggs', 110) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 25, column = 25)
    b15 = Button(root2, text = 'Cancel ' , command = lambda:cancel('Fried Eggs', 110) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 26, column = 25)
    b16 = Button(root2, text = 'Cancel ' , command = lambda:cancel('French Toast(Served with Maple Syrup)', 100) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 27, column = 25)

    
def appetizers():
    root3 = Tk()
    root3.geometry("1500x800+0+0")
    root3.configure(bg='light blue')
    root3.title("MENU")
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 0, column = 0)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 0, column = 1)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 0, column = 2)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 0, column = 3)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 0, column = 4)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 0, column = 5)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 0, column = 6)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 0, column = 7)
    label40 = Label(root3, text = "APPETIZERS", bg = 'dark blue',font = ("Times New Roman",27,"bold"))
    label40.grid(row = 0, column = 8)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 1, column = 8)
    label41 = Label(root3, text = 'Chilli Paneer', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 5, column = 8)
    label41 = Label(root3, text = 'Chilli Potato', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 6, column = 8)
    label42 = Label(root3, text = 'Thai BBQ Cottage Cheese', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 7, column = 8)
    label43 = Label(root3, text = 'Salt and Pepper Baby Corn', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 8, column = 8)
    label44 = Label(root3, text = 'Spring Rolls', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 9, column = 8)
    label45 = Label(root3, text = 'Chilli Chicken', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 10, column = 8)
    label46 = Label(root3, text = 'Salt and Pepper Chicken', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 11, column = 8)
    label47 = Label(root3, text = 'Fish in Chilli Mustard', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 12, column = 8)
    label48 = Label(root3, text = 'Korean Chilli Prawns', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 13, column = 8)
    label49 = Label(root3, text = 'Paneer Tikka', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 14, column = 8)
    label50 = Label(root3, text = 'Tandoori Stuffed Mushroom', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 15, column = 8)
    label51 = Label(root3, text = 'Fried Peanut Masala', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 16, column = 8)
    label52 = Label(root3, text = 'Chicken Tikka', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 17, column = 8)
    label53 = Label(root3, text = 'Ghee Roast Chicken', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 18, column = 8)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 19, column = 8)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 20, column = 8)
    label54 = Label(root3, text = "ORIENTAL BOWLS", bg = 'dark blue',font = ("Times New Roman",27,"bold")).grid(row = 21, column = 8)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 22, column = 8)
    label55 = Label(root3, text = 'Thai Curry and Garlic Rice', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 23, column = 8)
    label56 = Label(root3, text = 'Stir Fry Noodles', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 24, column = 8)
    label57 = Label(root3, text = 'Rice Bowl', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 25, column = 8)
    
    #Prices
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 1, column = 10)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 1, column = 11)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 2, column = 12)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 2, column = 13)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 2, column = 14)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 2, column = 15)
    label58 = Label(root3, text = "PRICES", bg = 'dark blue',font = ("Times New Roman",27,"bold"))
    label58.grid(row = 0, column = 16)
    label59 = Label(root3, text = '250', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 5, column = 16)
    label60 = Label(root3, text = '200', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 6, column = 16)
    label61 = Label(root3, text = '250', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 7, column = 16)
    label62 = Label(root3, text = '200', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 8, column = 16)
    label63 = Label(root3, text = '200', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 9, column = 16)
    label64 = Label(root3, text = '250', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 10, column = 16)
    label65 = Label(root3, text = '250', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 11, column = 16)
    label66 = Label(root3, text = '450', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 12, column = 16)
    label67 = Label(root3, text = '400', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 13, column = 16)
    label68 = Label(root3, text = '250', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 14, column = 16)
    label69 = Label(root3, text = '250', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 15, column = 16)
    label70 = Label(root3, text = '200', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 16, column = 16)
    label71 = Label(root3, text = '300', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 17, column = 16)
    label72 = Label(root3, text = '300', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 18, column = 16)
    label73 = Label(root3, text = '300', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 23, column = 16)
    label74 = Label(root3, text = '250', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 24, column = 16)
    label75 = Label(root3, text = '300', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 25, column = 16)
    button5 = Button(root3, text = 'Click here to view further' , command = pizza, highlightbackground = "dark blue", font = ("Times New Roman",25,"bold"))
    button5.place(rely = 1.0, relx = 1.0, x = 0, y = 0, anchor = SE)

    #order
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 1, column = 16)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 1, column = 17)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 2, column = 18)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 2, column = 19)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 2, column = 20)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 2, column = 21)
    b17 = Button(root3, text = '0rder ' , command = lambda:bill('Chilli Paneer', 250) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 5, column = 22)
    b18 = Button(root3, text = '0rder ' , command = lambda:bill('Chilli Potato', 200), highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 6, column = 22)
    b19 = Button(root3, text = '0rder ' , command = lambda:bill('Thai BBQ Cottage Cheese', 250) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 7, column = 22)
    b20 = Button(root3, text = '0rder ' , command = lambda:bill('Salt and Pepper Baby Corn', 200) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 8, column = 22)
    b21 = Button(root3, text = '0rder ' , command = lambda:bill('Spring Rolls', 200) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 9, column = 22)
    b22 = Button(root3, text = '0rder ' , command = lambda:bill('Chilli Chicken', 250) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 10, column = 22)
    b23 = Button(root3, text = '0rder ' , command = lambda:bill('Salt and Pepper Chicken', 250) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 11, column = 22)
    b24 = Button(root3, text = '0rder ' , command = lambda:bill('Fish in Chilli Mustard', 450) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 12, column = 22)
    b25 = Button(root3, text = '0rder ' , command = lambda:bill('Korean Chilli Prawns', 400) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 13, column = 22)
    b26 = Button(root3, text = '0rder ' , command = lambda:bill('Paneer Tikka', 250) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 14, column = 22)
    b27 = Button(root3, text = '0rder ' , command = lambda:bill('Tandoori Stuffed Mushroom', 250) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 15, column = 22)
    b28 = Button(root3, text = '0rder ' , command = lambda:bill('Fried Peanut Masala', 200) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 16, column = 22)
    b29 = Button(root3, text = '0rder ' , command = lambda:bill('Chicken Tikka', 300) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 17, column = 22)
    b30 = Button(root3, text = '0rder ' , command = lambda:bill('Ghee Roast Chicken', 300) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 18, column = 22)
    b31 = Button(root3, text = '0rder ' , command = lambda:bill('Thai Curry and Garlic Rice', 300) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 23, column = 22)
    b32 = Button(root3, text = '0rder ' , command = lambda:bill('Stir Fry Noodles', 250) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 24, column = 22)
    b33 = Button(root3, text = '0rder ' , command = lambda:bill('Rice Bowl', 300) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 25, column = 22)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 2, column = 23)
    label = Label(root3, text = ' ' , bg = 'light blue').grid(row = 2, column = 24)

    #Cancel
    b17 = Button(root3, text = 'Cancel ' , command = lambda:cancel('Chilli Paneer', 250) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 5, column = 25)
    b18 = Button(root3, text = 'Cancel ' , command = lambda:cancel('Chilli Potato', 200), highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 6, column = 25)
    b19 = Button(root3, text = 'Cancel ' , command = lambda:cancel('Thai BBQ Cottage Cheese', 250) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 7, column = 25)
    b20 = Button(root3, text = 'Cancel ' , command = lambda:cancel('Salt and Pepper Baby Corn', 200) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 8, column = 25)
    b21 = Button(root3, text = 'Cancel ' , command = lambda:cancel('Spring Rolls', 200) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 9, column = 25)
    b22 = Button(root3, text = 'Cancel ' , command = lambda:cancel('Chilli Chicken', 250) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 10, column = 25)
    b23 = Button(root3, text = 'Cancel ' , command = lambda:cancel('Salt and Pepper Chicken', 250) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 11, column = 25)
    b24 = Button(root3, text = 'Cancel ' , command = lambda:cancel('Fish in Chilli Mustard', 450) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 12, column = 25)
    b25 = Button(root3, text = 'Cancel ' , command = lambda:cancel('Korean Chilli Prawns', 400) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 13, column = 25)
    b26 = Button(root3, text = 'Cancel ' , command = lambda:cancel('Paneer Tikka', 250) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 14, column = 25)
    b27 = Button(root3, text = 'Cancel ' , command = lambda:cancel('Tandoori Stuffed Mushroom', 250) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 15, column = 25)
    b28 = Button(root3, text = 'Cancel ' , command = lambda:cancel('Fried Peanut Masala', 200) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 16, column = 25)
    b29 = Button(root3, text = 'Cancel ' , command = lambda:cancel('Chicken Tikka', 300) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 17, column = 25)
    b30 = Button(root3, text = 'Cancel ' , command = lambda:cancel('Ghee Roast Chicken', 300) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 18, column = 25)
    b31 = Button(root3, text = 'Cancel ' , command = lambda:cancel('Thai Curry and Garlic Rice', 300) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 23, column = 25)
    b32 = Button(root3, text = 'Cancel ' , command = lambda:cancel('Stir Fry Noodles', 250) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 24, column = 25)
    b33 = Button(root3, text = 'Cancel ' , command = lambda:cancel('Rice Bowl', 300) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 25, column = 25)
def pizza():
    root4 = Tk()
    root4.geometry("1500x800+0+0")
    root4.configure(bg='light blue')
    root4.title("MENU")
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 0, column = 0)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 0, column = 1)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 0, column = 2)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 0, column = 3)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 0, column = 4)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 0, column = 5)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 0, column = 6)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 0, column = 7)
    label76 = Label(root4, text = "PIZZAS", bg = 'dark blue',font = ("Times New Roman",27,"bold"))
    label76.grid(row = 0, column = 8)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 1, column = 8)
    label77 = Label(root4, text = 'Margherita', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 5, column = 8)
    label78 = Label(root4, text = 'Garden Pizza', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 6, column = 8)
    label79 = Label(root4, text = 'Peri Peri Fanatics', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 7, column = 8)
    label80 = Label(root4, text = 'Indian Tikka Pizza', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 8, column = 8)
    label81 = Label(root4, text = 'Meat Lovers', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 9, column = 8)
    label82 = Label(root4, text = 'Pepperoni pizza', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 10, column = 8)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 11, column = 8)
    label83 = Label(root4, text = "PASTA", bg = 'dark blue',font = ("Times New Roman",27,"bold")).grid(row = 13, column = 8)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 14, column = 8)
    label84 = Label(root4, text = 'Pesto', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 15, column = 8)
    label85 = Label(root4, text = 'Pasta Arabiata', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 16, column = 8)
    label86 = Label(root4, text = 'Creamy Cheese Sauce', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 17, column = 8)
    label87 = Label(root4, text = 'Italian Pasta Alfredo', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 18, column = 8)
    label88 = Label(root4, text = 'Olive Blasta Pasta', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 19, column = 8)
    label89 = Label(root4, text = 'Spaghetti Carbanora(Chicken)', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 20, column = 8)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 21, column = 8)
    label90 = Label(root4, text = "BURGERS", bg = 'dark blue',font = ("Times New Roman",27,"bold"))
    label90.grid(row = 22, column = 8)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 23, column = 8)
    label91 = Label(root4, text = 'Crunchy Veg Burger', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 24, column = 8)
    label92 = Label(root4, text = 'Cottage Cheese Burger', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 25, column = 8)
    label93 = Label(root4, text = 'Peri Peri Paneer', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 26, column = 8)
    label94 = Label(root4, text = 'Tex Mex Chicken Burger', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 27, column = 8)
    label95 = Label(root4, text = 'Lamb Burger', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 28, column = 8)
    label96 = Label(root4, text = 'Fish Fillet Burger', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 29, column = 8)

    #Prices
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 0, column = 9)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 1, column = 10)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 2, column = 11)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 2, column = 12)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 2, column = 13)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 2, column = 14)
    label97 = Label(root4, text = "PRICES", bg = 'dark blue',font = ("Times New Roman",27,"bold"))
    label97.grid(row = 0, column = 15)
    label98 = Label(root4, text = '350', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 5, column = 15)
    label99 = Label(root4, text = '350', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 6, column = 15)
    label100 = Label(root4, text = '400', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 7, column = 15)
    label101 = Label(root4, text = '350', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 8, column = 15)
    label102 = Label(root4, text = '450', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 9, column = 15)
    label103 = Label(root4, text = '450', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 10, column = 15)
    label104 = Label(root4, text = '300', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 15, column = 15)
    label105 = Label(root4, text = '350', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 16, column = 15)
    label106 = Label(root4, text = '300', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 17, column = 15)
    label107 = Label(root4, text = '400', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 18, column = 15)
    label108 = Label(root4, text = '350', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 19, column = 15)
    label109 = Label(root4, text = '400', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 20, column = 15)
    label110 = Label(root4, text = '350', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 24, column = 15)
    label111 = Label(root4, text = '300', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 25, column = 15)
    label112 = Label(root4, text = '350', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 26, column = 15)
    label113 = Label(root4, text = '400', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 27, column = 15)
    label114 = Label(root4, text = '450', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 28, column = 15)
    label115 = Label(root4, text = '450', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 29, column = 15)
    button6 = Button(root4, text = 'Click here to view further' , command = beverages, highlightbackground = "dark blue", font = ("Times New Roman",25,"bold"))
    button6.place(rely = 1.0, relx = 1.0, x = 0, y = 0, anchor = SE)

    #order
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 0, column = 16)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 1, column = 17)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 2, column = 18)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 2, column = 19)
    b34 = Button(root4, text = '0rder ' , command = lambda:bill('Margherita', 350) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 5, column = 22)
    b35 = Button(root4, text = '0rder ' , command = lambda:bill('Garden Pizza', 350), highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 6, column = 22)
    b36 = Button(root4, text = '0rder ' , command = lambda:bill('Peri Peri Fanatics', 400) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 7, column = 22)
    b37 = Button(root4, text = '0rder ' , command = lambda:bill('Indian Tikka Pizza', 350) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 8, column = 22)
    b38 = Button(root4, text = '0rder ' , command = lambda:bill('Meat Lovers', 450) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 9, column = 22)
    b39 = Button(root4, text = '0rder ' , command = lambda:bill('Pepperoni pizza', 450) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 10, column = 22)
    b40 = Button(root4, text = '0rder ' , command = lambda:bill('Pesto', 300) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 15, column = 22)
    b41 = Button(root4, text = '0rder ' , command = lambda:bill('Pasta Arabiata', 350) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 16, column = 22)
    b42 = Button(root4, text = '0rder ' , command = lambda:bill('Creamy Cheese Sauce', 300) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 17, column = 22)
    b43 = Button(root4, text = '0rder ' , command = lambda:bill('Italian Pasta Alfredo', 400) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 18, column = 22)
    b44 = Button(root4, text = '0rder ' , command = lambda:bill('Olive Blasta Pasta', 350) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 19, column = 22)
    b45 = Button(root4, text = '0rder ' , command = lambda:bill('Spaghetti Carbanora(Chicken', 400) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 20, column = 22)
    b46 = Button(root4, text = '0rder ' , command = lambda:bill('Crunchy Veg Burger', 350) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 24, column = 22)
    b47 = Button(root4, text = '0rder ' , command = lambda:bill('Cottage Cheese Burger', 300) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 25, column = 22)
    b48 = Button(root4, text = '0rder ' , command = lambda:bill('Peri Peri Paneer', 350) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 26, column = 22)
    b49 = Button(root4, text = '0rder ' , command = lambda:bill('Tex Mex Chicken Burger', 400) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 27, column = 22)
    b50 = Button(root4, text = '0rder ' , command = lambda:bill('Lamb Burger', 450) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 28, column = 22)
    b51 = Button(root4, text = '0rder ' , command = lambda:bill('Fish Fillet Burger', 450) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 29, column = 22)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 2, column = 23)
    label = Label(root4, text = ' ' , bg = 'light blue').grid(row = 2, column = 24)


    b34 = Button(root4, text = 'Cancel ' , command = lambda:cancel('Margherita', 350) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 5, column = 25)
    b35 = Button(root4, text = 'Cancel ' , command = lambda:cancel('Garden Pizza', 350), highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 6, column = 25)
    b36 = Button(root4, text = 'Cancel ' , command = lambda:cancel('Peri Peri Fanatics', 400) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 7, column = 25)
    b37 = Button(root4, text = 'Cancel ' , command = lambda:cancel('Indian Tikka Pizza', 350) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 8, column = 25)
    b38 = Button(root4, text = 'Cancel ' , command = lambda:cancel('Meat Lovers', 450) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 9, column = 25)
    b39 = Button(root4, text = 'Cancel ' , command = lambda:cancel('Pepperoni pizza', 450) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 10, column = 25)
    b40 = Button(root4, text = 'Cancel ' , command = lambda:cancel('Pesto', 300) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 15, column = 25)
    b41 = Button(root4, text = 'Cancel ' , command = lambda:cancel('Pasta Arabiata', 350) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 16, column = 25)
    b42 = Button(root4, text = 'Cancel ' , command = lambda:cancel('Creamy Cheese Sauce', 300) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 17, column = 25)
    b43 = Button(root4, text = 'Cancel ' , command = lambda:cancel('Italian Pasta Alfredo', 400) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 18, column = 25)
    b44 = Button(root4, text = 'Cancel ' , command = lambda:cancel('Olive Blasta Pasta', 350) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 19, column = 25)
    b45 = Button(root4, text = 'Cancel ' , command = lambda:cancel('Spaghetti Carbanora(Chicken', 400) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 20, column = 25)
    b46 = Button(root4, text = 'Cancel ' , command = lambda:cancel('Crunchy Veg Burger', 350) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 24, column = 25)
    b47 = Button(root4, text = 'Cancel ' , command = lambda:cancel('Cottage Cheese Burger', 300) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 25, column = 25)
    b48 = Button(root4, text = 'Cancel ' , command = lambda:cancel('Peri Peri Paneer', 350) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 26, column = 25)
    b49 = Button(root4, text = 'Cancel ' , command = lambda:cancel('Tex Mex Chicken Burger', 400) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 27, column = 25)
    b50 = Button(root4, text = 'Cancel ' , command = lambda:cancel('Lamb Burger', 450) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 28, column = 25)
    b51 = Button(root4, text = 'Cancel ' , command = lambda:cancel('Fish Fillet Burger', 450) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 29, column = 25)
    
def beverages():
    root5 = Tk()
    root5.geometry("1500x800+0+0")
    root5.configure(bg='light blue')
    root5.title("MENU")
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 0, column = 0)
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 0, column = 1)
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 0, column = 2)
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 0, column = 3)
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 0, column = 4)
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 0, column = 5)
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 0, column = 6)
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 0, column = 7)
    label116 = Label(root5, text = "BEVERAGES", bg = 'dark blue',font = ("Times New Roman",27,"bold"))
    label116.grid(row = 0, column = 8)
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 1, column = 8)
    label117 = Label(root5, text = 'Blue Curacao', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 5, column = 8)
    label118 = Label(root5, text = 'Green Apple', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 6, column = 8)
    label119 = Label(root5, text = 'Lime Juice', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 7, column = 8)
    label120 = Label(root5, text = 'Strawberry Milkshake', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 8, column = 8)
    label121 = Label(root5, text = 'Virgin Mojito', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 9, column = 8)
    label122 = Label(root5, text = 'Lemon Ice Tea', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 10, column = 8)
    label123 = Label(root5, text = 'Ferroro Rocher Shake', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 11, column = 8)
    label124 = Label(root5, text = 'Oreo Shake', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 12, column = 8)
    label125 = Label(root5, text = 'Irish Cold Coffee', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 13, column = 8)
    label126 = Label(root5, text = 'Choco Mocha', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 14, column = 8)
    label127 = Label(root5, text = 'Hot Coffee', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 15, column = 8)
    label128 = Label(root5, text = 'Blueberry Shake', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 16, column = 8)
    label129 = Label(root5, text = 'Coca Cola', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 17, column = 8)
    label130 = Label(root5, text = 'Red Bull', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 18, column = 8)

    #Prices
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 0, column = 9)
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 1, column = 10)
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 2, column = 11)
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 2, column = 12)
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 2, column = 13)
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 2, column = 14)
    label131 = Label(root5, text = "PRICES", bg = 'dark blue',font = ("Times New Roman",27,"bold"))
    label131.grid(row = 0, column = 15)
    label132 = Label(root5, text = '110', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 5, column = 15)
    label133 = Label(root5, text = '110', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 6, column = 15)
    label134 = Label(root5, text = '110', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 7, column = 15)
    label135 = Label(root5, text = '130', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 8, column = 15)
    label136 = Label(root5, text = '130', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 9, column = 15)
    label137 = Label(root5, text = '100', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 10, column = 15)
    label138 = Label(root5, text = '170', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 11, column = 15)
    label139 = Label(root5, text = '170', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 12, column = 15)
    label140 = Label(root5, text = '150', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 13, column = 15)
    label141 = Label(root5, text = '150', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 14, column = 15)
    label142 = Label(root5, text = '100', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 15, column = 15)
    label143 = Label(root5, text = '130', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 16, column = 15)
    label144 = Label(root5, text = '100', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 17, column = 15)
    label145 = Label(root5, text = '150', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 18, column = 15)
    button7 = Button(root5, text = 'Click here to view further' , command = desserts, highlightbackground = "dark blue", font = ("Times New Roman",25,"bold"))
    button7.place(rely = 1.0, relx = 1.0, x = 0, y = 0, anchor = SE)

    #Order
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 1, column = 16)
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 1, column = 17)
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 2, column = 18)
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 2, column = 19)

    b52 = Button(root5, text = '0rder ' , command = lambda:bill('Blue Curacao', 110) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 5, column = 22)
    b53 = Button(root5, text = '0rder ' , command = lambda:bill('Green Apple', 110), highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 6, column = 22)
    b54 = Button(root5, text = '0rder ' , command = lambda:bill('Lime Juice', 110) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 7, column = 22)
    b55 = Button(root5, text = '0rder ' , command = lambda:bill('Strawberry Milkshake', 130) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 8, column = 22)
    b56 = Button(root5, text = '0rder ' , command = lambda:bill('Virgin Mojito', 130) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 9, column = 22)
    b57 = Button(root5, text = '0rder ' , command = lambda:bill('Lemon Ice Tea', 100) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 10, column = 22)
    b58 = Button(root5, text = '0rder ' , command = lambda:bill('Ferroro Rocher Shake', 170) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 11, column = 22)
    b59 = Button(root5, text = '0rder ' , command = lambda:bill('Oreo Shake', 170) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 12, column = 22)
    b60 = Button(root5, text = '0rder ' , command = lambda:bill('Irish Cold Coffee', 150) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 13, column = 22)
    b61 = Button(root5, text = '0rder ' , command = lambda:bill('Choco Mocha', 150) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 14, column = 22)
    b62 = Button(root5, text = '0rder ' , command = lambda:bill('Hot Coffee', 100) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 15, column = 22)
    b63 = Button(root5, text = '0rder ' , command = lambda:bill('Blueberry Shake', 130) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 16, column = 22)
    b64 = Button(root5, text = '0rder ' , command = lambda:bill('Coca Cola', 100) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 17, column = 22)
    b65 = Button(root5, text = '0rder ' , command = lambda:bill('Red Bull', 150) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 18, column = 22)
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 2, column = 23)
    label = Label(root5, text = ' ' , bg = 'light blue').grid(row = 2, column = 24)

    #Cancel
    b52 = Button(root5, text = 'Cancel ' , command = lambda:cancel('Blue Curacao', 110) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 5, column = 25)
    b53 = Button(root5, text = 'Cancel ' , command = lambda:cancel('Green Apple', 110), highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 6, column = 25)
    b54 = Button(root5, text = 'Cancel ' , command = lambda:cancel('Lime Juice', 110) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 7, column = 25)
    b55 = Button(root5, text = 'Cancel ' , command = lambda:cancel('Strawberry Milkshake', 130) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 8, column = 25)
    b56 = Button(root5, text = 'Cancel ' , command = lambda:cancel('Virgin Mojito', 130) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 9, column = 25)
    b57 = Button(root5, text = 'Cancel ' , command = lambda:cancel('Lemon Ice Tea', 100) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 10, column = 25)
    b58 = Button(root5, text = 'Cancel ' , command = lambda:cancel('Ferroro Rocher Shake', 170) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 11, column = 25)
    b59 = Button(root5, text = 'Cancel ' , command = lambda:cancel('Oreo Shake', 170) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 12, column = 25)
    b60 = Button(root5, text = 'Cancel ' , command = lambda:cancel('Irish Cold Coffee', 150) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 13, column = 25)
    b61 = Button(root5, text = 'Cancel ' , command = lambda:cancel('Choco Mocha', 150) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 14, column = 25)
    b62 = Button(root5, text = 'Cancel ' , command = lambda:cancel('Hot Coffee', 100) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 15, column = 25)
    b63 = Button(root5, text = 'Cancel ' , command = lambda:cancel('Blueberry Shake', 130) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 16, column = 25)
    b64 = Button(root5, text = 'Cancel ' , command = lambda:cancel('Coca Cola', 100) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 17, column = 25)
    b65 = Button(root5, text = 'Cancel ' , command = lambda:cancel('Red Bull', 150) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 18, column = 25)

def desserts():
    root6 = Tk()
    root6.geometry("1500x800+0+0")
    root6.configure(bg='light blue')
    root6.title("MENU")
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 0, column = 0)
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 0, column = 1)
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 0, column = 2)
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 0, column = 3)
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 0, column = 4)
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 0, column = 5)
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 0, column = 6)
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 0, column = 7)
    label146 = Label(root6, text = "DESSERTS", bg = 'dark blue',font = ("Times New Roman",27,"bold"))
    label146.grid(row = 0, column = 8)
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 1, column = 8)
    label147 = Label(root6, text = 'Black Forest', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 5, column = 8)
    label148 = Label(root6, text = 'Ferroro Rocher Cake', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 6, column = 8)
    label149 = Label(root6, text = 'Almond and Chcocolate Fudge', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 7, column = 8)
    label150 = Label(root6, text = 'Choco Mousse', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 8, column = 8)
    label151 = Label(root6, text = 'Red Velvet', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 9, column = 8)
    label152 = Label(root6, text = 'Kitkat Cake', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 10, column = 8)
    label153 = Label(root6, text = 'Chocolate Truffle', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 11, column = 8)
    label154 = Label(root6, text = 'Apple Pie', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 12, column = 8)
    label155 = Label(root6, text = 'Mississippi Mud Pie', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 13, column = 8)
    label156 = Label(root6, text = 'Choco Lava Cake', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 14, column = 8)
    label157 = Label(root6, text = 'Tiramisu', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 15, column = 8)
    label158 = Label(root6, text = 'Oreo Cheese Cake', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 16, column = 8)
    label159 = Label(root6, text = 'Blueberry Cheese Cake', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 17, column = 8)
    label160 = Label(root6, text = 'Cappuccino Walnut Brownie', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 18, column = 8)
    label161 = Label(root6, text = 'Choclate Tart', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 19, column = 8)
    label162 = Label(root6, text = 'Liquid Lemon Cheese Cake', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 20, column = 8)

    #Prices
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 0, column = 9)
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 1, column = 10)
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 2, column = 11)
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 2, column = 12)
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 2, column = 13)
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 2, column = 14)
    label163 = Label(root6, text = "PRICES", bg = 'dark blue',font = ("Times New Roman",27,"bold"))
    label163.grid(row = 0, column = 15)
    label164 = Label(root6, text = '120', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 5, column = 15)
    label165 = Label(root6, text = '150', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 6, column = 15)
    label166 = Label(root6, text = '150', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 7, column = 15)
    label167 = Label(root6, text = '140', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 8, column = 15)
    label168 = Label(root6, text = '130', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 9, column = 15)
    label169 = Label(root6, text = '140', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 10, column = 15)
    label170 = Label(root6, text = '170', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 11, column = 15)
    label171 = Label(root6, text = '170', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 12, column = 15)
    label172 = Label(root6, text = '150', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 13, column = 15)
    label173 = Label(root6, text = '140', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 14, column = 15)
    label174 = Label(root6, text = '150', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 15, column = 15)
    label175 = Label(root6, text = '150', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 16, column = 15)
    label176 = Label(root6, text = '130', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 17, column = 15)
    label177 = Label(root6, text = '150', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 18, column = 15)
    label178 = Label(root6, text = '140', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 19, column = 15)
    label179 = Label(root6, text = '130', bg = 'light blue', font = ("Sans Serif",18)).grid(row = 20, column = 15)
    button8 = Button(root6, text = 'Click here to play some games while you wait for the order' , command = games , highlightbackground = "dark blue", font = ("Times New Roman",23,"bold"))
    button8.place(rely = 1.0, relx = 1.0, x = 0, y = 0, anchor = SE)    

    #Order
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 1, column = 16)
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 1, column = 17)
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 2, column = 18)
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 2, column = 19)

    b52 = Button(root6, text = '0rder ' , command = lambda:bill('Black Forest', 120) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 5, column = 22)
    b53 = Button(root6, text = '0rder ' , command = lambda:bill('Ferroro Rocher Cake', 150), highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 6, column = 22)
    b54 = Button(root6, text = '0rder ' , command = lambda:bill('Almond and Chcocolate Fudge', 150) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 7, column = 22)
    b55 = Button(root6, text = '0rder ' , command = lambda:bill('Choco Mousse', 140) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 8, column = 22)
    b56 = Button(root6, text = '0rder ' , command = lambda:bill('Red Velvet', 130) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 9, column = 22)
    b57 = Button(root6, text = '0rder ' , command = lambda:bill('Kitkat Cake', 140) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 10, column = 22)
    b58 = Button(root6, text = '0rder ' , command = lambda:bill('Chocolate Truffle', 170) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 11, column = 22)
    b59 = Button(root6, text = '0rder ' , command = lambda:bill('Apple Pie', 170) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 12, column = 22)
    b60 = Button(root6, text = '0rder ' , command = lambda:bill('Mississippi Mud Pie', 150) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 13, column = 22)
    b61 = Button(root6, text = '0rder ' , command = lambda:bill('Choco Lava Cake', 140) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 14, column = 22)
    b62 = Button(root6, text = '0rder ' , command = lambda:bill('Tiramisu', 150) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 15, column = 22)
    b63 = Button(root6, text = '0rder ' , command = lambda:bill('Oreo Cheese Cake', 150) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 16, column = 22)
    b64 = Button(root6, text = '0rder ' , command = lambda:bill('Blueberry Cheese Cake', 130) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 17, column = 22)
    b65 = Button(root6, text = '0rder ' , command = lambda:bill('Cappuccino Walnut Brownie', 150) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 18, column = 22)
    b64 = Button(root6, text = '0rder ' , command = lambda:bill('Choclate Tart', 140) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 19, column = 22)
    b65 = Button(root6, text = '0rder ' , command = lambda:bill('Liquid Lemon Cheese Cake', 130) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 20, column = 22)
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 2, column = 23)
    label = Label(root6, text = ' ' , bg = 'light blue').grid(row = 2, column = 24)

    #Cancel
    b52 = Button(root6, text = 'Cancel ' , command = lambda:cancel('Black Forest', 120) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 5, column = 25)
    b53 = Button(root6, text = 'Cancel ' , command = lambda:cancel('Ferroro Rocher Cake', 150), highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 6, column = 25)
    b54 = Button(root6, text = 'Cancel ' , command = lambda:cancel('Almond and Chcocolate Fudge', 150) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 7, column = 25)
    b55 = Button(root6, text = 'Cancel ' , command = lambda:cancel('Choco Mousse', 140) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 8, column = 25)
    b56 = Button(root6, text = 'Cancel ' , command = lambda:cancel('Red Velvet', 130) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 9, column = 25)
    b57 = Button(root6, text = 'Cancel ' , command = lambda:cancel('Kitkat Cake', 140) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 10, column = 25)
    b58 = Button(root6, text = 'Cancel ' , command = lambda:cancel('Chocolate Truffle', 170) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 11, column = 25)
    b59 = Button(root6, text = 'Cancel ' , command = lambda:cancel('Apple Pie', 170) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 12, column = 25)
    b60 = Button(root6, text = 'Cancel ' , command = lambda:cancel('Mississippi Mud Pie', 150) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 13, column = 25)
    b61 = Button(root6, text = 'Cancel ' , command = lambda:cancel('Choco Lava Cake', 140) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 14, column = 25)
    b62 = Button(root6, text = 'Cancel ' , command = lambda:cancel('Tiramisu', 150) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 15, column = 25)
    b63 = Button(root6, text = 'Cancel ' , command = lambda:cancel('Oreo Cheese Cake', 150) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 16, column = 25)
    b64 = Button(root6, text = 'Cancel ' , command = lambda:cancel('Blueberry Cheese Cake', 130) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 17, column = 25)
    b65 = Button(root6, text = 'Cancel ' , command = lambda:cancel('Cappuccino Walnut Brownie', 150) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 18, column = 25)
    b64 = Button(root6, text = 'Cancel ' , command = lambda:cancel('Choclate Tart', 140) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 19, column = 25)
    b65 = Button(root6, text = 'Cancel ' , command = lambda:cancel('Liquid Lemon Cheese Cake', 130) , highlightbackground = "dark blue", font = ("Times New Roman",15,"bold")).grid(row = 20, column = 25)


def bill(dish,rate):
    d.append([dish,rate])
    return d

def cancel(dish,rate):
    d.remove([dish,rate])
    return d

def display():
    root8 = Tk()
    root8.geometry("1500x800+0+0")
    root8.configure(bg='light blue')
    root8.title('FOOD DELIVERY')
    ld1 = Label(root8, text = "Your order is ready! Please enjoy", bg = 'dark blue', font = ('Times New Roman', 30, 'bold')).place(relx = 0.65, rely = 0.4, anchor = 'ne')
    bt1 = Button(root8,text = "Click here to view your bill",command  = bill_display, font = ('Times New Roman', 25, 'bold')).place(relx = 1.0, rely = 1.0, anchor = 'se')
sum1 = 0
def bill_display():
    root9 = Tk()
    root9.geometry("1500x800+0+0")
    root9.configure(bg='light blue')
    root9.title('BILL')
    lb1 = Label(root9, text = 'Quattro', bg = 'dark blue', font = ('Times New Roman', 30, 'bold')).place(relx = 0.5,  rely = 0.0 , anchor = 'ne')
    lb2 = Label(root9, text = today, bg = 'light blue', font = ('Times New Roman', 20, 'bold')).place(relx = 0.2,  rely = 0.1 , anchor = 'ne')
    i = 0
    j = 9
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 1, column = 1)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 2, column = 2)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 3, column = 3)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 4, column = 4)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 5, column = 5)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 6)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 7)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 8)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 9)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 10)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 11)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 12)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 13)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 14)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 15)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 16)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 17)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 18)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 19)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 20)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 21)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 22)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 23)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 24)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 25)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 26)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 27)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 28)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 29)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 30)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 31)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 32)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 33)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 34)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 35)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 36)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 37)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 38)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 39)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 40)
    lb3 = Label(root9, text = 'Dish', bg = 'dark blue', font = ('Times New Roman', 20, 'bold')).grid(row = 6, column = 8)
    lb4 = Label(root9, text = 'Price', bg = 'dark blue', font = ('Times New Roman', 20, 'bold')).grid(row = 6, column = 41)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 6, column = 6)
    label = Label(root9, text = ' ' , bg = 'light blue').grid(row = 7, column = 7)
    while(i<len(d)):
        global sum1
        lb2 = Label(root9, text = d[i][0], bg = 'light blue', font = ('Times New Roman', 20)).grid(row = j, column = 8)
        lb5 = Label(root9, text = d[i][1], bg = 'light blue', font = ('Times New Roman', 20)).grid(row = j, column = 41)
        sum1 = sum1 + d[i][1]
        i = i + 1
        j = j + 1
    sgst = 0.025 * sum1
    cgst = 0.025 * sum1
    sum1 = sum1 + sgst + cgst
    lb5 = Label(root9, text = "SGST:", bg = 'light blue', font = ('Times New Roman', 20)).grid(row = j + 1, column = 40)
    lb6 = Label(root9, text = str(sgst), bg = 'light blue', font = ('Times New Roman', 20)).grid(row = j + 1, column = 41)
    lb7 = Label(root9, text = "CGST", bg = 'light blue', font = ('Times New Roman', 20)).grid(row = j + 2, column = 40)
    lb8 = Label(root9, text = str(cgst), bg = 'light blue', font = ('Times New Roman', 20)).grid(row = j + 2, column = 41)
    lb9 = Label(root9, text = "Total Price:", bg = 'light blue', font = ('Times New Roman', 20)).grid(row = j + 3, column = 40)
    lb10 = Label(root9, text = str(sum1), bg = 'light blue', font = ('Times New Roman', 20)).grid(row = j + 3, column = 41)
    bd1 = Button(root9, text = "Click here to pay", command  = pay, highlightbackground = 'dark blue' , font = ('Times New Roman',25, 'bold')).place(relx = 1.0, rely = 1.0, anchor = 'se')


def pay():
    root10 = Tk()
    root10.geometry("1500x800+0+0")
    root10.configure(bg = 'light blue')
    root10.title("PAYMENT")
    def pay_display():
        global sum1
        if (float(ep1.get()) == sum1):
            lp1 = Label(root10, text = 'Thank you!! Visit Again', bg = 'dark blue', font = ('Times New Roman',30,'bold')).place(relx = 0.55, rely = 0.5, anchor = 'ne')
        elif (float(ep1.get()) < sum1):
            lp1 = Label(root10, text = 'You have paid less than the amount mentioned in the bill. Please pay the amount mentioned in the bill', bg = 'dark blue', font = ('Times New Roman',30,'bold')).place(relx = 0.95, rely = 0.5, anchor = 'ne')
            
        else:
            y = float(ep1.get()) - sum1
            lp1 = Label(root10, text = 'Here is your change of Rs. '+ str(y), bg = 'dark blue', font = ('Times New Roman',30,'bold'),justify = 'center').place(relx = 0.55, rely = 0.5, anchor = 'ne')
            lp1 = Label(root10, text = 'Thank you!! Visit Again', bg = 'dark blue', font = ('Times New Roman',30,'bold'), justify = 'center').place(relx = 0.55, rely = 0.6, anchor = 'ne')
    label = Label(root10, text = ' ' , bg = 'light blue').grid(row = 1, column = 1)
    label = Label(root10, text = ' ' , bg = 'light blue').grid(row = 2, column = 2)
    label = Label(root10, text = ' ' , bg = 'light blue').grid(row = 3, column = 3)
    label = Label(root10, text = ' ' , bg = 'light blue').grid(row = 4, column = 4)
    label = Label(root10, text = ' ' , bg = 'light blue').grid(row = 5, column = 4)
    lp1 = Label(root10, text = 'Enter the amount you are paying:  ', bg = 'dark blue', font = ('Times New Roman',20,'bold')).grid(row = 6, column = 5)
    ep1 = Entry(root10, width = 30, highlightbackground = 'dark blue')
    ep1.insert(0, "Pay here")
    ep1.grid(row = 6, column = 6)
    bp1 = Button(root10, text = "Click here to make payment",command = pay_display, font = ("Times New Roman",15)).grid(row = 7, column = 6)
    label = Label(root10, text = ' ' , bg = 'light blue').grid(row = 8, column = 3)
    label = Label(root10, text = ' ' , bg = 'light blue').grid(row = 9, column = 2)
    label = Label(root10, text = ' ' , bg = 'light blue').grid(row = 10, column = 3)
    label = Label(root10, text = ' ' , bg = 'light blue').grid(row = 11, column = 4)
    label = Label(root10, text = ' ' , bg = 'light blue').grid(row = 12, column = 4)
   
                
def games():
    root7 = Tk()
    root7.geometry("1500x800+0+0")
    root7.configure(bg='light blue')
    root7.title("GAMES")
    label = Label(root7, text = ' ' , bg = 'light blue').grid(row = 1, column = 1)
    label = Label(root7, text = ' ' , bg = 'light blue').grid(row = 2, column = 2)
    label = Label(root7, text = ' ' , bg = 'light blue').grid(row = 3, column = 3)
    label = Label(root7, text = ' ' , bg = 'light blue').grid(row = 4, column = 4)
    label = Label(root7, text = ' ' , bg = 'light blue').grid(row = 5, column = 5)
    label = Label(root7, text = ' ' , bg = 'light blue').grid(row = 6, column = 6)
    bg1 = Button(root7, text = "Click here to play 2048 game", command = a_2048, highlightbackground = 'dark blue', font = ("Times New Roman",25,"bold")).place(relx = 0.6, rely = 0.3, anchor = 'ne')
    bg2 = Button(root7, text = "Click here to play Flappy game", command = flappy, highlightbackground = 'dark blue', font = ("Times New Roman",25,"bold")).place(relx = 0.6, rely = 0.4, anchor = 'ne')
    bg3 = Button(root7, text = "Click here to play Snake game", command = snake, highlightbackground = 'dark blue', font = ("Times New Roman",25,"bold")).place(relx = 0.6, rely = 0.5, anchor = 'ne')
    bg4 = Button(root7, text = "Click here to track your order", command = display, highlightbackground = 'dark blue', font = ("Times New Roman",25,"bold")).place(relx = 1.0, rely = 1.0, anchor = 'se')
#2048 Game
def a_2048():
    from tkinter import messagebox
    import random
    class Board:
        bg_color={
            '2': '#eee4da',
            '4': '#ede0c8',
            '8': '#edc850',
            '16': '#edc53f',
            '32': '#f67c5f',
            '64': '#f65e3b',
            '128': '#edcf72',
            '256': '#edcc61',
            '512': '#f2b179',
            '1024': '#f59563',
            '2048': '#edc22e',
        }
        color={
             '2': '#776e65',
            '4': '#f9f6f2',
            '8': '#f9f6f2',
            '16': '#f9f6f2',
            '32': '#f9f6f2',
            '64': '#f9f6f2',
            '128': '#f9f6f2',
            '256': '#f9f6f2',
            '512': '#776e65',
            '1024': '#f9f6f2',
            '2048': '#f9f6f2',
        }
        def __init__(self):
            self.n=4
            self.window=Tk()
            self.window.title('2048')
            self.gameArea=Frame(self.window,bg= 'azure3')
            self.board=[]
            self.gridCell=[[0]*4 for i in range(4)]
            self.compress=False
            self.merge=False
            self.moved=False
            self.score=0
            for i in range(4):
                rows=[]
                for j in range(4):
                    l=Label(self.gameArea,text='',bg='azure4',
                    font=('arial',22,'bold'),width=4,height=2)
                    l.grid(row=i,column=j,padx=7,pady=7)
                    rows.append(l);
                self.board.append(rows)
            self.gameArea.grid()
        def reverse(self):
            for ind in range(4):
                i=0
                j=3
                while(i<j):
                    self.gridCell[ind][i],self.gridCell[ind][j]=self.gridCell[ind][j],self.gridCell[ind][i]
                    i+=1
                    j-=1
        def transpose(self):
            self.gridCell=[list(t)for t in zip(*self.gridCell)]
        def compressGrid(self):
            self.compress=False
            temp=[[0] *4 for i in range(4)]
            for i in range(4):
                cnt=0
                for j in range(4):
                    if self.gridCell[i][j]!=0:
                        temp[i][cnt]=self.gridCell[i][j]
                        if cnt!=j:
                            self.compress=True
                        cnt+=1
            self.gridCell=temp
        def mergeGrid(self):
            self.merge=False
            for i in range(4):
                for j in range(4 - 1):
                    if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                        self.gridCell[i][j] *= 2
                        self.gridCell[i][j + 1] = 0
                        self.score += self.gridCell[i][j]
                        self.merge = True
        def random_cell(self):
            cells=[]
            for i in range(4):
                for j in range(4):
                    if self.gridCell[i][j] == 0:
                        cells.append((i, j))
            curr=random.choice(cells)
            i=curr[0]
            j=curr[1]
            self.gridCell[i][j]=2
        
        def can_merge(self):
            for i in range(4):
                for j in range(3):
                    if self.gridCell[i][j] == self.gridCell[i][j+1]:
                        return True
            
            for i in range(3):
                for j in range(4):
                    if self.gridCell[i+1][j] == self.gridCell[i][j]:
                        return True
            return False
        def paintGrid(self):
            for i in range(4):
                for j in range(4):
                    if self.gridCell[i][j]==0:
                        self.board[i][j].config(text='',bg='azure4')
                    else:
                        self.board[i][j].config(text=str(self.gridCell[i][j]),
                        bg=self.bg_color.get(str(self.gridCell[i][j])),
                        fg=self.color.get(str(self.gridCell[i][j])))
    class Game:
        def __init__(self,gamepanel):
            self.gamepanel=gamepanel
            self.end=False
            self.won=False
        def start(self):
            self.gamepanel.random_cell()
            self.gamepanel.random_cell()
            self.gamepanel.paintGrid()
            self.gamepanel.window.bind('<Key>', self.link_keys)
            self.gamepanel.window.mainloop()
        
        def link_keys(self,event):
            if self.end or self.won:
                return
            self.gamepanel.compress = False
            self.gamepanel.merge = False
            self.gamepanel.moved = False
            presed_key=event.keysym
            if presed_key=='Up':
                self.gamepanel.transpose()
                self.gamepanel.compressGrid()
                self.gamepanel.mergeGrid()
                self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
                self.gamepanel.compressGrid()
                self.gamepanel.transpose()
            elif presed_key=='Down':
                self.gamepanel.transpose()
                self.gamepanel.reverse()
                self.gamepanel.compressGrid()
                self.gamepanel.mergeGrid()
                self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
                self.gamepanel.compressGrid()
                self.gamepanel.reverse()
                self.gamepanel.transpose()
            elif presed_key=='Left':
                self.gamepanel.compressGrid()
                self.gamepanel.mergeGrid()
                self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
                self.gamepanel.compressGrid()
            elif presed_key=='Right':
                self.gamepanel.reverse()
                self.gamepanel.compressGrid()
                self.gamepanel.mergeGrid()
                self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
                self.gamepanel.compressGrid()
                self.gamepanel.reverse()
            else:
                pass
            self.gamepanel.paintGrid()
            print(self.gamepanel.score)
            flag=0
            for i in range(4):
                for j in range(4):
                    if(self.gamepanel.gridCell[i][j]==2048):
                        flag=1
                        break
            if(flag==1): #found 2048
                self.won=True
                messagebox.showinfo('2048', message='You Wonnn!!')
                print("won")
                return
            for i in range(4):
                for j in range(4):
                    if self.gamepanel.gridCell[i][j]==0:
                        flag=1
                        break
            if not (flag or self.gamepanel.can_merge()):
                self.end=True
                messagebox.showinfo('2048','Game Over!!!')
                print("Over")
            if self.gamepanel.moved:
                self.gamepanel.random_cell()
            
            self.gamepanel.paintGrid()  
    gamepanel =Board()
    game2048 = Game( gamepanel)
    game2048.start()


#Memory game
def flappy():    
    from freegames import vector

    bird = vector(0, 0)
    balls = []

    def tap(x, y):
        "Move bird up in response to screen tap."
        up = vector(0, 30)
        bird.move(up)

    def inside(point):
        "Return True if point on screen."
        return -200 < point.x < 200 and -200 < point.y < 200

    def draw(alive):
        "Draw screen objects."
        clear()

        goto(bird.x, bird.y)

        if alive:
            dot(10, 'green')
        else:
            dot(10, 'red')

        for ball in balls:
            goto(ball.x, ball.y)
            dot(20, 'black')

        update()

    def move():
        "Update object positions."
        bird.y -= 5

        for ball in balls:
            ball.x -= 3

        if randrange(10) == 0:
            y = randrange(-199, 199)
            ball = vector(199, y)
            balls.append(ball)

        while len(balls) > 0 and not inside(balls[0]):
            balls.pop(0)

        if not inside(bird):
            draw(False)
            return

        for ball in balls:
            if abs(ball - bird) < 15:
                draw(False)
                return

        draw(True)
        ontimer(move, 50)

    setup(420, 420, 370, 0)
    hideturtle()
    up()
    tracer(False)
    onscreenclick(tap)
    move()
    done()

#Pacman game
def snake():
    from random import randrange
    from freegames import square, vector

    food = vector(0, 0)
    snake = [vector(10, 0)]
    aim = vector(0, -10)

    def change(x, y):
        "Change snake direction."
        aim.x = x
        aim.y = y

    def inside(head):
        "Return True if head inside boundaries."
        return -200 < head.x < 190 and -200 < head.y < 190

    def move():
        "Move snake forward one segment."
        head = snake[-1].copy()
        head.move(aim)

        if not inside(head) or head in snake:
            square(head.x, head.y, 9, 'red')
            update()
            return

        snake.append(head)

        if head == food:
            print('Snake:', len(snake))
            food.x = randrange(-15, 15) * 10
            food.y = randrange(-15, 15) * 10
        else:
            snake.pop(0)

        clear()

        for body in snake:
            square(body.x, body.y, 9, 'black')

        square(food.x, food.y, 9, 'green')
        update()
        ontimer(move, 100)

    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: change(10, 0), 'Right')
    onkey(lambda: change(-10, 0), 'Left')
    onkey(lambda: change(0, 10), 'Up')
    onkey(lambda: change(0, -10), 'Down')
    move()
    done()

root.mainloop()