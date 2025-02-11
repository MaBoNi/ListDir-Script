![License](https://img.shields.io/github/license/maboni/ListDir-Script?style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/maboni/ListDir-Script?style=for-the-badge)

A Python script to list the directory structure of the current folder with options to exclude certain directories and files.

## Features
- **Tree-like structure** – Displays the folder structure in a readable format.
- **Exclusion options** – Choose to exclude `.git`, `.DS_Store`, and `__pycache__` directories.
- **Automatic exclusion of script** – The script file itself (`list_files.py`) is always excluded.

## Getting Started

### Prerequisites
- Python 3.6+

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/maboni/ListDir-Script.git
    cd ListDir-Script
    ```

2. **Run the script**:
    ```bash
    python list_files.py
    ```

3. **Follow the prompts**:
    - You will be asked whether to exclude `.git`, `.DS_Store`, and `__pycache__` directories.

### Alternative Installation
If you prefer, you can download and run the script directly without cloning the repository:

```bash
curl -O https://raw.githubusercontent.com/maboni/ListDir-Script/main/list_files.py && python list_files.py
```

### Example Output

```plaintext
├── .gitignore
├── LICENSE
├── README.md
└── src
    ├── main.py
    ├── utils.py
    ├── data
    │   ├── config.json
    │   └── sample.txt
    └── tests
        ├── test_main.py
        └── test_utils.py
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.
