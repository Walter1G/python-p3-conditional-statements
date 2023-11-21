#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    code = "Access granted" if username.lower()=="admin" and password=="12345" else "Access denied"
    return code
    pass

def hows_the_weather(temperature):
    # your code here
    if(temperature <40):
        message="It's brisk out there!"
    elif(temperature >=40 and temperature<=65):
        message="It's a little chilly out there!"
    elif(temperature>85):
        message="It's too dang hot out there!"
    else:
        message="It's perfect out there!"
    
    return message
    pass

def fizzbuzz(num):
    # your code here
    if(num%3==0 and num%5==0):
        ans="FizzBuzz"
    elif(num%5==0):
        ans="Buzz"
    elif( num%3==0):
        ans="Fizz"
    else:
        ans=num
    
    return ans
    pass

def calculator(operation, num1, num2):
    # your code here
    if(operation=="+"):
        ans= num1 + num2
        return ans
    elif(operation=="-"):
        ans= num1 - num2
        return ans
    elif(operation=="/"):
        ans= num1 / num2
        return ans
    elif(operation=="*"):
        ans= num1 * num2
        return ans
    else:
        print("Invalid operation!")
    return None
    pass
