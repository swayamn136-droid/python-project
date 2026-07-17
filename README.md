INTERNSHIP TASK 1:
Python automation script:
Automatic File Organizer:

Overview:

The *Automatic File Organizer* is a simple Python project that helps organize files in a selected folder. It automatically sorts files into different folders such as *Images*, *Documents*, *Videos*, *Music*, *Archives*, *Programs*, and *Others* based on their file extensions.

This project was developed as a learning exercise to understand Python file handling, modules, and directory management.

Features:

* Organizes files automatically by file extension.
* Creates folders if they do not already exist.
* Supports multiple file types.
* Moves unknown file types into an **Others** folder.
* Uses only Python's built-in libraries.
* Beginner-friendly and easy to understand.

Technologies Used:

* Python 3
* 'os' module
* 'shutil' module

Project Structure:

Automatic-File-Organizer/
│── main.py
│── organizer.py
│── utils.py
│── config.py
│── README.md
│── requirements.txt

How It Works:

1. The user runs the program.
2. The program asks for the folder.
3. It scans all the files inside the folder.
4. Based on the file extension, it creates folders if required.
5. Files are moved into their respective folders.
6. Files with unsupported extensions are moved to the 'others' folder.

Supported File Types

| Folder    | Extensions                |
| --------- | ------------------------- |
| Images    | .jpg, .jpeg, .png, .gif   |
| Documents | .pdf, .doc, .docx, .txt   |
| Videos    | .mp4, .mkv, .avi          |
| Music     | .mp3, .wav                |
| Archives  | .zip, .rar                |
| Programs  | .exe, .msi                |
| Others    | Any unsupported file type |

Installation:

1. Clone this repository:

bash
git clone https://github.com/your-username/Automatic-File-Organizer.git

2. Open the project folder.

3. Make sure Python 3 is installed.

Running the Project:

Run the following command:

bash
python main.py


Enter the folder path when prompted.

Example:

C:\Users\YourName\Downloads
The program will organize the files automatically.

Future Improvements:

* Add a graphical user interface (GUI).
* Add drag-and-drop functionality.
* Allow users to customize file categories.
* Add logging of moved files.
* Add an undo feature.

Learning Outcomes:

This project helped me understand:

* Python modules
* File handling
* Directory management
* Functions
* Dictionaries
* Working with multiple Python files
* Basic project organization

 Author

'Manjunatha'

B.Tech – Information Science & Engineering

Python Developer | Machine Learning Enthusiast

License:

This project is created for educational and learning purposes.

You can copy this directly into your repository's `README.md`. It matches the multi-file project (`main.py`, `organizer.py`, `utils.py`, and `config.py`) and is suitable for a student GitHub portfolio.
