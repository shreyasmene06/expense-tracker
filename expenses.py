import csv
from datetime import datetime

# addition
def addition(amount, category, date):
    with open("expenses.csv", "a", newline='') as f:
        x = csv.writer(f)
        x.writerow([amount, category, date])
    print("Expense added successfully!")

# view expenses
def view():
    try:
        with open("expenses.csv", "r") as f:
            x = csv.reader(f)
            l = list(x)
            if not l:
                print("No records found.")
            else:
                for i in l:
                    if len(i) == 3:  # Ensure the row has exactly 3 elements
                        print(f"Amount: {i[0]}, Category: {i[1]}, Date: {i[2]}")
                    else:
                        print(f"Skipping malformed row: {i}")
    except FileNotFoundError:
        print("No records found.")

# delete expenses
def delete(index):
    try:
        with open("expenses.csv", "r") as f:
            x = csv.reader(f)
            l = list(x)
            if 0 <= index < len(l):
                del l[index]
                with open("expenses.csv", "w", newline='') as f:
                    x = csv.writer(f)
                    x.writerows(l)
                print("Expense deleted successfully!")
            else:
                print("Invalid index.")
    except FileNotFoundError:
        print("No expenses recorded.")

# expense summary
def summary():
    try:
        with open("expenses.csv", 'r') as f:
            x = csv.reader(f)
            l = list(x)
            if not l:
                print("No expenses recorded.")
                return

            total = sum(float(i[0]) for i in l if len(i) == 3)
            print(f"Total expenses: ${total:.2f}")
            categories = set(i[1] for i in l if len(i) == 3)
            for category in categories:
                category_total = sum(float(i[0]) for i in l if len(i) == 3 and i[1] == category)
                print(f"Total in {category}: ${category_total:.2f}")
    except FileNotFoundError:
        print("No expenses recorded.")

# main
def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Expense Summary")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                date = input("Enter date (YYYY-MM-DD): ")
                # Validate date
                try:
                    datetime.strptime(date, '%Y-%m-%d')
                    addition(amount, category, date)
                except ValueError:
                    print("Invalid date format. Please enter date in YYYY-MM-DD format.")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '2':
            view()
        elif choice == '3':
            try:
                index = int(input("Enter the index of the expense to delete: "))
                delete(index)
            except ValueError:
                print("Invalid index. Please enter a number.")
        elif choice == '4':
            summary()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
