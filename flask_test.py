from app import app, db, cli
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db, 
        'User': User, 
        'Post': Post,
        'getAllUser': User.query.all(),
        'getAllPost': Post.query.all(),
        'john': User.query.get(1),
        'alvin': User.query.get(2),
        'susan': User.query.get(3)
    }