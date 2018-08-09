# coding = utf-8
from flask import abort
from flask_login import current_user
from functools import wraps
from notebook.models import User


def role_required(role):
    """ 带参数的装饰器， 可以使用它保护一个路由处理函数只能
    被特定角色的用户访问：
        @role_required(User.Admin)
        def main():
            pass
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 未登录用户或者角色不满足引发 404
            if not current_user.is_authenticated or current_user.user_role < role:
                abort(404)
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 特定角色的装饰器
staff_required = role_required(User.ROLE_STAFF)
admin_required = role_required(User.ROLE_ADMIN)
