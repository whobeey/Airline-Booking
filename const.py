from rich import print # Allows more cognition and comprehensibility for users (Colors for seat type)
import tabulate as tbl # Provides utility for displaying CLI table in the terminal

# A dictionary to store simple messages that are available to be displayed in terminal output
message = {"welcome" : "Welcome to the Apache Airlines booking system!",
           "enter" : "Enter your Selection (list number): ",
           "goodbye" : "Goodbye valued customer!"}


# A dictionary to store strings that are options/messages to be displayed terminal output
option = {"check": "[green]Check availability of seats[/green]",
          "book": "[blue]Enter seat booking[/blue]",
          "free": "[yellow]Free booked seats[/yellow]",
          "status": "[orange1]Show seat booking status[/orange1]",
          "exit": "[red]Exit the program[/red]"}

# A dictionary to store strings that are options/messages to be displayed terminal output
error = {"invalid": "[red]ERROR: Invalid user input.[/red]"}

indicate = ["[green]\'F\' -> Free to book[/green]",
            "[red]\'R\' -> Reserved[/red]",
            "[grey37]\'X\' -> Aisle Row[/grey37]",
            "[white]\'S\' -> Aircraft Storage[/white]", ]