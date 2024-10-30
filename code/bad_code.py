def process_elements(input_lst):
    if len(input_lst) <= 1:
        print("List is too short to process.")
        return
    for element in input_lst:
        if element.lower() == "stop":
            break
        
        try:
            got_number = int(element)
        except ValueError:
            print("Not a number!")
            continue
        if got_number > 0:
            print("Got a positive number!")
        elif got_number == 0:
            print("Got zero.")
        else:
            print("Got a negative number.")
            

# Use this function
input_lst = ["1", "-2", "3", "stop"]
process_elements(input_lst)

def number_check(input_lst):
    if input_lst > 0:
        print("Got a positive number!")
    elif input_lst == 0:
        print("Got zero.")
    else:
        print("Got a negative number.")
