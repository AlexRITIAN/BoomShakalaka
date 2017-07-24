import random
import os

def initMineList(row, col):
    mineList = []
    statusList = []
    minestatusList = []

    r = 0
    while r < row:
        colList = []
        colStatusList = []
        l = 0
        while l < col:
            colList.append(0)
            colStatusList.append(0)
            l += 1
        mineList.append(colList)
        statusList.append(colStatusList)
        r += 1
    minestatusList.append(mineList)
    minestatusList.append(statusList)
    return minestatusList


def setMine(mineList, num):
    count = 0
    row = len(mineList)
    col = len(mineList[0])
    while count < num:
        row_id = random.randint(0, row - 1)
        col_id = random.randint(0, col - 1)
        if(mineList[row_id][col_id] != -1):
            mineList[row_id][col_id] = -1
            count += 1


def displayBorad(mineList, statusList):
    os.system('cls')
    row_id = len(mineList)
    col_id = len(mineList[0])

    setMineBoardNum(mineList)

    r = 0
    while r < row_id:
        l = 0
        if(r == 0):
            print(" ",end='')
            while l < col_id:
                print(" %d " % l,end="")
                l += 1
            print("")
        l = 0
        while l < col_id:
            if(l == 0):
                print("%d" % r ,end="")
            if(statusList[r][l] == 0):
                print("[-]",end="")
            elif mineList[r][l] != -1:
                print("[%d]" % mineList[r][l],end="")
            else:
                print("[BOM]",end="")
            l += 1
        print("")
        r += 1
            

def setMineBoardNum(mineList):
    row_id = len(mineList)
    col_id = len(mineList[0])

    r = 0
    while r < row_id:
        l = 0
        while l < col_id:
            setLocNum(mineList, r, l)
            l += 1
        r += 1


def setLocNum(mineList, r, l):
    mineList[r][l] = getLocNum(mineList, r, l)


def getLocNum(mineList, r, l):
    row_id = len(mineList)
    col_id = len(mineList[0])

    if(mineList[r][l] == -1):
        return -1
    count = 0
    if(r - 1 >= 0):
        if(l - 1 >= 0 and mineList[r - 1][l - 1] == -1):
            count += 1
        if(mineList[r - 1][l] == -1):
            count += 1
        if(l + 1 < col_id and mineList[r - 1][l + 1] == -1):
            count += 1

    if(l - 1 >= 0 and mineList[r][l - 1] == -1):
        count += 1
    if(mineList[r][l] == -1):
        count += 1
    if(l + 1 < col_id and mineList[r][l + 1] == -1):
        count += 1

    if(r + 1 < row_id):
        if(l - 1 >= 0 and mineList[r + 1][l - 1] == -1):
            count += 1
        if(mineList[r + 1][l] == -1):
            count += 1
        if(l + 1 < col_id and mineList[r + 1][l + 1] == -1):
            count += 1

    return count


def gemeLoop(mineList, statusList):
    re = move(mineList, statusList)
    while(re == 0):
        re = move(mineList, statusList)
    return re


def move(mineList, statusList):
    if checkEnd(mineList, statusList) == 0:
        return 2
    else:
        row, col = input("Enter row col what you want uncovered : ").split()
        #row = 2
        #col = 3
        re = uncovered(mineList, statusList, int(row), int(col))
        if(re == 0):
            displayBorad(mineList, statusList)
            return 0
        elif(re == 1):
            displayBoom(mineList, statusList)
            return 1


def checkEnd(mineList, statusList):
    row = len(mineList)
    col = len(mineList[0])

    r = 0
    while r < row:
        l = 0
        while l < col:
            if(statusList[r][l] == 0):
                if(mineList[r][l] != -1):
                    return 1
            l += 1
        r += 1
    return 0


def displayBoom(mineList, statusList):
    os.system('cls')
    row_id = len(mineList)
    col_id = len(mineList[0])

    setMineBoardNum(mineList)

    r = 0
    while r < row_id:
        l = 0
        if(r == 0):
            print(" ",end='')
            while l < col_id:
                print(" %d " % l,end="")
                l += 1
            print("")
        l = 0
        while l < col_id:
            if(l == 0):
                print("%d" % r ,end="")
            if(mineList[r][l] == -1):
                print("[B]",end="")
            elif(statusList[r][l] == 0):
                print("[-]",end="")
            elif mineList[r][l] != -1:
                print("[%d]" % mineList[r][l],end="")
            l += 1
        print("")
        r += 1

def uncovered(mineList,statusList,row,col):
    r = len(mineList)
    l = len(mineList[0])
    if(row >= r or col >= l or row < 0 or col < 0):
        return 0
    if(statusList[row][col] == 1):
        return 0
    statusList[row][col] = 1

    if(mineList[row][col] == -1):
        return 1
    else:
        if(getLocNum(mineList,row,col) == 0):

            if(row - 1 >= 0):
                if(col - 1 >= 0):
                    uncovered(mineList,statusList,row - 1,col - 1)
                uncovered(mineList,statusList,row - 1,col)
                if(col + 1 < l):
                    uncovered(mineList,statusList,row - 1,col + 1)

            if(col - 1 >= 0):
                uncovered(mineList,statusList,row,col - 1)
            if(col + 1 < l):
                uncovered(mineList,statusList,row,col + 1)

            if(row + 1 < r):
                if(col - 1 >= 0):
                    uncovered(mineList,statusList,row + 1,col - 1)
                uncovered(mineList,statusList,row + 1,col)
                if(col + 1 >= 0):
                    uncovered(mineList,statusList,row + 1,col + 1)

        return 0