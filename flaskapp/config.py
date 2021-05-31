import os


class Config:
    # app.config['SECRET_KEY'] = '87c1ad1887f27d9d537e701b19f60beb'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    SECRET_KEY = '87c1ad1887f27d9d537e701b19f60beb'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
