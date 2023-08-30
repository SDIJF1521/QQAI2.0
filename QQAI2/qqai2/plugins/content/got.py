import time
from QQAI2.qqai2.plugins.content.web import *
from QQAI2.qqai2.plugins.content.draw import *
from QQAI2.qqai2.plugins.content.store import *
from QQAI2.qqai2.plugins.content.music import *
from QQAI2.qqai2.plugins.content.welcome import *
from QQAI2.qqai2.plugins.content.picture import *
def got(user: str, data, power: str, GroupNumber: str = '', admin=None,grouplist=None) -> dict:
    '''

    :param use: 用户账号
    :param data: 用户输入数据
    :param power:
    :param GroupNumber: 群号
    :param admin: 群成员权限
    :param GroupNumber: 群号
    :param grouplist: 接管群
    :return:
    '''
    if admin is None:
        admin = []
    else:
        admin = list(admin)
    if user in RecordR()['name']:
        indexes = RecordR()['name'].index(user)
        if RecordR()['time'][RecordR()['name'].index(user)]+60 > time.time():

            # 存签
            if RecordR()['function'][indexes] == '存签':
                Save = save(data)
                RecordV(user)
                if isinstance(Save, list):
                    return {'str': '小白已将信息存入(✿◕‿◕✿)'}
                else:
                    return {'str': Save}



             # 点歌
            elif RecordR()['function'][indexes] == '点歌':
                MusicUrl=music(data)
                RecordV(user)
                return {'voice':MusicUrl}



            # 音乐下载
            elif RecordR()['function'][indexes] == '音乐下载':
                Data = MusicDownload(data)
                RecordV(user)
                if isinstance(Data, list):
                    return {'file': Data[0]}
                else:

                    return {'str':Data}



            # 网站收录
            elif RecordR()['function'][indexes] == '网站收录':
                Data = deposit(data)
                RecordV(user)
                return {'str': Data}



            # 网站查询
            elif RecordR()['function'][indexes] == '网站查询':
                Data = web(data)
                RecordV(user)
                return {'str': Data}

            # 欢迎语添加
            elif RecordR()['function'][indexes] == '欢迎语添加':
                print(power)
                user1 = AnalysisNews(News=user)[1]
                if user1 in admin:
                    if '|' in data:
                        welcomedata = AnalysisNews(News=data, symbol='|', ManyTimes=False)  # 群号与欢迎语参数分离
                        print(welcomedata)
                        print(welcomedata[0].istitle())
                        # 格式模板1“群号|欢迎语”
                        if welcomedata[0].isdigit() and len(welcomedata[0]) >= 6:
                            if welcomedata[0] in grouplist:  # 判断群是否为QQ机器人管辖范围内
                                Str = welcome_add(GroupNumber=welcomedata[0], WelcomeAdd=welcomedata[1],
                                                  whole=False)  # 欢迎语存入
                                RecordV(user)
                                return {'str': Str}
                            else:
                                RecordV(user)
                                return {'str': "该群不在小白的管辖范围内\n＞︿＜"}
                                # 格式模板2“欢迎语”
                        else:
                            print('')
                            Str = welcome_add(WelcomeAdd=AnalysisNews(News=data, division=False))  # 欢迎语存入
                            RecordV(user)
                            return {'str': Str}
                        # 格式模板2“欢迎语”
                    else:
                        Str = welcome_add(WelcomeAdd=AnalysisNews(News=data, division=False))  # 欢迎语存入
                        RecordV(user)
                        return {'str': Str}
                else:
                    # 非超管；群主&管理员添加欢迎语
                    print()
                    if power == 'owner' or power == 'admin':
                        Str = welcome_add(WelcomeAdd=AnalysisNews(News=data, division=False),
                                          GroupNumber=GroupNumber, whole=False)
                        RecordV(user)
                        return {'str': Str}




            # 欢迎语删除
            elif RecordR()['function'][indexes] == '欢迎语删除':
                user1 = AnalysisNews(News=user)[1]
                if user1 in admin:
                    if '|' in data:
                        welcomedata = AnalysisNews(News=data, symbol='|', ManyTimes=False)  # 群号与欢迎语参数分离
                        print(welcomedata)
                        print(welcomedata[0].istitle())
                        # 格式模板1“群号|欢迎语”
                        if welcomedata[0].isdigit() and len(welcomedata[0]) >= 6:
                            if welcomedata[0] in grouplist:  # 判断群是否为QQ机器人管辖范围内
                                Str = welcome_remove(GroupNumber=welcomedata[0], WelcomeRemove=welcomedata[1],
                                                  whole=False)  # 欢迎语移除
                                RecordV(user)
                                return {'str': Str}
                            else:
                                RecordV(user)
                                return {'str': "该群不在小白的管辖范围内\n＞︿＜"}
                                # 格式模板2“欢迎语”
                        else:
                            Str = welcome_remove(WelcomeRemove=AnalysisNews(News=data, division=False))  # 欢迎语移除
                            RecordV(user)
                            return {'str': Str}
                        # 格式模板2“欢迎语”
                    else:
                        Str = welcome_remove(WelcomeRemove=AnalysisNews(News=data, division=False))  # 欢迎语移除
                        RecordV(user)
                        return {'str': Str}
                else:
                    # 非超管；群主&管理员删除欢迎语
                    print()
                    if power == 'owner' or power == 'admin':
                        Str = welcome_remove(WelcomeRemove=AnalysisNews(News=data, division=False),
                                          GroupNumber=GroupNumber, whole=False)
                        RecordV(user)
                        return {'str': Str}



            # 离别语添加
            elif RecordR()['function'][indexes] == '离别语添加':
                print(power)
                user1 = AnalysisNews(News=user)[1]
                if user1 in admin:
                    if '|' in data:
                        welcomedata = AnalysisNews(News=data, symbol='|', ManyTimes=False)  # 群号与离别语参数分离
                        print(welcomedata)
                        print(welcomedata[0].istitle())
                        # 格式模板1“群号|欢迎语”
                        if welcomedata[0].isdigit() and len(welcomedata[0]) >= 6:
                            if welcomedata[0] in grouplist:  # 判断群是否为QQ机器人管辖范围内
                                Str = Farewell_add(GroupNumber=welcomedata[0], FarewellAdd=welcomedata[1],
                                                  whole=False)  # 离别语存入
                                RecordV(user)
                                return {'str': Str}
                            else:
                                RecordV(user)
                                return {'str': "该群不在小白的管辖范围内\n＞︿＜"}
                                # 格式模板2“离别语”
                        else:
                            print('')
                            Str = Farewell_add(FarewellAdd=AnalysisNews(News=data, division=False))  # 欢迎语存入
                            RecordV(user)
                            return {'str': Str}
                        # 格式模板2“离别语”
                    else:
                        Str = Farewell_add(FarewellAdd=AnalysisNews(News=data, division=False))  # 欢迎语存入
                        RecordV(user)
                        return {'str': Str}
                else:
                    # 非超管；群主&管理员添加离别语
                    print()
                    if power == 'owner' or power == 'admin':
                        Str = Farewell_add(FarewellAdd=AnalysisNews(News=data, division=False),
                                          GroupNumber=GroupNumber, whole=False)
                        RecordV(user)
                        return {'str': Str}



            # 离别语删除
            elif RecordR()['function'][indexes] == '离别语删除':
                user1 = AnalysisNews(News=user)[1]
                if user1 in admin:
                    if '|' in data:
                        welcomedata = AnalysisNews(News=data, symbol='|', ManyTimes=False)  # 群号与离别语参数分离
                        print(welcomedata)
                        print(welcomedata[0].istitle())
                        # 格式模板1“群号|离别语”
                        if welcomedata[0].isdigit() and len(welcomedata[0]) >= 6:
                            if welcomedata[0] in grouplist:  # 判断群是否为QQ机器人管辖范围内
                                Str = Farewell_remove(GroupNumber=welcomedata[0], FarewellRemove=welcomedata[1],
                                                  whole=False)  # 离别语移除
                                RecordV(user)
                                return {'str': Str}
                            else:
                                RecordV(user)
                                return {'str': "该群不在小白的管辖范围内\n＞︿＜"}
                                # 格式模板2“离别语”
                        else:
                            print('ok')
                            Str = Farewell_remove(FarewellRemove=AnalysisNews(News=data, division=False))  # 离别语移除
                            RecordV(user)
                            return {'str': Str}
                        # 格式模板2“离别语”
                    else:
                        print('okk')
                        Str = Farewell_remove(FarewellRemove=AnalysisNews(News=data, division=False))  # 离别语存入
                        RecordV(user)
                        return {'str': Str}
                else:
                    # 非超管；群主&管理员删除离别语
                    print()
                    if power == 'owner' or power == 'admin':
                        Str = Farewell_remove(FarewellRemove=AnalysisNews(News=data, division=False),
                                          GroupNumber=GroupNumber, whole=False)
                        RecordV(user)
                        return {'str': Str}


            # id找图
            elif RecordR()['function'][indexes] == 'id找图':
                DATA = Picture(data)  # 获取图像
                if isinstance(DATA, list):
                    RecordV(user)
                    return {'image':DATA[0]}
                else:
                    RecordV(user)
                    return {'str':DATA}
            # 好感商城上货
            elif RecordR()['function'][indexes] == '上货':
                content = AnalysisNews(data)
                if len(content) == 3:
                    content[1] = int(content[1])
                    content[2] = int(content[2])
                    print(content)
                    if isinstance(content[0], str) and isinstance(content[1], int) and isinstance(content[2], int):
                        RecordV(user)
                        return {'str':store_Add(goods=content[0],money=content[1],value=content[2])}
                else:
                    RecordV(user)
                    return {'str':'格式错误'}
            # 好感商城商品下架
            elif RecordR()['function'][indexes] == '下架':
                content = AnalysisNews(News=data,division=False,ManyTimes=False)
                RecordV(user)
                return {'str':store_remove(goods=content)}

            # 商品购买
            elif RecordR()['function'][indexes] == '购买':
                content = AnalysisNews(data)
                if isinstance(content,list) and len(content) == 2:
                    content[1] = int(content[1])
                    print(f'{GroupNumber}|{str(user)}')
                    RecordV(user)
                    return {'str':buy(user=f'{str(user)}',commodity=content[0],quantity=content[1])}
                elif isinstance(content, str):
                    RecordV(user)
                    return {'str':buy(user=f'{user}', commodity=content)}
                else:
                    RecordV(user)
                    return {'str':'参数错误≧ ﹏ ≦'}




        else:
            if RecordR()['time'][RecordR()['name'].index(user)]+20 <= time.time():
                RecordV(user)