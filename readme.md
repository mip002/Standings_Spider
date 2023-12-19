# Standings Spider

爬取洛谷、Codeforces、AtCoder 的榜单。

## 使用方法

1. 进入 `luogu.py`/`codeforces.py`/`atcoder.py` 所在的目录，创建两个文件：`conf.json` 和 `users.csv`。
2. 运行 `luogu.py`/`codeforces.py`/`atcoder.py`
3. 程序会将爬取下来的用户数据，分比赛存储在同一目录下的几个 csv 文件中，第一列为每一个爬取到的用户名在 `users.csv` 中对应的编号，第二列为该用户的分数，第三列为该用户的排名。

- `conf.json` 用于存储需要爬取的比赛 id 和 cookie（仅洛谷需要 cookie），下面是一个例子：

```json
{
    "id": [147239, 141486],
    "cookie": "paste your cookie here"   
}
```

- `users.csv` 用于存储 要找的用户名，表格的第一列为用户名，第二列为用户编号（随便填一个）。下面是一个例子：

```csv
mip001,20
fsdhmbb,19
```
