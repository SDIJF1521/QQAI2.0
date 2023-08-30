import os
import yaml
import config.yml as yml
import location
if yml.config_file():
    # yml数据
    yml_data = yaml.load(
        open
        (
            os.path.join
            (
                location.path[0]+'\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(),
        Loader=yaml.SafeLoader
    )[
        0
    ]
    # 名称
    name = yaml.load(
        open
        (
            os.path.join
            (
                location.path[0] + '\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'basic_information'
    ][
        'name'
    ]
    # 主机
    host = yaml.load(
        open
        (
            os.path.join
            (
                location.path[0]+'\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'basic_information'
    ][
        'host'
    ]
    # 端口
    port = yaml.load(
        open
        (
            os.path.join
            (
                location.path[0]+'\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'basic_information'
    ][
        'port'
    ]
    # 所有者
    admin = yaml.load(
        open
        (
            os.path.join
            (
                location.path[0]+'\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'basic_information'
    ][
        'admin'
    ]
    # 数据
    data = yaml.load(
        open
        (
            os.path.join
            (
                location.path[0]+'\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'content'
    ][
        'data'
    ]
    # 签到
    draw_lots = yaml.load(
        open
        (
            os.path.join
            (
                location.path[0]+'\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'content'
    ][
        'function'
    ][
        'sing_in'
    ]
    #商城
    store = yaml.load(
        open
        (
            os.path.join
            (
                location.path[0]+'\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'content'
    ][
        'function'
    ][
        'store'
    ]
    # 帮助
    help_yml = yaml.load(
        open
        (
            os.path.join
            (
                location.path[0]+'\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(),
        Loader=yaml.SafeLoader)[
        0
    ][
        'content'
    ][
        'function'
    ][
        'help'
    ]
    # 抽签
    include = yaml.load(
        open
        (
            os.path.join
            (
                location.path[0]+'\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'content'
    ][
        'function'
    ][
        'include'
    ]
    #入群检测
    welcome = yaml.load(
        open
        (
            os.path.join
            (
                location.path[0]+'\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'content'
    ][
        'function'
    ][
        'welcome'
    ]
    # 退群检测
    farewell = yaml.load(
        open
        (
            os.path.join
            (
                location.path[0]+'\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'content'
    ][
        'function'
    ][
        'farewell'
    ]
    # Gpt
    GPT = yaml.load(
        open
            (
            os.path.join
                (
                location.path[0] + '\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'content'
    ][
        'function'
    ][
        'GPT'
    ]
    #GPT_access_token
    GPT_access_token = yaml.load(
        open
            (
            os.path.join
                (
                location.path[0] + '\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'content'
    ][
        'function'
    ][
        'GPT_access_token'
    ]
    # GPT_convo_id
    GPT_convo_id = yaml.load(
        open
            (
            os.path.join
                (
                location.path[0] + '\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'content'
    ][
        'function'
    ][
        'GPT_convo_id'
    ]
    # 点歌
    music = yaml.load(
        open(
            os.path.join
            (
                location.path[0]+'\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'content'
    ][
        'function'
    ][
        'music'
    ]
    # 音乐文件路径
    music_File = yaml.load(
        open
        (
            os.path.join
            (
                location.path[0]+'\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'content'
    ][
        'function'
    ][
        'music_File'
    ]
    # 音乐api地址
    music_API = yaml.load(
        open
        (
            os.path.join
            (
                location.path[0]+'\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'content'
    ][
        'function'
    ][
        'music_API'
    ]
    # 音乐下载
    music_download = yaml.load(
        open
        (
            os.path.join
            (
                location.path[0]+'\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'content'
    ][
        'function'
    ][
        'music_download'
    ]
    # 入库
    sing_in = yaml.load(
        open
        (
            os.path.join
            (
                location.path[0]+'\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'content'
    ][
        'function'
    ][
        'sing_in'
    ]
    # web查询
    wed = yaml.load(
        open
        (
            os.path.join
            (
                location.path[0]+'\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8').read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'content'
    ][
        'function'
    ][
        'web'
    ]
    # 图功能
    picture = yaml.load(
        open
            (
            os.path.join
                (
                location.path[0] + '\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8').read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'content'
    ][
        'function'
    ][
        'picture'
    ]
    # 图片文件夹
    picture_File = yaml.load(
        open
            (
            os.path.join
                (
                location.path[0] + '\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8').read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'content'
    ][
        'function'
    ][
        'picture_File'
    ]
    # picture_cookie
    picture_cookie = yaml.load(
        open
            (
            os.path.join
                (
                location.path[0] + '\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8').read(),
        Loader=yaml.SafeLoader
    )[
        0
    ][
        'content'
    ][
        'function'
    ][
        'picture_cookie'
    ]
    # 禁言
    banned_to_post = yaml.load(
        open(
            os.path.join(
                location.path[0]+'\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(), Loader=yaml.SafeLoader)[
        0][
        'content'
    ][
        'management_function'
    ][
        'banned_to_post'
    ]
    # 群禁言
    group_banned_to_post = yaml.load(
        open(
            os.path.join(
                location.path[0]+'\\XB_config.yml'
            ),
            'r',
            encoding='UTF-8'
        ).read(

        ),
        Loader=yaml.SafeLoader
    )[
        0][
        'content'
    ][
        'management_function'][
        'group_banned_to_post'
    ]
