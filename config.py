# config.py

class Config(object):

    """
    Commo configurations
    """

    pass


class DevelopmentConfig(Config):

    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):

    """
    Production configurations
    """

    DEBUG = False

app_config = dict()

app_config["development"] = DevelopmentConfig
app_config["production"] = ProductionConfig
