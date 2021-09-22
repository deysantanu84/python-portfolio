# app/admin/forms.py

from flask_wtf import FlaskForm
from sys import maxsize
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class TagForm(FlaskForm):
    """
    Form for admin to add or edit a tag
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SubjectForm(FlaskForm):
    """
    Form for admin to add or edit a subject
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    course_subject_id = IntegerField('Course ID', validators=[NumberRange(min=0, max=maxsize)])
    submit = SubmitField('Submit')


class CourseForm(FlaskForm):
    """
    Form for admin to add or edit a course
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    lesson_course_id = IntegerField('Lesson ID', validators=[NumberRange(min=0, max=maxsize)])
    submit = SubmitField('Submit')


class LessonForm(FlaskForm):
    """
    Form for admin to add or edit a lesson
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    video_lesson_id = IntegerField('Video ID', validators=[NumberRange(min=0, max=maxsize)])
    submit = SubmitField('Submit')


class VideoForm(FlaskForm):
    """
    Form for admin to add or edit a video
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    link = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')
