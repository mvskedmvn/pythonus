def readff():
    openf = open('dataset_3363_2.txt','r').read()
    opentest = open('dataset_3363_2(test).txt','r').read()
    print(f'{openf}')
    print(f'{opentest}')
    
def writeff():

    digits = set('0123456789')
    i = 0
    multi = ''
    decryp = ''
    
    with open('dataset_3363_2.txt') as openf:
        string = openf.readline().strip()
        char = string[i]
        i+=1

        while i<len(string):
            while string[i] in digits:
                multi +=string[i]
                i+=1
                if i > (len(string) - 1):
                    break
            decryp += (char * int(multi))
            multi = ''
            if i > (len(string) - 1):
                    break
            char = string[i]
            i+=1

    with open('dataset_3363_2(test).txt', 'w') as opentest:
        writer = opentest.write(decryp)

    with open('dataset_3363_2(test).txt', 'r') as opentest:
        reader = opentest.read()
        print(f'{reader}')

def main():
    readff()
    writeff()

if __name__ == '__main__':
    main()
