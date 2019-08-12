# Important files to be used
from tkinter import *
import random
import time
from tkinter import messagebox


class RestaurantSystem():
    """
    This class contain all the necessary function of the project
    """
    def initUI(self):
        self.root = Tk()  # Tkinter interface creation
        self.root.geometry("1350x750+0+0")   # Geometery of the tkinter interface

        # ================= Title of the interface ==================
        self.root.title("Restaurant Management System")
        self.root.configure(background='#8A2446')

        # ================= Main frames of interface ==================
        self.Tops = Frame(self.root, width=1350, height=100, bd=14, relief="raise")
        self.Tops.pack(side=TOP)
        self.f1 = Frame(self.root, width=900, height=650, bd=8, relief="raise")
        self.f1.pack(side=LEFT)
        self.f2 = Frame(self.root, width=440, height=650, bd=8, relief="raise")
        self.f2.pack(side=RIGHT)

        self.Tops.configure(background='#8A2446')
        self.f1.configure(background='#8A2446')
        self.f2.configure(background='#8A2446')

        # =================  Frames inside left frame ==================
        self.f1a = Frame(self.f1, width=900, height=330, bd=8, relief="raise")
        self.f1a.pack(side=TOP)

        self.f2a = Frame(self.f1, width=900, height=330, bd=6, relief="raise")
        self.f2a.pack(side=BOTTOM)

        # ================= Frames inside right frame ==================
        self.ft2 = Frame(self.f2, width=440, height=450, bd=12, relief="raise")
        self.ft2.pack(side=TOP)

        self.fb2 = Frame(self.f2, width=440, height=250, bd=16, relief="raise")
        self.fb2.pack(side=BOTTOM)

        # =================  Frames inside left frame's top frame ==================
        self.f1aa = Frame(self.f1a, width=400, height=330, bd=16, relief="raise")
        self.f1aa.pack(side=LEFT)

        self.f1ab = Frame(self.f1a, width=400, height=330, bd=16, relief="raise")
        self.f1ab.pack(side=RIGHT)

        # =================  Frames inside right frame's bottom frame ==================
        self.f2aa = Frame(self.f2a, width=450, height=330, bd=14, relief="raise")
        self.f2aa.pack(side=LEFT)

        self.f2ab = Frame(self.f2a, width=450, height=330, bd=14, relief="raise")
        self.f2ab.pack(side=RIGHT)

        # ================= Label Set on Top Frame ==================

        self.lblInfo = Label(self.Tops, font=('arial', 64, 'bold'), text="Restaurant Management System", bd=9, fg="#8A2446")
        self.lblInfo.grid(row=0, column=0)

        # ================== Necessary Variables ===============

        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        self.var7 = IntVar()
        self.var8 = IntVar()
        self.var9 = IntVar()
        self.var10 = IntVar()
        self.var11 = IntVar()
        self.var12 = IntVar()
        self.var13 = IntVar()
        self.var14 = IntVar()
        self.var15 = IntVar()
        self.var16 = IntVar()

        self.DateofOrder = StringVar()
        self.Receipt_Ref = StringVar()
        self.PaidTax = StringVar()
        self.SubTotal = StringVar()
        self.TotalCost = StringVar()
        self.CostofCakesandDrinks = StringVar()
        self.CostofFood = StringVar()
        self.ServiceCharge = StringVar()

        self.E_Fries = StringVar()
        self.E_Lunch = StringVar()
        self.E_Burger = StringVar()
        self.E_Pizza = StringVar()
        self.E_CheeseBurger = StringVar()
        self.E_MacNuggets = StringVar()
        self.E_MacPuff = StringVar()
        self.E_ChickenWings = StringVar()

        self.E_Coffee_Cake = StringVar()
        self.E_Red_Velvet_Cake = StringVar()
        self.E_Black_Forest = StringVar()
        self.E_Boston_Cream_Cake = StringVar()
        self.E_Latta = StringVar()
        self.E_Coke = StringVar()
        self.E_Pepsi = StringVar()
        self.E_Cappuccino = StringVar()

        self.E_Fries.set("0")
        self.E_Lunch.set("0")
        self.E_Burger.set("0")
        self.E_Pizza.set("0")
        self.E_CheeseBurger.set("0")
        self.E_MacNuggets.set("0")
        self.E_MacPuff.set("0")
        self.E_ChickenWings.set("0")

        self.E_Coffee_Cake.set("0")
        self.E_Red_Velvet_Cake.set("0")
        self.E_Black_Forest.set("0")
        self.E_Boston_Cream_Cake.set("0")
        self.E_Latta.set("0")
        self.E_Coke.set("0")
        self.E_Pepsi.set("0")
        self.E_Cappuccino.set("0")

        # ================== Date on which order is placed ==================

        self.DateofOrder.set(time.strftime("%d/%m/%y"))

        # ================== Items Check buttons =========================

        Fries = Checkbutton(self.f1aa, font=('arial', 18, 'bold'), text="Fries Meal \t", variable=self.var1, onvalue=1,
                            fg="#8A2446",
                            offvalue=0, command=self.chkbutton_value).grid(row=0, sticky=W)

        Lunch = Checkbutton(self.f1aa, font=('arial', 18, 'bold'), text="Lunch Meal \t", variable=self.var2, onvalue=1,
                            fg="#8A2446",
                            offvalue=0, command=self.chkbutton_value).grid(row=1, sticky=W)

        Burger = Checkbutton(self.f1aa, font=('arial', 18, 'bold'), text="Burger Meal \t", variable=self.var3, onvalue=1,
                             fg="#8A2446",
                             offvalue=0, command=self.chkbutton_value).grid(row=2, sticky=W)

        Pizza = Checkbutton(self.f1aa, font=('arial', 18, 'bold'), text="Pizza Meal \t", variable=self.var4, onvalue=1,
                            fg="#8A2446",
                            offvalue=0, command=self.chkbutton_value).grid(row=3, sticky=W)

        CheeseBurger = Checkbutton(self.f1aa, font=('arial', 18, 'bold'), text="Cheese Burger  \t", variable=self.var5, onvalue=1,
                                   fg="#8A2446",
                                   offvalue=0, command=self.chkbutton_value).grid(row=4, sticky=W)

        MacNuggets = Checkbutton(self.f1aa, font=('arial', 18, 'bold'), text="Mac Nuggets \t", variable=self.var6, onvalue=1,
                                 fg="#8A2446",
                                 offvalue=0, command=self.chkbutton_value).grid(row=5, sticky=W)

        MacPuff = Checkbutton(self.f1aa, font=('arial', 18, 'bold'), text="Mac Puff \t", variable=self.var7, onvalue=1,
                              fg="#8A2446",
                              offvalue=0, command=self.chkbutton_value).grid(row=6, sticky=W)

        ChickenWings = Checkbutton(self.f1aa, font=('arial', 18, 'bold'), text="Chicken Wings \t", variable=self.var8, onvalue=1,
                                   fg="#8A2446",
                                   offvalue=0, command=self.chkbutton_value).grid(row=7, sticky=W)

        CoffeeCake = Checkbutton(self.f1ab, font=('arial', 18, 'bold'), text="Coffee Cake \t", variable=self.var9, onvalue=1,
                                 fg="#8A2446",
                                 offvalue=0, command=self.chkbutton_value).grid(row=0, sticky=W)

        Red_Velvet_Cake = Checkbutton(self.f1ab, font=('arial', 18, 'bold'), text="Red Velvet Cake \t", variable=self.var10,
                                      onvalue=1, fg="#8A2446",
                                      offvalue=0, command=self.chkbutton_value).grid(row=1, sticky=W)

        Black_Forest_Cake = Checkbutton(self.f1ab, font=('arial', 18, 'bold'), text="Black Forest Cake \t", variable=self.var11,
                                        fg="#8A2446",
                                        onvalue=1, offvalue=0, command=self.chkbutton_value).grid(row=2, sticky=W)

        Boston_Cream_Cake = Checkbutton(self.f1ab, font=('arial', 18, 'bold'), text="Boston Cream Cake \t", variable=self.var12,
                                        onvalue=1, fg="#8A2446",
                                        offvalue=0, command=self.chkbutton_value).grid(row=3, sticky=W)

        Latta = Checkbutton(self.f1ab, font=('arial', 18, 'bold'), text="Latte \t", variable=self.var13, fg="#8A2446",
                            onvalue=1, offvalue=0, command=self.chkbutton_value).grid(row=4, sticky=W)

        Coke = Checkbutton(self.f1ab, font=('arial', 18, 'bold'), text="Coke \t", variable=self.var14, fg="#8A2446",
                           onvalue=1, offvalue=0, command=self.chkbutton_value).grid(row=5, sticky=W)

        Pepsi = Checkbutton(self.f1ab, font=('arial', 18, 'bold'), text="Pepsi \t", variable=self.var15, onvalue=1, fg="#8A2446",
                            offvalue=0, command=self.chkbutton_value).grid(row=6, sticky=W)

        Cappuccino = Checkbutton(self.f1ab, font=('arial', 18, 'bold'), text="Cappuccino \t", variable=self.var16, fg="#8A2446",
                                 onvalue=1, offvalue=0, command=self.chkbutton_value).grid(row=7, sticky=W)

        # ================== Entry Widget for Items ==============================

        self.txtFries = Entry(self.f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=self.E_Fries,
                         state=DISABLED)
        self.txtFries.grid(row=0, column=1)
        self.txtLunch = Entry(self.f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=self.E_Lunch,
                         state=DISABLED)
        self.txtLunch.grid(row=1, column=1)
        self.txtBurger = Entry(self.f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=self.E_Burger,
                          state=DISABLED)
        self.txtBurger.grid(row=2, column=1)
        self.txtPizza = Entry(self.f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=self.E_Pizza,
                         state=DISABLED)
        self.txtPizza.grid(row=3, column=1)
        self.txtCheeseBurger = Entry(self.f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                                textvariable=self.E_CheeseBurger,
                                state=DISABLED)
        self.txtCheeseBurger.grid(row=4, column=1)
        self.txtMacNuggets = Entry(self.f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=self.E_MacNuggets
                              , state=DISABLED)
        self.txtMacNuggets.grid(row=5, column=1)
        self.txtMacPuff = Entry(self.f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                           textvariable=self.E_MacPuff, state=DISABLED)
        self.txtMacPuff.grid(row=6, column=1)
        self.txtChickenWings = Entry(self.f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                                textvariable=self.E_ChickenWings, state=DISABLED)
        self.txtChickenWings.grid(row=7, column=1)

        self.txtCoffee_Cake = Entry(self.f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                               textvariable=self.E_Coffee_Cake, state=DISABLED)
        self.txtCoffee_Cake.grid(row=0, column=1)
        self.txtRed_Valet_Cake = Entry(self.f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                                  textvariable=self.E_Red_Velvet_Cake, state=DISABLED)
        self.txtRed_Valet_Cake.grid(row=1, column=1)
        self.txtBlack_Forest_Cake = Entry(self.f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                                     textvariable=self.E_Black_Forest, state=DISABLED)
        self.txtBlack_Forest_Cake.grid(row=2, column=1)
        self.txtBoston_Cream_Cake = Entry(self.f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                                     textvariable=self.E_Boston_Cream_Cake, state=DISABLED)
        self.txtBoston_Cream_Cake.grid(row=3, column=1)
        self.txtLatta = Entry(self.f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                         textvariable=self.E_Latta, state=DISABLED)
        self.txtLatta.grid(row=4, column=1)
        self.txtCoke = Entry(self.f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                        textvariable=self.E_Coke, state=DISABLED)
        self.txtCoke.grid(row=5, column=1)
        self.txtPepsi = Entry(self.f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                         textvariable=self.E_Pepsi, state=DISABLED)
        self.txtPepsi.grid(row=6, column=1)
        self.txtCappuccino = Entry(self.f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                              textvariable=self.E_Cappuccino, state=DISABLED)
        self.txtCappuccino.grid(row=7, column=1)

        # =================== Information on Receipt =======================

        self.lblReceipt = Label(self.ft2, font=('arial', 12, 'bold'), text="Receipt", bd=2, anchor='w', fg="#8A2446")
        self.lblReceipt.grid(row=0, column=0, sticky=W)
        self.txtReceipt = Text(self.ft2, width=59, height=22, bg="white", bd=8, font=('arial', 11, 'bold'))
        self.txtReceipt.grid(row=1, column=0)

        # ================== Cost Items Information(In Left Frame's Bottom Frame(left)) ======================

        self.lblCostofFood = Label(self.f2aa, font=('arial', 16, 'bold'), text="Cost of Food", bd=8, fg="#8A2446")
        self.lblCostofFood.grid(row=2, column=0, sticky=W)
        self.txtCostofFood = Entry(self.f2aa, font=('arial', 16, 'bold'), bd=8, justify="left", textvariable=self.CostofFood)
        self.txtCostofFood.grid(row=2, column=1, sticky=W)

        self.lblCostofCakesandDrinks = Label(self.f2aa, font=('arial', 16, 'bold'), text="Drink & Cake", bd=8, fg="#8A2446")
        self.lblCostofCakesandDrinks.grid(row=3, column=0, sticky=W)
        self.txtCostofCakesandDrinks = Entry(self.f2aa, font=('arial', 16, 'bold'), bd=8, justify="left",
                                        textvariable=self.CostofCakesandDrinks)
        self.txtCostofCakesandDrinks.grid(row=3, column=1, sticky=W)

        self.lblServiceCharge = Label(self.f2aa, font=('arial', 16, 'bold'), text="Service Charge", bd=8, fg="#8A2446")
        self.lblServiceCharge.grid(row=4, column=0, sticky=W)
        self.txtServiceCharge = Entry(self.f2aa, font=('arial', 16, 'bold'), bd=8, justify="left", textvariable=self.ServiceCharge)
        self.txtServiceCharge.grid(row=4, column=1, sticky=W)

        # ======================Payment Information(In Left Frame's Bottom Frame(right)================================

        self.lblPaidTax = Label(self.f2ab, font=('arial', 16, 'bold'), text="Tax", bd=8, fg="#8A2446")
        self.lblPaidTax.grid(row=2, column=0, sticky=W)
        self.txtPaidTax = Entry(self.f2ab, font=('arial', 16, 'bold'), bd=8, justify="left", textvariable=self.PaidTax)
        self.txtPaidTax.grid(row=2, column=1, sticky=W)

        self.lblSubTotal = Label(self.f2ab, font=('arial', 16, 'bold'), text="Sub Total", bd=8, fg="#8A2446")
        self.lblSubTotal.grid(row=3, column=0, sticky=W)
        self.txtSubTotal = Entry(self.f2ab, font=('arial', 16, 'bold'), bd=8, justify="left", textvariable=self.SubTotal)
        self.txtSubTotal.grid(row=3, column=1, sticky=W)

        self.lblTotalCost = Label(self.f2ab, font=('arial', 16, 'bold'), text="Total", bd=8, fg="#8A2446")
        self.lblTotalCost.grid(row=4, column=0, sticky=W)
        self.txtTotalCost = Entry(self.f2ab, font=('arial', 16, 'bold'), bd=8, justify="left", textvariable=self.TotalCost)
        self.txtTotalCost.grid(row=4, column=1, sticky=W)

        # ==================Button(In Right Frame's Bottom)===============================

        btnTotal = Button(self.fb2, padx=5, pady=1, bd=4, fg="#8A2446", font=('arial', 16, 'bold'), width=5,
                          text="Total", command=self.CostofItems).grid(row=0, column=0)
        btnReset = Button(self.fb2, padx=5, pady=1, bd=4, fg="#8A2446", font=('arial', 16, 'bold'), width=5,
                          text="Reset", command=self.Reset).grid(row=0, column=1)
        btnReceipt = Button(self.fb2, padx=5, pady=1, bd=4, fg="#8A2446", font=('arial', 16, 'bold'), width=5,
                            text="Receipt", command=self.Receipt).grid(row=0, column=2)
        btnprice = Button(self.fb2, padx=5, pady=1, bd=4, fg="#8A2446", font=('arial', 16, 'bold'), width=5,
                          text="Price", command=self.price).grid(row=0, column=3)
        btnExit = Button(self.fb2, padx=5, pady=1, bd=4, fg="#8A2446", font=('arial', 16, 'bold'), width=5,
                         text="Exit", command=self.qExit).grid(row=0, column=4)

        self.name_label = Label(self.root, text="---By Aakanksha", fg="#900C3F", font=('arial', 14, 'bold'))
        self.name_label.place(x=1149, y=103)

        self.root.mainloop()

# ========================= Calculations of Cost of Items ===========================

    def CostofItems(self):

        self.Item1 = float(self.E_Fries.get())
        self.Item2 = float(self.E_Lunch.get())
        self.Item3 = float(self.E_Burger.get())
        self.Item4 = float(self.E_Pizza.get())
        self.Item5 = float(self.E_CheeseBurger.get())
        self.Item6 = float(self.E_MacNuggets.get())
        self.Item7 = float(self.E_MacPuff.get())
        self.Item8 = float(self.E_ChickenWings.get())

        self.Item9 = float(self.E_Coffee_Cake.get())
        self.Item10 = float(self.E_Red_Velvet_Cake.get())
        self.Item11 = float(self.E_Black_Forest.get())
        self.Item12 = float(self.E_Boston_Cream_Cake.get())
        self.Item13 = float(self.E_Latta.get())
        self.Item14 = float(self.E_Coke.get())
        self.Item15 = float(self.E_Pepsi.get())
        self.Item16 = float(self.E_Cappuccino.get())

        self.PriceofFood =(self.Item1 * 70) + (self.Item2 * 90) + (self.Item3 * 50) + (self.Item4 *100) + (self.Item5 * 50) + (self.Item6 * 80) +\
                       (self.Item7 * 50) + (self.Item8 * 120)

        self.PriceofCakesandDrinks =(self.Item9 * 100) + (self.Item10 * 110) + (self.Item11 * 100) + (self.Item12 *110) + (self.Item13 * 70) + \
                      (self.Item14 * 70) + (self.Item15 * 80) + (self.Item16 * 100)

        self.FoodPrice = 'Rs.' + " " + str(float('%.2f' % self.PriceofFood))
        self.DrinksandCakesPrice = 'Rs.' + " " + str(float('%.2f' % self.PriceofCakesandDrinks))
        self.CostofFood.set(self.FoodPrice)
        self.CostofCakesandDrinks.set(self.DrinksandCakesPrice)
        self.SC = 'Rs.' + " " + str(float('%.2f' % 15))
        print(self.SC)
        self.ServiceCharge.set(self.SC)

        self.SubTotalofITEMS = 'Rs.' + " " + str(float('%0.2f' % (self.PriceofFood + self.PriceofCakesandDrinks + 15)))
        self.SubTotal.set(self.SubTotalofITEMS)

        self.Tax = 'Rs.' + " " + str(float('%0.2f' % ((self.PriceofFood + self.PriceofCakesandDrinks + 15)*0.28)))
        self.PaidTax.set(self.Tax)
        self.TT = ((self.PriceofFood + self.PriceofCakesandDrinks + 15)*0.28)
        self.TC = 'Rs.' + " " + str(float('%0.2f' % ((self.PriceofFood + self.PriceofCakesandDrinks + 15) + self.TT)))
        print(self.TC)
        self.TotalCost.set(self.TC)

    # ========================== Exit the Main frame ============================
    def qExit(self):

        self.qExit = messagebox.askyesno("Quit System", "Do you want to quit?")
        if self.qExit > 0:
            self.root.destroy()
            return

    # ======================== Reset the Entries Module========================

    def Reset(self):

        self.PaidTax.set("")
        self.SubTotal.set("")
        self.TotalCost.set("")
        self.CostofFood.set("")
        self.CostofCakesandDrinks.set("")
        self.ServiceCharge.set("")
        self.txtReceipt.delete("1.0", END)

        self.E_Fries.set("0")
        self.E_Lunch.set("0")
        self.E_Burger.set("0")
        self.E_Pizza.set("0")
        self.E_CheeseBurger.set("0")
        self.E_MacNuggets.set("0")
        self.E_MacPuff.set("0")
        self.E_ChickenWings.set("0")

        self.E_Coffee_Cake.set("0")
        self.E_Red_Velvet_Cake.set("0")
        self.E_Black_Forest.set("0")
        self.E_Boston_Cream_Cake.set("0")
        self.E_Latta.set("0")
        self.E_Coke.set("0")
        self.E_Pepsi.set("0")
        self.E_Cappuccino.set("0")

        self.var1.set("0")
        self.var2.set("0")
        self.var3.set("0")
        self.var4.set("0")
        self.var5.set("0")
        self.var6.set("0")
        self.var7.set("0")
        self.var8.set("0")
        self.var9.set("0")
        self.var10.set("0")
        self.var11.set("0")
        self.var12.set("0")
        self.var13.set("0")
        self.var14.set("0")
        self.var15.set("0")
        self.var16.set("0")

        self.txtLatta.configure(state=DISABLED)
        self.txtLunch.configure(state=DISABLED)
        self.txtBurger.configure(state=DISABLED)
        self.txtPizza.configure(state=DISABLED)
        self.txtCheeseBurger.configure(state=DISABLED)
        self.txtMacNuggets.configure(state=DISABLED)
        self.txtMacPuff.configure(state=DISABLED)
        self.txtChickenWings.configure(state=DISABLED)
        self.txtCoffee_Cake.configure(state=DISABLED)
        self.txtRed_Valet_Cake.configure(state=DISABLED)
        self.txtBlack_Forest_Cake.configure(state=DISABLED)
        self.txtBoston_Cream_Cake.configure(state=DISABLED)
        self.txtLatta.configure(state=DISABLED)
        self.txtCoke.configure(state=DISABLED)
        self.txtPepsi.configure(state=DISABLED)
        self.txtCappuccino.configure(state=DISABLED)

    # ==========================Receipt Function======================

    def Receipt(self):
        self.txtReceipt.delete("1.0", END)
        self.x = random.randint(1000, 500890)
        self.randomRef = str(self.x)
        self.Receipt_Ref.set("BILL" + self.randomRef)

        self.txtReceipt.insert(END, 'Receipt Ref:\t\t\t' + self.Receipt_Ref.get() + '\t\t' + self.DateofOrder.get()+"\n")
        self.txtReceipt.insert(END, 'Items\t\t\t           ' + "Cost of Items \n\n")
        self.txtReceipt.insert(END, 'Fries:\t\t\t\t      ' + self.E_Fries.get() + "\n")
        self.txtReceipt.insert(END, 'Lunch Meal: \t\t\t\t      ' + self.E_Lunch.get() + "\n")
        self.txtReceipt.insert(END, 'Burger: \t\t\t\t      ' + self.E_Burger.get() + "\n")
        self.txtReceipt.insert(END, 'Pizza: \t\t\t\t      ' + self.E_Pizza.get() + "\n")
        self.txtReceipt.insert(END, 'Cheese Burger: \t\t\t\t      ' + self.E_CheeseBurger.get() + "\n")
        self.txtReceipt.insert(END, 'Mac Nuggets: \t\t\t\t      ' + self.E_MacNuggets.get() + "\n")
        self.txtReceipt.insert(END, 'Mac Puff: \t\t\t\t      ' + self.E_MacPuff.get() + "\n")
        self.txtReceipt.insert(END, 'Chicken Wings: \t\t\t\t      ' + self.E_ChickenWings.get() + "\n")
        self.txtReceipt.insert(END, 'Coffee Cake: \t\t\t\t      ' + self.E_Coffee_Cake.get() + "\n")
        self.txtReceipt.insert(END, 'Red Valet Cake: \t\t\t\t      ' + self.E_Red_Velvet_Cake.get() + "\n")
        self.txtReceipt.insert(END, 'Black Forest Cake: \t\t\t\t      ' + self.E_Black_Forest.get() + "\n")
        self.txtReceipt.insert(END, 'Boston Cream Cake: \t\t\t\t      ' + self.E_Boston_Cream_Cake.get() + "\n")
        self.txtReceipt.insert(END, 'Latte: \t\t\t\t      ' + self.E_Latta.get() + "\n")
        self.txtReceipt.insert(END, 'Coke: \t\t\t\t      ' + self.E_Coke.get() + "\n")
        self.txtReceipt.insert(END, 'Pepsi: \t\t\t\t      ' + self.E_Pepsi.get() + "\n")
        self.txtReceipt.insert(END, 'Cappuccino: \t\t\t\t      ' + self.E_Cappuccino.get() + "\n")
        self.txtReceipt.insert(END, 'Cost of Food: \t\t\t\t' + self.CostofFood.get() + "\nCost of Cakes and Drinks: \t\t\t\t" + self.CostofCakesandDrinks.get() + "\n")
        self.txtReceipt.insert(END, 'Service Charge: \t\t\t\t' + self.ServiceCharge.get() + "\nSub Total : \t\t\t\t" + self.SubTotal.get() + "\n")
        self.txtReceipt.insert(END, 'Tax Paid: \t\t\t\t' + self.PaidTax.get() + "\nTotal Cost: \t\t\t\t" + self.TotalCost.get() + "\n")

        # +++++++++++++++++++SCROLLBAR+++++++++++++++++++++++++++++++++++++

        self.f2.scroll = Scrollbar(self.f2, orient=VERTICAL, command=self.txtReceipt.yview)
        self.txtReceipt['yscroll'] = self.f2.scroll.set

        # f2.scroll.pack(side="right", fill="y")
        self.f2.scroll.place(x=430, y=45, height=402)


    # ========================= CheckButton check performed function =====================

    def chkbutton_value(self):
        if self.var1.get() == 1:
            self.txtFries.configure(state=NORMAL)
        elif self.var1.get() == 0:
            self.txtFries.configure(state=DISABLED)
            self.E_Fries.set("0")
        if self.var2.get() == 1:
            self.txtLunch.configure(state=NORMAL)
        elif self.var2.get() == 0:
            self.txtLunch.configure(state=DISABLED)
            self.E_Lunch.set("0")
        if self.var3.get() == 1:
            self.txtBurger.configure(state=NORMAL)
        elif self.var3.get() == 0:
            self.txtBurger.configure(state=DISABLED)
            self.E_Burger.set("0")
        if self.var4.get() == 1:
            self.txtPizza.configure(state=NORMAL)
        elif self.var4.get() == 0:
            self.txtPizza.configure(state=DISABLED)
            self.E_Pizza.set("0")
        if self.var5.get() == 1:
            self.txtCheeseBurger.configure(state=NORMAL)
        elif self.var5.get() == 0:
            self.txtCheeseBurger.configure(state=DISABLED)
            self.E_CheeseBurger.set("0")
        if self.var6.get() == 1:
            self.txtMacNuggets.configure(state=NORMAL)
        elif self.var6.get() == 0:
            self.txtMacNuggets.configure(state=DISABLED)
            self.E_MacNuggets.set("0")
        if self.var7.get() == 1:
            self.txtMacPuff.configure(state=NORMAL)
        elif self.var7.get() == 0:
            self.txtMacPuff.configure(state=DISABLED)
            self.E_MacPuff.set("0")
        if self.var8.get() == 1:
            self.txtChickenWings.configure(state=NORMAL)
        elif self.var8.get() == 0:
            self.txtChickenWings.configure(state=DISABLED)
            self.E_ChickenWings.set("0")
        if self.var9.get() == 1:
            self.txtCoffee_Cake.configure(state=NORMAL)
        elif self.var9.get() == 0:
            self.txtCoffee_Cake.configure(state=DISABLED)
            self.E_Coffee_Cake.set("0")
        if self.var10.get() == 1:
            self.txtRed_Valet_Cake.configure(state=NORMAL)
        elif self.var10.get() == 0:
            self.txtRed_Valet_Cake.configure(state=DISABLED)
            self.E_Red_Velvet_Cake.set("0")
        if self.var11.get() == 1:
            self.txtBlack_Forest_Cake.configure(state=NORMAL)
        elif self.var11.get() == 0:
            self.txtBlack_Forest_Cake.configure(state=DISABLED)
            self.E_Black_Forest.set("0")
        if self.var12.get() == 1:
            self.txtBoston_Cream_Cake.configure(state=NORMAL)
        elif self.var12.get() == 0:
            self.txtBoston_Cream_Cake.configure(state=DISABLED)
            self.E_Boston_Cream_Cake.set("0")
        if self.var13.get() == 1:
            self.txtLatta.configure(state=NORMAL)
        elif self.var13.get() == 0:
            self.txtLatta.configure(state=DISABLED)
            self.E_Latta.set("0")
        if self.var14.get() == 1:
            self.txtCoke.configure(state=NORMAL)
        elif self.var14.get() == 0:
            self.txtCoke.configure(state=DISABLED)
            self.E_Coke.set("0")
        if self.var15.get() == 1:
            self.txtPepsi.configure(state=NORMAL)
        elif self.var15.get() == 0:
            self.txtPepsi.configure(state=DISABLED)
            self.E_Pepsi.set("0")
        if self.var16.get() == 1:
            self.txtCappuccino.configure(state=NORMAL)
        elif self.var16.get() == 0:
            self.txtCappuccino.configure(state=DISABLED)
            self.E_Cappuccino.set("0")

    # ========================= Menu List Module =====================
    def price(self):
        self.roo = Tk()
        self.roo.geometry("360x530+0+0")
        self.roo.resizable(0, 0)
        self.roo.title("Price List")

        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="ITEM", fg="#8A2446", bd=5)
        self.lblinfo.grid(row=0, column=0)
        self.lblinfo = Label(self.roo, font=('aria', 15,'bold'), text="             ", fg="white", anchor=W)
        self.lblinfo.grid(row=0, column=2)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="PRICE", fg="#8A2446", anchor=W)
        self.lblinfo.grid(row=0, column=3)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=1, column=0)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="70", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=1, column=3)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=2, column=0)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="90", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=2, column=3)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=3, column=0)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=3, column=3)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=4, column=0)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="100", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=4, column=3)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=5, column=0)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=5, column=3)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="Mac Nuggets", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=6, column=0)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="80", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=6, column=3)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="Mac Puff", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=7, column=0)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=7, column=3)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="Chicken Wings", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=8, column=0)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="120", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=8, column=3)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="Coffee Cake", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=9, column=0)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="100", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=9, column=3)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="Red Velvet Cake", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=10, column=0)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="110", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=10, column=3)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="Black Forest Cake", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=11, column=0)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="100", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=11, column=3)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="Boston Cream Cake", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=12, column=0)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="110", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=12, column=3)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="Latte", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=13, column=0)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="70", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=13, column=3)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="Coke", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=14, column=0)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="70", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=14, column=3)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="Pepsi", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=15, column=0)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="80", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=15, column=3)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="Cappuccino", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=16, column=0)
        self.lblinfo = Label(self.roo, font=('aria', 15, 'bold'), text="100", fg="steel blue", anchor=W)
        self.lblinfo.grid(row=16, column=3)

        self.roo.mainloop()


# ============================= Execution of Code==========================
if __name__ == "__main__":
    try:
        RestaurantSystem().initUI()

    except Exception as e:
        messagebox.showinfo("Error", "Cannot open!")
