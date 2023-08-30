import os
import re
import json
import requests
import config.yml_DATA
from random import randint
def Picture(ID:str=''):
    '''

    :param ID: 图片（默认为空，为空时回随机选取图片）
    :return:
    '''
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Referer': "https://www.pixiv.net",
        'cookie':config.yml_DATA.picture_cookie}
    if not os.path.exists(config.yml_DATA.picture_File):
        os.mkdir(config.yml_DATA.picture_File)
    picture_url_list = []
    if ID == '':
        url = 'https://www.pixiv.net/ranking.php?mode=daily&content=illust&format=json'
        for i in range(1,3):
            data = json.loads(requests.get(url+f'&p={i}').text)          # 图片数据
            for j in data['contents']:
                picture_url_list.append(j['url'])
        picture_url=picture_url_list[randint(0,len(picture_url_list))]      # 获取图片链接
        name = ''
        for i in range(1,3):
            data = json.loads(requests.get(url + f'&p={i}').text)
            for j in data['contents']:
                if j['url'] == picture_url:
                    name=j['title']                   # 获取图片名称
        with open(f'{config.yml_DATA.picture_File}/{name}.png', mode='wb') as f:
            f.write(requests.get(picture_url,headers=headers).content)     # 将图片保存到本地
        return f'{config.yml_DATA.picture_File[2:]}/{name}.png'
    else:
        # id寻图
        print(ID)
        pid = re.findall("\d+",ID)
        if len(ID) == len(pid[0]):
            try:
                url = 'https://www.pixiv.net/artworks/'+pid[0]
                dara = requests.get(url=url,headers=headers).text
                picture_url = re.findall('"original":"(.+_p0\.jpg|.+_p0\.png)',dara)
                with open(f'{config.yml_DATA.picture_File}/picture.png', mode='wb') as f:
                    f.write(requests.get(picture_url[0], headers=headers).content)  # 将图片保存到本地
                return [f'{config.yml_DATA.picture_File[2:]}/picture.png']
            except:
                return '无效id'
        else:
            return 'id不正确,id只能为数字'
