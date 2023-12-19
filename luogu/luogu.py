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

# 从 conf.json 获取需爬取的比赛 id 和 cookie
with open('conf.json','r',encoding='utf-8') as f:
    content = f.read()
    
content_json=json.loads(content)

cookie=content_json['cookie']

for ii in range(len(content_json['id'])):
    contest_id=str(content_json['id'][ii])
    print("开始爬取比赛:",contest_id)
    # 网址
    url = "https://www.luogu.com.cn/fe/api/contest/scoreboard/"+contest_id
    # 请求头数据
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'referer': 'https://www.luogu.com.cn/contest/'+contest_id,
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                    '(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        'cookie': cookie
    }
    page=0
    rank=0

    # 循环 爬取每一页的内容
    while 1:
        
        rank=50*page
        page=page+1
        print("    已爬取至第",page,"页")
        
        # 构造请求参数
        params = {
            'page': page
        }

        # 通过 get 方法请求数据
        response = requests.get(url, headers=headers, params=params)

        if response.status_code!=200:
            print("Error: 获取数据失败，状态代码",response.status_code)
            break


        response.encoding = 'utf-8'

        data_json = json.loads(response.text)

        test=data_json['scoreboard']['result']

        ans=[]

        if len(test)==0:
            break

        for i in range(len(test)):
            if test[i]['user']['name'] in user_name:
                ans.append([user_id[user_name.index(test[i]['user']['name'])], test[i]['score'], rank+i+1])

        with open('lg'+contest_id+'.csv', 'a', newline='', encoding='utf-8') as fp:
            csv_writer = csv.writer(fp)
            csv_writer.writerows(ans)

        time.sleep(0.5) # 防止被 kkk ban 掉



