### Directory Structure
```
downloads-folder-automation/
│
├── auto.py
└── README.md

## Overview
This Python script is designed to automate the organization of files in your Downloads folder. It sorts files into respective folders based
on their file types (e.g., documents, images, videos, etc.), ensuring your Downloads folder remains clean and easy to navigate.

## Features
- **File Sorting:** Automatically moves files into categorized folders (Documents, Images, Videos, Music, Archives, Others).
- **Customizable:** Easily adjust file type categories and destination folders.


## Requirements
- Python 3.x
- Required Python packages (install via `pip install -r requirements.txt`):
  - `os`
  - `shutil`
  - `time`
  - `logging`
  - `watchdog` (for monitoring file changes)


## Configuration []
The location can be added where I have added mine, and dont worry its withn the code. 

## Usage
### Running the Script
For now you have to run the script manually through VS code or any other IDE,
Will add a command for concole in future.

## Logging
The script uses Python's `logging` module to record its activities. Logs are saved to `downloads_automation.log` in the script's directory.
You can customize the logging settings in `auto.py`.


## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.


## Contact
For any questions or feedback, please contact [rishifogla99@gmail.com].
