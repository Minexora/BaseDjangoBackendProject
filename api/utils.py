import jwt
import logging
import datetime
from config.config import settings


console_log = logging.getLogger("django")


def generate_access_token(user):
    expired = settings.login.get("session_time", None)
    if not expired:
        expired = 5
    access_token_payload = {
        "user_id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=expired),
        "iat": datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload, settings.SECRET_KEY, algorithm="HS256")
    return access_token


def generate_refresh_token(id):
    refresh_token_payload = {"user_id": id, "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7), "iat": datetime.datetime.utcnow()}
    refresh_token = jwt.encode(refresh_token_payload, settings.SECRET_KEY, algorithm="HS256")

    return refresh_token


def jwt_decode(token, verify=True):
    decoded = jwt.decode(token, key=settings.SECRET_KEY, algorithms="HS256", options={"verify_signature": verify})
    return decoded
