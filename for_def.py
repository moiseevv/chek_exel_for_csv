import ors_ready
import os
def check_error_fn(znach, item_zn):
    if znach == 0:
        print(f" ОШИБКА !!! -- Для элемента  {item_zn} не найдено .csv файла")
        print(" P.s. Cопоставление производилось по 1-м десяти символам в названии файла")
    if znach > 1:
        print(f" ОШИБКА !!! -- Для файла {item_zn} найдено несколько соответствий файлов .csv ")
    # Здесь бы еще панику завершения сделать, хотя может и не нужно . так как оставшиеся отработают нормально, но тогда еще try на открытие

def proverka_kovo_failov(mas_fls):
    for kl in mas_fls:
        str_etalon = kl[:10]
        check_etalon = 0
        for jr in mas_fls:
            if str_etalon in jr:
                check_etalon+=1
        if check_etalon != 1:
            print(" ОШИБКА !!!   Есть несколько файлов с одинаковыми первыми 10-ти символами пример -", kl)


def start():
    mas_csv = []
    mas_exel = []
    mas_sravn =[]

    list_all_files = os.listdir()
    for fl in list_all_files:
        if ('.csv' in fl) or ('.CSV' in fl):
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
        chek_error = 0;
        for item_csv in mas_csv:
            str_sravnenij = item_xl[:10]
            #print(str_sravnenij)
            if str_sravnenij in item_csv:
                mas_sravn.append((item_csv,item_xl))
                chek_error+=1
        check_error_fn(chek_error,item_xl)
        chek_error = 0
        print("-"*100)
    print("     Массив сравнения")
    print("   ")
    for i in mas_sravn:
        print(i[0], " #сопоставлен_с# ", i[1])
    return mas_sravn



mas_i = start()

for item in mas_i:
    ors_ready.use_files(item[0], item[1])