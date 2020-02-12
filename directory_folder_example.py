# Function that takes string param
# string param is a directory location on the machine
# while loop that checks that folder for the files on that folder
# return false if it is the same and then if it increases it will exit

import os, os.path
import time

def get_file_count(dir):
    # returns the number of files in a directory, excluding folders
    ct_files = []
    # getting file count in the directory
    for folder_or_file in os.listdir(dir):
        if os.path.isfile(folder_or_file):
            ct_files.append(folder_or_file)
    return len(ct_files)

def flag_file_count_change(dir):
    # getting initial file count in the directory
    init_files_ct = get_file_count(dir)
    # check if the number of files changes and return true
    while get_file_count(dir) == init_files_ct:
        time.sleep(0.5)
        print("file count unchanged")
        if get_file_count(dir) != init_files_ct:
            print("file count changed!")
            return True