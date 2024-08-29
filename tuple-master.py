'''   
Task 1: Formatting Flight Itineraries 
Create a Python function that takes a list of tuples as an argument. 
Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
The function should format and return a string that lists each itinerary. 

For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, the output should be a string formatted as:
"Itinerary 1: Alice - From New York to London
 Itinerary 2: Bob - From Tokyo to San Francisco"
''' 

itinerary_list = []    # set empty list to add tuples to 

def travel_info():   # function that ask for user input to make itinerary info
    #try: 
        print("Welcome to your itinerary planner!")  # Startup message
        while True: # loop for entire input, breaks when user enter 'no' on question
            initial = input("Would you like to create an itinerary (yes/no)? ")
            if initial.upper() == 'YES': 
                print("Please enter a name, place of origin, and destination to add to itinerary.")
                while True:   # ask user to enter name, if any numbers then ask user to enter a name again 
                    name = input("Name: ") 
                    if name.isalpha() == False:
                        print("Error, please enter a name.")
                    else: 
                        break
                while True:   # ask user to enter a place of origin, if any numbers have them enter again 
                    origin = input("Place of Origin: ") 
                    if origin.isalpha() == False: 
                        print("Error, please enter a place of origin.") 
                    else:
                        break 
                while True:   # ask user to enter a destination, if any numbers have them enter again 
                    destination = input("Destination: ") 
                    if destination.isalpha() == False: 
                        print("Error, please enter a destination.") 
                    else: 
                        break 
                input_tuple = (name, origin, destination)   # once variables are entered, put them together into a tuple
                itinerary_list.append(input_tuple)  # add the new tuple to the empty list already assigned
            elif initial.upper() == 'NO': 
                print("Awesome! We've got all the info we need for each itinerary then!")
                break 
            else: 
                print("I'm sorry, I didn't quite underatnd that") 
    #except Exception as e: 
        #print("Error occured.")   

def display_itinerary(list):   # function that takes list and prints out itinerary
    try: 
        print("Your current flight itinerary: ") 
        index = 0 
        for index, (name, origin, destination) in enumerate(list):   # for each tuple in the list (depends on how many tuples made) 
            print(f"Itinerary {index + 1}: {name} - From {origin} to {destination}")         
    except Exception as e: 
        print("Error occured.") 

travel_info()   # call first funciton to ask user to enter in info for itinerary 

display_itinerary(itinerary_list) # Display itinerary from input in format asked for 
