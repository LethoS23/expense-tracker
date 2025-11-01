import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('tracker.db')
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    category TEXT,
    description TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS income (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    category TEXT,
    description TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS budgets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    limit_amount REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS goals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    target_amount REAL,
    current_amount REAL DEFAULT 0
)
""")

conn.commit()

# Functions


def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    description = input("Enter expense description: ")
    cursor.execute(
        "INSERT INTO expenses (amount, category, description) "
        "VALUES (?, ?, ?)",
        (amount, category, description)
    )
    conn.commit()
    print("Expense added successfully.\n")


def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    for row in cursor.fetchall():
        print(row)
    print()


def view_expenses_by_category():
    category = input("Enter category: ")
    cursor.execute("SELECT * FROM expenses WHERE category = ?", (category,))
    for row in cursor.fetchall():
        print(row)
    print()


def add_income():
    amount = float(input("Enter income amount: "))
    category = input("Enter income category: ")
    description = input("Enter description: ")
    cursor.execute(
        "INSERT INTO income (amount, category, description) VALUES (?, ?, ?)",
        (amount, category, description)
    )
    conn.commit()
    print("Income added!\n")


def view_income():
    cursor.execute("SELECT * FROM income")
    for row in cursor.fetchall():
        print(row)
    print()


def view_income_by_category():
    category = input("Enter category: ")
    cursor.execute("SELECT * FROM income WHERE category = ?", (category,))
    for row in cursor.fetchall():
        print(row)
    print()


def set_budget():
    category = input("Enter category name: ")
    limit_amount = float(input("Enter budget limit: "))
    cursor.execute(
        "INSERT INTO budgets (category, limit_amount) VALUES (?, ?)",
        (category, limit_amount)
    )
    conn.commit()
    print("Budget set!\n")


def view_budget():
    cursor.execute("SELECT * FROM budgets")
    for row in cursor.fetchall():
        print(row)
    print()


def calculate_remaining_funds():
    cursor.execute("SELECT SUM(amount) FROM income")
    total_income = cursor.fetchone()[0] or 0
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total_expenses = cursor.fetchone()[0] or 0
    remaining = total_income - total_expenses
    print(f"Remaining funds: {remaining}\n")


def set_goal():
    name = input("Enter goal name: ")
    target_amount = float(input("Enter target amount: "))
    cursor.execute(
        "INSERT INTO goals (name, target_amount) VALUES (?, ?)",
        (name, target_amount)
    )
    conn.commit()
    print("Goal added!\n")


def view_goals():
    cursor.execute("SELECT * FROM goals")
    for row in cursor.fetchall():
        print(f"Goal: {row[1]} | Target: {row[2]} | Progress: {row[3]}")
    print()


def update_goal_progress():
    name = input("Enter goal name to update: ")
    amount = float(input("Enter amount to add to progress: "))
    cursor.execute(
        "UPDATE goals SET current_amount = current_amount + ? WHERE name = ?",
        (amount, name)
    )
    conn.commit()
    print("Goal progress updated!\n")


# Menu
def menu():
    while True:
        print("""
1. Add expense
2. View expenses
3. View expenses by category
4. Add income
5. View income
6. View income by category
7. Set budget for a category
8. View budget for a category
9. View remaining funds
10. Set financial goal
11. View financial goals
12. Update goal progress
13. Quit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_expenses_by_category()
        elif choice == "4":
            add_income()
        elif choice == "5":
            view_income()
        elif choice == "6":
            view_income_by_category()
        elif choice == "7":
            set_budget()
        elif choice == "8":
            view_budget()
        elif choice == "9":
            calculate_remaining_funds()
        elif choice == "10":
            set_goal()
        elif choice == "11":
            view_goals()
        elif choice == "12":
            update_goal_progress()
        elif choice == "13":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    menu()
    conn.close()
