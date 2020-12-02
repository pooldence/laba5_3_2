import stdiomask
alf="abcdefghijklmnopqrstuvwxyz"
one=input("Введите первое слово: ")
two=input("Введите второе слово: ")
three=input("Введите третье слово: ")
password=""
password+=alf[(alf.index(one[-1]) + 1)]
password+=alf[(alf.index(two[-1]) + 1)]
password+=alf[(alf.index(two[2]) - 1)]
if len(three)% 2 != 0:
    password+=alf[(alf.index(three[int(len(three)/2)])+5)]
else:
    if alf.index(three[len(three)//2])>alf.index(three[len(three)//2 -1]):
        password+=alf[(alf.index(three[len(three)//2]) - 1)]
    else:
        password+=alf[(alf.index(three[len(three)//2 -1]) - 1)]
if (len(three)+len(two))> 26:
    password+=alf[(((len(one)+len(two)))) % 26]
else:
    password+=alf[(len(one)+len(two))]
#проверка пароля
print(password)
#ввод скрытого пароля
userpassw=stdiomask.getpass()
if userpassw==password:
    print("Пароль верный")
else:
    print("Пароль неверный")
