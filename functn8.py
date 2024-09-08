# BMI calculator


def lbs_to_kg(weight_lbs):
    return weight_lbs * 0.45359237


def foot_and_in_to_m(h_foot, h_inch):
     height = h_foot * 0.3048 + h_inch * 0.0254
     return height


def bmi_is(weights, heights):
    return weights / heights ** 2


global height
global weight
print('''
    --------------------------------------
               BMI Calculator
    --------------------------------------''')
print('''You want to enter the weight  in Kgs or Lbs: 
             enter 'K' for kgs and 'L' for lbs ''')
ans = input("Your input: ")
ans.upper()
if ans == "K":
    print("Enter weight in Kgs: ")
    weight = int(input())
elif ans == "L":
    print("Enter weight in lbs: ")
    weight = int(input())
    weight = lbs_to_kg(weight)

else:
    raise ValueError("Invalid input! Please Enter a valid input")

print('''You want to enter the height in meter or in foot and inch: 
             Enter 'C' for centimeter and 'F' for foot and inch ''')
ans = input("Your input: ")
ans.upper()
if ans == "C":
    print("Enter height in centimmeter: ")
    height = int(input())
    
elif ans == "F":
    print("Enter  height in Foot and inch: ")
    height_foot = int(input("Foot: "))
    height_inch = int(input("inch: "))
    height = foot_and_in_to_m(height_foot, height_inch)
else:
    raise ValueError("Invalid input! Please Enter a valid input")

bmi = bmi_is(weight, height  )
print(f'''
          Your BMI is   
           ------------
                     
             {bmi}    
                 
           ------------ ''')




