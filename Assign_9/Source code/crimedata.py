################################################################################
## CS 101 Lab
## Program Lab Week 10
## Date : Fall 2021
## Name: Tin Nguyen
## Email: tdnng2@umsystem.edu
##
##
##
##
##
##
##
################################################################################


import csv  

def month_from_number(n):
    calendar = {
        '1':'January',
        '2':'February',
        '3':'March',
        '4':'April',
        '5':'May',
        '6':'June',
        '7':'July',
        '8':'August',
        '9':'September',
        '10':'October',
        '11':'November',
        '12':'December'
    }
    return calendar[str(n)]

def read_in_file(fname):
    data = []
    try:
        f = open(fname,'r',encoding='UTF-8')
    except:
        return -1
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
    f.close()
    return data

def create_dict_column(data,name):
    dict_ex = {}
    n = data[0].index(name)
    for sub in data[1:]:
        if sub[n]in dict_ex:
            dict_ex[sub[n]]+=1
        else:
            dict_ex[sub[n]]=1
    return dict_ex

def create_reported_date_dict(data):
    return create_dict_column(data,'Reported_Date')

def create_offense_dict(data):
    return create_dict_column(data,"Offense")

def create_reported_month_dict(data):
    dict_ex = {}
    for sub in data[1:]:
        temp = sub[1][0:2]
        if temp in dict_ex:
            dict_ex[temp]+=1
        else:
            dict_ex[temp]=1
    return dict_ex

def create_offense_by_zip(data):
    dict_ex={}
    for sub in data[1:]:
        temp = sub[7]
        if temp in dict_ex:
            temp_dict = dict_ex[temp]
            if sub[13] in temp_dict:
                temp_dict[sub[13]]+=1
            else:
                temp_dict[sub[13]] = 1
        else:
            dict_ex[temp] = {sub[13]:1}
    return dict_ex

    
            

def main():
    while(True):
        fname = input("Enter the name of the crime data file ==> ")
        data = read_in_file(fname)
        if(data==-1):
            print("Could not find the file specified. "+fname+" not found")
        else:
            break
    month = create_reported_month_dict(data)
    print(month)
    mx = max(month,key=month.get)
    print("The month with the highest # of crimes is "+month_from_number(mx)+" with "+str(month[mx])+" offenses")
    offense = create_offense_dict(data)
    mx = max(offense,key=offense.get)
    print("The offense with the highest # of crimes is "+mx+" with "+str(offense[mx])+" offenses")
    offense = create_offense_by_zip(data)
    print()
    while(True):
        off = input("Enter an offense : ")
        if off not in offense:
            print("Not a valid offense, please try again")
        else:
            break
    print(off+" offense by Zip Code")
    print("Zip Code\t\t\t# Offenses")
    print("==========================================")
    for k,v in offense[off].items():
        print(k+"\t\t\t\t\t"+str(v))

if __name__ == "__main__":
    main()

