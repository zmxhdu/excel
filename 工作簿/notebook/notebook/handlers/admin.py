from flask import Blueprint, render_template, request, current_app
from notebook.decorators import admin_required

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/')
@admin_required
def index():
    return render_template('admin/index.html')
