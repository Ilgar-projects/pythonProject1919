from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def create(self, genre_d):
        ent = User(**genre_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, uid):
        genre = self.get_one(uid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, genre_d):
        genre = self.get_one(genre_d.get("id"))
        genre.name = genre_d.get("name")

        self.session.add(genre)
        self.session.commit()

    def get_user_by_username(self, username):
        user = self.session.query(User).filter(User.username == username).one_or_none()
        return user
