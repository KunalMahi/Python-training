def main():
    try:
        ReadFile=open("test.txt","r")
        for line in ReadFile:
            print(line)
        ReadFile.close()
    except IOError:
        print("File does not exist")
    print("App is done")

if __name__ == '__main__':main()
