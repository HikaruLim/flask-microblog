from flask import render_template
from app import app,db

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()  # 会话重置为干净状态，数据库不受错误污染
    return render_template('500.html'),500