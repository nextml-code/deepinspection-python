from pydantic_settings import BaseSettings

import deepinspection


class Config(BaseSettings, env_file=".env.development.secrets"):
    deepinspection_customer: str
    deepinspection_client_id: str
    deepinspection_client_secret: str


config = Config()


def track():
    return deepinspection.track.client(
        customer_identifier=config.deepinspection_customer,
        client_id=config.deepinspection_client_id,
        client_secret=config.deepinspection_client_secret,
    )
