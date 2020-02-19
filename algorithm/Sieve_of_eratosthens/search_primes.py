import math

flag =[False] * 100
res = []
def getPrimes():
    for i in range(2,100):
        if flag[i] == False:
            for j in range(i*i,100,i):
                flag[j] = True

def printinfo():
    for index in range(len(flag)):
        if flag[index]== False:
            res.append(index)
    print(res)

def main():
    print(flag)
    getPrimes()
    print(flag)
    printinfo()

if __name__ == "__main__":
    main()