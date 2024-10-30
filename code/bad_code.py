def process_elements(input_lst):
    if input_lst is None:
        return
    elif len(input_lst) <= 1:
        print("List is too short to process.")
        return
    for element in input_lst:
        if not isinstance(element, (str, int)):
            continue
        if element.lower() == "stop":
            print("Found stop command:", element)
            break
        try:
            got_number = int(element)
        except ValueError:
            got_number = False
        if got_number is False:
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