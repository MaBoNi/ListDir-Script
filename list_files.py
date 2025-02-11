import os

def list_files(startpath, indent=0, excluded_dirs=set()):
    """ Recursively prints the directory structure in a nice format, excluding specified directories """
    items = sorted(os.listdir(startpath))  # Sort items alphabetically

    filtered_items = [item for item in items if item not in excluded_dirs]  # Exclude specified directories

    for index, item in enumerate(filtered_items):
        path = os.path.join(startpath, item)
        is_last = index == len(filtered_items) - 1  # Check if it's the last item

        # Format the tree structure
        prefix = "└── " if is_last else "├── "
        print("   " * indent + prefix + item)

        # Recursively list directories
        if os.path.isdir(path):
            list_files(path, indent + 1, excluded_dirs)

if __name__ == "__main__":
    # Ask the user whether to exclude the .git directory
    exclude_git = input("Do you want to exclude the .git directory? (y/n): ").strip().lower() == 'y'
    excluded_dirs = {".git"} if exclude_git else set()

    print("\n📂 Directory Structure {}\n".format("(excluding .git)" if exclude_git else "(including all directories)"))
    list_files(".", excluded_dirs=excluded_dirs)
