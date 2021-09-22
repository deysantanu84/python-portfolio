# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


# An Instructor is a User with a flag is_instructor = True.
# A Student is a User with is_instructor = False.
class Users(UserMixin, db.Model):
    """
    Create an Users table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.user_id

    def __repr__(self):
        return '<User: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Subjects(db.Model):
    """
    Create a Subjects table
    """

    __tablename__ = 'subjects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    course_subject_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    def __repr__(self):
        return '<Subjects: {}>'.format(self.name)


# A Course can belong to multiple Subjects.
class Courses(db.Model):
    """
    Create a Courses table
    """

    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    lesson_course_id = db.Column(db.Integer, db.ForeignKey('lessons.id'))
    subjects = db.relationship('Subjects', backref='course_subject', lazy='dynamic')

    def __repr__(self):
        return '<Courses: {}>'.format(self.name)


# A Lesson can belong to multiple Courses.
class Lessons(db.Model):
    """
    Create a Lessons table
    """

    __tablename__ = 'lessons'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    video_lesson_id = db.Column(db.Integer, db.ForeignKey('videos.id'))
    courses = db.relationship('Courses', backref='lesson_course', lazy='dynamic')

    def __repr__(self):
        return '<Lessons: {}>'.format(self.name)


video_tags = db.Table('video_tags',
                      db.Column('video_id', db.Integer, db.ForeignKey('videos.id')),
                      db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
                      )


# A Video can belong multiple Lessons.
# A Video can have multiple attached Tags.
# A Video should have a link field to save YouTube or Vimeo url.
class Videos(db.Model):
    """
    Create a Videos table
    """

    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    link = db.Column(db.String(512), unique=True)
    lessons = db.relationship('Lessons', backref='video_lesson', lazy='dynamic')
    taggings = db.relationship('Tags', secondary=video_tags, backref=db.backref('videoTags'), lazy='dynamic')

    def __repr__(self):
        return '<Videos: {}>'.format(self.name)


class Tags(db.Model):
    """
    Create a Tags table
    """

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))

    def __repr__(self):
        return '<Tag: {}>'.format(self.name)
