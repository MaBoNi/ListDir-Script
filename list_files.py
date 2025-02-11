import os

def list_files(startpath, indent=0):
    items = sorted(os.listdir(startpath))  # Sort items alphabetically
    for index, item in enumerate(items):
        path = os.path.join(startpath, item)
        is_last = index == len(items) - 1  # Check if it's the last item

        # Format the tree structure
        prefix = "└── " if is_last else "├── "
        print("   " * indent + prefix + item)

        # Recursively list directories
        if os.path.isdir(path):
            list_files(path, indent + 1)

if __name__ == "__main__":
    print("\n📂 Directory Structure:\n")
    list_files(".")
