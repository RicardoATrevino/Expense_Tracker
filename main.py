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


#View all expenses
def view_expenses():
  if not os.path.exists(file_path):
    print("No expenses recorded yet.")
    return
  



