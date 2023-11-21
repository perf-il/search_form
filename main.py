from flask import Flask, request
from flask_restful import Api
from tinydb import TinyDB, Query

from services import search_form, find_field_type
from config.settings import DATABASE_NAME, DEBUG_MODE, HOST, PORT

app = Flask(__name__)
api = Api(app)
db = TinyDB(DATABASE_NAME)

app.config['JSON_AS_ASCII'] = False

Template = Query()


@app.route('/get_form', methods=['GET', 'POST'])
def get_template_form():
    if request.method == "GET":
        params = dict(request.args)
    elif request.method == "POST":
        params = dict(request.form)
    else:
        return {"error": "Bad request method"}
    result = search_form(params, db.all())
    if result:
        return {"form_name": result}
    else:
        result = {field: find_field_type(value) for field, value in params.items()}
        return result


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG_MODE)

