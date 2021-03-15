import os, string, shutil
# This program takes all files in a directory and moves them to the root.
# NOTE: This does not handle directories within directories
# Perhaps implement this another time
root = input("Enter the directory path you want to extract")
backup = input("Do you want to backup your original files? (Y/N)").lower()
if backup == "y":
    make_backup = True
elif backup == "n":
    make_backup = False
else:
    print("Invalid input")
    quit()

dir_backup_folder = os.path.join(root, 'Backup')

os.chdir(root)
if make_backup:
    if os.path.exists(dir_backup_folder):     # Make this folder if it doesnt exist
        print("Deleting old backup folder")
        os.remove(dir_backup_folder)

    os.chdir(root)
    if not os.path.exists("#"):     # Make all the folders
        os.makedirs("#")
    for letter in string.ascii_uppercase:   # ignore case sensitivity
        if not os.path.exists(letter):
            os.makedirs(letter)

    shutil.copytree(root, dir_backup_folder)    # Copy everything to backup folder
    for directory in os.listdir(root):   # Delete all except backup folder
        if os.path.basename(directory) != "Backup":
            if os.path.isdir(directory):
                print("Removing " + directory)
                shutil.rmtree(directory)

    os.chdir(dir_backup_folder)

    for directory in os.listdir(dir_backup_folder):     # for each directory in the backup
        new_dir = os.path.join(dir_backup_folder, directory)
        if os.path.isdir(new_dir):
            os.chdir(new_dir)
            for file in os.listdir(new_dir):  # copying all files to root
                print("Copying " + file + " to " + root)
                if os.path.isfile(file):
                    shutil.copy(file, root)
                else:   # directory
                    if os.path.exists(root):
                        shutil.rmtree(root)
                        shutil.copytree(file, root)
        os.chdir(root)

else:   # Not making backup
    for directory in os.listdir(root):     # for each directory in the root
        new_dir = os.path.join(root, directory)
        if os.path.isdir(new_dir):
            os.chdir(new_dir)
            for file in os.listdir(os.path.join(root, directory)):  # moving all files to root
                print("Moving " + file + " to " + root)
                if os.path.isfile(file):
                    shutil.move(file, root)
                else:  # directory
                    shutil.move(file, root)
        os.chdir(root)

for directory in os.listdir(root):
    if os.path.isdir(directory):    # check if a directory first
        if len(os.listdir(directory)) == 0:     # remove directory if its empty
            print("Removing " + directory)
            shutil.rmtree(directory)




