## Words
## Wanyue Zhai

import pandas as pd
import numpy as np
import random


def main():
    sn = input('请输入sheet名: ')
    data = pd.read_excel(r'./单词.xlsx',sheet_name = sn)

    df = pd.DataFrame(data, columns = ['English','Translation'])

    df1 = df.sample(n = len(df), replace = False)

    mode = input("请选择类型：\n A. 填词 \t B. 选择 \n 您的选择：")

    if (mode == 'A') or (mode == 'a'):
        mode_A(df1)

    elif (mode =='B') or (mode == 'b'):
        mode_B(df1)


def mode_A(df1):
    for i in range(len(df1)):
        print('\n')
        print(df1.iloc[i,0])
        ans = input('Translation:')
        if (ans == df1.iloc[i,1]):
            print('correct')
        else:
            print('incorrect')
            print('Correct answer is:', df1.iloc[i,1])
    return

def mode_B(df1):
    wrong_list = {}
    for i in range(len(df1)):
        print('\n')
        print(i+1,'out of',len(df1))
        print('--------------')
        print(df1.iloc[i,0])
        df_trans = df1.sample(n = 3, replace = False)
        correct_trans = df1.iloc[i,1]
        trans = [correct_trans]
        
        false_trans = df_trans.iloc[:,1]
        for ftrans in false_trans:
            trans.append(ftrans)
        random.shuffle(trans)
        trans_dict = {}
        trans_dict['a'] = trans[0]
        trans_dict['b'] = trans[1]
        trans_dict['c'] = trans[2]
        trans_dict['d'] = trans[3]
        
        print('A.'+trans[0]+'\nB.'+trans[1],'\nC.'+trans[2],'\nD.'+trans[3])
        ans = input('Answer: ')
        
        ans = ans.lower()

        if trans_dict[ans] == correct_trans:
            print('correct')
        else:
            wrong_list[df1.iloc[i,0]] = correct_trans
            print('incorrect')
            print('Correct answer is:', correct_trans)
            
    
    for key,value in wrong_list.items():
        print('\n')
        print('Wrong list')
        print(key)
        df_trans = df1.sample(n = 3, replace = False)
        correct_trans = value
        trans = [correct_trans]
        
        false_trans = df_trans.iloc[:,1]
        for ftrans in false_trans:
            trans.append(ftrans)
        random.shuffle(trans)
        trans_dict = {}
        trans_dict['a'] = trans[0]
        trans_dict['b'] = trans[1]
        trans_dict['c'] = trans[2]
        trans_dict['d'] = trans[3]
        
        print('A.'+trans[0]+'\nB.'+trans[1],'\nC.'+trans[2],'\nD.'+trans[3])
        ans = input('Answer: ')
        
        while (trans_dict[ans] != correct_trans):
            print('\n')
            print(key)
            nans = input('Answer: ')
            if (nans == correct_trans):
                break
            else:
                print('incorrect')
                print('Correct answer is:', correct_trans)
            
        print('correct')
    print('\n')
    print('Accuracy:',(len(df1)-len(wrong_list))/len(df1))
    return


main()     
