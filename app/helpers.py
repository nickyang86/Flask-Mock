import os
from app.configs.personal import PersonalConfig
from app.configs.production import ProductionConfig


def select_config():
    """
    根据环境变量选择默认配置文件
    :return:
    """
    env = os.getenv('FLASK_ENV')
    if env == 'production':
        return ProductionConfig()
    else:
        return PersonalConfig()

