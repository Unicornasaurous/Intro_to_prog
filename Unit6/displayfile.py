def main():
    fileobj = open("numbers.txt", "r")
    for linenum in fileobj:
        print(int(linenum))
    fileobj.close()
main()
