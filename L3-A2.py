Height = float(input("Enter you height in Centimeters(CM): "))
Weight = float(input("Enter you height in Kilograms(KG): "))

BMI = Weight / (Height/100)** 2

if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are overweight")
elif BMI <= 34.9:
    print("You are severely overweight")
elif BMI <= 39.9:
    print("You are OBESE")
else:
    print("You are severely obese, fatty")