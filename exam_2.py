# Напишите функцию, которая проверяет: является ли слово палиндромом

def polindrom(slovo):
    revers_slovo= slovo[::-1]
    #print(slovo, revers_slovo)
    if slovo == revers_slovo:
        print(f'Слово {slovo} является палиндромом')
    else:
        print(f'Слово {slovo} не является палиндромом')

polindrom('molocolаom')
polindrom('molocolom')