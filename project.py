from tabulate import tabulate
n = int(input("Enter the no of data to enter:\n"))
# Initial data
data = []
h1 = ['Name', 'Amount', 'Purpose']

# Print the initial table
table = tabulate(data, headers=h1)
print(table)

# Dictionary to store total amounts for each purpose
purpose_totals = {}

def payment_record():
    amount = int(input("Enter the amount:\n"))
    name = input("Name in payment:\n")
    choice = int(input("Purpose:\n1. Rent\n2. Grocery\n3. Self-Expense\n4. Travel\n5. Other\n"))
    
    if choice == 1:
        purpose = 'Rent'
    elif choice == 2:
        purpose = 'Grocery'
    elif choice == 3:
        purpose = 'Self-Expense'
    elif choice == 4:
        purpose = 'Travel'
    elif choice == 5:
        purpose = 'Other'
    else:
        print("Invalid choice!!!")
        return

    print(record_store(name, amount, purpose))
    print("Successfully recorded")

def record_store(name, amount, purpose):
    global data, purpose_totals
    data.append([name, amount, purpose])
    
    if purpose in purpose_totals:
        purpose_totals[purpose] += amount
    else:
        purpose_totals[purpose] = amount

    return data

# Test the function
while n>0:
    print(payment_record())
    n=n-1

# Print the updated table
table = tabulate(data, headers=h1)
print(table)
print(purpose_totals)