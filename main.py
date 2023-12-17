from flask import Flask,request,jsonify
import os
from tensorflow import keras

PATH = os.getcwd()
IMAGE_LOCATION = os.path.join(PATH,"images")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app = Flask(__name__, static_url_path='/')
model = keras.models.load_model("MentalHealthV1.h5")

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predict(x):
    input = np.array(x)
    predictions = model.predict(x)
    return predictions

@app.route('/predict/', methods=['POST'])
def upload():
    if request.method == 'POST':
        data = request.get_json()

        data_array = json.loads(json_data)

        # predictions = predict(data_array)
        # data = {"prediction": predictions}
        return jsonify(data_array), 200
    else:
        respond.append({
            "message":"request error"
        })
    return jsonify(respond)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 443))