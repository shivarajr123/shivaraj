#Front End

from tkinter import*
import tkinter.messagebox
import Back_end
class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student database management system")
        self.root.geometry("1350x7500+0+0")
        self.root.config(bg="cadet blue")

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        # =====================================Functions===================================#

        def iExit():
            iExit=tkinter.messagebox.askyesno("Student Database Managenent Systems","Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return



        #=====================================Frames===================================#

        MainFrame = Frame(self.root,bg="cadet blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame ,font=('arial', 47, 'bold'),text="Student Database Management systems", bg="Ghost White")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, bg="cadet blue", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT =LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, bg="Ghost White", relief=RIDGE,font=('arial', 20, 'bold'), text="Student info\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, bg="Ghost White", relief=RIDGE,font=('arial', 20, 'bold'), text="Student Details\n")
        DataFrameRIGHT.pack(side=RIGHT)

        # =====================================Labels and Entry Widget===================================#

        self.lblStdID = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Student ID:",padx=2, pady=2,bg="Ghost White")
        self.lblStdID.grid(row=0,column=0,sticky=W)
        self.txtStdID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID, width=39)
        self.txtStdID.grid(row=0, column=1)

        self.lblfna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Firstname:", padx=2, pady=2, bg="Ghost White")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Firstname, width=39)
        self.txtfna.grid(row=1, column=1)

        self.lblSna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Surname:",padx=2, pady=2,bg="Ghost White")
        self.lblSna.grid(row=2,column=0,sticky=W)
        self.txtSna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Surname, width=39)
        self.txtSna.grid(row=2, column=1)

        self.lblDoB = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="DoB:", padx=2, pady=2, bg="Ghost White")
        self.lblDoB.grid(row=3, column=0, sticky=W)
        self.txtDoB = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=DoB, width=39)
        self.txtDoB.grid(row=3, column=1)

        self.lblAge = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Age:", padx=2, pady=2, bg="Ghost White")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1)

        self.lblGender = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Gender:", padx=2, pady=2, bg="Ghost White")
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.txtGender = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Gender, width=39)
        self.txtGender.grid(row=5, column=1)

        self.lblMobile = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Mobile:", padx=2, pady=2, bg="Ghost White")
        self.lblMobile.grid(row=7, column=0, sticky=W)
        self.txtMobile = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Mobile, width=39)
        self.txtMobile.grid(row=7, column=1)

        self.lblAddress = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Address:", padx=2, pady=2, bg="Ghost White")
        self.lblAddress.grid(row=6, column=0, sticky=W)
        self.txtAddress = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Address, width=39)
        self.txtAddress.grid(row=6, column=1)

        # =====================================Listbox and Scrollbar Widget===================================#

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')
        studentlist = Listbox(DataFrameRIGHT,width=41,height=16,font=('arial',12,'bold'),yscrollcommand= scrollbar.set)
        studentlist.grid(row=0,column=0,padx=8)
        scrollbar.config(command= studentlist.yview)


        # =====================================Button Widget===================================#

        self.btnAddData = Button(ButtonFrame,text="Add New", width=10,height=1,font=('arial',12,'bold'),bd=4)
        self.btnAddData.grid(row=0,column=0)
        self.btnDisplaydata = Button(ButtonFrame, text="Display", width=10, height=1, font=('arial', 12, 'bold'), bd=4)
        self.btnDisplaydata.grid(row=0, column=1)
        self.btnClearData = Button(ButtonFrame, text="Clear", width=10, height=1, font=('arial', 12, 'bold'), bd=4)
        self.btnClearData.grid(row=0, column=2)
        self.btnDeleteData = Button(ButtonFrame, text="Delete", width=10, height=1, font=('arial', 12, 'bold'), bd=4)
        self.btnDeleteData.grid(row=0, column=3)
        self.btnSearchData = Button(ButtonFrame, text="Search", width=10, height=1, font=('arial', 12, 'bold'), bd=4)
        self.btnSearchData.grid(row=0, column=4)
        self.btnUpdateData = Button(ButtonFrame, text="Update", width=10, height=1, font=('arial', 12, 'bold'), bd=4)
        self.btnUpdateData.grid(row=0, column=5)
        self.btnExitData = Button(ButtonFrame, text="Exit", width=10, height=1, font=('arial', 12, 'bold'), bd=4,command=iExit)
        self.btnExitData.grid(row=0, column=6)




if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()





