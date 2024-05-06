from pydantic_settings import BaseSettings


# test DB
# postgres://avnadmin:AVNS_iEhFLp2hd3wwm4cvyEM@pg-33e6aef5-iteos-26d6.a.aivencloud.com:23697/defaultdb?sslmode=require

class Settings(BaseSettings):
    TOKEN_URL: str ="auth"
    JWT_EXPIRY_MINUTES: int = 15
    SCOPES: dict ={
        "me": "Read and write access t user's data",
    }
    # SQLALCHEMY_DATABASE_URI: str ="postgresql://postgres:postgres@postgres.cvowww668jr9.ap-south-1.rds.amazonaws.com/postgres"
    SQLALCHEMY_DATABASE_URI: str ="postgresql://v_portal:QUOnEypcpIGqo6N@182.16.16.24:5432/VendorPortal"

settings= Settings()
