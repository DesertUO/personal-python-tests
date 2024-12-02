# To do list (Python) WIP
from enum import Enum
import os
from utils import sanitizeInputInt, makeLine

# ToDo List actions and definitions
class DateObj:
    def __init__(self, data: dict[str, int]):
        self.day = data.get("day", 1)
        self.month = data.get("month", 1)
        self.year = data.get("year", 2000)
        self.hour = data.get("hour", 0)
        self.minute = data.get("minute", 0)
        self.second = data.get("second", 0)

    def addYear(self, years: int):
        self.year += years
    
    def addMonth(self, month: int):
        months = self.month + month
        if months > 12:
            yearsPassed = months // 12
            self.month = months % 12
            if self.month == 0:
                self.month = 12
                yearsPassed -= 1
            self.addYear(yearsPassed)
        else:
            self.month = months

    def getDaysInMonth(self, month: int, year: int) -> int:
        if month == 2:
            return 29 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28
        elif month in {4, 6, 9, 11}:
            return 30
        else:
            return 31

    def addDay(self, days: int):
        self.day += days
        daysInCurrentMonth = self.getDaysInMonth(self.month, self.year)
        while self.day > daysInCurrentMonth:
            self.day -= daysInCurrentMonth
            self.addMonth(1)
            daysInCurrentMonth = self.getDaysInMonth(self.month, self.year)

    def __repr__(self):
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}"

class StatusModes(Enum):
    STATUS_PENDING = 1
    STATUS_DONE = 2

class ToDoListTasks:
    def __init__(self):
        self.tasks = []
        self.deadlines = []
        self.status = []

    def addTask(self, task: str, deadline: DateObj, status: StatusModes = StatusModes.STATUS_PENDING):
        self.tasks += [task]
        self.deadlines += [deadline]
        self.status += [status]

toDoListTasks = ToDoListTasks()


# ToDo List menu definition

listOfFunctionsNames = ["Add task to ToDo", "Remove task from ToDo", "Edit task in ToDo", "Mark task as completed in ToDo", "Mark task as pending in ToDo", "View tasks in ToDo"]
listOfFunctions = ["1 add", "2 rm", "3 edit", "4 mark completed", "5 mark pending", "6 view list"]
listOfFunctionsNames = listOfFunctionsNames + ["EXIT"]


def menuList():
	welcomeMsg = "Welcome to the To Do List project"
	print(welcomeMsg)
	makeLine(welcomeMsg)
	for i, function in enumerate(listOfFunctionsNames):
		print(f"{i + 1}. {function}")
	doNext = "What do you want to do?"
	makeLine(welcomeMsg)
	print(doNext)

def showList() -> None:
	for i, task in enumerate(toDoListTasks.tasks):
		print(f"{i}. {task}")

def menu() -> None:
	option = 0
	while option != len(listOfFunctionsNames):
		os.system("cls||clear")
		menuList()
		option = sanitizeInputInt(vmin=1, vmax=len(listOfFunctionsNames), errorMsg="Error, please enter a valid option", errorOutOfRange=f"Option must be between {1} and {len(listOfFunctionsNames)}")
	
	print("Thanks for using this To Do List project")

def main() -> None:
	menu()

if __name__ == "__main__":
	main()
