from pathlib import Path
from nonebot.rule import to_me
from revChatGPT.V1 import Chatbot
from nonebot.adapters import Event
from QQAI2.qqai2.plugins.content.got import *
from QQAI2.qqai2.plugins.content.web import *
from QQAI2.qqai2.plugins.content.store import *
from QQAI2.qqai2.plugins.content.music import *
from QQAI2.qqai2.plugins.content.SingIn import *
from QQAI2.qqai2.plugins.content.picture import *
from QQAI2.qqai2.plugins.content.welcome import *
from QQAI2.qqai2.plugins.content.analysis import *
from nonebot import get_driver,on_regex,on_notice,on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message,GroupIncreaseNoticeEvent,GroupDecreaseNoticeEvent,PokeNotifyEvent,MessageSegment
allocation = on_regex('.+', priority=5)  # 注册功能调度事件
notice=on_notice(priority=5)
gpt = on_regex('.+',priority=3,rule=to_me())
gpt_command = on_command('小白',priority=4)
gpt_user = []   # 使用人员列表用于避免功能冲突


# @形式触发gpt
@gpt.handle()
async def chatGPT(event:GroupMessageEvent):
    try:
        if GPT:
            gpt_user.append(str(event.group_id) + '|' + str(event.user_id))
            if len(str(event.message))!=0:
                chatbot = Chatbot(config={
                    "access_token":GPT_access_token},
                    conversation_id=GPT_convo_id)
                prompt = '小白'+str(event.message)
                response = ""

                for data in chatbot.ask(
                        prompt
                ):
                    response = data["message"]
                await gpt.send(Message(response))
            gpt_user.remove(str(event.group_id) + '|' + str(event.user_id))
    except:
        await gpt.send('小白出错了{{{(>_<)}}}请重试！')


# 命令形式触发got
@gpt_command.handle()
async def chatGPT(event:GroupMessageEvent):
    if not str(event.group_id) + '|' + str(event.user_id) in gpt_user:
        if GPT:
            try:
                gpt_user.append(str(event.group_id) + '|' + str(event.user_id))
                if len(str(event.message))!=0:
                    chatbot = Chatbot(config={
                        "access_token":GPT_access_token},
                        conversation_id=GPT_convo_id)

                    prompt = '小白'+str(event.message)
                    response = ""

                    for data in chatbot.ask(
                            prompt
                    ):
                        response = data["message"]
                    await gpt.send(Message(response))
                gpt_user.remove(str(event.group_id) + '|' + str(event.user_id))
            except:
                await gpt_command.send('小白出错了{{{(>_<)}}}请重试！')


@allocation.handle()
async def Allocation(event: GroupMessageEvent, bot: Bot,event1:Event):
    if not str(event.group_id) + '|' + str(event.user_id) in gpt_user:
        #获取发送者权限
        get_group_member_info = await bot.get_group_member_info(group_id=event.group_id, user_id=event.user_id)
        #获取机器人所接管的所有群
        groupdata = await bot.get_group_list()
        grouplist = []
        for h in groupdata:
            grouplist.append(str(h['group_id']))
        News = str(event.message)
        # 获取群内成员发送的消息
        print(News)
        # 回复式命令响应
        with open('./qqai2/plugins/data/reply.json', 'r', encoding="UTF-8") as f:
            JsonData = json.load(f)
        if str(event.group_id) + '|' + str(event.user_id) in JsonData['name']:
            if len(RecordR()['name']) != 0:
                value = got(user=str(event.group_id) + '|' + str(event.user_id), data=News, power=get_group_member_info['role'], GroupNumber=str(event.group_id),admin=get_driver().config.superusers,grouplist=grouplist)
                print(value)
                if 'str' in value:
                    msg = f'[CQ:at,qq={str(event.user_id)}]\n{value["str"]}'
                    await allocation.send(Message(msg))
                elif 'voice' in value:
                    msg = f'[CQ:record,file={value["voice"][0]}]'
                    try:
                        await allocation.send(Message(msg))
                    except:
                        await allocation.send('小白找不到该歌曲::>_<::')
                elif 'file' in value:
                    file = os.getcwd().replace('\\', '/') + '/' + value["file"][2:len(value["file"])]
                    #print(file)
                    try:
                        await bot.call_api('upload_group_file', **{'group_id': event.group_id,
                                                                   'file': f'{file}',
                                                                   'name': News + '.aac'})
                        os.remove(file)
                    except:
                        await bot.call_api('upload_group_file', **{'group_id': event.group_id,
                                                                   'file': f'{file}',
                                                                   'name': News + '.aac'})
                        os.remove(file)
                elif 'image' in value:
                    file = os.getcwd().replace('\\', '/') + '/' + value["image"] # 获取图像路径
                    await allocation.send(Message(MessageSegment.image(Path(file))))
                    os.remove(file)
        else:
            with open('./qqai2/plugins/data/command.json', encoding='UTF-8') as command:  # 提取command。json配置数据
                DataCommand = json.load(command)
                function = DataCommand['普通功能']
                AdminFunction = DataCommand['管理功能']
            with open('./qqai2/plugins/data/command_yml.json',encoding='UTF-8') as js_yml:
                command_yml = json.load(js_yml)




    # 普通功能
            for i in function:
                for j in function[i]:
                    if len(News) >= len(j):
                        NewsCommand = News[0:len(j)]
                        if NewsCommand in j:
                            print(j + ' 命令匹配成功功能为: ' + i)
                            # 签到事件
                            if NewsCommand in function['签到']:
                                Save = command_yml['function']['签到']
                                if yml_DATA.yml_data['content']['function'][Save]:
                                    ReverseBack = sing_in(str(event.group_id) + '|' + str(event.user_id))
                                    if isinstance(ReverseBack, list) or isinstance(ReverseBack, tuple):
                                        #print(ReverseBack)
                                        out = '[CQ:at,qq=%s]\n签到成功!\n获得积分：%d点\n您当前的积分为：%s 点\n您已签到: %s 天' % (
                                        event.user_id, ReverseBack[1], str(ReverseBack[0][0][1]), str(ReverseBack[0][0][3]))
                                        await allocation.send(Message(out))
                                    elif isinstance(ReverseBack, str):
                                        out = '[CQ:at,qq=%s]]%s' % (str(event.user_id), ReverseBack)
                                        await allocation.send(Message(out))
                                else:
                                    await allocation.send('该功能为开启如果想使用的话请联系管理')

                            # 存签事件
                            elif NewsCommand in function['存签']:
                                FunctionName = command_yml['function']['存签']
                                if yml_DATA.yml_data['content']['function'][FunctionName]:
                                    if len(News) > len(j):
                                        #print(AnalysisNews(News=News, command=j)[0])
                                        Save = (save(News))
                                        #print(Save)
                                        if isinstance(Save, list) or isinstance(Save, tuple):
                                            await allocation.send('小白已将信息存入(✿◕‿◕✿)')
                                        else:
                                            await allocation.send(Save)
                                    else:
                                        await allocation.send('请按照 签诗|意思 的形式存入')
                                        RecordW(use=str(event.group_id) + '|' + str(event.user_id), function=i,
                                                time=time.time())
                                else:
                                    await allocation.send('该功能为开启如果想使用的话请联系管理')

                            # 抽签事件
                            elif NewsCommand in function['抽签']:
                                FunctionName = command_yml['function']['抽签']
                                if yml_DATA.yml_data['content']['function'][FunctionName]:
                                    DL = DrawLots(str(event.group_id) + '|' + str(event.user_id))
                                    if isinstance(DL, str):
                                        out = '[CQ:at,qq=' + str(event.user_id) + ']' + DL
                                        await allocation.send(Message(out))
                                    elif isinstance(DL, list) or isinstance(DL, tuple):
                                        msg = '[CQ:at,qq=' + str(event.user_id) + ']\n您抽中小白签库第' + str(
                                            DL[0][0]) + '签\n签诗：' + str(DL[0][1])
                                        await allocation.send(Message(msg))
                                else:
                                    await allocation.send('该功能为开启如果想使用的话请联系管理')

                            # 解签事件
                            elif NewsCommand in function['解签']:
                                FunctionName = command_yml['function']['解签']
                                if yml_DATA.yml_data['content']['function'][FunctionName]:
                                    Inted = intend(str(event.group_id) + '|' + str(event.user_id))
                                    if isinstance(Inted, str):
                                        out = '[CQ:at,qq=' + str(event.user_id) + ']' + Inted
                                        await allocation.send(Message(out))
                                else:
                                    await allocation.send('该功能为开启如果想使用的话请联系管理')

                            # 点歌事件
                            elif NewsCommand in function['点歌']:
                                FunctionName = command_yml['function']['点歌']
                                if yml_DATA.yml_data['content']['function'][FunctionName]:
                                    if len(music_API) != 0:
                                        try:
                                            #print(requests.get(config.yml_DATA.music_API).status_code)
                                            if requests.get(music_API).status_code == 200:
                                                #print('ok')
                                                if len(News) > len(j):
                                                    data = str(News[2:len(News)]).replace(' ', '')
                                                    MusicUrl = music(data)
                                                    #print(MusicUrl)
                                                    msg = f'[CQ:record,file={MusicUrl[0]}]'
                                                    #print(msg)
                                                    try:
                                                        await allocation.send(Message(msg))
                                                    except:
                                                        await allocation.send('小白找不到该歌曲::>_<::')
                                                else:
                                                    RecordW(use=str(event.group_id) + '|' + str(event.user_id), function=i,
                                                            time=time.time())
                                                    await allocation.send('请输入歌名或音乐id:')
                                        except:
                                            await allocation.send('无效API请联系小白的管理进行API的配置{{{(>_<)}}}')
                                else:
                                    await allocation.send('该功能为开启如果想使用的话请联系管理')

                            # 音乐下载事件
                            elif NewsCommand in function['音乐下载']:
                                FunctionName = command_yml['function']['音乐下载']
                                if yml_DATA.yml_data['content']['function'][FunctionName]:
                                    if len(music_API) != 0:
                                        print(requests.get(music_API).status_code)
                                        if requests.get(music_API).status_code == 200:
                                            try:
                                                if len(News) > len(j):
                                                    data = str(News[4:len(News)]).replace(' ', '')
                                                    DATA = MusicDownload(data)
                                                    #print(DATA)
                                                    if isinstance(DATA, list):
                                                        file = os.getcwd().replace('\\', '/') + '/' + DATA[0]
                                                        #print(file)
                                                        await bot.call_api('upload_group_file',
                                                                           **{'group_id': event.group_id,
                                                                              'file': f'{file}',
                                                                              'name': data + '.aac'})
                                                        os.remove(file)
                                                    else:
                                                        print('yes')
                                                        await allocation.send(DATA)

                                                else:
                                                    RecordW(use=str(event.group_id) + '|' + str(event.user_id), function=i,
                                                            time=time.time())
                                                    await allocation.send('请输入歌名或音乐id:')
                                            except:
                                                await allocation.send('无效API请联系小白的管理进行API的配置{{{(>_<)}}}')
                                else:
                                    await allocation.send('该功能为开启如果想使用的话请联系管理')

                            # 网站存入
                            elif NewsCommand in function['网站收录']:
                                FunctionName = command_yml['function']['网站收录']
                                if yml_DATA.yml_data['content']['function'][FunctionName]:
                                    if len(News) > len(j):
                                        data = deposit(News, j)
                                        #print(data)
                                        if isinstance(data, str):
                                            msg = f'[CQ:at,qq={str(event.user_id)}]\n{data}'
                                            await allocation.send(Message(msg))
                                    else:
                                        RecordW(use=str(event.group_id) + '|' + str(event.user_id), function=i,
                                                time=time.time())
                                        await allocation.send('请按 网站名称|网址 方式写入')
                                else:
                                    await allocation.send('该功能为开启如果想使用的话请联系管理')

                            # 网站查询
                            elif NewsCommand in function['网站查询']:
                                FunctionName = command_yml['function']['网站查询']
                                if yml_DATA.yml_data['content']['function'][FunctionName]:
                                    if len(News) > len(j):
                                        print(News)
                                        data = web(News, j)
                                        #print(data)
                                        if isinstance(data, str):
                                            msg = f'[CQ:at,qq={str(event.user_id)}]\n{data}'
                                            await allocation.send(Message(msg))
                                    else:
                                        RecordW(use=str(event.group_id) + '|' + str(event.user_id), function=i,
                                                time=time.time())
                                        await allocation.send('请输入要查询的网站名称：')
                                else:
                                    await allocation.send('该功能为开启如果想使用的话请联系管理')

                            # 欢迎语添加
                            elif NewsCommand in function['欢迎语添加']:
                                FunctionName = command_yml['function']['入群欢迎']
                                get_group_member_info = await bot.get_group_member_info(group_id=event.group_id, user_id=event.user_id)
                                if yml_DATA.yml_data['content']['function'][FunctionName]:

                                    if len(News) > len(j):
                                        # QQ机器人超管添加欢迎语
                                        if str(event.user_id) in get_driver().config.superusers:
                                            if '|' in News:
                                                welcomedata = AnalysisNews(News=News, command=j, symbol='|', ManyTimes=False)     # 群号与欢迎语参数分离
                                                #print(welcomedata)
                                                #print(welcomedata[0].istitle())
                                                # 格式模板1“群号|欢迎语”
                                                if welcomedata[0].isdigit() and len(welcomedata[0]) >= 6:
                                                    if welcomedata[0] in grouplist:    # 判断群是否为QQ机器人管辖范围内
                                                        Str = welcome_add(GroupNumber=welcomedata[0], WelcomeAdd=welcomedata[1], whole=False)    # 欢迎语存入
                                                        await allocation.send(Str)
                                                    else:
                                                        await allocation.send("该群不在小白的管辖范围内\n＞︿＜")
                                                # 格式模板2“欢迎语”
                                                else:
                                                    Str = welcome_add(WelcomeAdd=AnalysisNews(News=News, command=j, division=False))  # 欢迎语存入
                                                    await allocation.send(Str)
                                            # 格式模板2“欢迎语”
                                            else:
                                                Str = welcome_add(WelcomeAdd=AnalysisNews(News=News, command=j, division=False))  # 欢迎语存入
                                                await allocation.send(Str)
                                        else:
                                            # 非超管；群主&管理员添加欢迎语
                                            if get_group_member_info['role'] == 'owner' or get_group_member_info['role'] == 'admin':
                                                #print(AnalysisNews(News=News, command=j, division=False)[0],str(event.group_id))
                                                Str = welcome_add(WelcomeAdd=AnalysisNews(News=News, command=j, division=False), GroupNumber=str(event.group_id),whole=False)
                                                await allocation.send(Str)
                                    elif str(event.user_id) in get_driver().config.superusers or get_group_member_info['role'] == 'owner' or get_group_member_info['role'] == 'admin':
                                        print("ok")
                                        RecordW(use=str(event.group_id) + '|' + str(event.user_id), function=i,
                                                time=time.time())
                                        await allocation.send('{:-<36}\n'.format('') +
                                                              '超管格式:\n'
                                                              '\t\t群号|欢迎语【指定群添加欢迎语】\n\n'
                                                              '\t\t欢迎语【欢迎语添加至机器人管辖范围内所有群】\n'
                                                              '\n{:—<14}\n'.format('') +
                                                              '非超管群主&管理员格式:\n'
                                                              '\t\t欢迎语【添加至该群】\n'
                                                              '{:-<36}\n'.format('') +
                                                              '请按照规定格式输入,{user}作为用户名的占位符号')

                            # 欢迎语删除
                            elif NewsCommand in function['欢迎语删除']:
                                FunctionName = command_yml['function']['入群欢迎']
                                get_group_member_info = await bot.get_group_member_info(group_id=event.group_id, user_id=event.user_id)
                                if yml_DATA.yml_data['content']['function'][FunctionName]:

                                    if len(News) > len(j):
                                        # QQ机器人超管删除欢迎语
                                        if str(event.user_id) in get_driver().config.superusers:
                                            print('ok')
                                            if '|' in News:
                                                welcomedata = AnalysisNews(News=News, command=j, symbol='|', ManyTimes=False)     # 群号与欢迎语参数分离
                                                #print(welcomedata)
                                                #print(welcomedata[0].istitle())
                                                # 格式模板1“群号|欢迎语”
                                                if welcomedata[0].isdigit() and len(welcomedata[0]) >= 6:
                                                    if welcomedata[0] in grouplist:    # 判断群是否为QQ机器人管辖范围内
                                                        Str = welcome_remove(GroupNumber=welcomedata[0], WelcomeRemove=welcomedata[1], whole=False)    # 欢迎语存入
                                                        await allocation.send(Str)
                                                    else:
                                                        await allocation.send("该群不在小白的管辖范围内\n＞︿＜")
                                                # 格式模板2“欢迎语”
                                                else:
                                                    Str = welcome_remove(WelcomeRemove=AnalysisNews(News=News, command=j, division=False))  # 欢迎语存入
                                                    await allocation.send(Str)
                                            # 格式模板2“欢迎语”
                                            else:
                                                Str = welcome_remove(WelcomeRemove=AnalysisNews(News=News, command=j, division=False))  # 欢迎语存入
                                                await allocation.send(Str)
                                        else:
                                            # 非超管；群主&管理员删除欢迎语
                                            if get_group_member_info['role'] == 'owner' or get_group_member_info['role'] == 'admin':
                                                print(AnalysisNews(News=News, command=j, division=False)[0],str(event.group_id))
                                                Str = welcome_remove(WelcomeRemove=AnalysisNews(News=News, command=j, division=False), GroupNumber=str(event.group_id),whole=False)
                                                await allocation.send(Str)
                                    elif str(event.user_id) in get_driver().config.superusers or get_group_member_info['role'] == 'owner' or get_group_member_info['role'] == 'admin':
                                        RecordW(use=str(event.group_id) + '|' + str(event.user_id), function=i,
                                                time=time.time())
                                        await allocation.send('{:-<36}\n'.format('') +
                                                              '超管格式:\n'
                                                              '\t\t群号|欢迎语【指定群删除欢迎语】\n\n'
                                                              '\t\t欢迎语【删除出场默认欢迎语至机器人管辖范围内所有群】\n'
                                                              '\n{:—<14}\n'.format('') +
                                                              '非超管群主&管理员格式:\n'
                                                              '\t\t欢迎语【删除该群的指定欢迎语】\n'
                                                              '{:-<36}\n'.format('') +
                                                              '请按照规定格式输入,{user}作为用户名的占位符号')

                            # 离别语添加
                            elif NewsCommand in function['离别语添加']:
                                FunctionName = command_yml['function']['退群检测']
                                get_group_member_info = await bot.get_group_member_info(group_id=event.group_id, user_id=event.user_id)
                                if yml_DATA.yml_data['content']['function'][FunctionName]:

                                    if len(News) > len(j):
                                        # QQ机器人超管添加离别语
                                        if str(event.user_id) in get_driver().config.superusers:
                                            if '|' in News:
                                                welcomedata = AnalysisNews(News=News, command=j, symbol='|', ManyTimes=False)     # 群号与欢迎语参数分离
                                                # 格式模板1“群号|欢迎语”
                                                if welcomedata[0].isdigit() and len(welcomedata[0]) >= 6:
                                                    if welcomedata[0] in grouplist:    # 判断群是否为QQ机器人管辖范围内
                                                        Str = Farewell_add(GroupNumber=welcomedata[0], FarewellAdd=welcomedata[1], whole=False)    # 欢迎语存入
                                                        await allocation.send(Str)
                                                    else:
                                                        await allocation.send("该群不在小白的管辖范围内\n＞︿＜")
                                                # 格式模板2“离别语”
                                                else:
                                                    Str = Farewell_add(FarewellAdd=AnalysisNews(News=News, command=j, division=False))  # 欢迎语存入
                                                    await allocation.send(Str)
                                            # 格式模板2“离别语”
                                            else:
                                                Str = Farewell_add(FarewellAdd=AnalysisNews(News=News, command=j, division=False))  # 欢迎语存入
                                                await allocation.send(Str)
                                        else:
                                            # 非超管；群主&管理员添加离别语
                                            if get_group_member_info['role'] == 'owner' or get_group_member_info['role'] == 'admin':
                                                #print(AnalysisNews(News=News, command=j, division=False)[0],str(event.group_id))
                                                Str = welcome_add(WelcomeAdd=AnalysisNews(News=News, command=j, division=False), GroupNumber=str(event.group_id),whole=False)
                                                await allocation.send(Str)
                                    elif str(event.user_id) in get_driver().config.superusers or get_group_member_info['role'] == 'owner' or get_group_member_info['role'] == 'admin':
                                        print("ok")
                                        RecordW(use=str(event.group_id) + '|' + str(event.user_id), function=i,
                                                time=time.time())
                                        await allocation.send('{:-<36}\n'.format('') +
                                                              '超管格式:\n'
                                                              '\t\t群号|离别语【指定群添加离别语】\n\n'
                                                              '\t\t离别语【离别语添加至机器人管辖范围内所有群】\n'
                                                              '\n{:—<14}\n'.format('') +
                                                              '非超管群主&管理员格式:\n'
                                                              '\t\t离别语【离别至该群】\n'
                                                              '{:-<36}\n'.format('') +
                                                              '请按照规定格式输入,{user}作为用户名的占位符号')


                            # 离别语删除
                            elif NewsCommand in function['离别语删除']:
                                FunctionName = command_yml['function']['退群检测']
                                get_group_member_info = await bot.get_group_member_info(group_id=event.group_id,
                                                                                        user_id=event.user_id)
                                if yml_DATA.yml_data['content']['function'][FunctionName]:

                                    if len(News) > len(j):
                                        # QQ机器人超管删除离别语
                                        if str(event.user_id) in get_driver().config.superusers:
                                            print('ok')
                                            if '|' in News:
                                                welcomedata = AnalysisNews(News=News, command=j, symbol='|',
                                                                           ManyTimes=False)  # 群号与欢迎语参数分离
                                                # print(welcomedata)
                                                # print(welcomedata[0].istitle())
                                                # 格式模板1“群号|离别语”
                                                if welcomedata[0].isdigit() and len(welcomedata[0]) >= 6:
                                                    if welcomedata[0] in grouplist:  # 判断群是否为QQ机器人管辖范围内
                                                        Str = Farewell_remove(GroupNumber=welcomedata[0],
                                                                             FarewellRemove=welcomedata[1],
                                                                             whole=False)  # 欢迎语存入
                                                        await allocation.send(Str)
                                                    else:
                                                        await allocation.send("该群不在小白的管辖范围内\n＞︿＜")
                                                # 格式模板2“离别语”
                                                else:
                                                    Str = Farewell_remove(
                                                        FarewellRemove=AnalysisNews(News=News, command=j,
                                                                                   division=False))  # 欢迎语存入
                                                    await allocation.send(Str)
                                            # 格式模板2“离别语”
                                            else:
                                                Str = Farewell_remove(
                                                    FarewellRemove=AnalysisNews(News=News, command=j,
                                                                               division=False))  # 欢迎语存入
                                                await allocation.send(Str)
                                        else:
                                            # 非超管；群主&管理员删除离别语
                                            if get_group_member_info['role'] == 'owner' or get_group_member_info[
                                                'role'] == 'admin':
                                                print(AnalysisNews(News=News, command=j, division=False)[0],
                                                      str(event.group_id))
                                                Str = Farewell_remove(
                                                    FarewellRemove=AnalysisNews(News=News, command=j,
                                                                               division=False),
                                                    GroupNumber=str(event.group_id), whole=False)
                                                await allocation.send(Str)
                                    elif str(event.user_id) in get_driver().config.superusers or \
                                            get_group_member_info['role'] == 'owner' or get_group_member_info[
                                        'role'] == 'admin':
                                        RecordW(use=str(event.group_id) + '|' + str(event.user_id), function=i,
                                                time=time.time())
                                        await allocation.send('{:-<36}\n'.format('') +
                                                              '超管格式:\n'
                                                              '\t\t群号|离别语【指定群删除离别语】\n\n'
                                                              '\t\t离别语【删除出场默认离别语至机器人管辖范围内所有群】\n'
                                                              '\n{:—<14}\n'.format('') +
                                                              '非超管群主&管理员格式:\n'
                                                              '\t\t离别语【删除该群的指定离别语】\n'
                                                              '{:-<36}\n'.format('') +
                                                              '请按照规定格式输入,{user}作为用户名的占位符号')



                            # help
                            elif NewsCommand in function['help']:
                                FunctionName = command_yml['function']['help']
                                if yml_DATA.yml_data['content']['function'][FunctionName]:
                                    msg = '{:-^19s}' \
                                          '\n{:^19s}' \
                                          '\n{:-^19s}'.format('','菜单','')
                                    for n in command_yml['function']:
                                        if yml_DATA.yml_data['content']['function'][command_yml['function'][n]]:
                                            if not (n =='入群欢迎' or n =='退群检测'or n=='不良言语撤回'):
                                                msg=msg+'\n{:^19s}'.format(function[n][0])
                                    await allocation.send(msg)



                            # 随机图片
                            elif NewsCommand in function['随机图片']:
                                FunctionName = command_yml['function']['随机图片']
                                if yml_DATA.yml_data['content']['function'][FunctionName]:
                                    try:
                                        DATA = Picture()
                                        print(DATA)
                                        file = os.getcwd().replace('\\', '/') + '/' + DATA
                                        await allocation.send(Message(MessageSegment.image(Path(file))))
                                        os.remove(file)
                                    except:
                                        await allocation.send('图片获取失败')


                            # id找图
                            elif NewsCommand in function['id找图']:
                                FunctionName = command_yml['function']['id找图']
                                if yml_DATA.yml_data['content']['function'][FunctionName]:
                                    if len(News) > len(j):
                                        content = AnalysisNews(News=News,command=j,division=False)
                                        print(content)
                                        DATA = Picture(content) # 获取图像
                                        if isinstance(DATA, list):
                                            file = os.getcwd().replace('\\', '/') + '/' + DATA[0]     # 获取图像路径
                                            await allocation.send(Message(MessageSegment.image(Path(file))))
                                            os.remove(file)
                                        else:
                                            await allocation.send(DATA)
                                    else:
                                        RecordW(use=str(event.group_id) + '|' + str(event.user_id), function=i,
                                                time=time.time())
                                        await allocation.send('请输入图片id（例:109477593）\n注意该功能无法寻找动图:')
                            # 商城上货
                            elif NewsCommand in function['上货']:
                                print(1)
                                FunctionName = command_yml['function']['上货']
                                if yml_DATA.yml_data['content']['function'][FunctionName]:
                                    if str(event.user_id) in get_driver().config.superusers:
                                        print(len(News),len(News))
                                        if len(News) > len(News):
                                            content = AnalysisNews(News=News,command=j)
                                            if len(content) == 3 :
                                                content[1] = int(content[1])
                                                content[2]= int(content[2])
                                                if isinstance(content[0],str) and isinstance(content[1],int) and isinstance(content[2],int):
                                                    print('ok')
                                                    await allocation.send(Message('[CQ:at,qq=' + str(event.user_id) + ']'+store_Add(goods=content[0],money=content[1],value=content[2])))
                                            else:
                                                await allocation.send(Message('[CQ:at,qq=' + str(event.user_id) + ']'+'格式错误'))
                                        else:
                                            print(2)
                                            RecordW(use=str(event.group_id) + '|' + str(event.user_id), function=i,
                                                    time=time.time())
                                            await allocation.send('请按照"商品|积分|好感"的方式填写（注意:一次只能上架一款商品）')
                            # 商城货物下架
                            elif NewsCommand in function['下架']:
                                FunctionName = command_yml['function']['下架']
                                if yml_DATA.yml_data['content']['function'][FunctionName]:
                                    if str(event.user_id) in get_driver().config.superusers:
                                        if len(News) > len(j):
                                            content = AnalysisNews(News=News, command=j,division=False,ManyTimes=False)
                                            await allocation.send(Message('[CQ:at,qq=' + str(event.user_id) + ']'+store_remove(goods=content)))
                                        else:
                                            RecordW(use=str(event.group_id) + '|' + str(event.user_id), function=i,
                                                    time=time.time())
                                            await allocation.send('请输入要下架的商品（注意:一次只能下架一款商品）')

                            # 商品购买
                            elif NewsCommand in function['购买']:
                                FunctionName = command_yml['function']['购买']
                                if yml_DATA.yml_data['content']['function'][FunctionName]:
                                    if len(News) > len(j):
                                        content = AnalysisNews(News=News,command=j)
                                        print(content)
                                        if isinstance(content,list) and len(content) == 2:
                                            content[1]=int(content[1])
                                            await allocation.send(Message('[CQ:at,qq=' + str(event.user_id) + ']'+buy(user=f'{event.group_id}|{str(event.user_id)}',commodity=content[0],quantity=content[1])))
                                        elif isinstance(content,str):
                                            await allocation.send(Message('[CQ:at,qq=' + str(event.user_id) + ']'+buy(user=f'{event.group_id}|{event.user_id}', commodity=content)))
                                        else:
                                            await allocation.send('参数错误≧ ﹏ ≦')
                                    else:
                                        store_content = buy(look_up=True)
                                        msg = '{:^26s}' \
                                              '\n{:-^26s}'.format('商城','')
                                        for s in store_content:
                                            msg += '\n{:^6s}\t{:^3s}：{:<5.2f}\t\t{:>5d}'.format(s,'积分',store_content[s]['积分'],store_content[s]['好感'])
                                        print(msg)
                                        RecordW(use=str(event.group_id) + '|' + str(event.user_id), function=i,
                                                time=time.time())
                                        await allocation.send(Message(f'{msg}'+'\n{:-^26s}\n请按照【商品|数量】的方式选择要购买的商品'.format('')))






    # 管理功能
            for i in AdminFunction:
                for j in AdminFunction[i]:
                    if len(News) >= len(j):
                        NewsCommand = News[0:len(j)]
                        if NewsCommand in j:
                            print(j + ' 命令匹配成功功能为: ' + i)
                            if str(event.user_id) in get_driver().config.superusers or (
                                    get_group_member_info['role'] == 'owner' or get_group_member_info[
                                'role'] == 'admin'):
                                print('是否具有操作权限:【✓】')
                                ID = await bot.call_api('get_login_info')
                                permissions = await bot.call_api("get_group_member_info",**{"group_id":event.group_id,'user_id':ID['user_id']})
                                # 判断机器人是否拥有禁言权限
                                if permissions['role'] == 'owner' or permissions['role'] == 'admin':
                                    # 群禁言ON
                                    if NewsCommand in AdminFunction['开启群禁言']:
                                        FunctionName = command_yml['AdminFunction']['开启群禁言']
                                        if yml_DATA.yml_data['content']['management_function'][FunctionName]:
                                            await bot.call_api("set_group_whole_ban",**{'group_id':event.group_id,'enable':True})
                                            await allocation.finish('群禁言开启')

                                    # 群禁言off
                                    if NewsCommand in AdminFunction['解除群禁言']:
                                        FunctionName = command_yml['AdminFunction']['解除群禁言']
                                        if yml_DATA.yml_data['content']['management_function'][FunctionName]:
                                            await bot.call_api("set_group_whole_ban",
                                                               **{'group_id': event.group_id, 'enable': False})
                                            await allocation.finish('群禁言已关闭')

                                    # 单人禁言
                                    if NewsCommand in AdminFunction['禁言']:
                                        FunctionName = command_yml['AdminFunction']['禁言']
                                        if len(News) > len(j):
                                            if yml_DATA.yml_data['content']['management_function'][FunctionName]:
                                                # 获取群成员列表
                                                member_data = json.loads(json.dumps(await bot.call_api('get_group_member_list',**{'group_id':event.group_id})))
                                                member_list=[]
                                                for h in member_data:
                                                    member_list.append(h['user_id'])
                                                # 获取用管理的群成员
                                                primary_bata=event1.get_event_description()
                                                print(primary_bata)
                                                rule = re.compile('\[at:qq=(\d+)]')
                                                name_list = rule.findall(str(primary_bata))  # 提取用户账号
                                                print(rule.findall(primary_bata))
                                                rule_time = re.compile(']</le>(\d+)')
                                                time_list = rule_time.findall(str(primary_bata).replace(" ",""))  # 提取设置禁言时间
                                                banned_to_post_list =[]                 # 被禁言人员名单
                                                not_banned_to_post_list = []            # 被放出禁言人员名单
                                                print(name_list,time_list)
                                                if len(name_list) == len(time_list):
                                                    for n in range(len(name_list)):
                                                        if int(name_list[n]) in member_list:
                                                            get_group_member_info = await bot.get_group_member_info(
                                                                group_id=event.group_id, user_id=int(name_list[n]))
                                                            if get_group_member_info['role'] != "owner" and get_group_member_info['role'] != "admin" and not name_list[n] in get_driver().config.superusers:
                                                                await bot.call_api("set_group_ban",**{"group_id":event.group_id,"user_id":name_list[n],"duration":int(time_list[n])*60})
                                                                if int(time_list[n])>0:
                                                                    banned_to_post_list.append(name_list[n])
                                                                else:
                                                                    not_banned_to_post_list.append(name_list[n])
                                                    print(banned_to_post_list)
                                                    white_list = name_list[:]
                                                    # 提取白名单成员
                                                    for n in banned_to_post_list:
                                                        if n in white_list:
                                                            white_list.remove(n)
                                                    for x in not_banned_to_post_list:
                                                        if x in white_list:
                                                            white_list.remove(x)
                                                            print('ok')
                                                    print(not_banned_to_post_list)

                                                    print(white_list)

                                                    # 情况一(禁言名单，白名单，解禁名单都有值)输出
                                                    if  len(banned_to_post_list) !=0 and len(not_banned_to_post_list)!=0 and len(white_list)!=0:
                                                        msg = "禁言成功被禁言人员名单如下：" \
                                                              "\n{:-^9s}".format("")
                                                        for n in banned_to_post_list:
                                                            msg = msg+f'\n[CQ:at,qq={n}]'
                                                        msg = msg+"\n{:-^9s}" \
                                                                  "\n\n解禁成功，被解除禁言人员名单如下:" \
                                                                  "\n{:-^9s}".format("","")
                                                        for n in not_banned_to_post_list:
                                                            msg=msg+f'\n[CQ:at,qq={n}]'
                                                        msg=msg+"\n{:-^9s}\n\n一下成员属于白名单无法被禁言:" \
                                                                "\n{:-^9s}".format("","")
                                                        for n in white_list:
                                                            msg=msg+f'\n[CQ:at,qq={n}]'
                                                        await allocation.send(Message(msg))

                                                    # 情况2(禁言名单，解禁名单有值)输出
                                                    elif len(banned_to_post_list) !=0 and len(not_banned_to_post_list)!=0 and len(white_list) == 0:
                                                        msg = "禁言成功被禁言人员名单如下：" \
                                                              "\n{:-^9s}".format("")
                                                        for n in banned_to_post_list:
                                                            msg = msg + f'\n[CQ:at,qq={n}]'
                                                        msg = msg + "\n{:-^9s}" \
                                                                    "\n\n解禁成功，被解除禁言人员名单如下:" \
                                                                    "\n{:-^9s}".format("", "")
                                                        for n in not_banned_to_post_list:
                                                            msg = msg + f'\n[CQ:at,qq={n}]'
                                                        await allocation.send(Message(msg))

                                                    # 情况3(禁言名单，白名单有值)输出输出
                                                    elif len(banned_to_post_list) !=0 and len(not_banned_to_post_list)==0 and len(white_list) != 0:
                                                        msg = "禁言成功被禁言人员名单如下：" \
                                                              "\n{:-^9s}".format("")
                                                        for n in banned_to_post_list:
                                                            msg = msg + f'\n[CQ:at,qq={n}]'
                                                        msg = msg + "\n{:-^9s}\n\n一下成员属于白名单无法被禁言:" \
                                                                    "\n{:-^9s}".format("", "")
                                                        for n in white_list:
                                                            msg = msg + f'\n[CQ:at,qq={n}]'
                                                        await allocation.send(Message(msg))

                                                    # 情况3(禁言名单值有值)输出
                                                    elif len(banned_to_post_list) != 0 and len(not_banned_to_post_list) == 0 and len(white_list) == 0:
                                                        msg = "禁言成功被禁言人员名单如下：" \
                                                              "\n{:-^9s}".format("")
                                                        for n in banned_to_post_list:
                                                            msg = msg + f'\n[CQ:at,qq={n}]'
                                                        await allocation.send(Message(msg))
                                                    elif len(banned_to_post_list) == 0 and len(not_banned_to_post_list) != 0 and len(white_list) == 0:
                                                        msg = "\n解禁成功，被解除禁言人员名单如下:" \
                                                                    "\n{:-^9s}".format("")
                                                        for n in not_banned_to_post_list:
                                                            msg = msg + f'\n[CQ:at,qq={n}]'
                                                        await allocation.send(Message(msg))
                                                    else:
                                                        await allocation.send('该成员为白名单成员并没有被禁言')
                                                else:
                                                    await allocation.send('格式不正确请按照@某人 禁言时间\n'
                                                                          '例如：\n'
                                                                          '     @小白 10 @X 20')
                                        else:
                                            await allocation.send('无参数')


                            else:
                                print('是否具有操作权限:【✕】')

#消息事件
@notice.handle()
#入群欢迎
async def greet(event: GroupIncreaseNoticeEvent):
    # 读取配置
    with open('./qqai2/plugins/data/command_yml.json', encoding='UTF-8') as js_yml:
        command_yml = json.load(js_yml)
        FunctionName = command_yml['function']['入群欢迎']
    # 进群欢迎是否启用
    if yml_DATA.yml_data['content']['function'][FunctionName]:
        user = str(event.user_id)
        template = use(GroupNumber=str(event.group_id))
        welcome_language = template
        if '{user}' in template:
            welcome_language = template.replace('{user}',f'[CQ:at,qq={user}]')
        await notice.finish(Message(welcome_language))



# 退群检测
@notice.handle()
async def greet1(event: GroupDecreaseNoticeEvent):
    with open('./qqai2/plugins/data/command_yml.json', encoding='UTF-8') as js_yml:
        command_yml = json.load(js_yml)
        FunctionName = command_yml['function']['退群检测']
    # 进群欢迎是否启用
    if yml_DATA.yml_data['content']['function'][FunctionName]:
        print('ok')
        user = str(event.user_id)
        template = use(GroupNumber=str(event.group_id),greet=False)
        welcome_language = template
        if '{user}' in template:
            welcome_language = template.replace('{user}', f'[CQ:at,qq={user}]')
        await notice.finish(Message(welcome_language))
@notice.handle()
async def Easter_Egg(event:PokeNotifyEvent,bot:Bot):
    ID = await bot.call_api('get_login_info')
    if event.target_id == ID['user_id']:
      await notice.send(Message('你不要在光天化日之下在这里戳我啊，哒咩!\n[CQ:image,file=b2566dfb4c8c7ef494a7e285161a0080.image,subType=1,url=https://gchat.qpic.cn/gchatpic_new/839682307/760705385-3101003974-B2566DFB4C8C7EF494A7E285161A0080/0?term=2&amp;is_origin=0]'))