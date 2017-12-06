import peewee as pw

DATABASE_NAME = 'kll.db'

database = pw.SqliteDatabase(DATABASE_NAME)


class BaseModel(pw.Model):
    class Meta:
        database = database


class Config(BaseModel):
    name = pw.CharField()
    description = pw.TextField()
    url = pw.CharField()
    # TODO: figure out how to implement categories and keyboards
    # (initial feeling: many to many?)
    # categories = SomeField()
    # keyboards = SomeField()
    author = pw.CharField()

    downloads = pw.IntegerField()
    likes = pw.IntegerField()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'url': self.url,
            'author': self.author,
            'stats': {
                'downloads': self.downloads,
                'likes': self.likes
            }
        }


def create_tables():
    database.connect()
    database.create_tables([Config])
