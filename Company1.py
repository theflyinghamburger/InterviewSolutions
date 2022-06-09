import random
from collections import defaultdict


def parseExp(expr):
    arrVar = []
    arrOp = []
    for x in range(len(expr)):
        if expr[x] == " ":
            pass
        elif expr[x] == "a":
            if expr[x + 1].isdigit():
                if int(expr[x + 1]) < 5:
                    arrVar.append(int(expr[x + 1]) - 1)
                else:
                    print("Invalid expression")
                    print("digit more than 5")
                    return False, False
            else:
                print("Invalid expression")
                print("not digit after a")
                return False, False

        elif expr[x] in ["+", "-", "/", "*"]:
            arrOp.append(expr[x])

    if len(arrVar) == len(arrOp) + 1:
        print(arrVar)
        print(arrOp)
        return arrVar, arrOp
    else:
        print("length mismatch")
        print("Invalid expression")
        return False, False


def preRearrange(arrVar, arrOp):
    count = 0
    runningOP = []
    runningVar = []
    while count < len(arrVar) - 1:
        if arrOp[count] in ["*", "/"]:
            runningOP.append(arrOp[count])
            if arrVar[count] not in runningVar:
                runningVar.append(arrVar[count])
            if arrVar[count + 1] not in runningVar:
                runningVar.append(arrVar[count + 1])
        count += 1

    count = 0
    while count < len(arrVar) - 1:

        if arrOp[count] in ["+", "-"]:
            runningOP.append(arrOp[count])
            if arrVar[count] not in runningVar:
                runningVar.append(arrVar[count])
            if count == (len(arrVar) - 2):
                runningVar.append(arrVar[count + 1])


        count += 1
    return runningVar, runningOP


def evalExpr(expr, arrayOfArrays_):
    arrVar, arrOp = parseExp(expr)
    arrVar, arrOp = preRearrange(arrVar, arrOp)
    tempVal = 0
    sumRegCntDict = defaultdict(list)
    print(arrVar)
    print(arrOp)
    for j in (range(len(arrayOfArrays_[0]))):
        for i in (range(len(arrOp))):
            if i == 0:
                tempVal = evalFnc(arrOp[i], arrayOfArrays_[arrVar[i]][j], arrayOfArrays_[arrVar[i + 1]][j])
            else:
                tempVal = evalFnc(arrOp[i], tempVal, arrayOfArrays_[arrVar[i + 1]][j])
        countryReg = arrayOfArrays_[4][j] + "_" + arrayOfArrays_[5][j]
        #print(tempVal)
        if countryReg in sumRegCntDict.keys(): # Improve code
            sumRegCntDict[countryReg] += tempVal
        else:
            sumRegCntDict[countryReg] = tempVal
    #print(sumRegCntDict)
    return sumRegCntDict


def evalFnc(operator, n1, n2):
    if operator == "+":
        return n1 + n2
    if operator == "-":
        return n1 - n2
    if operator == "*":
        return n1 * n2
    if operator == "/":
        return n1 / n2
    else:
        print("Invalid operator")


def randomArrayPopulate(length):
    countryList = ["india", "UK", "USA", "France"]
    regionList = ["Asia", "Europe", "NorthAm"]
    arr1 = [(random.randint(1, 9)) for i in range(length)]
    arr2 = [(random.randint(1, 9)) for i in range(length)]
    arr3 = [(random.randint(1, 9)) for i in range(length)]
    arr4 = [(random.randint(1, 9)) for i in range(length)]
    country = [(countryList[random.randint(0, len(countryList) - 1)]) for i in range(length)]
    region = [(regionList[random.randint(0, len(regionList) - 1)]) for i in range(length)]
    return [arr1, arr2, arr3, arr4, country, region]

def main():
    arrayOfArrays = randomArrayPopulate(1000)
    # for itrr in arrayOfArrays:
    #    print(itrr)
    outputDict = evalExpr("a1-a2*a3+a4+a1", arrayOfArrays)
    for key in outputDict.keys():
        strSplit = key.split("_")
        reg = strSplit[0]
        country = strSplit[1]
        print(reg + "\t" + country + "\t" + str(outputDict[key]))


if __name__ == '__main__':
    main()


"""
from multiprocessing import Process
      my_process1 = Process(target=functionName, args=('x',))
      my_process2 = Process(target=evenno, args=('x',))
      my_process1.start()
      my_process2.start()
      my_process1.join()
   my_process2.join()
print ("Done")
"""
