class Config:
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


config = {
    'default': DevelopmentConfig,
    'dev': DevelopmentConfig,
    'prod': ProductionConfig,
    'test': TestingConfig
}
