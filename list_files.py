import os

def list_files(startpath, indent=0, excluded_dirs=set(), excluded_files=set()):
    """ Recursively prints the directory structure in a nice format, excluding specified directories and files """
    items = sorted(os.listdir(startpath))  # Sort items alphabetically

    # Filter out excluded directories and files
    filtered_items = [item for item in items if item not in excluded_dirs and item not in excluded_files]

    for index, item in enumerate(filtered_items):
        path = os.path.join(startpath, item)
        is_last = index == len(filtered_items) - 1  # Check if it's the last item

        # Format the tree structure
        prefix = "└── " if is_last else "├── "
        print("   " * indent + prefix + item)

        # Recursively list directories
        if os.path.isdir(path):
            list_files(path, indent + 1, excluded_dirs, excluded_files)

if __name__ == "__main__":
    # Ask user whether to exclude specific directories and files
    exclude_git = input("Do you want to exclude the .git directory? (y/n): ").strip().lower() == 'y'
    exclude_ds_store = input("Do you want to exclude .DS_Store files? (y/n): ").strip().lower() == 'y'
    exclude_pycache = input("Do you want to exclude __pycache__ directories? (y/n): ").strip().lower() == 'y'

    # Create sets based on user input
    excluded_dirs = set()
    excluded_files = set()

    if exclude_git:
        excluded_dirs.add(".git")
    if exclude_pycache:
        excluded_dirs.add("__pycache__")
    if exclude_ds_store:
        excluded_files.add(".DS_Store")

    print("\n📂 Directory Structure")
    print("   Excluded: {} {} {}\n".format(
        "(.git)" if exclude_git else "",
        "(.DS_Store)" if exclude_ds_store else "",
        "(__pycache__)" if exclude_pycache else ""
    ))

    list_files(".", excluded_dirs=excluded_dirs, excluded_files=excluded_files)
