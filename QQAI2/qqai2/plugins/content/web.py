import requests
from QQAI2.qqai2.plugins.content.data import *
from QQAI2.qqai2.plugins.content.analysis import *
def deposit(data: str, command='')->str:
    OriginalData = AnalysisNews(data, command=command)
    DANGER = r'(!)|(-- -)|(#)|(or)|(and)|(slelct)|(\')|(FROM)|(union)|(ORDER)'
    testing = re.search(DANGER, OriginalData[0], re.I)
    try:
        if testing == None:
                if isinstance(OriginalData, list) and len(OriginalData) == 2:
                    OriginalData[1] = OriginalData[1].replace('http://', '').replace('https://', '')
                    # sql
                    if config.yml_DATA.data == 'sqlite' or config.yml_DATA.data == 'mysql':
                        print('ok')
                        sql = Data('select * from web')
                        # 初次存入
                        if len(sql) == 0:
                            Return = requests.get('http://'+OriginalData[1]).status_code
                            print(Return)
                            if Return == 200:                                          # 判断网址是否存在
                                Data('insert into web (name,url) values ("%s","%s")' % (OriginalData[0], OriginalData[1]))
                                print(Data('select * from web'))
                                return '收录成功'
                            else:
                                return '小白检测不到该网站≧ ﹏ ≦'
                        # 二次存入
                        else:
                            print('ok')
                            name = []
                            url = []

                            for i in sql:                         # 获取数据库
                                name.append(i[0])
                                url.append((i[1]))
                            if not OriginalData[0] in name and not OriginalData in url:
                                Return = requests.get('http://' + OriginalData[1]).status_code
                                print(Return)
                                if Return == 200:                         #判断网址是否可以访问
                                    Data('insert into web (name,url) values ("%s","%s")' % (OriginalData[0], OriginalData[1]))
                                    print(Data('select * from web'))
                                    return '收录成功'
                                else:
                                    '小白检测不到该网站≧ ﹏ ≦'
                            else:
                                return '小白已收录过相关网址'
                    # json
                    elif config.yml_DATA.data == 'json':
                        DATA = Data(ReadWrite='r')                   # 提取数据
                        if len(DATA['web']['name']) == 0:            # 初次存入
                            Rrturn = requests.get('http://'+OriginalData[1]).status_code
                            if Rrturn == 200:                        # 判断网址是否存在
                                DATA['web']['name'].append(OriginalData[0])
                                DATA['web']['url'].append(OriginalData[1])
                                Data(DATA, ReadWrite='w')            # 存入
                                print(DATA['web']['name'])
                                print(DATA['web']['url'])
                                return '收录成功'
                            else:
                                return '小白检测不到该网站≧ ﹏ ≦'
                        elif not OriginalData[0] in DATA['web']['name'] and OriginalData[1] in DATA['web']['url']:    # 二次存入
                            Rrturn = requests.get('http://' + OriginalData[1]).status_code
                            if Rrturn == 200:                     # 判断网址是否存在
                                DATA['web']['name'].append(OriginalData[0])
                                DATA['web']['url'].append(OriginalData[1])
                                Data(DATA, ReadWrite='w')         # 存入
                                print(DATA['web']['name'])
                                print(DATA['web']['url'])
                                return '收录成功'
                            else:
                                return '小白检测不到该网站≧ ﹏ ≦'
                        else:
                            return '小白已收录过相关网址'
                else:
                    return '参数不正确!'
        else:
            return '小白判断可能存在SQL注入威胁程序终止,(是小白做错什么了)'
    except:
        return '程序异常终止'


# 网址查询
def web(data:str,command='') -> str:
    OriginalData = data[len(command):].replace(' ','')
    print(OriginalData)
    DANGER = r'(!)|(-- -)|(#)|(or)|(and)|(slelct)|(\')|(FROM)|(union)|(ORDER)'
    testing = re.search(DANGER, OriginalData, re.I)
    print(testing)
    if testing == None:
        # sql
        if config.yml_DATA.data == 'sqlite' or config.yml_DATA.data == 'mysql':
            if len(Data('select * from web')) != 0:
                DATA = Data(f'select * from web where name = "{OriginalData}"')
                print(len(DATA))
                if len(DATA) != 0:
                    return '您要查询的网站网址为：'+DATA[0][1]
                else:
                    return "小白还没有收录过相关网址您可以使用【入库】命令帮小白收录吗(●'◡'●)"
            else:
                return "小白还没有收录过网址您可以使用【入库】命令帮小白收录吗(●'◡'●)"
        # json
        elif config.yml_DATA.data == 'json':
            DATA = Data(ReadWrite='r')
            if len(DATA['web']['name']) != 0:
                if OriginalData in DATA['web']['name']:
                    Indexes = DATA['web']['name'].index(OriginalData)
                    return '您要查询的网站网址为：'+DATA['web']['url'][Indexes]
                else:
                    return "小白还没有收录过相关网址您可以使用【入库】命令帮小白收录吗(●'◡'●)"
            else:
                return "小白还没有收录过网址您可以使用【入库】命令帮小白收录吗(●'◡'●)"
    else:
        return '小白判断可能存在SQL注入威胁程序终止,(是小白做错什么了)'
