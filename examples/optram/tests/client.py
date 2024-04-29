from pydantic_settings import BaseSettings

import deepinspection


class Config(BaseSettings, env_file=".env.development.secrets"):
    customer_id: str
    subdomain: str
    client_id: str
    client_secret: str


config = Config()


def track():
    return deepinspection.track.client(
        customer_id=config.customer_id,
        subdomain=config.subdomain,
        client_id=config.client_id,
        client_secret=config.client_secret,
    )
