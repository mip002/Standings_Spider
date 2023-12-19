# 导入模块
import requests
import time
import json
import csv

# 从 users.csv 获取需爬取的人的信息
user_name=[]
user_id=[]
with open('users.csv','rt') as f:
    cr=csv.reader(f)
    for row in cr:
        user_name.append(row[0])
        user_id.append(row[1])

# 从 conf.json 获取需爬取的比赛 id
with open('conf.json','r',encoding='utf-8') as f:
    content = f.read()
    
content_json=json.loads(content)


for ii in range(len(content_json['id'])):
    contest_id=content_json['id'][ii]
    print("开始爬取比赛:",contest_id)
    url = "https://atcoder.jp/contests/"+contest_id+"/results/json"


    response=requests.get(url)

    if response.status_code!=200:
            print("Error: 获取数据失败，状态代码",response.status_code)
            break
    
    response.encoding = 'utf-8'

    test = json.loads(response.text)


    ans=[]

    for i in range(len(test)):
        if test[i]['UserName'] in user_name:
             ans.append([user_id[user_name.index(test[i]['UserName'])],test[i]['Performance'],test[i]['Place']])
    
    with open('at_'+contest_id+'.csv', 'a', newline='', encoding='utf-8') as fp:
            csv_writer = csv.writer(fp)
            csv_writer.writerows(ans)