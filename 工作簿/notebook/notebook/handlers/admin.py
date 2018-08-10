from flask import Blueprint, render_template, request, current_app, flash, redirect, url_for
from notebook.decorators import admin_required
from notebook.models import Work
from notebook.forms import WorkForm

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/')
@admin_required
def index():
    return render_template('admin/index.html')


@admin.route('/works')
@admin_required
def works():
    page = request.args.get('page', default=1, type=int)
    pagination = Work.query.paginate(
        page=page,
        per_page=current_app.config['ADMIN_PER_PAGE'],
        error_out=False
    )
    return render_template('admin/works.html', pagination=pagination)


@admin.route('/works/create', methods=['GET', 'POST'])
@admin_required
def create_work():
    form = WorkForm()
    if form.validate_on_submit():
        form.create_work()
        flash('任务添加成功', 'success')
        return redirect(url_for('admin.works'))
    return render_template('admin/create_work.html', form=form)
