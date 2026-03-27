def funcA():
    print("Начали выполняь А")
    funcB()
    print("Закончили выполняь А")

def funcB():
    print("Начали выполняь B")
    funcC()
    print("Закончили выполняь B")

def funcC():
    print("Начали выполняь С")
    funcD()
    print("Закончили выполняь С")

def funcD():
    print("Начали выполняь D")
    print("Закончили выполняь D")

#funcA()

def Rekursy():
    print("Это охренительно бесконечная рекурсия")
    Rekursy()
Rekursy()


