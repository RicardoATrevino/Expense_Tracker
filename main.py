import os
import csv
from datetime import datetime 
import appdirs
from pathlib import Path

#get app specific directory (cross - platform)
app_name = 'ExpenseTrackerApp'
app_author = "Ricardo Trevino"
app_dir = appdirs.user_data_dir(appname=app_name, appauthor=app_author)

#defining file name and working directory path
file_name = 'expensesForTrackerApp.csv'
file_path = Path(app_dir)/file_name


# Ensuring directory exists (creating if it doesn't)
file_path.parent.mkdir(parents=True, exist_ok=True)

def initialize_csv():
  if not file_path.exists():
    try: #creates and writes csv file if not exists
      with file_path.open(mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Amount", "Category", "Description"])  # Column headers
    except OSError as e:
      print(f'Error creating file: {e}')
  else:
    print(f'file already exists at {file_path}')

# add expenses
def add_expense():
  date = datetime.now().strftime("%Y-%m-%d")
  try:
    amount = float(input("Enter Amount: "))
    category = input("Enter a category: (e.g., food, transport)")
    description = input("Enter a brief description")

    with open(file_path, 'a', newline='') as file:
      writer = csv.writer(file)
      writer.writerow([date, amount, category, description])
    print("Expense added successfully!")
  except ValueError:
    print("Invalid amount, please enter a valid number.")

#View all expenses
def view_expenses():
  if not os.path.exists(file_path):
    print("No expenses recorded yet.")
    return
  
  with open(file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader) #this skips the header
    for row in reader:
      print(f"Date: {row[0]}, Amount: {row[1]}, Category: {row[2]}, Description: {row[3]}")

  
def delete_expense():
  if not os.path.exists(file_path)
    print("No expenses to delete")
    return
  
  view_expenses()
  try:
    row_number = int(input("Enter Row Num to delete (starting from 1): "))
    with open(file_path, 'r') as file :
      lines = list(csv.reader(file))

    if 1 < row_number <= len(lines):
      del lines[row_number - 1]
      with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)
      print("Expense deleted successfully!")
    else:
      print("Invalid row number.")
  except ValueError:
    print("No expenses recorded yet.")
    return 


# Function to view total expenses
def view_total_expenses():
    if not os.path.exists(file_path):
        print("No expenses recorded yet.")
        return

    total = 0
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            total += float(row[1])
    print(f"Total expenses: ${total:.2f}")


def main():
  initialize_csv()
  while True:
    print("\nExpense Tracker Menu:")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. Delete an expense")
    print("4. View total expenses")
    print("5. Exit")

    choice = input("Enter your choice (1-5):")
    if choice == '1':
      add_expense()
    elif choice == '2':
      view_expenses()
    elif choice == '3':
      delete_expense()
    elif choice == '4':
      view_total_expenses()
    elif choice == '5':
      print("Exiting the program.")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == '__main__':
  main()



