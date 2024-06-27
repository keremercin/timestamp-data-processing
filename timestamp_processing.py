import pandas as pd

def process_csv(input_file_path, output_file_path):
    # Load the CSV file
    df = pd.read_csv(input_file_path)

    # Process 'DataBytes' column
    data_bytes_column = 'CAN_DataFrame.CAN_DataFrame.DataBytes'
    data_bytes_df = df[data_bytes_column].str.strip('[]').str.split(' ', expand=True)

    # Split 'DataBytes' column into new columns
    for i in range(data_bytes_df.shape[1]):
        df[f'{data_bytes_column}_{i}'] = data_bytes_df[i]

    # Use 'CAN_DataFrame.CAN_DataFrame.ID' column as a timestamp to categorize data
    pivot_df = df.pivot_table(index='CAN_DataFrame.CAN_DataFrame.ID', aggfunc='first')

    # Save the processed DataFrame to a new CSV file
    pivot_df.to_csv(output_file_path)

    print(f"Data categorized by timestamp has been successfully saved to {output_file_path}")

if __name__ == "__main__":
    input_file_path = "path/to/your/input_file.csv"  # Change this to the path of your input CSV file
    output_file_path = "path/to/your/output_file.csv"  # Change this to the path where you want to save the output CSV file
    process_csv(input_file_path, output_file_path)
