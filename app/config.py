class Config:
    '''
    general configuration for the app
    '''

    pass

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