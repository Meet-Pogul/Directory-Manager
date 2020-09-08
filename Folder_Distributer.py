import os

# ClearTheCulter
try:
    d = input("Directory Location: ")
    os.chdir(d)
    for i in os.listdir():
        if os.path.isfile(i):
            form = os.path.splitext(i)[1].split(".")[1].upper()
            if form not in os.listdir():
                os.mkdir(form)
            os.replace(i, form + '/' + i)
except FileNotFoundError:
    print("File Not Found")
