def main():
    try:
        x=int(input("Enter a number:"))
        print(x+5)
    except ValueError:
        print("You haven't entered a valid number")
if __name__ == '__main__':main()
