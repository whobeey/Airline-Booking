# Import this module which contains import statements and a collection of messages
from const import * 

def check():
    pass

def book():
    pass

def free():
    pass

def status():
    pass

# The main function of this module, it manages actions, data and it displays the main menu
def run(): # The run() function does not take any argument or return any value when called    
    while True: # Continue running the code inside the while statement unless commanded otherwise
        print("\n" + "Welcome to the Apache Airlines booking system!")

        for i, key in enumerate(option, start = 1): # We can use enumerate for easily iterating through a dictionary
            print(str(i) + ' - ' + option[key]) # String Concatenation, turn i/index into a string value in this statement

        choice = input("\n" + message["enter"]).strip()

        match choice: # Call a function or execute a statement depending of the user input
            case '1':
                check()
            case '2':
                book()
            case '3':
                free()
            case '4':
                status()
            case '5':
                print("\n" + message["goodbye"])
                break
            case _:
                print("\n" + error["invalid"] + ' ' + "[red]Please enter a number (1 - 5)[/red]")
                continue

# Creating the seating plan for the Burak 757, set all seats to either 'F'/Free or 'X'/Aisle or 'S'/Storage. In this stage, there will be no booked spaces, therefore no 'R'/Reserved
seats = {} # Initializing an empty dictionary for seating

columns = ["A", "B", "C", "X", "D", "E", "F"] # There will be seven columns, except one will be the aisle 'X'.

# Using a 'for' loop to create the seating map for our Burak 757 aircraft
for row in range(1, 80 + 1): # . We add 1 to the argument of range() to ensure there are 80 because of Python's indexing method
    seats[row] = {}

    # Using a 'for' loop to set certain seats as either 'F'/Free or 'X'/Aisle or 'S'/Storage. In this stage, there will be no booked spaces, therefore no 'R'/Reserved
    for column in columns: # For the column A, B, C... Check and do the following:

        if column == "X": # While iterating through columns, when at 'X' create
            seats[row][column] = "X"  # 'X' -> These are aisle spaces and they are never bookable

        elif 70 < row <= 75: # the rows 71, 72, 73, 74 and 75 are storage areas inside of the aircraft 
            seats[row][column] = "S"  # 'S' -> These are designated & unbookable storage areas in the aircraft

        else: # If no condition applies, set the rest as free seats available for consumer booking
            seats[row][column] = "F"  # 'F' -> These are going to be free/unbooked seats available
