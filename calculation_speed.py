from random import randint
from time import time

def light_calculation(choice1):
    right = 0
    for i in range(choice1):
        number1 = randint(1,100)
        number2 = randint(1,100)
        a = randint(1,2)
        if a == 1:
            print("Скільки буде:", number1, "+", number2,)
            reply = int(input())
            if reply == (number1 + number2):
                print("Правильна відповідь")
                right += 1
            else:
                print("Неправильна відповідь")
        elif a == 2:
            print("Скільки буде:", number1, "-", number2)
            reply = int(input())
            if reply == (number1 - number2):
                print("Правильна відповідь")
                right += 1
            else:
                print("Неправильна відповідь")
    return right

def normal_calculation(choice1):
    right = 0
    for i in range(choice1):
        a = randint(1,2)
        if a == 1:
            a = randint(1,2)
            if a == 1:
                a = randint(1,2)
                number1 = randint(1,20)
                number2 = randint(1,20)  
                print("Скільки буде:", number1, "*", number2,)
                reply = int(input())
                if reply == (number1 * number2):
                    print("Правильна відповідь")
                    right += 1
                else:
                    print("Неправильна відповідь")
            elif a == 2:
                number3 = number2 * number1
                print("Скільки буде:", number3, "/", number2)
                reply = int(input())
                if reply == number1:
                    print("Правильна відповідь")
                    right += 1
                else:
                    print("Неправильна відповідь")
        elif a == 2:
            a = randint(1,4)
            number1 = randint(1,250)
            number2 = randint(1,250)
            number3 = randint(1,250)
            if a == 1:
                print("Скільки буде:",number1 ,"+", number2, "-", number3)
                reply = int(input())
                if reply == (number1 + number2 - number3):
                    print("Правильна відповідь")
                    right += 1
                else:
                    print("Неправильна відповідь")
            elif a == 2:
                print("Скільки буде:",number1, "-", number2, "+", number3)
                reply = int(input())
                if reply == (number1 - number2 + number3):
                    print("Правильна відповідь")
                    right += 1
                else:
                    print("Неправильна відповідь")
            elif a == 3:
                print("Скільки буде:",number1 ,"-", number2, "-", number3)
                reply = int(input())
                if reply == (number1 - number2 - number3):
                    print("Правильна відповідь")
                    right += 1
                else:
                    print("Неправильна відповідь")
            elif a == 4:
                print("Скільки буде:",number1, "+", number2, "+", number3)
                reply = int(input())
                if reply == (number1 + number2 + number3):
                    print("Правильна відповідь")
                    right += 1
                else:
                    print("Неправильна відповідь")
    return right
    
def hard_calculation(choice1):
    right = 0
    for i in range(choice1):
        a = randint(1,3)
        if a == 1:
            a = randint(1,2)
            number1 = randint(1,50)
            number2 = randint(1,50)
            if a == 1:
                print("Скільки буде:", number1, "*", number2,)
                reply = int(input())
                if reply == (number1 * number2):
                    print("Правильна відповідь")
                    right += 1
                else:
                    print("Неправильна відповідь")
            elif a == 2:
                number3 = number2 * number1
                print("Скільки буде:", number3, "/", number2)
                reply = int(input())
                if reply == number1:
                    print("Правильна відповідь")
                    right += 1
                else:
                    print("Неправильна відповідь")
        elif a == 2:
            a = randint(1,4)
            number1 = randint(1,1000)
            number2 = randint(1,1000)
            number3 = randint(1,1000)
            if a == 1:
                print("Скільки буде:",number1 ,"+", number2, "-", number3)
                reply = int(input())
                if reply == (number1 + number2 - number3):
                    print("Правильна відповідь")
                    right += 1
                else:
                    print("Неправильна відповідь")
            elif a == 2:
                print("Скільки буде:",number1, "-", number2, "+", number3)
                reply = int(input())
                if reply == (number1 - number2 + number3):
                    print("Правильна відповідь")
                    right += 1
                else:
                    print("Непраельна відповідь")
            elif a == 3:
                print("Скільки буде:",number1 ,"-", number2, "-", number3)
                reply = int(input())
                if reply == (number1 - number2 - number3):
                    print("Правильна відповідь")
                    right += 1
                else:
                    print("Неправильна відповідь")
            elif a == 4:
                print("Скільки буде:",number1, "+", number2, "+", number3)
                reply = int(input())
                if reply == (number1 + number2 + number3):
                    print("Правильна відповідь")
                    right += 1
                else:
                    print("Непраельна відповідь")
        elif a == 3:
            a = randint(1,2)
            if a == 1:
                number1 = randint(1,50)
                print("Скільки буде:", number1, "в кубі")
                reply = int(input())
                if reply == (number1 ** 2):
                    print("Правильна відповідь")
                    right += 1
                else:
                    print("Неправильна відповідь")
            if a == 2:
                number1 = randint(1,30)
                number2 = number1 ** 2
                print("Корінь з", number2, "це?")
                reply = int(input())
                if reply == number1:
                    print("Правильна відповідь")
                    right += 1
                else:
                    print("Неправильна відповідь")
    return right
            
def clculaton_speed():                
    choice = input("Ви хочете пройти тест на швидку калькуляцію")
    if choice == "так":
        choice = input("Як ви хочете: 1-складність росте з часом, 2-самі хочетет вибрати складність")
        if "1" == choice:
            choice1 = int(input("Скільки прикладів ви бажаєте виконати:"))
            examples = choice1 // 3
            choice_rmndr = choice1 % 3
            examples_lght = examples
            examples_n = examples
            if choice_rmndr >= 1:
                examples_lght += 1
                choice_rmndr -= 1
            if choice_rmndr >= 1:
                examples_n += 1
            time1 = time()              
            print("Правильних відповідей", light_calculation(examples_lght) + normal_calculation(examples_n) + hard_calculation(examples) ,"з", choice1)          
            time2 = time()
            choice1 = float(choice1)
            time_calc = time2 - time1
            print("Середній час який ви потратили на один приклад:",round((time_calc/choice1),2))
            
        elif "2" == choice:
            choice = input("Виберіть складність прикладів: 1-легка, 2-середня, 3-складна")
            if choice == "1":
                choice1 = int(input("Скільки прикладів ви бажаєте виконати:"))
                time1 = time()
                print("Правильних відповідей", light_calculation(choice1), "з", choice1)
                time2 = time()
                choice1 = float(choice1)
                time_calc = time2 - time1
                print("Середній час який ви потратили на один приклад:",round((time_calc/choice1),2))
            elif choice == "2":
                choice1 = int(input("Скільки прикладів ви бажаєте виконати:"))
                time1 = time()
                print("Правильних відповідей", normal_calculation(choice1), "з", choice1)
                time2 = time()
                choice1 = float(choice1)
                time_calc = time2 - time1
                print("Середній час який ви потратили на один приклад:",round((time_calc/choice1),2))
            elif choice == "3":
                choice1 = int(input("Скільки прикладів ви бажаєте виконати:"))
                time1 = time()
                print("Правильних відповідей", hard_calculation(choice1), "з", choice1)
                time2 = time()
                choice1 = float(choice1)
                time_calc = time2 - time1
                print("Середній час який ви потратили на один приклад:",round((time_calc/choice1),2))
            else:
                print("Немає такого номера")
    elif choice == "ні":
        print("Так нашо ти сюда зайшов")
    else:
        print("Відповідь має бути так або ні")

clculaton_speed()