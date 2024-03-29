from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    HOST:str = "182.16.16.24"
    DATABASE:str ="VendorPortal"
    USERNAME:str = "v_portal"
    PASSWORD:str = "QUOnEypcpIGqo6N"
    PORT: int = 5432
    SQLALCHEMY_DATABASE_URI: str ="postgresql://v_portal:QUOnEypcpIGqo6N@182.16.16.24:5432/VendorPortal"

settings= Settings()
