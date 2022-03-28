# coding: utf8

import pandas as pd
import numpy as np
import csv
from datetime import datetime as dt

def use_files(s1_path,e1_path):
    print("-"*100)
    c = 0
    print("Загрузка csv      -  ",s1_path)
    # s1_path = "УКЖХ Октябрьского района_202203_постфикс.CSV"
    print ("Загрузка exel    -  ", e1_path)
    # e1_path = "УКЖХ Октябрьского района_202203_постфикс_20220324_проверено_Оля.xlsx"

    print("   ")
    print("Время запуска: ", dt.now())
    print("   ")
    s1 = pd.read_csv(s1_path, sep=';', engine='python')



    e1 = pd.read_excel(e1_path, dtype={'LC':float})

    list_zn = e1.columns.tolist()
    nomer_stolbca_komment = 0
    for i in range(0,len(list_zn)):
        if "ейств" in list_zn[i]:
            nomer_stolbca_komment = i
            print("Индекс для поля действия ", nomer_stolbca_komment)
    if nomer_stolbca_komment == 0:
        print("Ошибка !!! Так и не смогли определить в какой колонке написано действие")


    #nomer_stolbca_komment = 19  # поле действия - по хорошему прописать бы его авто определение
    nomer_st_dopls = nomer_stolbca_komment + 2  # номер поля где стоит новый лицевой, есть if на поле действия

    #e1 = pd.read_excel(e1_path)
    e1 = e1.fillna(0)
    e1 = e1.astype({'LC' : np.int64})
    #e1 = pd.read_csv('ОРС_Остальное_для проверки.csv', sep=';', engine='python')



    l = e1.columns[11]

    s_sort = s1.sort_values(by=l)
    e_sort = e1.sort_values(by=l)
    #h = s_sort.copy()
    lf = list()



    k = len(s_sort)
    kn = 0


    for i in range(0, k):
        #print("uuu = ", s_sort.iat[i,11])
        #print("1 e_sort.iat[i,nomer_stolbca_komment]  = ", e_sort.iat[i,nomer_stolbca_komment])
        #print("2 e_sort.iat[i,nomer_stolbca_komment+1]  = ", e_sort.iat[i,nomer_stolbca_komment+1])
        #print("3 e_sort.iat[i,nomer_stolbca_komment-1]  = ", e_sort.iat[i,nomer_stolbca_komment-1])
        if (e_sort.iat[i,nomer_stolbca_komment] == 'запрет на обмен'):  # u=20
            if ( s_sort.iat[i,11] == e_sort.iat[i,11] ):
                lf.append(i)
                #print("i = ", i)
                #print("lf", lf)
                #print("1 = ", s_sort.iat[i,11])
                #print("2 = ", e_sort.iat[i,11])

                c = c+1

            else:
                print("ОШИБКА!!! Строки не совпадают!!!")
                print("сравнивание значение в csv = ", s_sort.iat[i,11])
                print("сравнивание значение в xlsx = ", e_sort.iat[i,11])
                #print("i = ", i)
                break
        if ('внести' in str(e_sort.iat[i,nomer_stolbca_komment])):
            kn = kn +1
            #print('Успех на ВНЕСТИ', kn)
            s_sort.iat[i, 12] = e_sort.iat[i, nomer_st_dopls]
    print('Успех на ВНЕСТИ ,    количество строк =', kn)


    '''
            for r in range(0,len(s1)):
                if (s1.iat[r, 6] == iskom_ls):
                    print("Номер лицевого в ОРС", s1.iat[i, 6])
                    #print(h1)
                    h1 = h1.drop([r])
                    break
    '''

    print("Количество удаленных строк = ", c)
    #print("Длинна lf", len(lf))
    if (c == len(lf)):
        #print("lf", lf)
        s_sort2 = s_sort.reset_index()
        s_sort2.drop(lf, inplace=True)
        sl = len(s_sort2)
        raz = k-sl
        print("В таблице записей до обработки= ", k, "   Записей на удаление = ",c, "   Записей после удаленния=",sl, "   Разница:", raz)

    else:
        print("ДИВНАЯ ОШИБКА!!! 1 , длина массива на удаление не совпала с количеством записей 'запрет на обмен' ")

    g = dt.now()
    y = str(g.year)
    da = g.month
    if da < 10:
        da = str(da)
        da = '0'+da
    da = str(da)

    #h.to_csv(f"ORS_{y}{da}.csv", sep=";", index=False, header=True, encoding="ansi")

    if (raz == c):

        if  '.csv' in s1_path:
            jj = s1_path.replace('.csv','load.csv')
        else:
            jj = s1_path.replace('.CSV','load.csv')
        #print(jj)
        #print("s_sort2['LC']")
        #print(s_sort2['LC'])
        s_sort2['LC'] = s_sort2['LC'].fillna(0)
        s_sort2 = s_sort2.astype({'LC' : np.int64})
        s_sort2['LC'].replace(0,'', inplace = True)
        s_sort2 = s_sort2.drop(['index'], axis = 1)
        s_sort2.to_csv(jj,index=False, sep=";",  quoting=csv.QUOTE_NONE, header=True, encoding="ansi")

    else:
        print("Не дивная ОШИБКА!!!")
        #8357, 8373, 23942, 26101, 27427, 28655, 30930,

    print("   ")
    print("Время завершения: ", g)
