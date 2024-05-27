import os
import shutil

def remove_pycache(directory):
    """
    Recursively traverses the directory tree starting from the given directory
    and removes any __pycache__ directories encountered.
    
    Args:
    directory (str): The directory from which to start traversing.
    """
    for root, dirs, files in os.walk(directory):
        if '__pycache__' in dirs:
            pycache_dir = os.path.join(root, '__pycache__')
            try:
                shutil.rmtree(pycache_dir)
                print("Removed:", pycache_dir)
            except OSError as e:
                print("Error:", e)

# Example usage:
if __name__ == "__main__":
    directory = os.path.join(os.path.dirname(__file__), "../src")
    remove_pycache(directory)
