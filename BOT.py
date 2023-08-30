import os
import config.yml
from config import yml_DATA
from config import execute
from config import config_json
if config.yml.config_file():
    if config.yml.config_file():  # yml配置文件执行
        config.execute.file(HOST=str(config.yml_DATA.host), PORT=str(config.yml_DATA.port), name=config.yml_DATA.name,
                            admin=str(config.yml_DATA.admin))
        print(config.yml_DATA.data)
    if config.yml_DATA.data == 'sqlite' or config.yml_DATA.data == 'mysql':
        if not os.path.exists('./config.json'):
            config.config_json.xb_json()
        if config.yml_DATA.data == 'sqlite' or config.yml_DATA.data == 'mysql':
            print('ok')
            if config.config_json.xb_json():  # json配置文件执行
                config.execute.data(config.yml_DATA.data)
    elif config.yml_DATA.data == 'json':
        print('OK')
        config.execute.data(config.yml_DATA.data)
