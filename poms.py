from app import app, db
from app.models import User, Poms

@app.shell_context_processor
def make_shell_contect():
    return {'db': db, 'User': User, 'Poms': Poms}