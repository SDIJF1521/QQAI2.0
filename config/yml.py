import yaml
import sys
import os
import location
def config_file():                               #配置生成yml
    if os.path.exists(str(location.path[0]+'\\XB_config.yml')) == 0:
        print(location.path)
        d = [{'basic_information': {
                      'name': 'XB',
                      'port': 8080,
                      'host': '127.0.0.1',
                      'admin': 12345678},
             'content':
                 {
                    'data': 'json',
                    'function':
                            {
                                'sing_in': True,
                                'store':True,
                                'music': False,
                                'music_download': True,
                                'music_API': 'http://127.0.0.1:3000/',
                                'music_File': './music',
                                'draw_lots': True,
                                'web': True,
                                'include': True,
                                'welcome': True,
                                'farewell':True,
                                'GPT':False,
                                'GPT_access_token':'',
                                'GPT_convo_id':'',
                                'picture':False,
                                'picture_cookie':"",
                                'picture_File':'./picture',
                                'help': True},
                     'management_function':
                         {
                             'banned_to_post': True,
                             'kick_out': True,
                             'group_banned_to_post': True
                         }
                 }
        }
        ]
        print(yaml.dump(d))
        with open(str(location.path[0]+'\\XB_config.yml'), 'w', encoding='UTF-8') as yaml_file:
            yaml.dump(d, yaml_file, default_flow_style=False)
        print('XB_config.yml文件生成成功请进行配置')
        sys.exit(0)
    else:
        return True