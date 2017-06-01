# This program ask's the user to enter the attributes for the supervisor object,
# stores the data in the object, and displays the information.

# imports the employee class and all it's attributes
import employee

# Main function
def main():

    # Calls the get super visor function
    supervisor = getSupervisor()

    # Displays all the user entered information
    displaySupervisor(supervisor)

# Function to get supervisor data from the user
def getSupervisor():

    # Input
    name = input('Enter the supervisor name: ')
    idNumber = int(input('Enter the supervisor ID number: '))
    salary = float(input('Enter the supervisor salary: '))
    bonus = float(input('Enter the supervisor bonus: '))
    print()

    # Creates the shift supervisor object ans stores the data
    supervisor = employee.ShiftSupervisor(name, idNumber, salary, bonus)
    return supervisor

# Function to display the information
def displaySupervisor(supervisor):

    #Output
    print('Shift Supervisor:')
    print('---------------------')
    print('Name:', supervisor.get_name())
    print('ID number:', supervisor.get_idNumber())
    print('Salary: $', format(supervisor.get_salary(),',.2f'),sep='')
    print('Bonus: $', format(supervisor.get_bonus(),',.2f'),sep='')

# Calls the main function
main()