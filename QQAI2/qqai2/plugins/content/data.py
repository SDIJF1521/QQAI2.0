import json
import pymysql
import sqlite3
import config.yml_DATA
import config.config_json
def Data(data=None, ReadWrite=None):
    """

    :param data: sql语句或者json数据默认为空
    :param ReadWrite: json读写选项（w/r）
    :return:
    """

    if config.yml_DATA.data == 'sqlite':
        conn = sqlite3.connect('./qqai2/plugins/data/data.db')         #连接sqlite数据库
        cursor = conn.cursor()                                         #创建游标对象
        sqldata = cursor.execute(data)
        conn.commit()                                                  #提交
        return sqldata.fetchall()
    if config.yml_DATA.data == 'mysql':
        conn = pymysql.connect(host=str(config.config_json.DataJson()['mysql']['host']),
                               user=config.config_json.DataJson()['mysql']['user'],
                               password=config.config_json.DataJson()['mysql']['password'],
                               database=config.config_json.DataJson()['mysql']['数据库'])
        cursor = conn.cursor()
        cursor.execute(data)
        conn.commit()
        return cursor.fetchall()
    elif config.yml_DATA.data == 'json' and ReadWrite == 'r':
        with open('./qqai2/plugins/data/data.json', 'r',encoding='UTF-8') as f:
            return json.load(f)
    elif config.yml_DATA.data == 'json' and ReadWrite == 'w':
        with open('./qqai2/plugins/data/data.json', 'w', encoding="UTF-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
# 欢迎语功能依赖
def GroupingTestingFile(data=None, ReadWrite=None):
    """

    :param data: 内容
    :param ReadWrite: 存入（w）&读取(r)
    :return:
    """
    if ReadWrite == 'r':
        with open('./qqai2/plugins/data/GroupingTesting.json', 'r', encoding='UTF-8') as f:
            reverse_back=json.load(f)
            return reverse_back
    elif ReadWrite == 'w':
        with open('./qqai2/plugins/data/GroupingTesting.json', 'w', encoding="UTF-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
# 商店功能依赖
def store_change(data=None, ReadWrite=None):
    """

    :param data: 内容
    :param ReadWrite: 存入（w）&读取(r)
    :return:
    """
    if ReadWrite == 'r':
        with open('./qqai2/plugins/data/store.json', 'r', encoding='UTF-8') as f:
            reverse_back=json.load(f)
            return reverse_back
    elif ReadWrite == 'w':
        with open('./qqai2/plugins/data/store.json', 'w', encoding="UTF-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
def knapsack_deposit(data=None, ReadWrite=None):
    """
    :param data: 内容
    :param ReadWrite: 存入（w）&读取(r)
    :return:
    """
    if ReadWrite == 'r':
        with open('./qqai2/plugins/data/knapsack.json', 'r', encoding='UTF-8') as f:
            reverse_back=json.load(f)
            return reverse_back
    elif ReadWrite == 'w':
        with open('./qqai2/plugins/data/knapsack.json', 'w', encoding="UTF-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)