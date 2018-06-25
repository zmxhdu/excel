# coding = utf-8
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'TRISK_USER'

    """用数值表示角色，方便判断是否有权限，比如说有个操作要角色为员工及以上的用户才可以做，那么只要判断 user.role >= ROLE_STAFF就可以了，数值之间设置了 10 的间隔是为了方便以后加入其他角色"""
    ROLE_USER = 10
    ROLE_STAFF = 20
    ROLE_ADMIN = 30

    user_id = db.Column('user_id', db.String(50), primary_key=True)  # 用户ID
    _user_password = db.Column('user_password', db.String(100), nullable=False)
    user_name = db.Column('user_name', db.String(100), nullable=False, unique=True)

    # user_works = db.relationship('Work')

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

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_staff(self):
        return self.role == self.ROLE_STAFF


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
    task_id = db.Column('task_id', db.String(50), db.ForeignKey('TRISK_TASK.task_id'))  # 任务 OA ID
    project_id = db.Column('project_id', db.String(50), db.ForeignKey('TRISK_PROJECT.project_id'))  # 项目ID
    transactor_id = db.Column('transactor_id', db.String(50), db.ForeignKey('TRISK_USER.user_id'))  # 经办人ID
    dev_id = db.Column('dev_id', db.String(50), db.ForeignKey('TRISK_USER.user_id'))  # 开发ID
    work_start = db.Column('work_start', db.DATE)
    development = db.Column('development', db.Integer)  # 开发进度
    work_status = db.Column('work_status', db.Integer)  # 开发状态
    work_text = db.Column('work_text', db.String(4000))
    work_end = db.Column('work_end', db.DATE)

    transactor_user = db.relationship('User', foreign_keys='Work.transactor_id')
    dev_user = db.relationship('User', foreign_keys='Work.dev_id')
