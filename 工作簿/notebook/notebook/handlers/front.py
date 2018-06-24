# coding = utf-8
from flask import Blueprint, render_template, flash, url_for, redirect
from flask import request, current_app
from notebook.models import db, User, Work
from notebook.forms import LoginForm, RegisterForm
from flask_login import login_user, logout_user, login_required


front = Blueprint('front', __name__)


@front.route('/')
def index():
    page = request.args.get('page', default=1, type=int)
    pagination = Work.query.paginate(
        page=page,
        per_page=current_app.config['INDEX_PER_PAGE'],
        error_out=False
    )

    return render_template('index.html', pagination=pagination)


@front.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_name=form.user_name.data).first()
        logout_user(user, form.remember_me.data)
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
