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

    def delete_movie(self, username: str, movie):
        if not self.__movie_is_added(movie.title):
            raise Exception(f"The movie {movie.title} is not uploaded!")
        elif not movie.owner.username == username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        self.movies_collection.pop(self.movies_collection.index(movie))
        for user in self.users_collection:
            if user.username == username:
                user.movies_owned.pop(user.movies_owned.index(movie))
                return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie):
        if self.__movie_is_liked(username, movie.title):
            raise Exception(f"{username} already liked the movie {movie.title}!")
        elif username == movie.owner.username:  # ??????????????????????
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        movie.likes += 1
        for user in self.users_collection:
            if user.username == username:
                user.movies_liked.append(movie)
                return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie):
        if not self.__movie_is_liked(username, movie.title):
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie.likes -= 1
        for user in self.users_collection:
            if user.username == username:
                user.movies_liked.pop(user.movies_liked.index(movie))
                return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        sorted_result = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        result = []
        for movie in sorted_result:
            result.append(movie.details())
        return '\n'.join(result)

    def __str__(self):
        result = []
        if self.users_collection:
            result.append(f"All users: {', '.join(x.username for x in self.users_collection)}\n")
        else:
            result.append("All users: No users.\n")

        if self.movies_collection:
            result.append(f"All movies: {', '.join(x.title for x in self.movies_collection)}")
        else:
            result.append("All movies: No movies.")

        return "".join(result)
