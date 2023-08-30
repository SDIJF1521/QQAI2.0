import re
from QQAI2.qqai2.plugins.content.record import *
def AnalysisNews(News: str, command='', symbol='\|', division: bool = True, ManyTimes: bool = True):
    """

    :param News: 文本内容
    :param command: 触发命令
    :param symbol: 可选参数 分离符号不可为空格默认为|
    :param division: 分割可选参数用于执行相关参数的分割，默认为true
    :param ManyTimes:多次分割默认为多次即True
    :return:
    """
    Len = re.findall(re.compile(symbol), News)
    if division:
        if ManyTimes:
            if len(Len) != 0:
                if len(re.findall(re.compile(symbol), News)) != 0:
                    data = News.replace(' ', '')[len(command):]
                    return re.split(symbol, data)
            else:
                return News.replace(command, '').replace(' ', '')
        else:
            print('OK')
            if symbol in News:
                data = News.replace(' ', '')[len(command):]
                Index = data.index(symbol)
                print(Index)
                return [data[0:Index], data[Index+1:len(data)]]
            else:
                raise ValueError('参数内未检出割符')
    else:
        data = (News.replace(' ', '')[len(command):])
        return data
