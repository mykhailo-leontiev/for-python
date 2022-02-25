from decimal import Decimal
while True:
    mode = int(input("Какой ты хочешь режим?(1-прибавление,2-отнимание,3-умножение,4-деление,5-возведение в степень): "))
    if mode == 1:
        print ("Ты выбрал прибавление")
        s = "добавить"
    elif mode == 2:
        print ("Ты выбрал отнимание")
        s = "отнять"
    elif mode == 3:
        print ("Ты выбрал умножение")
        s = "умножить"
    elif mode == 4:
        print ("Ты выбрал деление")
        s = "поделить"
    elif mode == 5:
        print ("Ты выбрал возведение в степень")
        s = "возвести в степень"
    x = Decimal(input(f"Введите число, которое хотите  {s}: "))
    b = Decimal(input(f"Введите число, которое хотите  {s}: "))
    def sum(a,b,m):
        if m == 1:
            return a + b
        elif m == 2:
            return a - b
        elif m == 3:
            return a * b
        elif m == 4:
            return a / b
        elif m == 5:
            return a ** b
    print (sum(x,b,mode))
    
    n = str(input("Ты хочешь начать сначала?(напиши yes/no) "))
    if n in ["no","No","NO"]:
        print ("Bye")
        break


        
            

