from pydantic_settings import BaseSettings


# test DB
# postgres://avnadmin:AVNS_iEhFLp2hd3wwm4cvyEM@pg-33e6aef5-iteos-26d6.a.aivencloud.com:23697/defaultdb?sslmode=require

class Settings(BaseSettings):
    JWT_EXPIRY_MINUTES: int= 15
    HOST:str = "182.16.16.24"
    DATABASE:str ="VendorPortal"
    USERNAME:str = "v_portal"
    PASSWORD:str = "QUOnEypcpIGqo6N"
    PORT: int = 5432
    SQLALCHEMY_DATABASE_URI: str ="postgresql://v_portal:QUOnEypcpIGqo6N@182.16.16.24:5432/VendorPortal"

settings= Settings()