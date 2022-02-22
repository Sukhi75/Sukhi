try:
    #trying to open a file in read mode
    f1 = open("myfile.txt","rt")
    print("File opened")
except FileNotFoundError:
    print("File does not exist")
except:
    print("Other error")

    