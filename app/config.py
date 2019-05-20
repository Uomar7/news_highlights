class Config:
    '''
    general configuration for the app
    '''

    NEWS_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'

class ProdConfig:
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with general configuration settings.
    '''

    pass

class DevConfig:
    '''
    Development configurations child class 

    args:
        config: The parent configurations class with general configurations settings
    '''

    DEBUG = True
