#find oldest person

#create empty list 
people_name_and_age = {}

#ask for name and age inputs
while True:
    try: 
        name = input("Input name please: ")
        age = int(input("Input age please: "))
#make sure inputs are valid
    except:
        print("Invalid input, try again.")
       

#store inputs on array(dictionary)
    people_name_and_age[name] = {
            "age" : age
        }

    print(people_name_and_age[name]["age"])

#ask user if he wants to input another 

#rank the age to find the oldest 





