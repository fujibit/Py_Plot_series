
import os
import csv
import pandas as pd
import string
import openpyxl
from datetime import date
from datetime import datetime
from datetime import timedelta


def read_data(file):
    file_obj=open(file,'r',encoding='utf8',newline='')
    reader_obj=csv.reader(file_obj,delimiter=',')
    data=list(reader_obj)
    return(data)

def write_list(file,listx):
    file_obj=open(file,'w',encoding='utf8',newline='')
    writer_obj=csv.writer(file_obj)
    writer_obj.writerows(listx)

def list_sum(l):
    summ=0
    for i in range(len(l)):
        summ=summ+float(l[i])
    return(summ)

def list_sum_space(l):
    summ = 0
    for i in range(len(l)):
        try:
            k = float(l[i])
            if type(k) is float:
                summ = summ + k
            else:
                pass
        except:
            pass
    return(summ)

def list_sum_space_xl(l):
    summ = 0
    for i in range(len(l)):
        try:
            k = float(str(l[i]).replace("(","").replace(")","").replace(",","").replace(" ",""))
            if type(k) is float:
                summ = summ + k
            else:
                pass
        except:
            pass
    return(summ)

def convert_to_csv(file,file_w):
    read_file=pd.read_excel(file)
    read_file.to_csv(file_w,encoding='utf-8',index=False)

def path_edit(s):
    p=s.replace("\\","//")
    return(p)

def today():
    today = date.today()
    return(today)

def now():
    now = datetime.now()
    return(now)

def date_format_common(datee):
    
    a = datee.split("-")
    
    m = a[0]
    n = a[1]
    p = a[2]
    
    dict_month = {1:"Jan",
                  2:"Feb",
                  3:"Mar",
                  4:"Apr",
                  5:"May",
                  6:"Jun",
                  7:"Jul",
                  8:"Aug",
                  9:"Sep",
                  10:"Oct",
                  11:"Nov",
                  12:"Dec"
                  }

    if n in "01234567891011":
        x = int(n)
        y = dict_month[x]
        z = y + "-" + p + "," + m
        return(z)
    else:
        pass

def div_error(x,y):
    try:
        r = x/y
    except:
        r = 0

    return(r)

def date_num(date): # yyyy-mm-dd
    m = date.split("-")
    a = m[0]
    b = m[1]
    c = m[2]
    s = a+b+c
    n = int(s)
    return(n)

def sum_list_array_n(l,n):
    s = list_sum_space_xl([ i[n] for i in l])
    return(s)
    
def average_list_array_n(l,n):
    ll = [ i[n] for i in l]
    s = sum(ll)
    n = len(ll)
    a = div_error(s,n)
    return(a)

def ratio_list_array_n(l,n1,n2):
    
    f1 = [ i[n1] for i in l]
    f2 = [ i[n2] for i in l]
    
    s1 = list_sum_space_xl(f1)
    s2 = list_sum_space_xl(f2)
    
    ratio = div_error(s1,s2)
    
    return(ratio)

def list_str_to_num(l):
    l_n = []
    for i in range(len(l)):
        a = l[i]
        b = a.isdigit()
        if b == True:
            a = int(float(l[i]))
            l_n.append(a)
        else:
            l_n.append(0)
    return(l_n)
        
def dir_list(dir_path, type_file, type_null, tag_date, tag_month, tag_year, tag_group):
    path_raw_read = dir_path
    path_read = path_edit(path_raw_read)
    dir_list_x = os.listdir(path_read)
    l = []
    for x in dir_list_x:
        if type_file in x and type_null not in x and tag_date in x and tag_month in x and tag_year in x and tag_group in x:
            a = path_read + "//" + x
            l.append([a])
    return(l)

def list_build(l,s,e):
    for i in range(len(l)):
        a = s + l[i] + e
        return(a)
    
def list_read(l):
    for i in range(len(l)):
        print(l[i])

def gen_attribute(l):
    for i in range(len(l)):
        a = l[i].replace(" ", "_")
        b = a + " = data[row][" + str(i) + "]"
        c = b.lower()
        print(c)
