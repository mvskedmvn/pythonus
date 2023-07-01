import os

def read():
    def openfile():

        readfile = open('F:\чобы глянуть.txt', 'r', encoding='utf-8', errors='replace').read()
        print(readfile)

    openfile()

def main():
    read()

if __name__ == "__main__":
    main()