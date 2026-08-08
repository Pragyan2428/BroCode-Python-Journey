import os

def main():
    file_path = input("Enter the path of the file: " )
    if (os.path.exists(file_path)):
        print("File exists.")
        if (os.path.isdir(file_path)):
            print("It is a directory.")
        if(os.path.isfile(file_path)):
            print("It is a file.")
    else:
        print("File does not exist.")

main()