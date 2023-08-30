import random
from QQAI2.qqai2.plugins.content.data import *
#欢迎语添加
def welcome_add(WelcomeAdd: str, whole: bool = True, GroupNumber: str = '') -> str:
    '''

    :param WelcomeAdd: 欢迎语
    :param whole: 是否为全部默认为True
    :param GroupNumber:群号
    :return:
    '''
    WlcomeData = GroupingTestingFile(ReadWrite='r')     # 获取GroupingTesting.json文件参数
    if whole:
        if not WelcomeAdd in WlcomeData['welcome']['*']:    # 检测欢迎语是否已存在
            WlcomeData['welcome']['*'].append(WelcomeAdd)
            GroupingTestingFile(data=WlcomeData, ReadWrite='w')
            return '成功存入'
        else:
            return '该欢迎语已存在'
    else:
        if GroupNumber in WlcomeData['welcome']:    # 群号存在GroupingTesting.json文件
            if not WelcomeAdd in WlcomeData['welcome']['*']:  # 检测欢迎语是否已存在
                WlcomeData['welcome'][GroupNumber].append(WelcomeAdd)
                GroupingTestingFile(data=WlcomeData, ReadWrite='w')
                return '成功存入'
            else:                                  # 对应群在GroupingTesting.json文件在操作
                if WelcomeAdd in WlcomeData['welcome'][GroupNumber]:
                    return '该欢迎语已存在'
                else:
                    WlcomeData['welcome'][GroupNumber].append(WelcomeAdd)
                    GroupingTestingFile(data=WlcomeData, ReadWrite='w')
                    return '成功存入'
        else:                                       # 群号不存在GroupingTesting.json文件
            if not GroupNumber in WlcomeData['welcome']:  # 群号存在GroupingTesting.json文件
                WlcomeData['welcome'].update({GroupNumber:[WelcomeAdd]})
                GroupingTestingFile(data=WlcomeData, ReadWrite='w')
                return '成功存入'
            else:
                return '该欢迎语已存在'

#欢迎语删除
def welcome_remove(WelcomeRemove: str, whole: bool = True, GroupNumber: str = ''):
    '''

    :param WelcomeRemove: 欢迎语
    :param whole: 是否为全部默认为True
    :param GroupNumber: 群号
    :return:
    '''
    WlcomeData = GroupingTestingFile(ReadWrite='r')  # 获取GroupingTesting.json文件参数
    if whole:
        if WelcomeRemove in WlcomeData['welcome']['*']:
            WlcomeData['welcome']['*'].remove(WelcomeRemove)
            GroupingTestingFile(data=WlcomeData, ReadWrite='w')
            return '删除成功'
        else:
            return '该欢迎语不存在'
    else:
        if GroupNumber in WlcomeData['welcome']:  # 群号存在GroupingTesting.json文件
            if WelcomeRemove in WlcomeData['welcome'][GroupNumber]:
                WlcomeData['welcome'][GroupNumber].remove(WelcomeRemove)
                GroupingTestingFile(data=WlcomeData, ReadWrite='w')
                return '删除成功'
            else:                                  # 对应群在GroupingTesting.json文件在操作
                if not WelcomeRemove in WlcomeData['welcome'][GroupNumber]:
                    return '该欢迎语不存在'
                else:
                    WlcomeData['welcome'][GroupNumber].remove(WelcomeRemove)
                    GroupingTestingFile(data=WlcomeData, ReadWrite='w')
                    return '删除成功'
        else:
            return '该欢迎语不存在'


#离别语添加
def Farewell_add(FarewellAdd: str, whole: bool = True, GroupNumber: str = '') -> str:
    '''

    :param FarewellAdd: 离别语
    :param whole: 是否为全部默认为True
    :param GroupNumber:群号
    :return:
    '''
    WlcomeData = GroupingTestingFile(ReadWrite='r')     # 获取GroupingTesting.json文件参数
    if whole:
        if not FarewellAdd in WlcomeData['Farewell']['*']:    # 检测欢迎语是否已存在
            WlcomeData['Farewell']['*'].append(FarewellAdd)
            GroupingTestingFile(data=WlcomeData, ReadWrite='w')
            return '成功存入'
        else:
            return '该离别已存在'
    else:
        if GroupNumber in WlcomeData['Farewell']:    # 群号存在GroupingTesting.json文件
            if not FarewellAdd in WlcomeData['Farewell']['*']:  # 检测欢迎语是否已存在
                WlcomeData['Farewell'][GroupNumber].append(FarewellAdd)
                GroupingTestingFile(data=WlcomeData, ReadWrite='w')
                return '成功存入'
            else:                                  # 对应群在GroupingTesting.json文件在操作
                if FarewellAdd in WlcomeData['Farewell'][GroupNumber]:
                    return '该离别语已存在'
                else:
                    WlcomeData['welcome'][GroupNumber].append(FarewellAdd)
                    GroupingTestingFile(data=WlcomeData, ReadWrite='w')
                    return '成功存入'
        else:                                       # 群号不存在GroupingTesting.json文件
            if not GroupNumber in WlcomeData['Farewell']:  # 群号存在GroupingTesting.json文件
                WlcomeData['Farewell'].update({GroupNumber:[FarewellAdd]})
                GroupingTestingFile(data=WlcomeData, ReadWrite='w')
                return '成功存入'
            else:
                return '该离别语已存在'


# 离别语删除
def Farewell_remove(FarewellRemove: str, whole: bool = True, GroupNumber: str = ''):
    '''

    :param FarewellRemove: 离别语
    :param whole: 是否为全部默认为True
    :param GroupNumber: 群号
    :return:
    '''
    WlcomeData = GroupingTestingFile(ReadWrite='r')  # 获取GroupingTesting.json文件参数
    if whole:
        if FarewellRemove in WlcomeData['Farewell']['*']:
            WlcomeData['Farewell']['*'].remove(FarewellRemove)
            GroupingTestingFile(data=WlcomeData, ReadWrite='w')
            return '删除成功'
        else:
            return '该离别语不存在'
    else:
        if GroupNumber in WlcomeData['Farewell']:  # 群号存在GroupingTesting.json文件
            if FarewellRemove in WlcomeData['Farewell'][GroupNumber]:
                WlcomeData['Farewell'][GroupNumber].remove(FarewellRemove)
                GroupingTestingFile(data=WlcomeData, ReadWrite='w')
                return '删除成功'
            else:                                  # 对应群在GroupingTesting.json文件在操作
                if not FarewellRemove in WlcomeData['Farewell'][GroupNumber]:
                    return '该离别语不存在'
                else:
                    WlcomeData['Farewell'][GroupNumber].remove(FarewellRemove)
                    GroupingTestingFile(data=WlcomeData, ReadWrite='w')
                    return '删除成功'
        else:
            return '该离别语不存在'
#欢迎语&离别语应用
def use(GroupNumber: str, greet:bool=True) -> str:
    '''

    :param GroupNumber: 群号
    :param greet: 欢迎离别判断，True为欢迎,False为离别（默认True）
    :return:
    '''
    WlcomeData = GroupingTestingFile(ReadWrite='r')  # 获取GroupingTesting.json文件参数
    if greet:
        if GroupNumber in WlcomeData['welcome']:  # 群号存在GroupingTesting.json文件
            return WlcomeData['welcome']["*"][random.randint(1,len(WlcomeData['welcome'][GroupNumber]))-1]
        else:
            return WlcomeData['welcome']["*"][random.randint(1,len(WlcomeData['welcome']['*']))-1]
    elif not greet:
        if GroupNumber in WlcomeData['Farewell']:  # 群号存在GroupingTesting.json文件
            return WlcomeData['Farewell']["*"][random.randint(1, len(WlcomeData['Farewell'][GroupNumber])) - 1]
        else:
            return WlcomeData['Farewell']["*"][random.randint(1, len(WlcomeData['Farewell']['*'])) - 1]