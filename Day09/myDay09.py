# Day 09
# Calculating Arithmetic Mean in Python

# Initialize the exit flag to control the loop
exit_flag = False

# Initialize an empty list to store numbers
num_list = list()

# Continuously prompt the user to enter numbers
while not exit_flag:
    data = input("Enter a number (type 'done' to finish): ")

    if data.lower() == "done":  # Allowing both 'done' and 'Done'
        exit_flag = True
    else:
        try:
            value = float(data)  	  # Convert input to a float type
            num_list.append(value)  # Add the value to the list
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Calculate the average of the numbers in the list
if num_list: 		 # Check if the list is not empty to avoid ZeroDivisionError
    average = sum(num_list) / len(num_list)
    print("Average: ", average)    # Print the calculated average
else:
    print("No data entered. Cannot calculate average.")  # Print a message if no data is entered
