# Title
print("\n\033[1;32;40m", "*"*20, "LEAP YEARS CHECKER", "*"*20+"\n")
# Initial input
start_input = input("\033[1;32;40m"+"Please enter the starting year (numbers only):\n")
# Checks if player entered a valid input
while not start_input.isnumeric():
    print("\n\033[1;31;40m"+"Invalid input: Starting year must be only numbers!"+"\033[1;32;40m\n")
    start_input = input("Please try again:\n")
# Ending input
end_input = input("\nPlease enter the ending year:\n")
# Checks if player entered a valid input
while not end_input.isnumeric() or int(end_input) < int(start_input):
    print("\n\033[1;31;40m"+"Invalid input: Ending year must be greater than the starting year and numbers only!"+"\033[1;32;40m\n")
    end_input = input("Please try again:\n")
print("\nLeap years:")
# Checks the conditions for a leap year
print("*"*60)
for year in range(int(start_input), int(end_input)+1):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print(year, " "*54+"*")
print("*"*60+"\n")