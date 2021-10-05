import os
import shutil
import time

def main():
    os.getcwd()
    deletedfolders= 0
    deletedfiles = 0
    path="c:/Users/skyla/Downloads/JunkFolder"
    isexists = os.path.exists(path)
    print(isexists)
    days = 2
    seconds = time.time() - (days*24*60*60)
    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if seconds >= get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deletedfolders += 1

                break
            else: 
                for folder in folders:

                    folder_path = os.path.join(root_folder,folder)
                    if seconds >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deletedfolders += 1

                for file in files:

                    file_path = os.path.join(root_folder,file)
                    if seconds >= get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deletedfiles += 1
            
        else:
            if seconds >= get_file_or_folder_age(path):
                remove_file(path)
                deletedfiles += 1

    else:

        print(f'"{path}" is nowhere to be found.')     
        deletedfiles += 1       




    
    print(f"Total folders deleted: {deletedfolders}")
    print(f"Total files deleted: {deletedfiles}")




def remove_folder(path):
    if not shutil.rmtree(path):
        print(f"{path} has successfully been deleted.")
    
    else:
        print(f"We have failed to delete the" + path)

def remove_file(path):
    if not os.remove(path):
        print(f"{path} has successfully been deleted.")
    
    else:
        print(f"We have failed to delete the" + path)

def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime

    print(ctime)

if __name__ == '__main__':
	main()