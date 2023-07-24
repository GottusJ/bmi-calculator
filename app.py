def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))

        if weight <= 0 or height <= 0:
            print("Invalid input. Weight and height must be positive values.")
            return

        bmi = calculate_bmi(weight, height)
        bmi_category = get_bmi_category(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"BMI Category: {bmi_category}")
    except ValueError:
        print("Invalid input. Please enter valid weight and height.")

if __name__ == "__main__":
    main()
