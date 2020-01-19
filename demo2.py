#字典
'''
a = {}  #key-value, 键值对

a = {
    "name":"张三",
    "age": 15,
    "job":"三轮车"
}
print(a)
输出 {'name': '张三', 'age': 15, 'job': '三轮车'}



a = {
    "name":"张三",
    "age": 15,
    "job":"三轮车"
}
a["name"] = "李四"    #将name的值修改为李四
print(a)
输出{'name': '李四', 'age': 15, 'job': '三轮车'}



a = {
    "name":"张三",
    "age": 15,
    "job":"三轮车"
}
a["aihao"] = "唱跳arp"   #新增键值对
print(a)    
输出 {'name': '张三', 'age': 15, 'job': '三轮车', 'aihao': '唱跳arp'}


a = {
    "name":"张三",
    "age": 15,
    "job":"三轮车"
}

del a["name"]    删除 键值对
print(a)
输出 {'age': 15, 'job': '三轮车'}



a = {
    "name":"张三",
    "age": 15,
    "job":"三轮车"
}
a.update(name="l")     #修改值
print(a)
输出 {'name': 'l', 'age': 15, 'job': '三轮车'}



a = {
    "name":"张三",
    "age": 15,
    "job":"三轮车"
}
a.update(name11="aa")  #输入不存在的键值对就会增加进去
print(a)
输出{'name': '张三', 'age': 15, 'job': '三轮车', 'name11': 'aa'}


a = {
    "name":"张三",
    "age": 15,
    "job":"三轮车"
}
print(a.get("name"))
print(a["name"])
#输出 张三
#    张三

a = {
    "name":"张三",
    "age": 15,
    "job":"三轮车"
}
print(a.get("msg"))   #输入存在的时候两个效果一样 
print(a("msg"))       #输入的值不存在 那么 print(a.get("msg"))  会提示为NOne(空)
                      # print(a("msg"))会报错  
'''
