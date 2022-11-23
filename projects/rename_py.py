import os, sys

def listdir():
    """Gets a listing of the scripts directory, and excludes the script"""
    orig_files = os.listdir()
    orig_files.remove('rename_py.py')
    return orig_files

def old_extension_list(old_extension, new_extension):
    """Checks directory listing for files that are already the desired new 
    extension.Quits if no files are identified for conversion"""
    for file in orig_files:
        if new_extension in file:
            orig_files.remove(file)
            if len(orig_files) == 1:
                orig_files.clear()
                print(f"No files needing to be converted to {new_extension} "
                    "were located."
                    f"\nExiting...")
                sys.exit()
    
def new_extension_list(old_extension, new_extension):
    """Builds a a new list of files with the preferred new extension provided"""
    new_files = []
    for file in orig_files:
        file = file.removesuffix(old_extension)
        new_files.append(file + new_extension)
    return new_files

def add_file_extension(orig_files, new_files):
    """Renames the files from the original list to a matching file name in the
    new list with the desired extension"""
    i = 1
    num = len(orig_files)
    while i <= num :
        file = orig_files.pop()
        new_file = new_files.pop()
        os.rename(file, new_file)
        i += 1

def conversion_report(orig_files, new_files):
    """Prints a report detailing what files were identified and then renamed
    with the new extention"""
    print("Old files detected were: ")
    for file in orig_files:
        print(file)
    print("\nThey have now been renamed to: ")
    for file in new_files:
        print(file)

orig_files = listdir()
old_extension_list(sys.argv[1], sys.argv[2])
new_files = new_extension_list(sys.argv[1], sys.argv[2])
add_file_extension(orig_files[:], new_files[:])
conversion_report(orig_files[:], new_files[:])