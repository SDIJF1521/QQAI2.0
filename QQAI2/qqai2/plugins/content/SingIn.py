import datetime
import random
import config.yml_DATA
from QQAI2.qqai2.plugins.content.data import *


def sing_in(use: str):
    if config.yml_DATA.sing_in:
        tobay = datetime.date.today()
        integral = random.randint(5, 20)
        print(tobay)
        # 数据存储为sql
        if config.yml_DATA.data == 'sqlite' or config.yml_DATA.data == 'mysql':
            UsrParameter = Data(data='select user from qd')
            print(UsrParameter)
            user = []
            for i in UsrParameter:
                user.append(i[0])
            # 初次存入
            if not str(use) in user:
                Data('insert into qd (user,积分,日期,天数) values ("%s",%d,"%s",%d)' % (use, integral, str(tobay), 1))
                return [Data('select * from qd where user = "%s"' % use), integral]
            else:
                data = Data('select * from qd where user = "%s"' % use)
                # 二次存入
                if data[0][2] != str(tobay):
                    Data('update qd set 积分= 积分+%d where user = "%s"' % (integral, use))
                    Data('update qd set 日期= %s where user = "%s"' % (str(tobay), use))
                    Data('update qd set 天数= 天数+%d where user = "%s"' % (1, use))
                    return [Data('select * from qd where user = "%s"' % use), integral]
                # 已签到
                else:
                    return '今天你已经签过到了请明天再来把(≧∇≦)ﾉ'
        # 数据存储为json
        elif config.yml_DATA.data == 'json':

            data = Data(ReadWrite='r')
            # 初次存入
            if not use in data['qd']['user']:
                data['qd']['user'].append(use)
                data['qd']['积分'].append(integral)
                data['qd']['日期'].append(str(tobay))
                data['qd']['天数'].append(1)
                Data(data=data,ReadWrite='w')
                subscript = data['qd']['user'].index(use)
                return [[(data['qd']['user'][subscript], str(data['qd']['积分'][subscript]), data['qd']['日期'][subscript], data['qd']['天数'][subscript])],integral]
            else:
                subscript = data['qd']['user'].index(use)
                # 二次存入
                if data['qd']['日期'][subscript] != str(tobay):
                    data['qd']['积分'][subscript] = data['qd']['积分'][subscript]+integral
                    data['qd']['日期'][subscript] = str(tobay)
                    data['qd']['天数'][subscript] = data['qd']['天数'][subscript] + 1
                    Data(data=data, ReadWrite='w')
                    return [[(data['qd']['user'][subscript], str(data['qd']['积分'][subscript]),
                             data['qd']['日期'][subscript], data['qd']['天数'][subscript])], integral]
                # 已签到
                else:
                    return '今天你已经签过到了请明天再来把(≧∇≦)ﾉ'