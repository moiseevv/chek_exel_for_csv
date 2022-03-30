import ors_ready
import os
from datetime import datetime as dt

nachalo = 0
kolsimvolov = nachalo + 20

def creat_direction(name_direction):
    if not os.path.isdir(name_direction):
        os.mkdir(name_direction)

def check_error_fn(znach, item_zn):
    if znach == 0:
        print(f" ОШИБКА !!! -- Для элемента  {item_zn} не найдено .csv файла")
        print(f" P.s. Cопоставление производилось по 1-м {kolsimvolov} символам в названии файла")

        ors_ready.creat_direction("no_find_csv")
        os.replace(item_zn, f"no_find_csv/{item_zn}")

        print(f"Перемещен файл {item_zn} в директорию - no_find_csv ")
    if znach > 1:
        print(f" ОШИБКА !!! -- Для файла {item_zn} найдено несколько соответствий файлов .csv ")
    # Здесь бы еще панику завершения сделать, хотя может и не нужно . так как оставшиеся отработают нормально, но тогда еще try на открытие

def proverka_kovo_failov(mas_fls):
    for kl in mas_fls:
        str_etalon = kl[nachalo:kolsimvolov]
        check_etalon = 0
        for jr in mas_fls:
            if str_etalon in jr:
                check_etalon+=1
        if check_etalon != 1:
            print(f" ОШИБКА !!!   Есть несколько файлов с одинаковыми первыми {kolsimvolov}-ти символами пример -", kl)


def start():
    mas_csv = []
    mas_exel = []
    mas_sravn =[]

    list_all_files = os.listdir()
    for fl in list_all_files:
        if ('.csv' in fl) or ('.CSV' in fl):
            if 'load' not in fl:
                mas_csv.append(fl)
        if ('.xlsx' in fl) and ("~" not in fl):
            mas_exel.append(fl)
    # print(" Массив csv")
    # print(mas_csv)
    # print(" Массив xlsx")
    # print(mas_exel)
    proverka_kovo_failov(mas_csv)
    proverka_kovo_failov(mas_exel)
    for item_xl in mas_exel:
        chek_error = 0
        for item_csv in mas_csv:
            str_sravnenij = item_xl[nachalo:kolsimvolov]
            #print(str_sravnenij)
            if str_sravnenij in item_csv:
                mas_sravn.append((item_csv,item_xl))
                chek_error+=1
        check_error_fn(chek_error,item_xl)
        chek_error = 0
        print("-"*20)
    print("     Массив сравнения")
    print("   ")
    for i in mas_sravn:
        print(i[0], " #сопоставлен_с# ", i[1])
    return mas_sravn



mas_i = start()

for item in mas_i:
    ors_ready.use_files(item[0], item[1])