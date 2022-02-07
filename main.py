__author__ = "7639047, Azimov"

from tkinter import *


# Main Information
root= Tk()
root["bg"] = "#000"
root.geometry("900x800")
root.title("Döner Cafe")
root.wm_attributes("-alpha", 0.9)
root.resizable(width=True, height=True)

# Frames here
Header = Frame(width=1400, height=50, relief=GROOVE)
Header.pack(side=TOP)

f1 = Frame(root, background="#000", width=1400, height=600, relief=GROOVE)
f1.pack(side=BOTTOM)

f2 = Frame(root, background="#000", width=1400, height=800, relief=GROOVE)
f2.pack(side=TOP)


# Header
lblinfo = Label(
    Header,
    font=("Calibri", 30, "bold"),
    text="Döner am Fischtein",
    bg="black",
    fg="white",
    bd=10,
    anchor="w",
)
lblinfo.grid(row=1, column=0)


# Main functions
def btnclick(numbers, text_Input=None):
    """
    Button Click :D
    :param numbers: numbers :p
    :param text_Input: Inputted Text
    :return:
    """
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def Sumup(text_Input=None):
    """
    Global parameters for calculation
    :param text_Input: Inputted Text
    :return:
    """
    global operator
    sumup = str(eval(operator))

    text_Input.set(sumup)
    operator = ""


def Calculate():
    """
    Calculating prices
    :return:
    """
    program.calculate()


def qexit():
    """
    Exiting the GUI
    :return:
    """
    root.destroy()


def reset():
    """
    Resetting all fields
    :return: it just sets the fields to 0
    """
    program.reset()


class Program:
    """
    main program Class
    """
    # String Evaluation
    donermeal = StringVar()
    burgermeal = StringVar()
    pizzameal = StringVar()
    falafelmeal = StringVar()
    forestburgermeal = StringVar()
    pepsidrink = StringVar()
    fantadrink = StringVar()
    wasserdrink = StringVar()
    sevendrink = StringVar()
    coladrink = StringVar()
    Total = StringVar()

    def reset(self):
        """
        resets all price values
        :return:
        """
        self.donermeal.set(0)
        self.pizzameal.set(0)
        self.wasserdrink.set(0)
        self.falafelmeal.set(0)
        self.burgermeal.set(0)
        self.forestburgermeal.set(0)
        self.pepsidrink.set(0)
        self.fantadrink.set(0)
        self.sevendrink.set(0)
        self.coladrink.set(0)
        self.Total.set("")

    def calculate(self):
        """
        gets the prices and evaluates them
        :return:
        """
        doner = float(self.donermeal.get())
        burger = float(self.burgermeal.get())
        pizza = float(self.pizzameal.get())
        falafel = float(self.falafelmeal.get())
        forestburger = float(self.forestburgermeal.get())
        wasser = float(self.wasserdrink.get())
        pepsi = float(self.pepsidrink.get())
        fanta = float(self.fantadrink.get())
        sevenup = float(self.sevendrink.get())
        cola = float(self.coladrink.get())
        # Price Calculation
        donerprice = doner * 7
        burgerprice = burger * 9
        pizzaprice = pizza * 10
        falafelprice = falafel * 13
        forestburgerprice = forestburger * 12
        wasserprice = wasser * 2
        pepsiprice = pepsi * 3
        colaprice = cola * 3.5
        sevenprice = sevenup * 2.5
        fantaprice = fanta * 3.5

        dinnercost = (
            str(
                "%.2f"
                % (
                    donerprice
                    + burgerprice
                    + pizzaprice
                    + falafelprice
                    + forestburgerprice
                    + wasserprice
                    + pepsiprice
                    + fantaprice
                    + sevenprice
                    + colaprice
                )
            ),
            "Euro",
        )
        self.Total.set(dinnercost)

    def create_labels(self):
        """
        creates labels for GUI
        :return:
        """
        lbldoner = Label(
            f1,
            font=("Calibri", 16, "bold"),
            text="Döner",
            bg="black",
            fg="white",
            bd=10,
            anchor="w",
        )
        lbldoner.grid(row=0, column=0)
        txtdoner = Entry(
            f1,
            font=("Calibri", 16, "bold"),
            textvariable=self.donermeal,
            bd=2,
            insertwidth=4,
            bg="#fafafa",
            justify="right",
        )
        txtdoner.grid(row=0, column=1)
        txtdoner.insert(END, "0")
        lblburger = Label(
            f1,
            font=("Calibri", 16, "bold"),
            text="Burger",
            bg="black",
            fg="white",
            bd=10,
            anchor="w",
        )
        lblburger.grid(row=1, column=0)
        lblburger.grid(row=1, column=0)
        txtburger = Entry(
            f1,
            font=("Calibri", 16, "bold"),
            textvariable=self.burgermeal,
            bd=2,
            insertwidth=4,
            bg="white",
            justify="right",
        )
        txtburger.grid(row=1, column=1)
        txtburger.insert(END, "0")

        # Still food labels
        lblpizza = Label(
            f1,
            font=("Calibri", 16, "bold"),
            text="Pizza",
            bg="black",
            fg="white",
            bd=10,
            anchor="w",
        )
        lblpizza.grid(row=3, column=0)
        txtpizza = Entry(
            f1,
            font=("Calibri", 16, "bold"),
            textvariable=self.pizzameal,
            bd=2,
            insertwidth=4,
            bg="white",
            justify="right",
        )
        txtpizza.grid(row=3, column=1)
        txtpizza.insert(END, "0")

        lblfalafel = Label(
            f1,
            font=("Calibri", 16, "bold"),
            text="Falafel",
            bg="black",
            fg="white",
            bd=10,
            anchor="w",
        )
        lblfalafel.grid(row=4, column=0)
        txtfalafel = Entry(
            f1,
            font=("Calibri", 16, "bold"),
            textvariable=self.falafelmeal,
            bd=2,
            insertwidth=4,
            bg="white",
            justify="right",
        )
        txtfalafel.grid(row=4, column=1)
        txtfalafel.insert(END, "0")

        lblforestb = Label(
            f1,
            font=("Calibri", 16, "bold"),
            text="Forest Burger",
            bg="black",
            fg="white",
            bd=10,
            anchor="w",
        )
        lblforestb.grid(row=5, column=0)
        txtforestb = Entry(
            f1,
            font=("Calibri", 16, "bold"),
            textvariable=self.forestburgermeal,
            bd=2,
            insertwidth=4,
            bg="white",
            justify="right",
        )
        txtforestb.grid(row=5, column=1)
        txtforestb.insert(END, "0")

        lblwasser = Label(
            f1,
            font=("Calibri", 16, "bold"),
            text="Wasser",
            bg="black",
            fg="white",
            bd=10,
            anchor="w",
        )
        lblwasser.grid(row=0, column=2)
        txtwasser = Entry(
            f1,
            font=("Calibri", 16, "bold"),
            textvariable=self.wasserdrink,
            bd=2,
            insertwidth=4,
            bg="white",
            justify="right",
        )
        txtwasser.grid(row=0, column=3)
        txtwasser.insert(END, "0")

        lblcola = Label(
            f1,
            font=("Calibri", 16, "bold"),
            text="Cola",
            bg="black",
            fg="white",
            bd=10,
            anchor="w",
        )
        lblcola.grid(row=1, column=2)
        txtcola = Entry(
            f1,
            font=("Calibri", 16, "bold"),
            textvariable=self.coladrink,
            bd=2,
            insertwidth=4,
            bg="white",
            justify="right",
        )
        txtcola.grid(row=1, column=3)
        txtcola.insert(END, "0")

        lblfanta = Label(
            f1,
            font=("Calibri", 16, "bold"),
            text="Fanta",
            bg="black",
            fg="white",
            bd=10,
            anchor="w",
        )
        lblfanta.grid(row=2, column=2)
        txtfanta = Entry(
            f1,
            font=("Calibri", 16, "bold"),
            textvariable=self.fantadrink,
            bd=2,
            insertwidth=4,
            bg="white",
            justify="right",
        )
        txtfanta.grid(row=2, column=3)
        txtfanta.insert(END, "0")

        lblSevenup = Label(
            f1,
            font=("Calibri", 16, "bold"),
            text="7UP",
            bg="black",
            fg="white",
            bd=10,
            anchor="w",
        )
        lblSevenup.grid(row=3, column=2)
        txtSevenup = Entry(
            f1,
            font=("Calibri", 16, "bold"),
            textvariable=self.sevendrink,
            bd=2,
            insertwidth=4,
            bg="white",
            justify="right",
        )
        txtSevenup.grid(row=3, column=3)
        txtSevenup.insert(END, "0")

        lvlPepsi = Label(
            f1,
            font=("Calibri", 16, "bold"),
            text="Pepsi",
            bg="black",
            fg="white",
            bd=10,
            anchor="w",
        )
        lvlPepsi.grid(row=4, column=2)
        txtPepsi = Entry(
            f1,
            font=("Calibri", 16, "bold"),
            textvariable=self.pepsidrink,
            bd=2,
            insertwidth=4,
            bg="white",
            justify="right",
        )
        txtPepsi.grid(row=4, column=3)
        txtPepsi.insert(END, "0")

        lblTotal = Label(
            f1,
            font=("Calibri", 16, "bold"),
            text="Total",
            bg="black",
            fg="green",
            bd=10,
            anchor="w",
        )
        lblTotal.grid(row=5, column=2)
        txtTotal = Entry(
            f1,
            font=("Calibri", 16, "bold"),
            textvariable=self.Total,
            bd=2,
            insertwidth=4,
            bg="white",
            justify="right",
        )
        txtTotal.grid(row=5, column=3)

        # Cheesecheck

    def cheeseCheck(self):
        """
        Checks whether cheese option is checked
        :return:
        """
        var1 = IntVar()
        Checkbutton(
            f1, text="extra cheese", variable=var1, bg="black", fg="white"
        ).grid(row=2, column=0)
        var2 = IntVar()
        Checkbutton(f1, text="no cheese", variable=var2,
                    bg="black", fg="white").grid(
            row=2, column=1
        )

        # Buttons

    def createButtons(self):
        """
        Button creation WOW
        :return:
        """
        btnTotal = Button(
            f1,
            padx=6,
            pady=4,
            bd=4,
            fg="white",
            font=("Calibri", 16, "bold"),
            width=10,
            text="CALCULATE",
            bg="green",
            command=Calculate,
        )
        btnTotal.grid(row=8, column=1)

        btnreset = Button(
            f1,
            padx=6,
            pady=4,
            bd=4,
            fg="black",
            font=("Calibri", 16, "bold"),
            width=7,
            text="RESET",
            bg="white",
            command=reset,
        )
        btnreset.grid(row=8, column=2)

        btnexit = Button(
            f1,
            padx=6,
            pady=4,
            bd=4,
            fg="white",
            font=("Calibri", 16, "bold"),
            width=7,
            text="EXIT",
            bg="red",
            command=qexit,
        )
        btnexit.grid(row=8, column=3)

        # Pricelist

    def createPrices(self):
        """
        Prices are created here bro
        :return:
        """
        lblprice = Label(
            f2,
            font=("Calibri", 15, "bold"),
            text="Products",
            bg="white",
            fg="black",
            bd=5,
        )
        lblprice.grid(row=0, column=0)
        lblprice = Label(
            f2,
            font=("Calibri", 15, "bold"),
            bg="black",
            text="             ",
            fg="black",
            anchor=W,
        )
        lblprice.grid(row=0, column=2)
        lblprice = Label(
            f2,
            font=("Calibri", 15, "bold"),
            text="Price",
            bg="white",
            fg="black",
            anchor=W,
        )
        lblprice.grid(row=0, column=3)
        lblprice = Label(
            f2,
            font=("Calibri", 15, "bold"),
            text="Döner",
            bg="black",
            fg="white",
            anchor=W,
        )
        lblprice.grid(row=1, column=0)
        lblprice = Label(
            f2, font=("Calibri", 15, "bold"), text="7",
            bg="black", fg="white", anchor=W
        )
        lblprice.grid(row=1, column=3)
        lblprice = Label(
            f2,
            font=("Calibri", 15, "bold"),
            text="Döner mit Käse",
            bg="black",
            fg="white",
            anchor=W,
        )
        lblprice.grid(row=2, column=0)
        lblprice = Label(
            f2, font=("Calibri", 15, "bold"), text="8",
            bg="black", fg="white", anchor=W
        )
        lblprice.grid(row=2, column=3)
        lblprice = Label(
            f2,
            font=("Calibri", 15, "bold"),
            text="Pizza",
            bg="black",
            fg="white",
            anchor=W,
        )
        lblprice.grid(row=3, column=0)
        lblprice = Label(
            f2,
            font=("Calibri", 15, "bold"),
            text="10",
            bg="black",
            fg="white",
            anchor=W,
        )
        lblprice.grid(row=3, column=3)
        lblprice = Label(
            f2,
            font=("Calibri", 15, "bold"),
            text="Falafel",
            bg="black",
            fg="white",
            anchor=W,
        )
        lblprice.grid(row=4, column=0)
        lblprice = Label(
            f2,
            font=("Calibri", 15, "bold"),
            text="13",
            bg="black",
            fg="white",
            anchor=W,
        )
        lblprice.grid(row=4, column=3)
        lblprice = Label(
            f2,
            font=("Calibri", 15, "bold"),
            text="Forest Burger ",
            bg="black",
            fg="white",
            anchor=W,
        )
        lblprice.grid(row=5, column=0)
        lblprice = Label(
            f2,
            font=("Calibri", 15, "bold"),
            text="12",
            bg="black",
            fg="white",
            anchor=W,
        )
        lblprice.grid(row=5, column=3)
        lblprice = Label(
            f2,
            font=("Calibri", 15, "bold"),
            text="Wasser",
            bg="black",
            fg="white",
            anchor=W,
        )
        lblprice.grid(row=5, column=0)
        lblprice = Label(
            f2, font=("Calibri", 15, "bold"), text="2",
            bg="black", fg="white", anchor=W
        )
        lblprice.grid(row=6, column=3)
        lblprice = Label(
            f2,
            font=("Calibri", 15, "bold"),
            text="Pepsi",
            bg="black",
            fg="white",
            anchor=W,
        )
        lblprice.grid(row=6, column=0)
        lblprice = Label(
            f2, font=("Calibri", 15, "bold"), text="3",
            bg="black", fg="white", anchor=W
        )
        lblprice.grid(row=7, column=3)
        lblprice = Label(
            f2,
            font=("Calibri", 15, "bold"),
            text="Cola",
            bg="black",
            fg="white",
            anchor=W,
        )
        lblprice.grid(row=7, column=0)
        lblprice = Label(
            f2,
            font=("Calibri", 15, "bold"),
            text="3.5",
            bg="black",
            fg="white",
            anchor=W,
        )
        lblprice.grid(row=8, column=3)
        lblprice = Label(
            f2,
            font=("Calibri", 15, "bold"),
            text="SevenUp",
            bg="black",
            fg="white",
            anchor=W,
        )
        lblprice.grid(row=8, column=0)
        lblprice = Label(
            f2,
            font=("Calibri", 15, "bold"),
            text="2.5",
            bg="black",
            fg="white",
            anchor=W,
        )
        lblprice.grid(row=9, column=3)
        lblprice = Label(
            f2,
            font=("Calibri", 15, "bold"),
            text="Fanta",
            bg="black",
            fg="white",
            anchor=W,
        )
        lblprice.grid(row=9, column=0)


program = Program()
program.create_labels()
program.cheeseCheck()
program.createPrices()
program.createButtons()
root.mainloop()

if __name__ == '__main__':
    main()