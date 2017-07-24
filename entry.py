import game
import sys

def main(row,col,num):
    initMineList = game.initMineList(row,col)
    mineList = initMineList[0]
    statusList = initMineList[1]

    game.setMine(mineList,num)
    game.displayBorad(mineList,statusList)
    re = game.gemeLoop(mineList,statusList)
    if(re == 2):
        print("You win !!!!!")
    elif(re == 1):
        print("BOOM you lose !!!!")

if __name__ == "__main__":
    row = int(sys.argv[1])
    col = int(sys.argv[2])
    num = int(sys.argv[3])
    #row = 5
    #col = 5
    #num = 5
    main(row,col,num)