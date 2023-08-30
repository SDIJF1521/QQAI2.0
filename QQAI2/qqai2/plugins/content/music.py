import requests
from config.yml_DATA import *
from QQAI2.qqai2.plugins.content.analysis import *
def music(name: str):
    try:
        name = AnalysisNews(name, division=False)
        number = re.findall(re.compile('(\d+)'), name)
        Str = ''
        for i in number:
            Str = Str + i
        if len(Str) == len(name):
            ID = int(name)
            return ['http://music.163.com/song/media/outer/url?id=' + str(ID) + '.mp3']
        else:
            print(f'{music_API}search?keywords={name}')
            IdData = requests.get(f'{music_API}search?keywords={name}')
            ID = json.loads(IdData.text)['result']['songs'][0]['id']
            return ['http://music.163.com/song/media/outer/url?id='+str(ID)+'.mp3']
    except:
        return '无效API！'
def MusicDownload(name: str):
    if not os.path.exists(music_File):
        os.mkdir(music_File)
    print(name)
    data = requests.get(music(name)[0]).content
    with open(f'{music_File}/{name}.aac', mode='wb') as f:
        f.write(data)
    print('ok')
    return [f'{music_File}/{name}.aac']