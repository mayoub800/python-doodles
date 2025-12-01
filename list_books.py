import os
import pandas as pd

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

    # REVERTED TO os.walk
    # os.walk is recursive (goes into subfolders) and returns the 3 items 
    # (dirpath, dirnames, filenames) that your logic relies on.
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Extract the subfolder name relative to the root directory
        subfolder = os.path.relpath(dirpath, root_dir)
        if subfolder == ".":  # If it's the root directory itself
            subfolder = "Root Directory"

        for filename in filenames:
            if filename.lower().endswith(('.pdf', '.epub', '.doc', '.txt', '.djvu', '.cbz', '.cbr')):
                filepath = os.path.join(dirpath, filename)
                
                # Check if file exists to avoid errors with broken symlinks or permissions
                try:
                    filesize_bytes = os.path.getsize(filepath)
                    filesize_mb = filesize_bytes / (1024 * 1024)  # convert to MB

                    data.append({
                        'Subfolder': subfolder,
                        'Filename': filename,
                        'Filepath': filepath,
                        'Filesize (MB)': f"{filesize_mb:.2f}"  # format to 2 decimal places
                    })
                except OSError as e:
                    print(f"Skipping file due to error: {filepath} ({e})")
                    continue

    if not data:
        print(f"No ebook files found in '{root_dir}' or its subdirectories.")
        return None

    df = pd.DataFrame(data)
    df = df.sort_values(by=['Subfolder', 'Filename'])  # sort by subfolder then filename
    df = df[['Subfolder', 'Filename', 'Filesize (MB)', 'Filepath']]  # Reorder columns for better readability
    return df


def main():
    """
    Main function to get user input (multiple directories using '|' delimiter),
    process them, and export to CSV files.
    """
    root_directories_input = input("Enter the full paths to the directories, separated by '|': ")  # Updated input prompt - using '|' as delimiter
    root_directories = [path.strip() for path in root_directories_input.split("|")]  # Split by '|'

    for root_directory in root_directories:
        df_result = list_books_in_directory(root_directory)

        if df_result is not None:
            # Extract the folder name from the path
            folder_name = os.path.basename(os.path.normpath(root_directory)) # normpath handles trailing slashes correctly
            output_filename = f"{folder_name}.csv"

            df_result.to_csv(output_filename, index=False)
            print(f"Results for '{root_directory}' exported to '{output_filename}'")
        else:
            pass  # Error messages are already handled within list_books_in_directory


if __name__ == "__main__":
    main()
