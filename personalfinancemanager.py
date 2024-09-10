import tkinter as tk
from tkinter import messagebox, simpledialog
import mysql.connector
from mysql.connector import Error


class Transaction:
    def __init__(self, date, description, amount):

        self.date = date
        self.description = description
        self.amount = amount


class FinanceManager:
    def __init__(self):
        self.transactions = []
        host = 'localhost'
        user = 'root'
        password = 'root'
        database = 'venkat'

        try:
            self.conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                self._create_transactions_table()
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error: {e}")
            self.conn = None
            self.cursor = None

    def _create_transactions_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS transactions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            date DATE,
            description VARCHAR(255),
            amount DECIMAL(10, 2)
        )
        """
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def add_transaction(self, date, description, amount):
        insert_query = """
        INSERT INTO transactions (date, description, amount)
        VALUES (%s, %s, %s)
        """
        self.cursor.execute(insert_query, (date, description, amount))
        self.conn.commit()
        messagebox.showinfo("Success", "Transaction added successfully!")

    def view_transactions(self):
        select_query = "SELECT date, description, amount FROM transactions"
        self.cursor.execute(select_query)
        rows = self.cursor.fetchall()

        if rows:
            transaction_details = "\nTransaction History:\n"
            for row in rows:
                transaction_details += f"Date: {row[0]}, Description: {row[1]}, Amount: {row[2]}\n"
            messagebox.showinfo("Transaction History", transaction_details)
        else:
            messagebox.showwarning("Empty", "Your transaction history is empty!")

    def calculate_balance(self):
        income_query = "SELECT SUM(amount) FROM transactions WHERE amount > 0"
        expense_query = "SELECT SUM(amount) FROM transactions WHERE amount < 0"

        self.cursor.execute(income_query)
        total_income = self.cursor.fetchone()[0] or 0

        self.cursor.execute(expense_query)
        total_expenses = self.cursor.fetchone()[0] or 0

        balance = total_income + total_expenses
        balance_info = f"Total Income: {total_income}\nTotal Expenses: {total_expenses}\nCurrent Balance: {balance}"
        messagebox.showinfo("Balance Information", balance_info)


def add_income():
    date = simpledialog.askstring("Add Income", "Enter date (YYYY-MM-DD):")
    if not date:
        return
    description = simpledialog.askstring("Add Income", "Enter description:")
    if not description:
        return
    amount = simpledialog.askfloat("Add Income", "Enter income amount:")
    if amount is None:
        return
    finance_manager.add_transaction(date, description, amount)


def add_expense():
    date = simpledialog.askstring("Add Expense", "Enter date (YYYY-MM-DD):")
    if not date:
        return
    description = simpledialog.askstring("Add Expense", "Enter description:")
    if not description:
        return
    amount = simpledialog.askfloat("Add Expense", "Enter expense amount:")
    if amount is None:
        return
    finance_manager.add_transaction(date, description, -amount)


def view_transactions():
    finance_manager.view_transactions()


def calculate_balance():
    finance_manager.calculate_balance()


def main():
    global finance_manager
    finance_manager = FinanceManager()

    root = tk.Tk()
    root.title('Personal Finance Manager')

    addincomebtn = tk.Button(root, text='Add Income', command=add_income)
    addincomebtn.place(x=100, y=20, width=100)

    addexpensebtn = tk.Button(root, text='Add Expense', command=add_expense)
    addexpensebtn.place(x=100, y=40, width=100)

    viewtransactionbtn = tk.Button(root, text='View Transactions', command=view_transactions)
    viewtransactionbtn.place(x=100, y=60, width=100)

    calculatebalancebtn = tk.Button(root, text='Calculate Balance', command=calculate_balance)
    calculatebalancebtn.place(x=100, y=80, width=100)

    exitbtn = tk.Button(root, text='Exit', command=root.destroy)
    exitbtn.place(x=100, y=100, width=100)

    root.mainloop()


if __name__ == "__main__":
    main()
