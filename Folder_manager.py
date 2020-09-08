import os


def soldier(address, dic_file, extension):
    try:
        os.chdir(address)
    except FileNotFoundError:
        print("Directory not Found")
        print("Program is not successful ran")
        exit()
    k = []
    try:
        with open(dic_file, "r") as f:
            for i in f:
                k.append(i.strip().replace("\n", ""))
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("You have no permission to read file or it is Directory")
    finally:
        print(k)
        if len(k) == 0:
            print("Dictionary List is empty")
            y = 'k'
            while y != 'y' and y != 'n':
                y = input("Do you want to apply filter to whole directory's file(y/n): ").lower()
            if y != 'y':
                print("Program Is Not Successful Ran")
                exit()

    n = 0
    for i in os.listdir():
        if os.path.isfile(i) and i not in k:
            os.rename(i, i.capitalize())
        if i.find("." + extension) != -1 and i not in k:
            n += 1
            os.rename(i, str(n) + "." + extension)
    print("Program Ran Successfully")


if __name__ == '__main__':
    soldier(input("Enter Directory Address: "), input("Enter Dictionary File: "), input("Enter Format: "))
