#find oldest person

#create empty list 
people_name_and_age = {}
oldest_age = 0
person= ""
#ask for name and age inputs
while True:
    try:
     name = input("Input name please: ")
     age = int(input("Input age please: "))

#store inputs on array(dictionary)
     people_name_and_age[name] = age
     
#rank the age to find the oldest
     if age > oldest_age:
        oldest_age = age
        person = name 

#display name and age  
     print(f"Name: {name}, Age: {age}")
    
#make sure inputs are valid
    except:
       print("Invalid age, try again.")
     
#ask user if he wants to input another
    another_person = input("Do you want to add another person? Yes/No?: ")
    if another_person != "Yes":
      break
      
print(f"The oldest person is {person} at age {oldest_age}.")
      



 





