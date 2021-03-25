height = float(input("Enter your height (m) : "))
weight = float(input("Enter your weight (kg) : "))
bmi = round(weight / height**2)

if bmi < 18.5:
   print(f"Your bmi is {bmi} ,You are underweight")
elif bmi <25:
   print(f"Your bmi is {bmi} ,You are the normal weight.")
elif bmi <30:
   print(f"Your bmi is {bmi} ,You are the overweight.")
elif bmi <35:
   print(f"Your bmi is {bmi} ,You are the obese.")
else:
   print(f"Your bmi is {bmi} ,clinically obese") 

