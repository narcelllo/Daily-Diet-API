from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = "my_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/Daily-diet'

if __name__ == '__main__':
    app.run(debug=True)