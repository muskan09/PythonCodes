import operator

saved_string = ''

def remove_letter(): #Remove a selected letter from a string
    base_string = str(raw_input("Enter String: "))
    letter_remove = str(raw_input("Enter Letter: ")) #takes any size string
    letter_remove = letter_remove[0]
    string_length = len(base_string)
    location = 0
    
    while (location < string_length): #by reference (rather than by value)
        if base_string[location] == letter_remove:
            base_string = base_string[:location] + base_string[location+1::]
            string_length -= 1
        location+=1

    print "Result: %s" % base_string
    return

def num_compare(): #Compare 2 numbers to determine the larger
    num1 = int(raw_input("Enter First Number: "))
    num2 = int(raw_input("Enter Second Number: "))
    
    if num1 > num2:
        print num1
    elif num2 > num1: #elif = else if
        print num2
    else:
        print "EQUAL"
    return

def print_string(): #Print the previously stored string
    print saved_string
    return

def calculator(): #Basic Calculator (addition, subtraction, multiplication, division)
    sign_dict = {'+': operator.add , '-' : operator.sub , '*' : operator.mul , '%' : operator.div}
    
    num1 = int(raw_input("Input first number: "))
    sign = str(raw_input("Action: "))
    num2 = int(raw_input("Input second number: "))
    
    print sign_dict[sign](num1, num2)
    
    return

def accept_and_store(): #Accept and store a string
    global saved_string
    saved_string = str(raw_input("Input String: "))
    return

def main(): #menu goes here
    opt_list = [accept_and_store, 
                calculator, 
                print_string,
                num_compare,
                remove_letter]
    
    while(True):            
        print "SELECT OPTION:"
        print "1\tAccept and Store"
        print "2\tCalculator"
        print "3\tPrint Stored String"
        print "4\tNumber Comparison"
        print "5\tLetter Remover"
        opt_choice = int(raw_input("SELECTION: "))
        opt_choice -= 1
        opt_list[opt_choice]()
        
    return

main()
