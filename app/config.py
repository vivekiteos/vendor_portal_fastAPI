from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    TOKEN_URL: str ="auth"
    JWT_EXPIRY_MINUTES: int = 2
    SCOPES: dict ={
        "me": "Read and write access t user's data",
    }
    SQLALCHEMY_DATABASE_URI: str ="postgresql://user1:ZnRc5zzfQgvZmygRep5zLxBqJT08iVal@dpg-cotnbjv109ks73aoekgg-a.oregon-postgres.render.com/vdb_c3on"

settings= Settings()
