import os, os.path
import time


class Folder():
    # dir = "C:/Users/DELL/AppData/Local/Temp"
    def ObtainInfo(self, dir):
        #This piece of code shows the files and folders separately, I can sum the 2 variables or use them to show just files or folders inside the path
            path, dirs, files = next(os.walk(dir))
            file_count = len(files)
            folder_count = len(dirs)
            print("Just counting files: ", file_count, " on path: ", dir)
            print("Just counting folders: ", folder_count, " on path: ", dir)

            #This part includes the files and folders
            list = os.listdir(dir)  # dir is your directory path
            number_files = len(list)
            print ("Number of files & folders under the selected path: ", number_files, " on path: ", dir)

            while (file_count <= (file_count)):
                print("False")
                return False
            if (file_count +1):
                print("True")
                return True

Attempt = Folder()
tm = 0
while True:
    tm += 1
    Attempt.ObtainInfo(dir = "C:/Users/DELL/AppData/Local/Temp")
    time.sleep(5)

    # (len(list) or len(files) or len(dirs)) <= (len(list) or len(files) or len(dirs)):
#https://gist.github.com/jmingtan/1171288/8286cd988b90f0df41b5ed8d8cfc4a185ce95504