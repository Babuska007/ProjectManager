from tkinter import *
import main
from main import manager

PJManager = manager()
#start app time
PJManager.programStart()

root = Tk()
root.title("Project Manager")

#root.iconbitmap('/Users/augustinasvelicka/Desktop/PJicon.ico')
root.geometry("380x400")

myMenu = Menu(root)
root.config(menu=myMenu)

def myCommand(self):
    pass

def buttonFunction(self):
    pass

#----------------------BUTTON 1 FUNCTIONS-----------------------

def newProject():
    top = Toplevel()
    top.title('New Project Creation')
    top.geometry("380x400")
    label = Label(top, text = "Enter your project name")
    label.pack()
    textBox = Entry(top, width = 30)
    textBox.pack()
    saveButton = Button(top, text="Save", command =lambda: button1Commands(top, textBox))
    saveButton.pack()

def button1Commands(top, textBox):
    button1Click(textBox)
    exitWindow(top)

def button1Click(textBox):
    PJManager.createProject(textBox.get())

#----------------------BUTTON 2 FUNCTIONS-----------------------
    
def createEmployeeBase():
    employeeBaseCreated = PJManager.createEmployeeBase()
    if employeeBaseCreated:
        return
    top = Toplevel()
    top.title('Create Employee Base')
    top.geometry("380x400")
    
    label = Label(top, text = "Enter employee amount")
    label.pack()
    textBox = Entry(top, width = 30)
    textBox.pack()

    saveButton = Button(top, text="Save", command =lambda: button2Commands(top, textBox))
    saveButton.pack()

def button2Commands(top, textBox):
    button2Click(textBox)
    exitWindow(top)

def button2Click(textBox):
    amount = int(textBox.get())
    for _ in range(amount):
        addEmployee()
#----------------------BUTTON 3 FUNCTIONS-----------------------
#todo: check if boxes are empty
def addEmployee():
    top = Toplevel()
    top.title('Add an employee')
    top.geometry("380x400")
    label1 = Label(top, text = "Enter employee name")
    label1.pack()
    textBox1 = Entry(top, width = 30)
    textBox1.pack()
    label2 = Label(top, text = "Enter employee job role")
    label2.pack()
    textBox2 = Entry(top, width = 30)
    textBox2.pack()
    label3 = Label(top, text = "Enter employee other information")
    label3.pack()
    textBox3 = Entry(top, width = 30)
    textBox3.pack()
    saveButton = Button(top, text="Save", command =lambda: button3Commands(top, textBox1, textBox2, textBox3))
    saveButton.pack()

def button3Commands(top, textBox1, textBox2, textBox3):
    button3Click(textBox1, textBox2, textBox3)
    exitWindow(top)

def button3Click(textBox1, textBox2, textBox3):
    PJManager.addMember(textBox1.get(), textBox2.get(), textBox3.get())

#----------------------BUTTON 4 FUNCTIONS-----------------------
def removeEmployee():
    PJManager.displayAllEmployees()
    top = Toplevel()
    top.title('Remove employee')
    top.geometry("380x400")
    label = Label(top, text = "Enter the employee you want to remove")
    label.pack()
    textBox = Entry(top, width = 30)
    textBox.pack()
    saveButton = Button(top, text="Save", command =lambda: button4Commands(top, textBox))
    saveButton.pack()

def button4Commands(top, textBox):
    button4Click(textBox)
    exitWindow(top)

def button4Click(textBox):
    PJManager.removeMember(textBox.get())

#----------------------BUTTON 5 FUNCTIONS-----------------------
def displayAllEmployees():
    PJManager.displayAllEmployeesFull()
#----------------------BUTTON 6 FUNCTIONS-----------------------
def declareTasksForEmployee():
    PJManager.displayAllEmployees()
    top = Toplevel()
    top.title('Declare tasks for employee')
    top.geometry("380x400")
    label = Label(top, text="Enter the employee you would like to add tasks to")
    label.pack()
    textBox = Entry(top, width=30)
    textBox.pack()
    saveButton = Button(top, text="Save", command=lambda: button5Commands(top, textBox))
    saveButton.pack()

def button5Commands(top, textBox):
    UIEmployeeName = textBox.get()
    isEmptyAndNotFound = PJManager.canDeclareTasks(UIEmployeeName)
    if isEmptyAndNotFound:
        exitWindow(top)
        button5Click(UIEmployeeName)
    else:
        exitWindow(top)

def button5Click(UIEmployeeName):
    top = Toplevel()
    top.title('Declare task amount for employee')
    top.geometry("500x400")
    label = Label(top, text="Enter the amount of tasks you would like to add for your employee")
    label.pack()
    textBox = Entry(top, width=30)
    textBox.pack()
    saveButton = Button(top, text="Save", command=lambda: button5ClickAddTasks(top, UIEmployeeName, textBox))
    saveButton.pack()

def button5ClickAddTasks(top, UIEmployeeName, textBox):
    try:
        amount = int(textBox.get())
        exitWindow(top)
        for _ in range(amount):
            addTask(UIEmployeeName)
    except ValueError:
        pass

def addTask(UIEmployeeName):
    top3 = Toplevel()
    top3.title('Add task')
    top3.geometry("380x400")
    label1 = Label(top3, text="Enter task name")
    label1.pack()
    textBox1 = Entry(top3, width=30)
    textBox1.pack()
    label2 = Label(top3, text="Enter task description")
    label2.pack()
    textBox2 = Entry(top3, width=30)
    textBox2.pack()
    label3 = Label(top3, text="Enter task priority")
    label3.pack()
    textBox3 = Entry(top3, width=30)
    textBox3.pack()
    label4 = Label(top3, text="Enter task other information")
    label4.pack()
    textBox4 = Entry(top3, width=30)
    textBox4.pack()
    saveButton = Button(top3, text="Save", command=lambda: button5CommandsFinal(UIEmployeeName, top3, textBox1, textBox2, textBox3, textBox4))
    saveButton.pack()

def button5CommandsFinal(UIEmployeeName, top3, textBox1, textBox2, textBox3, textBox4):
    PJManager.addTask(UIEmployeeName, textBox1.get(), textBox2.get(), textBox3.get(), textBox4.get())
    exitWindow(top3)

#----------------------BUTTON 7 FUNCTIONS-----------------------
def moveTask():
    top = Toplevel()
    top.title('Move task')
    top.geometry("380x400")
    label = Label(top, text="Enter the employee you would like to move the tasks from")
    label.pack()
    textBox = Entry(top, width=30)
    textBox.pack()
    saveButton = Button(top, text="Save", command = lambda: button7Commands(top, textBox))
    saveButton.pack()

def button7Commands(top, textBox):
    UIFromEmployee = textBox.get()
    shouldWindowClose = PJManager.moveTask1(UIFromEmployee)
    if shouldWindowClose:
        exitWindow(top)
    else:
        exitWindow(top)
        button7Click(UIFromEmployee)

def button7Click(UIFromEmployee):
    top1 = Toplevel()
    top1.title('Find task')
    top1.geometry("380x400")
    label = Label(top1, text = "Enter task name")
    label.pack()
    textBox = Entry(top1, width = 30)
    textBox.pack()
    saveButton = Button(top1, text="Save", command =lambda: button7Commands2(top1, UIFromEmployee, textBox))
    saveButton.pack()

def button7Commands2(top1, UIFromEmployee, textBox):
    UITaskName = textBox.get()
    shouldWindowClose = PJManager.moveTask2(UIFromEmployee, UITaskName)
    if shouldWindowClose:
        exitWindow(top1)
    else:
        exitWindow(top1)
        button7click2(UIFromEmployee, UITaskName)

def button7click2(UIFromEmployee, UITaskName):
    top2 = Toplevel()
    top2.title('Find task')
    top2.geometry("380x400")
    label = Label(top2, text = "Enter the employee you would like to move the tasks to")
    label.pack()
    textBox = Entry(top2, width = 30)
    textBox.pack()
    saveButton = Button(top2, text="Save", command =lambda: button7CommandsFinal(top2, UIFromEmployee, UITaskName, textBox))
    saveButton.pack()

def button7CommandsFinal(top2, UIFromEmployee, UITaskName, textBox):
    UITOEmployee = textBox.get()
    PJManager.moveTask3(UIFromEmployee, UITOEmployee, UITaskName)
    exitWindow(top2)

#----------------------BUTTON 8 FUNCTIONS-----------------------
    
def button8Commands(top, textBox):
    PJManager.checkTasks(textBox.get())
    exitWindow(top)

def checkEmployeeTasks():
    top = Toplevel()
    top.title('Check employee tasks')
    top.geometry("380x400")
    label = Label(top, text="Enter the employee you would like to check the tasks")
    label.pack()
    textBox = Entry(top, width=30)
    textBox.pack()
    saveButton = Button(top, text="Save", command = lambda: button8Commands(top, textBox))
    saveButton.pack()

#----------------------BUTTON 9 FUNCTIONS-----------------------
    
def removeEmployeeTask():
    top = Toplevel()
    top.title('New Project Creation')
    top.geometry("380x400")
    label = Label(top, text = "Enter employee name")
    label.pack()
    textBox = Entry(top, width = 30)
    textBox.pack()
    saveButton = Button(top, text="Save", command =lambda: button9Commands(top, textBox))
    saveButton.pack()

def button9Commands(top, textBox):
    UIEmployeeName = textBox.get()
    shouldWindowClose = PJManager.removeTask1(UIEmployeeName)
    if shouldWindowClose:
        exitWindow(top)
    else:
        button9Click(UIEmployeeName)
        exitWindow(top)

def button9Click(UIEmployeeName):
    top1 = Toplevel()
    top1.title('Find task')
    top1.geometry("380x400")
    label = Label(top1, text = "Enter task name")
    label.pack()
    textBox = Entry(top1, width = 30)
    textBox.pack()
    saveButton = Button(top1, text="Save", command =lambda: button9CommandsFinal(top1, UIEmployeeName, textBox))
    saveButton.pack()
    
def button9CommandsFinal(top1, UIEmployeeName, textBox):
    PJManager.removeTask2(UIEmployeeName, textBox.get())
    exitWindow(top1)

#----------------------BUTTON 10 FUNCTIONS----------------------
def createFileForEmployee():
    PJManager.displayAllEmployees()
    top = Toplevel()
    top.title('Create file for employee')
    top.geometry("380x400")
    label = Label(top, text = "Enter the employee you would like to create a file for")
    label.pack()
    textBox = Entry(top, width = 30)
    textBox.pack()
    saveButton = Button(top, text="Save", command =lambda: button10Commands(top, textBox))
    saveButton.pack()

def button10Commands(top, textBox):
    button10Click(textBox)
    exitWindow(top)

def button10Click(textBox):
    PJManager.createFileForEmployee(textBox.get())   
#----------------------BUTTON 11 FUNCTIONS----------------------
def finishProject():
    top = Toplevel()
    top.title('Finish project')
    top.geometry("380x400")
    label = Label(top, text = "Enter your project status")
    label.pack()
    textBox = Entry(top, width = 30)
    textBox.pack()
    saveButton = Button(top, text="Save", command =lambda: button11Commands(top, textBox))
    saveButton.pack()

def button11Commands(top, textBox):
    button11Click(textBox)
    exitWindow(top)

def button11Click(textBox):
    PJManager.finishProject(textBox.get())
#----------------------BUTTON 12 FUNCTIONS----------------------
def button12Commands(root):
    PJManager.exitProgram()
    exitProgram(root)

#-----------------------SIDE FUNCTIONS------------------------
    
def createLabel(windowName, labelName, addText):
    labelName = Label(windowName, text = addText)
    labelName.pack()

def createTextBox(windowName, textBoxName, addWidth):
    textBoxName = Entry(windowName, width = addWidth)
    textBoxName.pack()
    return textBoxName.get()

def exitWindow(top):
    top.destroy()

def exitProgram(root):
    root.quit()

#-------------------TOP BAR----------------------------

#create a menu item
fileMenu = Menu(myMenu, tearoff = 0)
myMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=newProject)
fileMenu.add_command(label="Logs", command=myCommand)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=lambda: button12Commands(root))

#edit menu
editMenu = Menu(myMenu)
myMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=myCommand)
editMenu.add_command(label="Copy", command=myCommand)

#options menu
optionsMenu = Menu(myMenu)
myMenu.add_cascade(label="Options", menu=optionsMenu)
optionsMenu.add_command(label="Theme", command=myCommand)
optionsMenu.add_command(label="Size", command=myCommand)

#------------------------MAIN MENU BUTTONS----------------------------------

label = Label(root, text = "Main Menu", font = ('Arial', 20))
label.grid(row=0, column=0, columnspan=2, sticky = "nsew") 

#Define buttons
button1 = Button(root, text="New Project",width=15,height=2,padx=10, pady=10, command=newProject)
button2 = Button(root, text="Create employee base",width=15,height=2,padx=10, pady=10, command=createEmployeeBase)
button3 = Button(root, text="Add a team member",width=15,height=2,padx=10, pady=10, command=addEmployee)
button4 = Button(root, text="Remove a team member",width=15,height=2,padx=10, pady=10, command=removeEmployee)
button5 = Button(root, text="Display all employees",width=15,height=2,padx=10, pady=10, command=displayAllEmployees)
button6 = Button(root, text="Declare tasks for employee",width=15,height=2,padx=10, pady=10, command=declareTasksForEmployee)
button7 = Button(root, text="Move a certain task",width=15,height=2,padx=10, pady=10, command=moveTask)
button8 = Button(root, text="Check employee tasks",width=15,height=2,padx=10, pady=10, command=checkEmployeeTasks)
button9 = Button(root, text="Remove employee task",width=15,height=2,padx=10, pady=10, command=removeEmployeeTask)
button10 = Button(root, text="Create a file for an employee",width=15,height=2,padx=10, pady=10, command=createFileForEmployee)
button11 = Button(root, text="Finish project",width=15,height=2,padx=10, pady=10, command=finishProject)
button12 = Button(root, text="Exit program",width=15,height=2,padx=10, pady=10, command=lambda: button12Commands(root))

#Put buttons on the screen
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=2,column=0)
button4.grid(row=2,column=1)
button5.grid(row=3,column=0)
button6.grid(row=3,column=1)
button7.grid(row=4,column=0)
button8.grid(row=4,column=1)
button9.grid(row=5,column=0)
button10.grid(row=5,column=1)
button11.grid(row=6,column=0)
button12.grid(row=6,column=1)



root.mainloop()