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

    def upload_movie(self, username: str, movie):
        if not self.__user_is_added(username):
            raise Exception("This user does not exist!")
        elif not movie.owner.username == username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        elif self.__movie_is_added(movie.title):
            raise Exception("Movie already added to the collection!")
        self.movies_collection.append(movie)
        for user in self.users_collection:
            if user.username == username:
                user.movies_owned.append(movie)
                return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie, **kwargs):
        if not self.__movie_is_added(movie.title):
            raise Exception(f"The movie {movie.title} is not uploaded!")
        elif not movie.owner.username == username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for key, value in kwargs.items():  # key = attribute, value = new value
            setattr(movie, key, value)     # movie = object, key = attribute, value = new value
        return f"{username} successfully edited {movie.title} movie."
