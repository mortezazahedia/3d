from easystudy import app,db
from easystudy.models import User, Post

with app.app_context():
    # Create all tables
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)



