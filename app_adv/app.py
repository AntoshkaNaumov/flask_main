from flask import Flask, jsonify
from views import AdvertisementView, OwnerView
from errors import ApiException

app = Flask("app")

@app.errorhandler(ApiException)
def error_handler(error: ApiException):
    response = jsonify({
        'status': 'error',
        'message': error.message
    })
    response.status_code = error.status_code
    return response


app.add_url_rule('/owners/<int:owner_id>', view_func=OwnerView.as_view('owners'), methods=['GET', 'PATCH',
                                                                                           'DELETE'])
app.add_url_rule('/owners/', view_func=OwnerView.as_view('owners_create'), methods=['POST'])

app.add_url_rule('/ads/<int:advertisement_id>', view_func=AdvertisementView.as_view('ads'), methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule('/ads/', view_func=AdvertisementView.as_view('ads_create'), methods=['POST'])


if __name__ == '__main__':
    app.run()