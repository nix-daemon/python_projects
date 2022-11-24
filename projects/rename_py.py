import os, sys

script_name = sys.argv[0]

def listdir():
    """Retrieves a directory listing, removes the called script, and returns the
    directory listing."""
    orig_files = os.listdir()
    if ".\\" in script_name:
        orig_files.remove(script_name.strip(".\\"))
    else:
        orig_files.remove(script_name)
    return orig_files

def old_extension_list(old_extension, new_extension):
    """Checks directory listing for files that are already the desired new 
    extension. Quits if no files are identified for conversion"""
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
    """Builds a a list of files adding the new extension provided"""
    new_files = []
    for file in orig_files:
        file = file.removesuffix(old_extension)
        new_files.append(file + new_extension)
    return new_files

def add_file_extension(orig_files, new_files):
    """Copies each file from the directory listing, and moves it to a list with 
    the old extension replaced by the new extension"""
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
    if orig_files:
        print("Old files detected were: ")
        for file in orig_files:
            print(file)
    if new_files:
        print("\nThey have now been renamed to: ")
        for file in new_files:
            print(file)

orig_files = listdir() # Stores listing of the current directory
if len(sys.argv) > 1: # If command line arguments were given, they are assigned
    # to variables and used to call the function.
    old_extension = sys.argv[1]
    new_extension = sys.argv[2]
    old_extension_list(old_extension, new_extension)
else: # Takes user input for the function call if no command line arguments given
    old_extension = input("What extension are you converting from?")
    new_extension = input("What extension are you converting to?")
    old_extension_list(old_extension, new_extension)
if len(sys.argv) > 1: # If command line argments were given, function is called
    # with the correct variables assigned
    new_files = new_extension_list(old_extension, new_extension)
else: # # If command line argments were given, function is called
    # with the correct variables assigned
    new_files = new_extension_list(old_extension, new_extension)
add_file_extension(orig_files[:], new_files[:]) # Provide the function a copy 
# of the file directory lists
conversion_report(orig_files[:], new_files[:]) # Provide the function a copy 
# of the file directory lists  