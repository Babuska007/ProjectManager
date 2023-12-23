#Project managment system

from collections import deque
from pyllist import sllist
import datetime
import os
import sys
import logs

class project:
    def __init__(self):
        self.projectName = ""
        self.projectTime = ""

class task:
    def __init__(self):
        self.taskName = ""
        self.description = ""
        self.priority = ""
        self.otherTaskInfo = ""

class employeeInfo:
    def __init__(self):
        self.name = ""
        self.jobRole = ""
        self.otherEmployeeInfo = ""
        self.tasks = deque()

class manager:
    def __init__(self):
        self.employeeList = sllist()
        self.projectList = sllist()
        self.projectCreated = False
        self.employeeBaseCreated = False

    #---------------MAIN FUNCTIONS(PROJECT MANAGMENT)----------------------

    def createProject(self,UIProjectName):
        os.system('clear')
        if self.projectCreated:
            print("A project has already been created. You can not create another project before finishing the previous project.")
            return        
        newProject = project()
        newProject.projectName = UIProjectName

        timeString = self.getTime()
        newProject.projectTime = timeString

        print("Project:", newProject.projectName)
        print("Project start:", newProject.projectTime)
        
        self.generateProjectDocument(newProject)
        logs.projectDocumentLogs(newProject)

        self.projectList.append(newProject)
        self.projectCreated = True;

    def finishProject(self, UIStatus):
        os.system('clear')
        if not self.projectList:
            print("No projects to finish")
            return
        
        currentProject = self.projectList[-1]
        enterStatus = UIStatus

        print("Project name:", currentProject.projectName)
        print("Project start:", currentProject.projectTime)

        timeString = self.getTime()
        print("Project end:", timeString)
        print("Status:", enterStatus)

        fileName = f"{currentProject.projectName}.txt"
        with open(fileName, "a") as projectFile:
            projectFile.write(f"Project end: {timeString}\n")
            projectFile.write(f"Project status: {enterStatus}\n")

        print("Project document finished successfully")

        self.projectCreated = False
        self.employeeBaseCreated = False

        logs.finishedProjectDocumentLogs(currentProject, enterStatus)
        #todo when creating a new project, the members stay from the previous projects
        self.projectList.pop()
        
#-------------------MAIN FUNCTIONS(EMPLOYEE MANAGEMENT)---------------------

    def createEmployeeBase(self):
        os.system('clear')
        if self.employeeBaseCreated:
            print("An employee team has already been created, you can only add or remove employees.")
            return self.employeeBaseCreated
        self.employeeBaseCreated = True

    def displayAllEmployeesFull(self):
        os.system('clear')
        if not self.employeeList:
            print("Employee list is empty")
            return
        print("List of all employees:")
        for employee in self.employeeList:
            print("Employee name:",employee.name)
            print("Employee job role:",employee.jobRole)
            print("Employee other information:",employee.otherEmployeeInfo)
            print()
        timeString = self.getTime()
        logs.displayAllEmployeesLogs(timeString)

    def addMember(self, UIName, UIJobRole, UIOtherInfo):
            temp = employeeInfo()
            os.system('clear')
            temp.name = UIName
            temp.jobRole = UIJobRole
            temp.otherEmployeeInfo = UIOtherInfo
            self.employeeList.append(temp)
            timeString = self.getTime()
            logs.createEmployeeBaseLogs(temp, timeString)

    def removeMember(self, UIEmployeeName):
        os.system('clear')
        if not self.employeeList:
            print("Employee list is empty")
            return

        self.displayAllEmployees()

        employeeName = UIEmployeeName

        foundEmployee = self.findEmployee(employeeName)

        if not foundEmployee:
            print("Employee does not exist")
            return
        
        timeString = self.getTime()
        logs.removeEmployeeLogs(employeeName, timeString)

        nodeToRemove = self.employeeList.first
        while nodeToRemove:
            if nodeToRemove.value == foundEmployee:
                self.employeeList.remove(nodeToRemove)
                print(f"Employee {foundEmployee.name} has been removed.")
                return
            nodeToRemove = nodeToRemove.next

#--------------------MAIN FUNCTIONS(TASK MANAGEMENT)-----------------------

    def canDeclareTasks(self, UIEmployeeName):
        os.system('clear')
        isEmployeeListEmpty = not bool(self.employeeList)
    
        if isEmployeeListEmpty:
            print("Employee list is empty")
            return False

        self.displayAllEmployees()

        employeeName = UIEmployeeName
        foundEmployee = self.findEmployee(employeeName)

        if not foundEmployee:
            print(f"Employee {employeeName} was not found")
            return False

        return True



    def addTask(self, UIEmployeeName, UITaskName, UIDescriprionName, UIPriority, UIOtherInfo):
        foundEmployee = self.findEmployee(UIEmployeeName)
        newTask = task()
        os.system('clear')
        newTask.taskName = UITaskName
        newTask.description = UIDescriprionName
        newTask.priority = UIPriority
        newTask.otherTaskInfo = UIOtherInfo
        foundEmployee.tasks.append(newTask)

        timeString = self.getTime()
        logs.declareTasksLogs(UIEmployeeName, newTask, timeString)

        print(f"Tasks for employee {UIEmployeeName} have been added successfully.")
    
    def removeTask1(self, UIEmployeeName):
        os.system('clear')
        
        if not self.employeeList:
            print("Employee list is empty, no tasks have been added yet.")
            return True

        self.displayAllEmployees()
        
        employeeName = UIEmployeeName
        foundEmployee = self.findEmployee(employeeName)

        if not foundEmployee:
            print(f"Employee {employeeName} not found")
            return True

        self.printTasks(foundEmployee)
        return False
    
    def removeTask2(self, UIEmployeeName, UITaskName):
        foundEmployee = self.findEmployee(UIEmployeeName)
        searchTask = UITaskName
        foundTask = self.findTaskName(foundEmployee, searchTask)

        if not foundTask:
            print(f"Task {searchTask} not found")
            return

        timeString = self.getTime()
        logs.removeTaskLogs(UIEmployeeName, searchTask, timeString)
        foundEmployee.tasks.remove(foundTask)

    def checkTasks(self, UIEmployeeName):
        os.system('clear')
        if not self.employeeList:
            print("Employee list is empty.")
            return

        self.displayAllEmployees()

        employeeName = UIEmployeeName

        foundEmployee = self.findEmployee(employeeName)

        if foundEmployee:
            self.printTasks(foundEmployee)
            timeString = self.getTime()
            logs.checkTasksLogs(employeeName, timeString)
        else:
            print(f"Employee {employeeName} was not found")

    def moveTask1(self, UIFromEmployee):
        os.system('clear')

        if not self.employeeList:
            print("Employee list is empty")
            return True
        
        self.displayAllEmployees()

        fromEmployee = UIFromEmployee
        fromFoundEmployee = self.findEmployee(fromEmployee)

        if not fromFoundEmployee:
            print(f"Employee {fromFoundEmployee} was not found")
            return True
            
        self.printTasks(fromFoundEmployee)
        return False

    def moveTask2(self, UIFromEmployee, UITaskName):
        fromFoundEmployee = self.findEmployee(UIFromEmployee)
        searchTask = UITaskName
        foundTask = self.findTaskName(fromFoundEmployee, searchTask)

        if not foundTask:
            print(f"Task {searchTask} not found for {fromFoundEmployee}")
            return True
        return False

    def moveTask3(self, UIFromEmployee, UITOEmployee, UITaskName):
        fromFoundEmployee = self.findEmployee(UIFromEmployee)
        searchTask = UITaskName
        foundTask = self.findTaskName(fromFoundEmployee, searchTask)
        toEmployee = UITOEmployee
        toFoundEmployee = self.findEmployee(toEmployee)

        if not toFoundEmployee:
            print(f"Employee {toEmployee} not found")
            return

        timeString = self.getTime()
        logs.moveTaskLogs(UIFromEmployee, toEmployee, UITaskName, timeString)
        toFoundEmployee.tasks.append(foundTask)
        fromFoundEmployee.tasks.remove(foundTask)

#-------------------SIDE FUNCTIONS------------------------

    def printTasks(self, employee):
            print(f"{employee.name}'s tasks: ")
            if not employee.tasks:
                print("No tasks are assigned to this employee.")
            else:
                for task in employee.tasks:
                    print("Task:", task.taskName)
                    print("Description:", task.description)
                    print("Priority:", task.priority)
                    print("Other:", task.otherTaskInfo)
                    print()

    def getTime(self):
        currentTime = datetime.datetime.now()
        return currentTime.strftime("%Y-%m-%d  %H:%M:%S")

    def displayAllEmployees(self):
        os.system('clear')
        if not self.employeeList:
            print("Employee list is empty")
            return
        print("List of all employees:")
        for employee in self.employeeList:
            print("Employee name:",employee.name)

    def findEmployee(self, employeeName):
        foundEmployee = None
        for employee in self.employeeList:
            if employee.name == employeeName:
                foundEmployee = employee
                break
        return foundEmployee

    def findTaskName(self, employeeName, taskN):
        foundTaskName = None
        for task in employeeName.tasks:
            if task.taskName == taskN:
                foundTaskName = task
                break
        return foundTaskName

#------------Function printAllTasks() is not fully functional----------

    def printAllTasks(self):
        currentEmployeeNode = self.employeeList.first
        while currentEmployeeNode:
            currentEmployee = currentEmployeeNode.value
            if currentEmployee.tasks:
                currentEmployeeTaskNode = currentEmployeeNode.tasks[0]
                for task in currentEmployeeTaskNode:
                    print("Task:", currentEmployeeTaskNode.taskName)
                    print("Description:", currentEmployeeTaskNode.description)
                    print("Priority:", currentEmployeeTaskNode.priority)
                    print("Other:", currentEmployeeTaskNode.otherTaskInfo)
                    print()
                    currentEmployeeTaskNode = currentEmployeeTaskNode.next

            currentEmployeeNode = currentEmployeeNode.next

#------------------FUNCTIONS THAT GENERATE--------------------------------

    def generateProjectDocument(self, proj):
        fileName = f"{proj.projectName}.txt"
        with open(fileName, "w") as projectFile:
            projectFile.write(f"Project name: {proj.projectName}\n")
            projectFile.write(f"Project start: {proj.projectTime}\n")

        print("Project document created successfully")

    def createFileForEmployee(self, UIEmployeeName):
        os.system('clear')
        if not self.employeeList:
            print("Employee list is empty.")
            return
        
        self.displayAllEmployees()

        employeeName = UIEmployeeName

        foundEmployee = self.findEmployee(employeeName)

        if foundEmployee:
            filename = f"{foundEmployee.jobRole}.txt"
            with open(filename, "w") as employeeFile:
                if not foundEmployee.tasks:
                    employeeFile.write("Employee has no tasks.")
                else:
                    for task in foundEmployee.tasks:
                        employeeFile.write(f"Task: {task.taskName}\n")
                        employeeFile.write(f"Description: {task.description}\n")
                        employeeFile.write(f"Priority: {task.priority}\n")
                        employeeFile.write(f"Other: {task.otherTaskInfo}\n\n")
            
            timeString = self.getTime()
            logs.createFileForEmployeeLogs(employeeName, timeString)
            print(f"File for employee {employeeName} has been created.")
        else:
            print(f"Employee {employeeName} was not found")

    def programStart(self):
        timeString = self.getTime()
        logs.programStartedLogs(timeString)

    def exitProgram(self):
        print("Exiting program")
        timeString = self.getTime()
        logs.exitProgramLogs(timeString)
        sys.exit(0)