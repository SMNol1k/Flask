from flask import Flask, request, jsonify, Response
from flask.views import MethodView

from models import Session, Ad
import sqlalchemy
from errors import HttpError

app = Flask('Ad')

@app.before_request
def before_request():
    session = Session()
    request.session = session

@app.after_request
def after_request(response: Response):
    request.session.close()
    return response

@app.errorhandler(HttpError)
def error_errorhandler(err: HttpError):
    json_response = jsonify({"status": "error", "message": err.message})
    json_response.status_code = err.status_code
    return json_response

def get_Ad_by_id(ad_id):
    ad: Ad = request.session.get(Ad, ad_id)
    if ad is None:
        return jsonify({'error': 'Ad not found'}), 404
    return ad

def delete_Ad_by_id(ad_id):
    ad: Ad = get_Ad_by_id(ad_id)
    request.session.delete(ad)
    request.session.commit()

def add_Ad(ad: Ad):
    request.session.add(ad)
    try:
        request.session.commit()
    except sqlalchemy.exc.IntegrityError:
        raise HttpError(409, "user already exists")
    
class AdView(MethodView):
    def get(self, ad_id):
        ad = get_Ad_by_id(ad_id)
        return jsonify(ad.dict)
    
    def post(self):
        ad_data = request.get_json()

        ad = Ad(**ad_data)
        add_Ad(ad)
        return jsonify(ad.dict)
    
    def delete(self, ad_id):
        delete_Ad_by_id(ad_id)
        return jsonify({'message': 'Ad deleted'})
    
ad_view = AdView.as_view('Ad')

app.add_url_rule('/api/<int:ad_id>', view_func=ad_view, methods=['GET', 'DELETE'])
app.add_url_rule('/api', view_func=ad_view, methods=['POST'])

app.run()
