class Config(object):
    ENV = "Production"
    DEBUG = False
    TESTING = False
    SERVER_NAME = "127.0.0.1:5000"


class DevelopmentConfig(Config):
    ENV = "Development"
    DEBUG = True
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024
    SERVER_NAME = "localhost:3003"


config = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig,
}