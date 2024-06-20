import pandas as pd
def check_data_in_excel(filename):
  """
  Checks if the Excel file contains data (assumes data is in a DataFrame).
  Returns True if data exists, False otherwise.
  """
  try:
    # Read a small sample of the data (first 10 rows)
    data = pd.read_excel(filename, nrows=10)
    # Check if there are any rows (data is not empty)
    return not data.empty
  except FileNotFoundError:
    print("Error: File", filename, "not found.")
    return False
  except pd.errors.EmptyDataError:
    print(filename, "is empty (no data found).")
    return False

# Example usage
filename = "mydata.xlsx"
has_data = check_data_in_excel(filename)

if has_data:
  print("Excel file contains data!")
else:
  print("Excel file is empty or does not exist.")

#print(file)
#print(file.head())
#print(file.tail())
#print(file.shape)
#print(file.describe())
#print(file.iloc[5:9,1:3])
#print(file.loc[5:9,('sepal_width','petal_length')])