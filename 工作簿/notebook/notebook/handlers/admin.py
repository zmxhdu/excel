from flask import Blueprint, render_template, request, current_app
from notebook.decorators import admin_required
from notebook.models import Work

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
