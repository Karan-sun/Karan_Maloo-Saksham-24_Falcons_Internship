import pandas as pd


def get_user_input():
    """
    Gets user input for amount, name, and purpose with error handling.
    """
    while True:
        try:
            amount = float(input("Enter the amount (positive number):\n"))
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            break
        except ValueError:
            print("Invalid amount! Please enter a positive number.")

    name = input("Name in payment:\n")

    purpose_choices = {
        1: "Rent",
        2: "Grocery",
        3: "Self-Expense",
        4: "Travel",
        5: "Other",
    }

    while True:
        print("Purpose:\n" + "\n".join(f"{key}. {value}" for key, value in purpose_choices.items()))
        try:
            choice = int(input(":"))
            if choice not in purpose_choices:
                raise ValueError
            break
        except ValueError:
            print("Invalid choice! Please enter a number between 1 and 5.")

    return name, amount, purpose_choices[choice]


def record_payment(data, purpose_totals):
    """
    Records payment data to the pandas DataFrame and updates purpose totals.
    """
    name, amount, purpose = get_user_input()
    new_record = pd.Series({"Name": name, "Amount": amount, "Purpose": purpose})
    data = pd.concat([data, new_record.to_frame().T], ignore_index=True) # Efficiently concatinate new record

    if purpose in purpose_totals:
        purpose_totals[purpose] += amount
    else:
        purpose_totals[purpose] = amount

    return data, purpose_totals


def save_data_to_excel(data, purpose_totals_df, filename="mydata.xlsx"):
    """
    Saves data and purpose totals to separate sheets in an Excel file with error handling.
    """
    writer = pd.ExcelWriter(filename, engine="xlsxwriter")
    try:
        data.to_excel(writer, sheet_name="Sheet1", index=False)
        purpose_totals_df.to_excel(writer, sheet_name="Sheet2", index=False)
        writer.close()
        print("Data saved to Excel successfully!")
    except PermissionError:
        print("Error: Could not save data to", filename, ". Check file permissions or try a different location.")


def create_purpose_totals_df(purpose_totals):
    """
    Creates a pandas DataFrame from the purpose totals dictionary.
    """
    purpose_totals_df = pd.DataFrame.from_dict(purpose_totals, orient="index", columns=["Total"])
    return purpose_totals_df


def main():
    """
    Main program loop for user interaction.
    """
    data = pd.DataFrame(columns=["Name", "Amount", "Purpose"])
    purpose_totals = {}

    n = int(input("Enter the number of payments to record:\n"))

    for _ in range(n):
        data, purpose_totals = record_payment(data.copy(), purpose_totals.copy())  # Avoid modifying original data and totals
        print("Successfully recorded!")

    purpose_totals_df = create_purpose_totals_df(purpose_totals)
    save_data_to_excel(data, purpose_totals_df)


if __name__ == "__main__":
    main()
