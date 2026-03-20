# Import the function from the app module, this allows us to launch the app and enter the menu and perform actions
from app import run as main # Import and assign an Alias to the imported Variable/Function called run() in app(.py)

# Ensures non-accidental execution of Functions or Programs in all modules located in the project's directory
if __name__ == "__main__": # If this file is run by the user and it has the name "main(.py)" do the following:
    main() # Calls the function main, performs the actions of run() in the app(.py) module which was imported