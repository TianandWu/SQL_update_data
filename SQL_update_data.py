import pymysql

#簡單理解一下調用，故沒有特別使用def
#創建連接
config = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456789",
    database="maplestory",
    charset="utf8",
    autocommit=True
)

#調用
config_use =config.cursor()

#show出有幾個表
table_name ="drop_data"
show_tables ="""show tables like '{}';""".format(table_name)  #SQL語法
show_table =config_use.execute(show_tables)
print(show_table)

#show影響的列表名稱
show_table_name =config_use.fetchall()
print(show_table_name)

#show裡面的資料有幾筆
select_name ="drop_data"
select_tables ="""select *from """+select_name+";"  #SQL語法
show_select_tables =config_use.execute(select_tables)
print(show_select_tables)

#迴圈列出資料看不到第一行cloums，補一下
column_names =[column[0] for column in config_use.description]
print(column_names)

#寫個迴圈show出資料
"""
show_select_name =config_use.fetchall()
for i in show_select_name:
    print(i)
"""

#假設對某個特定cloums做事情
cloums_name ="dropperid"

#新的值
new_value =2047

#觸發條件
condition_use =2084
condition ="{} = {}".format(cloums_name,condition_use)

#sql語句
use_change_cloums ="update {} set {} = {} where {};".format(table_name,cloums_name,new_value,condition_use)
#print(use_change_cloums)
show_use_change_cloums =config_use.execute(use_change_cloums)
show_all =config_use.fetchall()

#執行完後看看cloums的資料有沒有更改
use_cloums_name ="""select {} from {};""".format(cloums_name,select_name) #SQL語法
config_use.execute(use_cloums_name)

show_all =config_use.fetchall()
for i in show_all:
    print(i)