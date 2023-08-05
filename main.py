n = int(input("Введите число:"))
maxNumber = n*n
matrix = [[0] * n for i in range(n)]

currentNumber=1
maxStep = 0
cursorX=0
cursorY=0

def printMatrix(m,n):
    for y in range(n):
        for x in range(n):
            print(m[x][y],end='\t')
        print()

matrix[0][0]=1


#заполняем влево (первый раз)
#12345
vectorX=1
vectorY=0
maxCurrentNumber = currentNumber + n-maxStep
while currentNumber!=maxCurrentNumber:
    matrix[cursorX][cursorY] = currentNumber
    cursorX += vectorX
    cursorY += vectorY
    currentNumber+=1
cursorX -= vectorX
cursorY -= vectorY
# print("======")
# printMatrix(matrix,n)
# print("i={},X={},Y={}".format(currentNumber,cursorX,cursorY))


while(True):
    #заполняем вниз
    #6  7  8  9
    maxStep +=1
    vectorX=0
    vectorY=1
    cursorX += vectorX
    cursorY += vectorY
    maxCurrentNumber = currentNumber + n-maxStep
    while currentNumber!=maxCurrentNumber:
        matrix[cursorX][cursorY] = currentNumber
        cursorX += vectorX
        cursorY += vectorY
        currentNumber+=1
    cursorX -= vectorX
    cursorY -= vectorY
    # print("======")
    # printMatrix(matrix,n)
    # print("i={},X={},Y={}".format(currentNumber,cursorX,cursorY))
    if currentNumber>maxNumber:
        break


    #заполняем вправо
    #10 11 12 13
    vectorX=-1
    vectorY=0
    cursorX += vectorX
    cursorY += vectorY
    maxCurrentNumber = currentNumber + n-maxStep
    while currentNumber!=maxCurrentNumber:
        matrix[cursorX][cursorY] = currentNumber
        cursorX += vectorX
        cursorY += vectorY
        currentNumber+=1
    cursorX -= vectorX
    cursorY -= vectorY
    # print("======")
    # printMatrix(matrix,n)
    # print("i={},X={},Y={}".format(currentNumber,cursorX,cursorY))
    if currentNumber>=maxNumber:
        break    

    #заполняем вверх
    #14 15 16
    maxStep +=1
    vectorX=0
    vectorY=-1
    cursorX += vectorX
    cursorY += vectorY
    maxCurrentNumber = currentNumber + n-maxStep
    while currentNumber!=maxCurrentNumber:
        #print("[{}][{}] = {} ".format(cursorY,cursorX,i+1))
        matrix[cursorX][cursorY] = currentNumber
        cursorX += vectorX
        cursorY += vectorY
        currentNumber+=1
    cursorX -= vectorX
    cursorY -= vectorY
    # print("======")
    # printMatrix(matrix,n)
    # print("i={},X={},Y={}".format(currentNumber,cursorX,cursorY))
    if currentNumber>maxNumber:
        break    

    #заполняем влево
    #17 18 19
    vectorX=1
    vectorY=0
    cursorX += vectorX
    cursorY += vectorY
    maxCurrentNumber = currentNumber + n-maxStep
    while currentNumber!=maxCurrentNumber:
        #print("[{}][{}] = {} ".format(cursorY,cursorX,i+1))
        matrix[cursorX][cursorY] = currentNumber
        cursorX += vectorX
        cursorY += vectorY
        currentNumber+=1
    cursorX -= vectorX
    cursorY -= vectorY
    # print("======")
    # printMatrix(matrix,n)
    # print("i={},X={},Y={}".format(currentNumber,cursorX,cursorY))
    if currentNumber>maxNumber:
        break    

printMatrix(matrix,n)

