import pandas as pd

def read_excel_file(file_path, sheet_name="Sheet1"):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        # Display the contents
        print("Excel file data:\n")
        print(df)
        
        # Optionally return the DataFrame
        return df

    except FileNotFoundError:
        print(f"Error: File not found -> {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    file_path = "MahamayaApartment.xlsx"  # Replace with your file path
    read_excel_file(file_path,"Cashbook")
