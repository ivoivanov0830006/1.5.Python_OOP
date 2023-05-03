from project import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def __user_is_added(self, username):
        for user in self.users_collection:
            if user.username == username:
                return True
        return False

    def __movie_is_added(self, title):
        for movie in self.movies_collection:
            if movie.title == title:
                return True
        return False

    def __movie_is_liked(self, username, title):
        for user in self.users_collection:
            if user.username == username:
                for movie in user.movies_liked:
                    if movie.title == title:
                        return True
                return False

    def register_user(self, username: str, age: int):
        if self.__user_is_added(username):
            raise Exception("User already exists!")
        current_user = User(username, age)
        self.users_collection.append(current_user)
        return f"{username} registered successfully."
