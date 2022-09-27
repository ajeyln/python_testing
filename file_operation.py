import time

# file operations
def file_operation(t):
    read_file = open(t, "r")
    file_content = set(read_file.read().split(" "))
    read_file.close()
    return file_content


if __name__ == '__main__':
    text1 = input("Enter the first file name: ")
    set1 = file_operation(text1)
    time.sleep(2)
    print("file is ready...")
    text2 = input("Enter the second file name: ")
    set2 = file_operation(text2)
    print("file is ready...")
    time.sleep(2)
    print("wait...")
    time.sleep(5)
    print(set1.intersection(set2))


