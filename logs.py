def projectDocumentLogs(proj):
    filename = f"logs.txt"
    with open(filename, "a") as logFile:
        logFile.write(f"Project name: {proj.projectName}\n")
        logFile.write(f"Project start: {proj.projectTime}\n")
        logFile.write(f"Project successfully created\n\n")

def finishedProjectDocumentLogs(proj, status):
    filename = f"logs.txt"
    with open(filename, "a") as logFile:
        logFile.write(f"Project name: {proj.projectName}\n")
        logFile.write(f"Project end: {proj.projectTime}\n")
        logFile.write(f"Project status: {status}\n\n")

def createEmployeeBaseLogs(newEmployee, curTime):
    filename = f"logs.txt"
    with open(filename, "a") as logFile:
        logFile.write("New employee added\n")
        logFile.write(f"Employee name: {newEmployee.name}\n")
        logFile.write(f"Employee job role: {newEmployee.jobRole}\n")
        logFile.write(f"Employee other information: {newEmployee.otherEmployeeInfo}\n")
        logFile.write(f"Time added: {curTime}\n\n")

def displayAllEmployeesLogs(curTime):
    filename = f"logs.txt"
    with open(filename, "a") as logFile:
        logFile.write("Request to display all employees has been executed\n")
        logFile.write(f"Request time: {curTime}\n\n")

def createFileForEmployeeLogs(employeeName, curTime):
    filename = f"logs.txt"
    with open(filename, "a")as logFile:
        logFile.write(f"New file with personal tasks created for employee {employeeName}\n")
        logFile.write(f"File creation time: {curTime}\n\n")

def removeEmployeeLogs(employeeName, curTime):
    filename = f"logs.txt"
    with open(filename, "a") as logFile:
        logFile.write(f"Employee {employeeName} has been removed from the project\n")
        logFile.write(f"Removal time: {curTime}\n\n")

def declareTasksLogs(employeeName, newTask, curTime):
    filename = f"logs.txt"
    with open(filename, "a") as logFile:
        logFile.write(f"New task added for employee {employeeName}\n")
        logFile.write(f"Task name: {newTask.taskName}\n")
        logFile.write(f"Task description: {newTask.description}\n")
        logFile.write(f"Task priority: {newTask.priority}\n")
        logFile.write(f"Other task information: {newTask.otherTaskInfo}\n")
        logFile.write(f"Time added: {curTime}\n\n")

def removeTaskLogs(employeeName, taskName, curTime):
    filename = f"logs.txt"
    with open(filename, "a")as logFile:
        logFile.write(f"Task {taskName} has been removed from employee {employeeName}\n")
        logFile.write(f"Removal time: {curTime}\n\n")

def moveTaskLogs(fromEmployee, toEmployee, taskName, curTime):
    filename = f"logs.txt"
    with open(filename, "a") as logFile:
        logFile.write(f"Task {taskName} has been moved from employee {fromEmployee} to employee {toEmployee}\n")
        logFile.write(f"Execution time: {curTime}\n\n")

def checkTasksLogs(employeeName, curTime):
    filename = f"logs.txt"
    with open(filename, "a") as logFile:
        logFile.write(f"Request to display all tasks for employee {employeeName} has been executed\n")
        logFile.write(f"Request time: {curTime}\n\n")

def programStartedLogs(curTime):
    filename = f"logs.txt"
    with open(filename, "a")as logFile:
        logFile.write('\n')
        logFile.write('-' * 50)
        logFile.write(f"\nProgram started at: {curTime}\n\n")

def exitProgramLogs(curTime):
    filename = f"logs.txt"
    with open(filename, "a")as logFile:
        logFile.write(f"Program exited at: {curTime}\n")
        logFile.write('-' *50)