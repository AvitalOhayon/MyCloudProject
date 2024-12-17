from app.db import db
from app.user_model import User


class UserRepository:
    """Class for interacting with the visits collection in MongoDB."""

    def __init__(self):
        """
        Initialize the VisitRepository instance.
        """
        self.collection = db.get_collection('users')


    def find_all(self):
        """
        Retrieve all documents in the users collection.
        """
        result = []
        try:
            for data in self.collection.find():
                data['user_id'] = data.pop('_id')
                print(data)
                result.append(User(**data))
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def create(self, user_data: User):
        """
        Insert a document into the users collection.
        """
        user_data = user_data.to_dict()
        user_data['_id'] = user_data.pop('id')
        try:
            result = self.collection.insert_one(user_data)
            return str(result.inserted_id)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def delete_all(self):
        """
        Deletes all documents in the users collection.
        """
        try:
            result = self.collection.delete_many({})
            return {"deleted_count": result.deleted_count}
        except Exception as e:
            print(f"An error occurred while deleting all users: {e}")
            return {"error": str(e)}
