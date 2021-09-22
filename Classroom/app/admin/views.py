# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from sqlalchemy import exc

from . import admin
from .forms import CourseForm, LessonForm, SubjectForm, TagForm, VideoForm
from .. import db
from ..models import Courses, Lessons, Subjects, Tags, Videos


def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)


# Tags Views
@admin.route('/tags', methods=['GET', 'POST'])
@login_required
def list_tags():
    """
    List all tags
    """
    check_admin()

    tags = Tags.query.all()

    return render_template('admin/tags/tags.html',
                           tags=tags, title="Tags")


@admin.route('/tags/add', methods=['GET', 'POST'])
@login_required
def add_tag():
    """
    Add a tag to the database
    """
    check_admin()

    addTag = True

    form = TagForm()
    if form.validate_on_submit():
        tag = Tags(name=form.name.data,
                   description=form.description.data)
        try:
            # add tag to the database
            db.session.add(tag)
            db.session.commit()
            flash('You have successfully added a new tag.')
        except exc.SQLAlchemyError:
            # in case tag name already exists
            flash('Error: tag name already exists.')

        # redirect to tags page
        return redirect(url_for('admin.list_tags'))

    # load tags template
    return render_template('admin/tags/tag.html', action="Add",
                           add_tag=addTag, form=form,
                           title="Add Tag")


@admin.route('/tags/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_tag(id):
    """
    Edit a tag
    """
    check_admin()

    addTag = False

    tag = Subjects.query.get_or_404(id)
    form = SubjectForm(obj=tag)
    if form.validate_on_submit():
        tag.name = form.name.data
        tag.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the tag.')

        # redirect to the tags page
        return redirect(url_for('admin.list_tags'))

    form.description.data = tag.description
    form.name.data = tag.name
    return render_template('admin/tags/tag.html', action="Edit",
                           add_tag=addTag, form=form,
                           tag=tag, title="Edit Tag")


@admin.route('/tags/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_tag(id):
    """
    Delete a tag from the database
    """
    check_admin()

    tag = Tags.query.get_or_404(id)
    db.session.delete(tag)
    db.session.commit()
    flash('You have successfully deleted the tag.')

    # redirect to the tags page
    return redirect(url_for('admin.list_tags'))

    # return render_template(title="Delete Tag")


# Subjects Views
@admin.route('/subjects', methods=['GET', 'POST'])
@login_required
def list_subjects():
    """
    List all subjects
    """
    check_admin()

    subjects = Subjects.query.all()

    return render_template('admin/subjects/subjects.html',
                           subjects=subjects, title="Subjects")


@admin.route('/subjects/add', methods=['GET', 'POST'])
@login_required
def add_subject():
    """
    Add a subject to the database
    """
    check_admin()

    addSubject = True

    form = SubjectForm()
    if form.validate_on_submit():
        subject = Subjects(name=form.name.data,
                           description=form.description.data,
                           course_subject_id=form.course_subject_id.data)
        try:
            # add subject to the database
            db.session.add(subject)
            db.session.commit()
            flash('You have successfully added a new subject.')
        except exc.SQLAlchemyError as error:
            # in case subject name already exists
            print(error)
            flash('Error: subject name already exists.')

        # redirect to subjects page
        return redirect(url_for('admin.list_subjects'))

    # load subjects template
    return render_template('admin/subjects/subject.html', action="Add",
                           add_subject=addSubject, form=form,
                           title="Add Subject")


@admin.route('/subjects/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_subject(id):
    """
    Edit a subject
    """
    check_admin()

    addSubject = False

    subject = Subjects.query.get_or_404(id)
    form = SubjectForm(obj=subject)
    if form.validate_on_submit():
        subject.name = form.name.data
        subject.description = form.description.data
        subject.course_subject_id = form.description.data
        db.session.commit()
        flash('You have successfully edited the subject.')

        # redirect to the subjects page
        return redirect(url_for('admin.list_subjects'))

    form.description.data = subject.description
    form.name.data = subject.name
    form.course_subject_id.data = subject.course_subject_id
    return render_template('admin/subjects/subject.html', action="Edit",
                           add_subject=addSubject, form=form,
                           subject=subject, title="Edit Subject")


@admin.route('/subjects/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_subject(id):
    """
    Delete a subject from the database
    """
    check_admin()

    subject = Subjects.query.get_or_404(id)
    db.session.delete(subject)
    db.session.commit()
    flash('You have successfully deleted the subject.')

    # redirect to the subjects page
    return redirect(url_for('admin.list_subjects'))

    # return render_template(title="Delete Subject")


# Courses Views
@admin.route('/courses', methods=['GET', 'POST'])
@login_required
def list_courses():
    """
    List all courses
    """
    check_admin()

    courses = Courses.query.all()

    return render_template('admin/courses/courses.html',
                           courses=courses, title="Courses")


@admin.route('/courses/add', methods=['GET', 'POST'])
@login_required
def add_course():
    """
    Add a course to the database
    """
    check_admin()

    addCourse = True

    form = CourseForm()
    if form.validate_on_submit():
        course = Courses(name=form.name.data,
                         description=form.description.data,
                         lesson_course_id=form.lesson_course_id.data)
        try:
            # add course to the database
            db.session.add(course)
            db.session.commit()
            flash('You have successfully added a new course.')
        except exc.SQLAlchemyError:
            # in case course name already exists
            flash('Error: course name already exists.')

        # redirect to courses page
        return redirect(url_for('admin.list_courses'))

    # load course template
    return render_template('admin/courses/course.html', action="Add",
                           add_course=addCourse, form=form,
                           title="Add Course")


@admin.route('/courses/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_course(id):
    """
    Edit a course
    """
    check_admin()

    addCourse = False

    course = Courses.query.get_or_404(id)
    form = CourseForm(obj=course)
    if form.validate_on_submit():
        course.name = form.name.data
        course.description = form.description.data
        course.lesson_course_id = form.lesson_course_id.data
        db.session.commit()
        flash('You have successfully edited the course.')

        # redirect to the courses page
        return redirect(url_for('admin.list_courses'))

    form.description.data = course.description
    form.name.data = course.name
    form.lesson_course_id.data = course.lesson_course_id
    return render_template('admin/courses/course.html', action="Edit",
                           add_course=addCourse, form=form,
                           course=course, title="Edit Course")


@admin.route('/courses/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_course(id):
    """
    Delete a course from the database
    """
    check_admin()

    course = Courses.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    flash('You have successfully deleted the course.')

    # redirect to the courses page
    return redirect(url_for('admin.list_courses'))

    # return render_template(title="Delete Course")


# Lessons Views
@admin.route('/lessons', methods=['GET', 'POST'])
@login_required
def list_lessons():
    """
    List all lessons
    """
    check_admin()

    lessons = Lessons.query.all()

    return render_template('admin/lessons/lessons.html',
                           lessons=lessons, title="Lessons")


@admin.route('/lessons/add', methods=['GET', 'POST'])
@login_required
def add_lesson():
    """
    Add a lesson to the database
    """
    check_admin()

    addLesson = True

    form = LessonForm()
    if form.validate_on_submit():
        lesson = Lessons(name=form.name.data,
                         description=form.description.data,
                         video_lesson_id=form.video_lesson_id.data)
        try:
            # add lesson to the database
            db.session.add(lesson)
            db.session.commit()
            flash('You have successfully added a new lesson.')
        except exc.SQLAlchemyError:
            # in case lesson name already exists
            flash('Error: lesson name already exists.')

        # redirect to lessons page
        return redirect(url_for('admin.list_lessons'))

    # load lesson template
    return render_template('admin/lessons/lesson.html', action="Add",
                           add_lesson=addLesson, form=form,
                           title="Add Lesson")


@admin.route('/lessons/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_lesson(id):
    """
    Edit a lesson
    """
    check_admin()

    addLesson = False

    lesson = Lessons.query.get_or_404(id)
    form = LessonForm(obj=lesson)
    if form.validate_on_submit():
        lesson.name = form.name.data
        lesson.description = form.description.data
        lesson.video_lesson_id = form.video_lesson_id.data
        db.session.commit()
        flash('You have successfully edited the lesson.')

        # redirect to the lessons page
        return redirect(url_for('admin.list_lessons'))

    form.description.data = lesson.description
    form.name.data = lesson.name
    form.video_lesson_id.data = lesson.video_lesson_id
    return render_template('admin/lessons/lesson.html', action="Edit",
                           add_lesson=addLesson, form=form,
                           lesson=lesson, title="Edit Lesson")


@admin.route('/lessons/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_lessons(id):
    """
    Delete a lesson from the database
    """
    check_admin()

    lesson = Lessons.query.get_or_404(id)
    db.session.delete(lesson)
    db.session.commit()
    flash('You have successfully deleted the lesson.')

    # redirect to the lessons page
    return redirect(url_for('admin.list_lessons'))

    # return render_template(title="Delete Lesson")


# Videos Views
@admin.route('/videos', methods=['GET', 'POST'])
@login_required
def list_videos():
    """
    List all videos
    """
    check_admin()

    videos = Videos.query.all()

    return render_template('admin/videos/videos.html',
                           lessons=videos, title="Videos")


@admin.route('/videos/add', methods=['GET', 'POST'])
@login_required
def add_video():
    """
    Add a video to the database
    """
    check_admin()

    addVideo = True

    form = VideoForm()
    if form.validate_on_submit():
        video = Videos(name=form.name.data,
                       description=form.description.data,
                       link=form.link.data)
        try:
            # add video to the database
            db.session.add(video)
            db.session.commit()
            flash('You have successfully added a new video.')
        except exc.SQLAlchemyError:
            # in case video name already exists
            flash('Error: video name already exists.')

        # redirect to videos page
        return redirect(url_for('admin.list_videos'))

    # load video template
    return render_template('admin/videos/video.html', action="Add",
                           add_video=addVideo, form=form,
                           title="Add Video")


@admin.route('/videos/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_video(id):
    """
    Edit a video
    """
    check_admin()

    addVideo = False

    video = Videos.query.get_or_404(id)
    form = LessonForm(obj=video)
    if form.validate_on_submit():
        video.name = form.name.data
        video.description = form.description.data
        video.link = form.link.data
        db.session.commit()
        flash('You have successfully edited the video.')

        # redirect to the videos page
        return redirect(url_for('admin.list_videos'))

    form.description.data = video.description
    form.name.data = video.name
    form.link.data = video.link
    return render_template('admin/videos/video.html', action="Edit",
                           add_video=addVideo, form=form,
                           video=video, title="Edit Video")


@admin.route('/videos/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_video(id):
    """
    Delete a video from the database
    """
    check_admin()

    video = Videos.query.get_or_404(id)
    db.session.delete(video)
    db.session.commit()
    flash('You have successfully deleted the video.')

    # redirect to the videos page
    return redirect(url_for('admin.list_videos'))

    # return render_template(title="Delete Videos")
