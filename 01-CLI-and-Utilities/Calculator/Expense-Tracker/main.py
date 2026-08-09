from datetime import datetime
import json
import os

FILENAME = "expenses.json"


def load_expenses():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    try:
        title = input("Enter expense title/description: ").strip()
        amount = float(input("Enter amount (in ₹ or $): "))
        if amount <= 0:
            print("⚠️ Amount must be greater than 0.")
            return

        category = (
            input(
                "Enter category (Food, Travel, Bills, Entertainment, Other): "
            )
            .strip()
            .title()
        )
        if not category:
            category = "Other"

        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        expense = {
            "title": title,
            "amount": amount,
            "category": category,
            "date": date_str,
        }

        expenses.append(expense)
        save_expenses(expenses)
        print(f"✅ Added expense: '{title}' - ₹{amount:.2f} [{category}]")

    except ValueError:
        print("❌ Invalid input! Please enter a valid number for amount.")


def view_expenses(expenses):
    if not expenses:
        print("\n📭 No expenses recorded yet.")
        return

    print("\n" + "=" * 55)
    print(f"{'ID':<4} {'Title':<15} {'Amount':<10} {'Category':<15} {'Date'}")
    print("=" * 55)

    total = 0
    for idx, item in enumerate(expenses, start=1):
        print(
            f"{idx:<4} {item['title']:<15} ₹{item['amount']:<9.2f} {item['category']:<15} {item['date']}"
        )
        total += item["amount"]

    print("=" * 55)
    print(f"💰 Total Expense: ₹{total:.2f}")
    print("=" * 55)


def category_summary(expenses):
    if not expenses:
        print("\n📭 No expenses recorded yet.")
        return

    summary = {}
    for item in expenses:
        cat = item["category"]
        summary[cat] = summary.get(cat, 0) + item["amount"]

    print("\n" + "=" * 35)
    print("📊 EXPENSE SUMMARY BY CATEGORY")
    print("=" * 35)
    for cat, amt in summary.items():
        print(f"🔸 {cat:<15}: ₹{amt:.2f}")
    print("=" * 35)


def main():
    expenses = load_expenses()

    while True:
        print("\n--- 💸 EXPENSE TRACKER MENU ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Category Summary")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            category_summary(expenses)
        elif choice == "4":
            print("\n👋 Goodbye! Keep tracking your spending!")
            break
        else:
            print("⚠️ Invalid choice! Please select between 1 and 4.")


if __name__ == "__main__":
    main()