## Digital Library Inventory Tool

A Python-based automation utility designed to index large collections of ebooks and documents. This tool traverses complex directory structures, extracts file metadata, and generates structured CSV reports for data archiving and analysis.

### Overview

Managing local libraries scattered across multiple drives and subfolders can be difficult. This script automates the inventory process by recursively scanning specified root directories for common ebook formats. It leverages Pandas to organize the data, calculate file sizes in Megabytes (MB), and export clean, sortable CSV manifests.

### Features

Multi-Directory Support: Accepts multiple root paths simultaneously using a pipe (|) delimiter.

Recursive Scanning: Traverses all subdirectories using os.walk to ensure no file is missed.

Format Filtering: Automatically detects and catalogs specific extensions:

.pdf, .epub, .doc, .txt

.djvu (scanned documents)

.cbz, .cbr (comic book archives)

Data Transformation: Converts raw byte data into human-readable MB format.

Automated Reporting: Generates a separate CSV file for each root directory scanned, sorted by subfolder and filename.

### Prerequisites

Python 3.x installed on your system.

The pandas library.

### Installation

Clone the repository:

git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
cd your-repo-name


Install dependencies:
This script relies on Pandas for data manipulation.

pip install pandas


### Usage

Run the script from your terminal:

python list_books.py


(Note: Replace list_books.py with whatever you named your script)

Enter directory paths:
When prompted, paste the full paths to the directories you want to scan. If scanning multiple locations, separate them with a pipe | character.

Example Input:

C:\Users\Name\Documents\Books|D:\ExternalDrive\Comics


View Results:
The script will generate CSV files in the current working directory named after the scanned folders (e.g., Books.csv, Comics.csv).

### Output Structure

The generated CSV contains the following columns:

Column

Description

Subfolder

The relative path where the file was found (or "Root Directory").

Filename

The name of the file including extension.

Filesize (MB)

The size of the file converted to Megabytes (2 decimal places).

Filepath

The absolute full path to the file.

### Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the issues page.

📝 License

This project is open source and available under the MIT License.
