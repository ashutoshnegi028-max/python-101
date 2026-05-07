from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    app_name: str = 'Workforce Tracker API'
    app_env: str = 'development'
    app_host: str = '0.0.0.0'
    app_port: int = 8000
    database_url: str
    jwt_secret: str
    jwt_algorithm: str = 'HS256'
    jwt_expiry_minutes: int = 120
    dashboard_refresh_seconds: int = 60


settings = Settings()
