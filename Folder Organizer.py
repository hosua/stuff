import os, string, shutil
# This program organizes every file in the directory into alphabetized folders.
root = input("Enter the directory path you want to organize")
backup = input("Do you want to backup your original files? (Y/N)").lower()
if backup == "y":
    make_backup = True
elif backup == "n":
    make_backup = False
else:
    print("Invalid input")
    quit()
dir_organized_folder = os.path.join(root, 'Organized folder')
dir_backup_folder = os.path.join(root, 'Backup')
os.chdir(root)

if not os.path.exists(dir_organized_folder):     # Make this folder if it doesnt exist
    os.makedirs('Organized folder')
if make_backup:
    if not os.path.exists(dir_backup_folder):     # Make this folder if it doesnt exist
        os.makedirs('Backup')

os.chdir(dir_organized_folder)   # Move to directory


if not os.path.exists("#"):     # Make all the folders
    os.makedirs("#")
for letter in string.ascii_uppercase:   # ignore case sensitivity
    if not os.path.exists(letter):
        os.makedirs(letter)

os.chdir(root)  # We need to go into root
for file in os.listdir(root):
    if os.path.isfile(os.path.join(root, file)):  # Check if path is a file
        print(file + " is a file")
        filename = file.rsplit()    # Gets only name of file
        firstLetter = filename[0].upper()[0]
        if firstLetter in string.ascii_letters:
            new_path = os.path.join(dir_organized_folder, firstLetter)
            print(new_path)
            if not make_backup:
                shutil.move(file, new_path)     # Copying files to each directory
                print("Moving " + file + " to " + new_path)
            else:
                shutil.copy(file, new_path)     # Copying files to each directory
                print("Copying " + file + " to " + new_path)
                shutil.move(file, dir_backup_folder)    # Move files into a backup folder
                print("Moving " + file + " to " + dir_backup_folder)   # use this if you want to make a backup folder
        else:
            new_path = os.path.join(dir_organized_folder, "#")
            if make_backup:
                shutil.copy(file, dir_backup_folder)
                print("Moving " + file + " to " + dir_backup_folder)
            shutil.move(file, new_path)
            print("Moving " + file + " to " + new_path)


os.chdir(dir_organized_folder)  # Go into the new organized folder
for directory in os.listdir(dir_organized_folder):  # Delete any directories that are empty
    if len(os.listdir(directory)) == 0:
        shutil.rmtree(directory)
        print("Deleting '" + os.path.join(root, directory) + "' because it was empty")



