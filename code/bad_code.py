def process_elements(input_lst):
    
    if len(input_lst) > 1:
        for element in input_lst:
            if isinstance(element, (str, int)):
                if element.lower() == "stop":
                    print("Found stop command:", element)
                else:
                    got_number = int(element)

                    if got_number > 0:
                        print("Got a positive number!")
                    elif got_number == 0:
                        print("Got zero.")
                    else:
                        print("Got a negative number.")
    else:
        print("List is too short to process.")
    

# Use this function
input_lst = ["1", "-2", "3", "stop"]
process_elements(input_lst)
