# Import this module which contains import statements and a collection of messages
from const import * 

# This function will create a table showing seating plan of the Burak 757 Aircraft, reflects later dictionary content
def create_table(): # Only the dictionary will be changed/edited, the table created only reflects*
    seats_table = [] # The purpose of initializing is for storing seating table rows

    for row in range(1, 80 + 1): # Iterating for 80. We add 1 to the argument of range() to ensure there are 80 because of Python's indexing method
        seats_table.append([row, # The current row, from iteration argument given (range(1, 80 + 1))
                            color(seats[row]["A"]), color(seats[row]["B"]),
                            color(seats[row]["C"]), color(seats[row]["X"]), # Note that what is marked as Mark 'X' will never be available, just like 'S'/storage
                            color(seats[row]["D"]), color(seats[row]["E"]),
                            color(seats[row]["F"])]) 

    return seats_table # Returns an updated table, it should not take any argument since we are dealing with one Burak 757 aircraft at the moment

def color(seat_status): # Colors a seat's character depending on status
    if seat_status == "F":
        return "[green1]F[/green1]" # Color indicates available, Free
    elif seat_status == "R":
        return "[bright_red]R[/bright_red]" # Color indicates unavailable, reserved
    elif seat_status == "X":
        return "[grey37]X[/grey37]" # Color indicates grey, ignore
    elif seat_status == "S":
        return "[white]S[/white]" # Color indicates storage, also ignore

    return seat_status # Returns a colored character for status

def check():
    pass

def book():
    pass

def free():
    pass



def status(): # Check status of seats that are free or reserved or aisles or storage spaces
    table_columns = ["  A", "B", "C", "X", "D", "E", "F"] # These are the columns for our aircraft and seating table
    seats_table = create_table() # Calls the function for creating/updating our table that reflects our dictionary (initalized later in code, position follows PEP 8 mostly, so I am sorry about that)

    # Create/Output the seven headers, (A - F) including X -> Aisle
    print("\n", *table_columns, "\n")

    for row in seats_table: # Iterate through each created row of our seating table
        print(f"{row[0]:02}", row[1], row[2], row[3], row[4], row[5], row[6], row[7]) # Creating/Printing the Burak 757 aircraft seating layout plan

    print("\n") # New line, to make sure output is neat in terminal

    for i, indicator in enumerate(indicate, start = 1): # Print list of indicators for information about the aircraft's seats
        print(i, indicator) # Prints a character and what it corresponds to



# Intializing a dictionary to call functions depending on user input
ability = {'1' : check, # calls check()
           '2' : book, # calls book()
           '3' : free, # calls free()
           '4' : status} # calls status()

# The main function of this module, it manages actions, data and it displays the main menu
def run(): # The run() function does not take any argument or return any value when called    
    while True: # Continue running the code inside the while statement unless commanded otherwise
        print("\n" + "Welcome to the Apache Airlines booking system!")

        for i, key in enumerate(option, start = 1): # We can use enumerate for easily iterating through a dictionary
            print(str(i) + ' - ' + option[key]) # String Concatenation, turn i/index into a string value in this statement

        choice = input("\n" + message["enter"]).strip() # Strip spaces to ensure input is compatible

        try: # Try converting input into an integer, to make sure it is valid
            choice = int(choice) # Try converting the user input for item choice into an integer
        except ValueError: # If it fails, then allow them to try again and inform them properly
            print("\n" + error["invalid"] + ' ' + "[red]Please enter a number (1 - 5)[/red]") # Error and explanation
            continue # Restarts the while loop from the beginning   

        # If user input of chosen list item number is 1 to 4, call a function depending on the key value (abilty dictionary)
        if 1 <= choice <= len(ability): # String value must be turned to an integer in the accepted range for this if statement
            ability[str(choice)]() # If true -> call the function based on the key's value, except we need a string value so we used str() to access dictionary indexing. Alternatively, we could remove quotes from the keys
            continue # Go back to the menu, which restarts the current while loop

        elif choice == 5: # If 5 is inputted, then the user wishes to exit
            print("\n" + message["goodbye"])
            break # Exit out of the while loop and end the program
        else: # If input is invalid, let user know and go through the while loop again
            print("\n" + error["invalid"] + ' ' + "[red]Please enter a number (1 - 5)[/red]") # Prints error message
            continue # Continues the while True loop statement

# Creating the seating plan for the Burak 757, set all seats to either 'F'/Free or 'X'/Aisle or 'S'/Storage. In this stage, there will be no booked spaces, therefore no 'R'/Reserved
seats = {} # Initializing an empty dictionary for seating

columns = ["A", "B", "C", "X", "D", "E", "F"] # There will be seven columns, except one will be the aisle 'X'.

# Using a 'for' loop to create the seating map for our Burak 757 aircraft
for row in range(1, 80 + 1): # Iterating for 80. We add 1 to the argument of range() to ensure there are 80 because of Python's indexing method
    seats[row] = {}

    # Using a 'for' loop to set certain seats as either 'F'/Free or 'X'/Aisle or 'S'/Storage. In this stage, there will be no booked spaces, therefore no 'R'/Reserved
    for column in columns: # For the column A, B, C... Check and do the following:

        if column == "X": # While iterating through columns, when at 'X' create
            seats[row][column] = "X"  # 'X' -> These are aisle spaces and they are never bookable

        elif 70 < row <= 75: # the rows 71, 72, 73, 74 and 75 are storage areas inside of the aircraft 
            seats[row][column] = "S"  # 'S' -> These are designated & unbookable storage areas in the aircraft

        else: # If no condition applies, set the rest as free seats available for consumer booking
            seats[row][column] = "F"  # 'F' -> These are going to be free/unbooked seats available