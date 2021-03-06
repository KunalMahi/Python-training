def main():
    ReadFile=open("Write.txt","r")
    for line in ReadFile:
        print(line)
    ReadFile.close()

if __name__ == '__main__':main()
