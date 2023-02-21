from telnetlib import BM


height = float(input("Enter you height in centimeters: "))
weight = float(input("Enter your Weight in Kg"))
height = height/100
BMI = weight/(height*height)

if (BMI>0):
    if(BMI<=16):
        print("you are severely underweight")
    elif (BMI<=18.5):
        print("you are under weight")
    elif(BMI<=25):
        print("you are Healthy")
    elif(BMI<=30):
        print("you are overweight")
    else:
        print("you are serverely overweight")
else:
    print("please enter valid details")