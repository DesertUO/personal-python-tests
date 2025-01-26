# To do list (Python) WIP
from enum import Enum
import os
from utils import sanitizeInputInt, makeLine
import datetime

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
    # STOP

class DateT:
    def __init__(self, dateStr: str):
        # dateStr structure: year-month-day hour:minute:second
        dateParts = dateStr.split()
        datePart =  dateParts[0].split("-")
        hourPart = dateParts[1].split(":")
        self.year = int(datePart[0])
        self.month = int(datePart[1])
        self.day = int(datePart[2])
        self.hour = int(hourPart[0])
        self.minute = int(hourPart[1])
        self.second = int(hourPart[2])
        self.data = datetime.datetime(self.year, self.month, self.day, self.hour, self.minute, self.second)

    def __repr__(self):
        return str(self.data)

def sanatizeDateInput(msg: str, displayFormat: bool = True, errorMsg: str = "ERROR. Input must be a valid date", defaultDate: str = "1970-1-1 0:0:0", exitKey: str = "q", useExitKey: bool = True) -> str:
    while True:
        userInput = input(msg + (" 'year-month-day hour:minute:second'" if displayFormat == True else "") + ": ")
        if userInput == exitKey and useExitKey == True:
            print("Exiting input...")
            return defaultDate
        try:
            DateStr = userInput
            dateParts = DateStr.split()
            if len(dateParts) != 2:
                print("Use the format 'year-month-day hour:minute:second' with a space ( )")
                raise ValueError

            datePart =  dateParts[0].split("-")
            if len(datePart) != 3:
                print("Date part must be formated as 'year-month-year with dashes (-)'")
                raise ValueError

            hourPart = dateParts[1].split(":")
            if len(hourPart) != 3:
                print("Hour part must be formated as 'hour:minute:second with double points (:)'")
                raise ValueError

            year = int(datePart[0])
            if year < 0:
                print("Year must be positive")
                raise ValueError

            month = int(datePart[1])
            if month < 1 or month > 12:
                print("Month must be between 1 and 12")
                raise ValueError

            day = int(datePart[2])
            if day < 1:
                print("Day must be positive")
                raise ValueError
            #Validate the day based on the month and leap year
            if month == 2:  # February
                max_days = 29 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28
            elif month in {4, 6, 9, 11}:  # April, June, September, November
                max_days = 30
            else:  # Other months
                max_days = 31
            if day > max_days:
                print(f"Day must be between 1 and {max_days} for the given month and year")
                raise ValueError

            hours = int(hourPart[0])
            if hours < 0 or hours > 23:
                print("Hours must be between 0 and 23")
                raise ValueError
            minutes = int(hourPart[1])
            if minutes < 0 or minutes > 59:
                print("Minutes must be between 0 and 59")
                raise ValueError
            seconds = int(hourPart[2])
            if seconds < 0 or seconds > 59:
                print("Seconds must be between 0 and 59")
                raise ValueError
            return DateStr

        except ValueError:
            print(errorMsg)


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
 