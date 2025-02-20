import os
import pandas as pd
import random
import uuid

def list_books_in_directory(root_dir):
    """
    Lists all ebook files within a specified directory and its subdirectories.

    Args:
        root_dir: The path to the root directory to search.

    Returns:
        A Pandas DataFrame containing the file information, or None if an error occurs.
    """

    if not os.path.isdir(root_dir):
        print(f"Error: '{root_dir}' is not a valid directory.")
        return None

    data = []  # List to store file information

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Extract the subfolder name relative to the root directory
        subfolder = os.path.relpath(dirpath, root_dir)
        if subfolder == ".":  # If it's the root directory itself
            subfolder = "Root Directory"

        for filename in filenames:
            if filename.lower().endswith(('.pdf', '.epub', '.doc', '.txt', '.djvu', '.cbz', '.cbr')):
                filepath = os.path.join(dirpath, filename)
                filesize_bytes = os.path.getsize(filepath)
                filesize_mb = filesize_bytes / (1024 * 1024) #convert to MB

                data.append({
                    'Subfolder': subfolder,
                    'Filename': filename,
                    'Filepath': filepath,
                    'Filesize (MB)': f"{filesize_mb:.2f}" #format to 2 decimal places
                })

    if not data:
        print(f"No ebook files found in '{root_dir}' or its subdirectories.")
        return None

    df = pd.DataFrame(data)
    df = df.sort_values(by=['Subfolder', 'Filename']) #sort by subfolder then filename
    df = df[['Subfolder', 'Filename', 'Filesize (MB)', 'Filepath']]  # Reorder columns for better readability
    return df


def main():
    """
    Main function to get user input (multiple directories using '|' delimiter),
    process them, and export to CSV files.
    """
    root_directories_input = input("Enter the full paths to the directories, separated by '|': ") # Updated input prompt - using '|' as delimiter
    root_directories = [path.strip() for path in root_directories_input.split("|")] # Split by '|'

    # Get filename choice ONCE at the beginning
    while True:
        filename_choice = input("Do you want to use random filenames for the CSVs (yes/no)? ")
        if filename_choice.lower() == 'yes':
            use_random_names = True
            break
        elif filename_choice.lower() == 'no':
            use_random_names = False
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    if not use_random_names:
        custom_filename_base = input("Enter a base custom filename (e.g., my_books): ")
        if not custom_filename_base.lower().endswith('.csv'):
            custom_filename_base += ".csv"

    for i, root_directory in enumerate(root_directories):
        df_result = list_books_in_directory(root_directory)

        if df_result is not None:
            # --- COMMENTED OUT TABLE PRINTING ---
            # print(f"\nList of PDF and EPUB files in '{root_directory}':")
            # print(df_result.to_string(index=False))

            if use_random_names:
                random_filename = str(uuid.uuid4()) + ".csv"
            else:
                random_filename = f"{custom_filename_base.replace('.csv','')}_{i}.csv"

            df_result.to_csv(random_filename, index=False)
            print(f"Results for '{root_directory}' exported to '{random_filename}'")
        else:
            pass  # Error messages are already handled within list_books_in_directory


if __name__ == "__main__":
    main()

