import json
def RecordW(use, function, time):
    '''

    :param use: 用户账号
    :param function: 功能名称
    :param time: 记录时间
    :return:
    '''
    with open('./qqai2/plugins/data/reply.json','r',encoding="UTF-8") as recordR:       #向reply.json文件存入信息
        data = json.load(recordR)
        data['name'].append(use)
        data['function'].append(function)
        data['time'].append(time)
    with open('./qqai2/plugins/data/reply.json', 'w', encoding="UTF-8") as recordW:
        json.dump(data, recordW, indent=4, ensure_ascii=False)
def RecordR():                                                          #读取reply.json
    with open('./qqai2/plugins/data/reply.json','r', encoding="UTF-8") as recordR:
        return json.load(recordR)
def RecordV(id):                                                        #修改reply.json
    with open('./qqai2/plugins/data/reply.json', 'r', encoding="UTF-8") as recordR:
        data = json.load(recordR)
        del data['name'][RecordR()['name'].index(id)]
        del data['function'][RecordR()['name'].index(id)]
        del data['time'][RecordR()['name'].index(id)]
    with open('./qqai2/plugins/data/reply.json', 'w', encoding="UTF-8") as recordW:
        json.dump(data, recordW, indent=4, ensure_ascii=False)
