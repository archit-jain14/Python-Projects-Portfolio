import csv
import os
from collections import defaultdict
import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table

console = Console()

CSV_FILE = "01-CLI-and-Utilities/04-Expense-Tracker/expenses.csv"
CHART_FILE = "01-CLI-and-Utilities/04-Expense-Tracker/expense_summary.png"

def load_expenses():
    expenses = []
    if not os.path.exists(CSV_FILE):
        console.print(f"[bold red]Error:[/] File '{CSV_FILE}' not found.")
        return expenses

    with open(CSV_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Amount"] = float(row["Amount"])
            expenses.append(row)
    return expenses

def display_summary_table(expenses):
    table = Table(title="📊 Expense Log Summary", style="cyan")
    table.add_column("Date", style="dim")
    table.add_column("Category", style="bold yellow")
    table.add_column("Amount (₹)", style="bold green", justify="right")
    table.add_column("Description")

    total_spent = 0
    for exp in expenses:
        table.add_row(exp["Date"], exp["Category"], f"₹{exp['Amount']:.2f}", exp["Description"])
        total_spent += exp["Amount"]

    console.print(table)
    console.print(f"[bold magenta]Total Spending:[/] [bold green]₹{total_spent:.2f}[/]\n")

def generate_chart(expenses):
    category_totals = defaultdict(float)
    for exp in expenses:
        category_totals[exp["Category"]] += exp["Amount"]

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure(figsize=(8, 5))
    colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6"]
    
    plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140, colors=colors)
    plt.title("Expense Breakdown by Category")
    plt.tight_layout()
    
    plt.savefig(CHART_FILE)
    console.print(f"[bold green]Success:[/] Visual report saved as '[bold white]{CHART_FILE}[/]'!")

if __name__ == "__main__":
    console.print("[bold cyan]=== Personal Expense Tracker & Report Generator ===[/]\n")
    data = load_expenses()
    if data:
        display_summary_table(data)
        generate_chart(data)