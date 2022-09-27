import re

class Filename:

    def __init__(self, file_name):
        self.filename = file_name

    def reg_exp(self):
        file_read = open(self.filename, "r")
        list1 = []
        for i in set(file_read.read().split()):
            x = re.search(".*in", i)
            if x:
                list1.append(i)
        return(list1)
            

    def setfilename(self, newname):
        self.filename = newname
        print(self.reg_exp())
    
    def getfilename(self):
        return self.filename


if __name__ == "__main__":
    file1 = Filename("text1.txt")
    print(file1.reg_exp())
    file1.setfilename("text2.txt")
    print(file1.getfilename())