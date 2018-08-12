# coding = utf-8
from flask import Blueprint, render_template
from flask_login import login_required
from notebook.models import Work, Task, Project

work = Blueprint('work', __name__, url_prefix='/works')

@work.route('/<int:work_id>')
def detail(work_id):
    work = Work.query.get_or_404(work_id)
    return render_template('work/detail.html', work=work)
