from functools import reduce

def collect_expenses():
    """
    Collects user input for monthly expenses until 'done' is entered.
    Returns a list of tuples (expense_type, amount).
    """
    expenses = []
    print("Enter your monthly expenses. Type 'done' when finished.\n")

    while True:
        expense_type = input("Enter the type of expense (or 'done' to finish): ")
        if expense_type.lower() == "done":
            break
        try:
            amount = float(input(f"Enter the amount for {expense_type}: $"))
            expenses.append((expense_type, amount))
        except ValueError:
            print("Invalid amount. Please enter a number.")
    return expenses


def calculate_total(expenses):
    """Uses reduce to calculate the total expense amount."""
    return reduce(lambda acc, x: acc + x[1], expenses, 0)


def calculate_highest(expenses):
    """Uses reduce to find the highest expense (tuple)."""
    return reduce(lambda a, b: a if a[1] > b[1] else b, expenses)


def calculate_lowest(expenses):
    """Uses reduce to find the lowest expense (tuple)."""
    return reduce(lambda a, b: a if a[1] < b[1] else b, expenses)


def main():
    expenses = collect_expenses()

    if not expenses:
        print("No expenses entered.")
        return

    total = calculate_total(expenses)
    highest = calculate_highest(expenses)
    lowest = calculate_lowest(expenses)

    print("\nExpense Analysis")
    print(f"Total Expenses: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} (${highest[1]:.2f})")
    print(f"Lowest Expense: {lowest[0]} (${lowest[1]:.2f})")


if __name__ == "__main__":
    main()
