from app.user_model import User
from app.user_repository import UserRepository


class UserService:
    repo = UserRepository()

    def get_all_users(self):
        return [user.to_dict() for user in self.repo.find_all()]

    def create(self, user_id, name):
        user = User(user_id, name)
        return self.repo.create(user)

    def delete_all(self) -> int:
        return self.repo.delete_all()