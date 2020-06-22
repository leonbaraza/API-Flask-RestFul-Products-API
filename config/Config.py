import secrets

class Config():
    DEBUG=True
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Config):
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:Leon@1996@127.0.0.1:5432/api_products'
