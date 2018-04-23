# coding = utf-8

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'TRISK_USER'

    user_id = db.Column('user_id', db.String(50), primary_key=True)  # 用户ID
    _user_password = db.Column('user_password', db.String(100), nullable=False)
    user_name = db.Column('user_name', db.String(100), nullable=False, unique=True)

    @property
    def password(self):
        """ Python风格的getter """
        return self._user_password

    @password.setter
    def password(self, orig_password):
        """ Python 风格的 setter，这样设置 user.user_password 就会自动为 password 生成哈希值存入 _user_password 字段
        """
        self._user_password = generate_password_hash(orig_password)

    def check_password(self, password):
        """判断用户输入的密码和存储的 hash 密码是否相等
        """
        return check_password_hash(self._user_password, password)


class Project(db.Model):
    __tablename__ = 'TRISK_PROJECT'

    project_id = db.Column('project_id', db.Integer, primary_key=True)  # 项目ID
    project_name = db.Column('project_name', db.String(50), nullable=False, unique=True)
    project_remarks = db.Column('project_remarks', db.String(4000), nullable=False)


class Task(db.Model):
    __tablename__ = 'TRISK_TASK'

    task_id = db.Column('task_id', db.String(50), primary_key=True)  # 任务 OA ID
    task_type = db.Column('task_type', db.String(10), nullable=False)
    task_detail = db.Column('task_detail', db.String(4000), nullable=False)


class Work(db.Model):
    __tablename__ = 'TRISK_WORK'

    work_id = db.Column('work_id', db.Integer, primary_key=True)
    task_id = db.Column('task_id', db.String(50), db.ForeignKey('Task.task_id'))  # 任务 OA ID
    project_id = db.Column('project_id', db.String(50), db.ForeignKey('Project.project_id'))  # 项目ID
    transactor_id = db.Column('transactor_id', db.String(50), db.ForeignKey('User.user_id'))  # 经办人ID
    dev_id = db.Column('dev_id', db.String(50), db.ForeignKey('User.user_id'))  # 开发ID
    work_start = db.Column('work_start', db.DATE)
    development = db.Column('development', db.Integer)  # 开发进度
    work_status = db.Column('work_status', db.Integer)  # 开发状态
    work_text = db.Column('work_text', db.String(4000))
    work_end = db.Column('work_end', db.DATE)
