import os

class Config:
    # Add configurations here
    # SQL_DB_URI = "sqlite:///site.db" OR os.environ.get('')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', "")  # server of our email ID
    MAIL_PORT = int(os.environ.get('MAIL_PORT', ""))
    MAIL_USE_TLS = True # for security and encryption
    MAIL_USE_SSL = False # for security and encryption
    # MAIL_DEBUG = False  # True if app[DEBUG] = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', "") 
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', "") 

    MAIL_DEFAULT_SENDER = ("Team NewsPlanet", MAIL_USERNAME)  # default from sender
    MAIL_MAX_EMAILS =  None # prevent one mail call from sending too many emails
    # MAIL_SUPPRESS_SEND =  None # similar to debug...here its app[TESTING] = True
    MAIL_ASCII_ATTACHMENTS = False # File names to ASCII

    # DATEBASE
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' # /// means realtive path from current file
    