from flask import Flask
from models import db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:secret@database/testdatabase'
db.init_app(app)
@app.route('/test-connection')
def hello():
    try:
        db.session.query('1').all()
        return 'Connected.'
    except Exception as e:
        return str(e)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


