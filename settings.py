from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/database.db'
app.config['SQL_ALCHEMY_TRACK_MODIFICATIONS'] = False
