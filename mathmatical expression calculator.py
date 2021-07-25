import warnings
print('Enter a mathematical expression to view its result')

#we put a while to cotinously prompt the yser to input expressions
cond = True
while cond is True:

    #this ignores other warnings
    warnings.simplefilter('ignore')

    #input is taken here
    a = input("\nEnter a mathematical expression: ")

    #this shows history of the entered expressions
    if a == "history":
        file = open("history.txt", mode="r")
        data = file.read()
        print(data)
        file.close()

    #this clears the history
    elif a == "clear":
        file = open("history.txt", mode="w")
        file.close()
        print("Your History has been cleared :) ")

    #this exits the program
    elif a == "exit":
        cond = False
        print("program closed, Adios master :-)")
        

    #the expression is solved here
    else:
        try:
            b = eval(a)
            print(f'The result of the entered expression is {b}.')

            #the expression is stored in the file history
            file = open("history.txt", mode="a")
            file.write(f"{a}\n")
            file.close()
            print()

        #if an operator i.e. +, -, *, / is missing
        except TypeError:
            print("Operator is missing")
            continue

        #if the value is divided by zero
        except ZeroDivisionError:
            print("Division with 0 is infinity")
            continue

        #this handles other errors
        except Exception as e:
            print(e.__class__, "has occoured")
            continue
