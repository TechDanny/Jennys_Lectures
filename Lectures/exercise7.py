weight = int(input("Enter your weight(kgs): "))
height = float(input("Enter your height(metres): "))
BMI = weight / (height ** 2)

if BMI < 16.0:
    print("Underweight (Severe thinness)")
elif BMI < 17.0:
    print("Underweight (Moderate thinness)")
elif BMI < 18.5:
    print("Underweight (Mild thinness)")
elif BMI < 25.0:
    print("Normal range")
elif BMI < 30.0:
    print("Overweight (Pre-obese)")
elif BMI < 35.0:
    print("Obese (Class I)")
else:
    print("Obese (Class II)")
