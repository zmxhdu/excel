# coding = utf-8
from flask import Blueprint, render_template, flash, url_for, redirect
from flask import request, current_app, abort
from notebook.models import db, User, Work
from notebook.forms import LoginForm, RegisterForm, ChangePassWordForm
from flask_login import login_user, logout_user, login_required, current_user


front = Blueprint('front', __name__)


@front.route('/')
def index():
    page = request.args.get('page', default=1, type=int)
    pagination = db.session.query(Work.task_id, Work.project_id, Work.work_status, Work.work_text, Work.work_id,
                                  User.user_name).join(User, User.user_id == Work.transactor_id).paginate(
        page=page,
        per_page=current_app.config['INDEX_PER_PAGE'],
        error_out=False
    )

    return render_template('index.html', pagination=pagination)


@front.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_id=form.user_id.data).first()
        login_user(user, form.remember_me.data)
        return redirect(url_for('.index'))

    return render_template('login.html', form=form)


@front.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功，请登录！', 'success')

        return redirect(url_for('.login'))
    return render_template('register.html', form=form)


@front.route('/logout')
def logout():
    logout_user()
    flash('您已经退出登录', 'success')
    return redirect(url_for('.index'))


@front.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePassWordForm()
    if form.validate_on_submit():
        if current_user.check_password(form.old_password.data):
            current_user.user_password = form.new_password.data
            db.session.add(current_user)
            db.session.commit()
            flash('密码修改成功，请重新登录')
            logout_user()
            return redirect(url_for('.login'))
        else:
            flash('密码错误')
    return render_template('change_password.html', form=form)
