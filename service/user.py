import base64
import hashlib
import hmac
from helpers.constant import PWD_HASH_SALT, PWD_HASH_ITERATIONS

from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def create(self, user_json):
        user_json["password"] = self.generate_passwords(user_json.get("password"))  # превращаю пароль в хэш и создаю пользователя
        return self.dao.create(user_json)

    def update(self, user_json):
        user_json["password"] = self.generate_passwords(user_json.get("password"))  # при обновлении пароля обновлем хеш
        return self.dao.update(user_json)

    def delete(self, uid):
        return self.dao.delete(uid)

    def generate_passwords(self, password):  # хешируем пароль у создающего пользователя
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def compare_passwords(self, password_hash, other_password) -> bool:
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return hmac.compare_digest(decoded_digest, hash_digest)
