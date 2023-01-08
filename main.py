import random 

MAX_LINES =3  # this is a global constant
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
     "A": 2,
     "B": 4,
     "C": 6,
     "D": 8,
}

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():#getting the key and value looping through the dict
        for _ in range(symbol_count): #_ is anyonmous symbol
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value) #find first instant in the value list and get rid of it
            column.append(value)

        columns.append(column)

    return columns    

def print_slot_machine(columns):
     for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
               print(column[row], end=" | ")
            else:
                print(column[row],end="")

        print()


def deposit(): # getting the user input and getting the info
 while True:
    amount = input("What would you like to deposit? $")
    if amount.isdigit(): #tells if it's a  valid number
        amount = int(amount) #converts it into a int
        if amount > 0 : 
            break
        else:
            print("Amount must be greater than 0.")            
    else:
        print("Please enetr a number.")            

    return amount

def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line ? $")
        if amount.isdigit(): #tells if it's a  valid number
            amount = int(amount) #converts it into a int
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET}-${MAX_BET}.")            
        else:
            print("Please enter a number.")

    return amount







def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet= get_bet()
    total_bet = bet * lines 
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
  
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)



main()    
