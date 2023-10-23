# Day 07
# Employee Hour-Rate Conversion in Python

# Get user inputs for hours worked and hourly rate
hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate (in $): "))

# Calculate pay based on regular and overtime rates
if hours_worked > 40:
    regular_pay = 40 * hourly_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (hourly_rate * 1.5)  # Overtime rate is 1.5 times the hourly rate
    total_pay = regular_pay + overtime_pay
else:
    total_pay = hours_worked * hourly_rate

# Display the calculated pay
print(f"Pay: ${total_pay:.2f}")

