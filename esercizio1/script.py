#!/usr/bin/env python3
import os
import sys
from collections import defaultdict

def is_executable(file_path):
    """Check if a file is executable based on extension and permissions."""
    if sys.platform == "win32":
        return file_path.lower().endswith(('.exe', '.bat', '.cmd', '.ps1', '.py', '.pl', '.sh'))
    return os.access(file_path, os.X_OK)

def get_shebang(file_path):
    """Get the shebang line from a file if it exists."""
    try:
        with open(file_path, 'rb') as f:
            first_line = f.readline().decode('utf-8', errors='ignore').strip()
            if first_line.startswith('#!'):
                return first_line[2:].strip()
    except (IOError, UnicodeDecodeError):
        pass
    return None

def count_scripts(directory):
    """Count executable files by their shebang interpreter."""
    shebang_counts = defaultdict(int)
    
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' does not exist")
        sys.exit(1)
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if is_executable(file_path):
                shebang = get_shebang(file_path)
                if shebang:
                    shebang_counts[shebang] += 1
    
    if not shebang_counts:
        print(f"No executable files with shebang lines found in {directory}")
        return
        
    sorted_counts = sorted(shebang_counts.items(), key=lambda x: (-x[1], x[0]))
    
    for shebang, count in sorted_counts:
        print(f"{count} #!/{shebang}")

def main():
    if len(sys.argv) != 2:
        print("Usage: contaScript <directory>")
        sys.exit(1)
    
    directory = sys.argv[1]
    count_scripts(directory)

if __name__ == "__main__":
    main()