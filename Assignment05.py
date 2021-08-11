# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Vera Poliakova,8.9.2021, Added code to complete assignment 5
#   Add strFile variable to represent location of file
#   Step 1: Add code to read ToDoList.txt and load any data into a dictionary & list
#   Step 3: Print dictionary items
#   Step 4: add new item
#   Step 5: remove last item from list using .pop()
#   Step 6: Save tasks to the ToDoToDoList.txt file
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"  # An object that represents a file
objFile = ""  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows
objFile = open(strFile, "r+")
for row in objFile:
     lstRow = row.split(",")
     dicRow = {"task": lstRow[0], "priority": lstRow[1].strip()}
     lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    #print(lstTable) # view that lsttable is populating correctly
    if (strChoice.strip() == '1'):
        for item in lstTable:
            for key in item:
                if (key == "task"):
                    print(key,':',item[key],", ", end="")
                else:
                    print(key, ':', item[key], end="\n")
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task = input("What is the task?")
        priority = input("What is this task's priority?")
        dicRow = {"task": task, "priority": priority}
        lstTable.append(dicRow)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        lstTable.pop() # Removes last item from the list
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        for item in lstTable:
            for key in item:
                if (key == "task"):
                    objFile.write(item[key] + ",")
                else:
                    objFile.write(item[key]+ "\n")
        objFile.close()
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("You have exited the program. Goodbye.")
        break  # and Exit the program
