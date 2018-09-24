# coding = utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, ValidationError, SelectField, RadioField
from wtforms.validators import Length, Email, EqualTo, DataRequired, NumberRange
from notebook.models import db, User, Work


class RegisterForm(FlaskForm):
    user_name = StringField('用户', validators=[DataRequired(), Length(2, 100)])
    # user_email = StringField('邮箱', validators=[DataRequired(), Email()])
    user_id = StringField('帐号', validators=[DataRequired(), Length(3, 24)])
    user_password = PasswordField('密码', validators=[DataRequired(), Length(6, 24)])
    repeat_user_password = PasswordField('重复密码', validators=[DataRequired(), EqualTo('user_password')])
    submit = SubmitField('提交')

    def validate_user_name(self, field):
        if User.query.filter_by(user_name=field.data).first():
            raise ValidationError('用户名称已经存在')

    # def validate_user_email(self, field):
    #     if User.query.filter_by(user_email=field.data).first():
    #         raise ValidationError('邮箱已经存在')

    def create_user(self):
        user = User()
        user.user_name = self.user_name.data
        # user.user_email = self.user_email.data
        user.user_id = self.user_id.data
        user.user_password = self.user_password.data
        db.session.add(user)
        db.session.commit()

        return user


class LoginForm(FlaskForm):
    user_id = StringField('帐号', validators=[DataRequired(), Length(2, 100)])
    user_password = PasswordField('密码', validators=[DataRequired(), Length(6, 24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

    def validate_user_id(self, field):
        if field.data and not User.query.filter_by(user_id=field.data).first():
            raise ValidationError('帐号未注册')

    def validate_user_password(self, field):
        user = User.query.filter_by(user_id=self.user_id.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')


class ChangePassWordForm(FlaskForm):
    old_password = PasswordField('旧密码', validators=[DataRequired(), Length(6, 24)])
    new_password = PasswordField('新密码', validators=[DataRequired(), Length(6, 24)])
    repeat_new_password = PasswordField('重复新密码', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('提交')


class WorkForm(FlaskForm):
    task_id = IntegerField('任务 OA ID', validators=[DataRequired()])
    transactor_id = SelectField('经办人', validators=[DataRequired()])
    # dev_id = SelectField('开发人员', validators=[DataRequired()])
    work_text = TextAreaField('任务描述', validators=[DataRequired(), Length(2, 4000)])
    # development = RadioField('开发进度', validators=[DataRequired()])
    work_status = SelectField('任务状态', validators=[DataRequired()], choices=[('0', '未开始'), ('1', '正在进行'), ('2', '提交测试') ,('3', '完成'), ('-1', '暂停')])
    submit = SubmitField('提交')

    def __init__(self, *args, **kwargs):
        super(WorkForm, self).__init__(*args, **kwargs)
        self.transactor_id.choices = [(u.id, u.user_name) for u in User.query.all()]
        # self.dev_id.choices = [(u.id, u.user_name) for u in User.query.all()]
        # self.transactor_id.choices = [(u.id, u.user_name) for u in User.query.all()]


    def create_work(self):
        work = Work()
        self.populate_obj(work)
        db.session.add(work)
        db.session.commit()
        return work

    def update_work(self, work):
        self.populate_obj(work)
        db.session.add(work)
        db.session.commit()
        return work

    def delete_work(self, work):
        self.populate_obj(work)
        db.session.delete(work)
        db.session.commit()
