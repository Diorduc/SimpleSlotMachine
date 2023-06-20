import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 5

# Define the count and value of symbols
symbol_count = {
    "A": 5,
    "B": 5,
    "C": 5,
    "D": 5 
}
symbol_value = {
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 1
}


def get_slot_machine_spin(rows, cols):
    """
    Generates a random spin of the slot machine.
    :param rows: Number of rows in the slot machine.
    :param cols: Number of columns in the slot machine.
    :return: List of columns representing the spin result.
    """
    all_symbols = []
    for symbol, count in symbol_count.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def check_winnings(columns, lines, bet, values):
    """
    Checks the winnings based on the spin result and bet.
    :param columns: List of columns representing the spin result.
    :param lines: Number of lines to bet on.
    :param bet: Amount bet on each line.
    :param values: Dictionary mapping symbols to their respective values.
    :return: Total winnings and list of winning lines.
    """
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def print_slot_machine(columns):
    """
    Prints the slot machine spin result.
    :param columns: List of columns representing the spin result.
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def spin(balance):
    """
    Simulates a spin of the slot machine.
    :param balance: Current balance of the player.
    :return: Balance change after the spin.
    """
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is: ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print("You won on lines:", *winning_lines)
    return winnings - total_bet


def deposit():
    """
    Accepts the deposit amount from the player.
    :return: The deposit amount.
    """
    while True:
        amount = input("Please add your $ deposit amount: ")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 0:
                break
            else:
                print("Amount must be greater than or equal to 0!")
        else:
            print("Please enter a valid number.")

    return amount


def display_rules():
    """Displays the rules of the game."""
    print("Rules of the game:")
    print("- You will be presented with a slot machine consisting of 3 rows and 3 columns.")
    print("- Each column will contain a randomly selected symbol from the available symbols.")
    print("- You can choose the number of lines to bet on (1-3) and the amount to bet.")
    print("- If the symbols on the selected lines match, you will win based on the symbol values.")
    print("- Your winnings will be added to your balance.")
    print("- If your balance reaches 0, you can choose to add more money or quit the game.")


def get_number_of_lines():
    """
    Gets the number of lines to bet on from the player.
    :return: Number of lines.
    """
    while True:
        try:
            lines = input("Please enter the number of lines to bet on (1-3): ")
            lines = int(lines)
            if 1 <= lines <= 3:
                break
            else:
                print("Invalid number of lines. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return lines


def get_bet():
    """
    Gets the bet amount from the player.
    :return: Bet amount.
    """
    while True:
        try:
            bet = input(f"Please enter the amount to bet (minimum bet: {MIN_BET}, maximum bet: {MAX_BET}): ")
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Invalid bet amount. Please enter a number between {MIN_BET} and {MAX_BET}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return bet


def main():

    input("Welcome to the best slot machines, where you always win! Please press anything + enter (or just enter) to "
          "check below the rules")
    display_rules()

    balance = 0
    name = input("Hello there, lucky person, what is your name? ")

    while True:
        option = input(f"\n{name}, press enter to play (q + enter to quit) ")
        if option.strip() == "":
            if balance == 0:
                add_more = input(f"{name}, you have a balance of $0. Do you want to add money to start playing? ("
                                 f"Press 'y' for yes or 'n' for no): ")
                add_more = add_more.lower()
                if add_more == "y":
                    balance = deposit()
                elif add_more == "n":
                    print("Thank you for playing")
                    break
                else:
                    print("Invalid input. Please provide a valid answer!")
                    continue

            balance_change = spin(balance)
            balance += balance_change
            print(f"Your balance, {name}, is: ${balance}")
        elif option.lower() == "q":
            print("Thank you for playing.")
            break
        else:
            print("Invalid option. Please press enter or enter 'q' to quit.")


main()
