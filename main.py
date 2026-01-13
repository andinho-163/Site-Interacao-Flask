from dinhoflix import app

if __name__ == '__main__':
    app.run(debug=True)

with app.app_context():
    database.create_all()