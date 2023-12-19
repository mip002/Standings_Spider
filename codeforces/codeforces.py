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
    contest_id=str(content_json['id'][ii])
    print("开始爬取比赛:",contest_id)
    url = "https://codeforces.com/api/contest.standings"

    params = {
        'contestId': contest_id,
        # 排名从 1 开始
        'from': 1,
        #'showUnofficial': 'true'
    }

    response=requests.get(url,params=params)

    if response.status_code!=200:
            print("Error: 获取数据失败，状态代码",response.status_code)
            break
    
    response.encoding = 'utf-8'

    data_json = json.loads(response.text)

    test=data_json['result']['rows']

    ans=[]

    for i in range(len(test)):
        if test[i]['party']['members'][0]['handle'] in user_name:
             ans.append([user_id[user_name.index(test[i]['party']['members'][0]['handle'])],test[i]['points'],test[i]['rank']])
    
    with open('cf'+contest_id+'.csv', 'a', newline='', encoding='utf-8') as fp:
            csv_writer = csv.writer(fp)
            csv_writer.writerows(ans)