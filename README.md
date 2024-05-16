this whole stuff is same as the readme you will get in the foulder so just skip to foulder and enjoy :)

### Files to Included in the First Commit
1. `auto.py` (the main script, config is within)
2. `README.md` (project documentation)

### Directory Structure
```
downloads-folder-automation/
│
├── auto.py
└── README.md

## Overview
This Python script is designed to automate the organization of files in your Downloads folder. It sorts files into respective folders based on their file types (e.g., documents, images, videos, etc.), ensuring your Downloads folder remains clean and easy to navigate.

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
The location can be added where I have added mine, and dont worry its withn the code  

## Usage
### Running the Script
For now you have to run the script manually through VS code or any other IDE, will add a run for through concole in future

## Logging
The script uses Python's `logging` module to record its activities. Logs are saved to `downloads_automation.log` in the script's directory. You can customize the logging settings in `organize_downloads.py`.


## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.


## License
This project is licensed under the MIT License.

## Contact
For any questions or feedback, please contact [rishifogla99@gmail.com].
