import os
import sys
import json
import location
def xb_json():             #配置生成json
    if not os.path.exists('./config.json'):
        data = {
            'sqlite': {
                '签到': 'CREATE TABLE qd (user varchar (255),积分 int,日期 varchar (255),天数 int)',
                '抽签': 'CREATE TABLE cq (user varchar (255),id int,日期 varchar (255))',
                'web': 'CREATE TABLE web(name varchar (255),url varchar(255))',
                '签': 'CREATE TABLE sgin (id int , 签诗 varchar (255), 解签 varchar(255))',
                '好感': 'CREATE TABLE favorability (user varchar (255), 好感度 int)'
            },
            'mysql': {
                'host': '127.0.0.1',
                'user': 'root',
                'password': 'root',
                '创建数据库': 'CREATE DATABASE QQAI',
                '数据库': 'QQAI',
                '建表':
                    {
                        '签到': 'CREATE TABLE qd (user VARCHAR(255) , 积分 INT, 日期 VARCHAR(255) , 天数 INT)',
                        '抽签': 'CREATE TABLE cq (user VARCHAR(255)  ,id INT, 日期 VARCHAR(255))',
                        'web': 'CREATE TABLE web (name VARCHAR (255) , url VARCHAR(255))',
                        '签': 'CREATE TABLE sgin (id INT , 签诗 VARCHAR (255) , 解签 VARCHAR(255))',
                        '好感': 'CREATE TABLE favorability (user VARCHAR (255) , 好感度 INT)'
                    }
            }
        }
        with open('config.json', 'w', encoding="UTF-8") as config:
            json.dump(data, config, indent=4, ensure_ascii=False)
        print('\033[33mjson文件生成功请进行配置\033[0m')
        sys.exit(0)
    else:
        return True
def DataJson():
    if os.path.exists(str(location.path[0]+'\\config.json')):
        with open(str(location.path[0]+'\\config.json'),encoding="UTF-8") as jo:
            data = json.load(jo)
    return data
