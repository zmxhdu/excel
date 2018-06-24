class BaseConfig(object):
    """ 配置基类 """
    SECRET_KEY = 'makesure to set a very secret key'
    INDEX_PER_PAGE = 9
    ADMIN_PRE_PAGE = 15


class DevelopmengConfig(BaseConfig):
    """ 开发环境配置 """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'oracle+cx_oracle://xrisk:xrisk@ORCL'


class ProductionConfig(BaseConfig):
    """ 生产环境配置 """
    pass


class TestingConfig(BaseConfig):
    """ 测试环境配置 """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'oracle+cx_oracle://xrisk:xrisk@XRISK'


configs = {
    'development': DevelopmengConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
