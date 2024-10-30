def process_elements(input_lst):
    while True:
        if input_lst is None:
            break
        elif len(input_lst) > 1:
            for element in input_lst:
                if isinstance(element, (str, int)) and element.lower() != "stop":
                        try:
                            got_number = int(element)
                        except ValueError:
                            got_number = False
                        else:
                            number_check()
                else:
                    print("Found stop command:", element)
        else:
            print("List is too short to process.")
        break

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
