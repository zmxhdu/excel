# coding = utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, ValidationError
from wtforms.validators import Length, Email, EqualTo, DataRequired
from notebook.models import db, User, Work


class RegisterForm(FlaskForm):
    user_name = StringField('用户名称', validators=[DataRequired(), Length(2,100)])
    # user_email = StringField('邮箱', validators=[DataRequired(), Email()])
    user_id = StringField('用户名', validators=[DataRequired(), Length(3,24)])
    user_password = PasswordField('密码', validators=[DataRequired(), Length(6,24)])
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
    user_id = StringField('用户名', validators=[DataRequired(), Length(2, 100)])
    user_password = PasswordField('密码', validators=[DataRequired(), Length(6, 24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

    def validate_user_id(self, field):
        if field.data and not User.query.filter_by(user_id=field.data).first():
            raise ValidationError('用户名未注册')

    def validate_user_password(self, field):
        user = User.query.filter_by(user_id=self.user_id.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')
