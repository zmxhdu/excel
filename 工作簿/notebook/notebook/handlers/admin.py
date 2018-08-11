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


@admin.route('/works/<int:work_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_work(work_id):
    work = Work.query.get_or_404(work_id)
    form = WorkForm(obj=work)
    if form.validate_on_submit():
        form.update_work(work)
        flash('任务更新成功', 'success')
        return redirect(url_for('admin.works'))
    return render_template('admin/edit_work.html', form=form, work=work)


@admin.route('/works/<int:work_id>/delete')
@admin_required
def delete_work(work_id):
    work = Work.query.get_or_404(work_id)
    form = WorkForm(obj=work)
    form.delete_work(work)
    flash('任务删除成功', 'success')
    return redirect(url_for('admin.works'))
