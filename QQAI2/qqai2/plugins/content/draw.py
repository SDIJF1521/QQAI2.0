import random
import datetime
from config import yml_DATA
from QQAI2.qqai2.plugins.content.data import *
from QQAI2.qqai2.plugins.content.analysis import *
tobay = datetime.date.today()
#存签功能
def save(data:str):
    # 参数分离
    dATA = AnalysisNews(data)
    if isinstance(dATA, list) and len(dATA) ==2:
        sign = dATA[0]
        meaning = dATA[1]
        #sql
        if yml_DATA.data == 'sqlite' or yml_DATA.data == 'mysql':
            DANGER = r'(!)|(-- -)|(#)|(or)|(ande)|(slelct)(from)|(union)|(ORDER)'
            testing = re.search(DANGER, sign, re.I)
            testing1 = re.search(DANGER, meaning, re.I)
            if testing == None and testing1 == None:
                DataId = Data('select id from sgin')
                print(DataId)
                DataContent = Data('select * from sgin')
                print(DataId)
                if len(DataId) == 0:
                    print(sign,meaning)
                    print(Data('select 解签 from sgin'))
                    Data('insert into sgin (id,签诗,解签) values (%d,"%s","%s")' % (1, sign, meaning))
                    sqldata = (Data('select * from sgin'))
                    return sqldata
                else:
                    lot = []
                    idea = []
                    for i in DataContent:
                        lot.append(i[1])
                        idea.append(i[2])
                    if not sign in lot and not meaning in idea:
                        print(DataId)
                        Data('insert into sgin (id,签诗,解签) values (%d,"%s","%s")'% (DataId[len(DataId)-1][len(DataId[0])-1]+1, sign, meaning))
                        print(Data('select * from sgin')[0])
                        return [Data('select * from sgin')[0]]
                    else:
                        return '小白检测到该内容已存在！'
            else:
                return '小白判断可能存在SQL注入威胁程序终止,(是小白做错什么了)'
        #json
        if yml_DATA.data == 'json':
            print('ok')
            data = Data(ReadWrite='r')
            if len(data['sgin']['id']) == 0:
                data['sgin']['id'].append(1)
                data['sgin']['签诗'].append(sign)
                data['sgin']['解签'].append(meaning)
                Data(data=data, ReadWrite='w')
                lise = []  # 值列表
                for i in range(len(data['sgin']['id'])):
                    value = (data['sgin']['id'][i], data['sgin']['签诗'][i], data['sgin']['解签'][i])
                    lise.append(value)
                return lise
            else:
                if not sign in data['sgin']['签诗'] and not meaning in data['sgin']['解签']:
                    data['sgin']['id'].append(data['sgin']['id'][-1]+1)
                    data['sgin']['签诗'].append(sign)
                    data['sgin']['解签'].append(meaning)
                    Data(data=data, ReadWrite='w')
                    lise = []        #值列表
                    for i in range(len(data['sgin']['id'])):
                        value = (data['sgin']['id'][i], data['sgin']['签诗'][i], data['sgin']['解签'][i])
                        lise.append(value)
                    return lise
                else:
                    return '小白检测到该内容已存在！'
    else:
        return '参数不正确！'


#抽签功能
def DrawLots(use:str):
    #sql
    if yml_DATA.data == 'sqlite' or yml_DATA.data == 'mysql':
        SqlData = Data(f'select * from cq where user = "{use}"')
        SaveData = Data('select id from sgin')
        if not len(SaveData) == 0:
            ID = random.randint(1, SaveData[-1][0])
            #初次存入
            if len(SqlData) == 0:
                Data('insert into cq (user,id,日期) values ("%s",%d,"%s")' % (use, ID, str(tobay)))
                print(Data('select * from cq'))
                return Data(f'select * from sgin where id = {ID}')
            #二次存入
            elif SqlData[0][-1] != str(tobay):
                Data(f'update cq set id = {ID} where user = {use}')
                Data(f'update cq set 日期 = "{tobay}" where user = {use}')
                return Data(f'select * from sgin where id = {ID}')
            else:
                return '\n您今天已经抽过签了请明天再来把ヽ(✿ﾟ▽ﾟ)ノ'
        else:
            return '小白还没有签≧ ﹏ ≦'
    #json
    if yml_DATA.data == 'json':
        JsonData = Data(ReadWrite='r')
        #初次存入
        if len(JsonData['sgin']['id']) != 0:
            ID = random.randint(1, JsonData['sgin']['id'][-1])
            if not use in JsonData['cq']['user']:
                JsonData['cq']['user'].append(use)
                JsonData['cq']['日期'].append(str(tobay))
                JsonData['cq']['id'].append(ID)
                Data(data=JsonData,ReadWrite='w')
                return [(JsonData['sgin']['id'][ID - 1], JsonData['sgin']['签诗'][ID - 1], JsonData['sgin']['解签'][ID - 1]), ]
            else:
                subscript = JsonData['cq']['user'].index(use)
                #二次存入
                if JsonData['cq']['日期'][subscript] != str(tobay):
                    JsonData['cq']['日期'][subscript] = str(tobay)
                    JsonData['cq']['id'][subscript] = ID
                    Data(data=JsonData,ReadWrite='w')
                    return [
                        (JsonData['sgin']['id'][ID - 1], JsonData['sgin']['签诗'][ID - 1], JsonData['sgin']['解签'][ID - 1]), ]
                else:
                    return '您今天已经抽过签了请明天再来把ヽ(✿ﾟ▽ﾟ)ノ'
        else:
            return '小白还没有签≧ ﹏ ≦'


 #解签功能
def intend(use:str):
    print(yml_DATA.data)
    #sql
    if yml_DATA.data == 'sqlite' or yml_DATA.data == 'mysql':
        data = Data(f'select * from cq where user = "{use}"')
        if len(data) != 0:
            if data[0][-1] == str(tobay):
                ID = Data(f'select id from cq where user = "{use}"')[0][0]
                return '\n'+Data(f'select * from sgin where id = {ID}')[0][-1]
            else:
                return '\n小白检测到您还没有抽过签'
        else:
            return '\n小白检测到您还没有抽过签'
    #json
    elif yml_DATA.data == 'json':
        JsonData = Data(ReadWrite='r')
        if use in JsonData['cq']['user']:
            data = JsonData['cq']['user'].index(use)
            #print(data)
            if JsonData['cq']['日期'][data] == str(tobay):
                return JsonData['sgin']['解签'][data-1]
        else:
            return '\n小白检测到您还没有抽过签'''