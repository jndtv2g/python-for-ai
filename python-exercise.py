#Enter Python code here and hit the Run button.


def loop_natural_numbers():
    for o in range(1, 11):
        print(o)


def loop_number_pattern():
    for i in range(1, 6): # outer loop for rows
        for j in range(i): # inner loop for columns
            print(j, end=" ")
        print("\n")

loop_natural_numbers()
print("\n")
loop_number_pattern()
print("\n")