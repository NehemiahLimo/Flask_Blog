import os
class Config:
    SECRET_KEY='1ad685f672817084afb2404272468465'
    SQLALCHEMY_DATABASE_URI='sqlite:///cite.db'
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get('EMAIL_USER')
    MAIL_PASSWORD=os.environ.get('EMAIL_PASS')
