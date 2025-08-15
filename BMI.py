def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)

name=input("Enter your name: ")
print("Hello", name)
try:
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))
except ValueError:
    print("Please enter valid numbers for height and weight.")
    exit()
if height <= 0 or weight <= 0:
    print("Height and weight must be positive numbers.")
elif height > 300 or weight > 500:
    print("Please enter realistic values for height and weight.")
else:
    BMI=round(calculate_bmi(weight, height),2)  
    if BMI < 18.5:
        print(name, "Your BMI is:", BMI, "- You are underweight.")
    elif 18.5 <= BMI < 24.9:
        print(name, "Your BMI is:", BMI, "- You have a normal weight.")
    elif 25 <= BMI < 29.9:
        print(name, "Your BMI is:", BMI, "- You are overweight.")
    elif 30 <= BMI < 34.9:
        print(name, "Your BMI is:", BMI, "- You are in the obese class I category.")
    elif 35 <= BMI < 39.9:
        print(name, "Your BMI is:", BMI, "- You are in the obese class II category.")
    else:  
        print(name, "Your BMI is:", BMI, "- You are in the obese class III category.")

with open("bmi.txt", "a") as f:
    f.write(f"Name={name}, BMI={BMI}\n")
# This code calculates the Body Mass Index (BMI) based on user input for weight and height.
# It provides feedback on the user's weight category based on their BMI value.
# The code includes input validation for height and weight to ensure they are within realistic ranges.
# The BMI is calculated using the formula: weight (kg) / (height (m))^2
# The output is rounded to two decimal places for clarity.
# The user's name and BMI are saved to a text file for record-keeping.
# The file is opened in append mode to add new entries without overwriting existing data.