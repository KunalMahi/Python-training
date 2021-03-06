x=10
def Display():
    global x
    print("x={}".format(x))
def main():
    global x
    print(x)
    Display()

if __name__ == '__main__':main()

