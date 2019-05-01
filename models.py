import flask_sqlalchemy
db = flask_sqlalchemy.SQLAlchemy()
class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    deadline = db.Column(db.DateTime)
    is_done = db.Column(db.Boolean, nullable=False, default=False)


