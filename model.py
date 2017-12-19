import peewee as pw

DATABASE_NAME = 'kll.db'

database = pw.SqliteDatabase(DATABASE_NAME)


class BaseModel(pw.Model):
    class Meta:
        database = database


class Keyboard(BaseModel):
    name = pw.CharField()
    slug = pw.CharField()


class Category(BaseModel):
    name = pw.CharField()
    slug = pw.CharField()


class Config(BaseModel):
    name = pw.CharField()
    description = pw.TextField()
    githubUrl = pw.CharField()
    author = pw.CharField()

    downloads = pw.IntegerField()
    likes = pw.IntegerField()

    # TODO: figure out how to implement categories and keyboards
    # (initial feeling: many to many?)
    # categories = SomeField()
    keyboard = pw.ForeignKeyField(Keyboard, related_name='configs')

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


def setup_db():
    database.connect()
    database.create_tables([Config, Keyboard, Category])

    keyboards = [{'name': 'K-Type', 'slug': 'ktype'},
                 {'name': 'White Fox', 'slug': 'whitefox'},
                 {'name': 'Ergodox Infinity', 'slug': 'ergodox_infinity'}]

    categories = [{'name': 'Layouts', 'slug': 'layouts'},
                  {'name': 'Animations', 'slug': 'animations'}]

    with database.atomic():
        Keyboard.insert_many(keyboards).execute()
        Category.insert_many(categories).execute()
