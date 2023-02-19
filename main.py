import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5

ROWS = 3
COLS = 3

###Number of time we can repeat a symbol. the less we repat the more valuable. 
symbolCount = {
    'A' : 2, 
    'B' : 4, 
    'C' : 6, 
    'D' : 8,
}

#how many times does the bet multiply depending on the symbols. 
symbolValue = {
    'A' : 5, 
    'B' : 4, 
    'C' : 3, 
    'D' : 2,
}

###Function to collect the money from the player
def deposit():
    #While true so that we can get a valid deposit
    while True: 
        amount = input('How much are you going to deposit? $ ')
        #If statement with isdigit method so that he don´t get something different from a positive number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0!')
        else:
            print('Please enter a number!')
    return amount 

def number_of_lines():
        #While true so that we can a valid number of lines
    while True: 
        lines = input(f'How many lines would you like to bed on (1-{MAX_LINES})? ')
        #Get valid number of lines with is digit method
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f'The number of lines must be between 1 and {MAX_LINES}!')
        else:
            print('Please enter a number!')
    return lines 

###Function to collect the bet from the user
def amount_bet():
    #While true so that we can get a valid amount
    while True: 
        amount = input('How much are you going to bet on each line? $ ')
        #If statement with isdigit method so that he don´t get something different from a positive number
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must between ${MIN_BET} and ${MAX_BET}!')
        else:
            print('Please enter a number!')
    return amount 

###Generate which symbols are goping to be en each column
def get_slot_machine_spin(rows, columns, symbols):
    allSymbols = []
    #uses dictionary called symbol_count to create a list with each time the symbol repeats, key is the symbol, value is the number of times it repeats. 
    for symbol, symbol_count in symbols.items():
        #in range of the value in the key value pair, appends the symbol to the all_symbols list
        for _ in range(symbol_count):
            allSymbols.append(symbol)

    columns = []
    #for the number of columns we have we repeat the loop. 
    for _ in range(COLS):
        column = []
        #creating a copy of the list so that we have the same list for each iteration of the columns
        currentSymbols = allSymbols[:]
        #iterating over the number of rows in the column
        for _ in range(ROWS):
            #choosing a random value of the list, removing it from the list and appending it to the column list. 
            value = random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)
        # then we append the list of symbols of the column to the list of columns. 
        columns.append(column)

    return columns

###Function to print each column vertically and not horizontally.
def print_slot_machine(columns):
     for row in range(len(columns[0])):
        for i, column in enumerate(columns): 
            if i != len(columns) - 1:
                print(column[row], end = '|')
            else:
                print(column[row], end = '')
        
        print()

def check_winnings(columns, lines, bet, values):
    winnings = 0 
    winningLines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbolToCheck = column[line]
            if symbol != symbolToCheck: 
                break
        else:
            winnings += values[symbol] * bet
            winningLines.append(line + 1)
    
    return winnings, winningLines

def spins(balance): 
    lines = number_of_lines()
    #To verify that the amount that user is betting is less than his balance. 
    while True:
        bet = amount_bet()
        totalBet = bet * lines
        if balance >= totalBet:
            break
        else: 
            print(f"You don't have enough balance to make that bet. Your total balance is {balance}.")
            
    print(f'you are betting {bet} on {lines} lines. Your total bet is equal to {totalBet}!')

    slots = get_slot_machine_spin(ROWS, COLS, symbolCount)
    print_slot_machine(slots)
    winnings, winningLines = check_winnings(slots, lines, bet, symbolValue)
    print(f'You won ${winnings}')
    if len(winningLines) > 0:
        print(f'You won on: ', *winningLines)
    else: 
        print('Better luck next time!!')

    return winnings - totalBet

###Main function of the game
def main():
    balance = deposit()
    while True: 
        print(f'Current balance is ${balance}')
        spin = input ('Press enter to play (q to quit).')
        if spin == 'q':
            break
        balance += spins(balance)
        if balance <= 0: 
            print('You runned out of money!!!')
            break

    print(f'Your balance left is {balance}')

main()