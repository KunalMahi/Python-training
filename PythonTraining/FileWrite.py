def main():
    writefile=open("Write.txt","a")
    for i in range(5):
        inputtofile=input("Enter the string to be entered: ")
        writefile.write("\n{}".format(inputtofile))

    writefile.close()

if __name__ == '__main__':main()
