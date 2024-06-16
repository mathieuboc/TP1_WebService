from flask import Flask
from ml import predict_image # On importe la fonction "predict_image" pour pouvoir l'appeler dans l'API 

app = Flask(__name__)

@app.route("/predict", methods= ["GET"])
def home():
    result = predict_image(None) # On appelle notre fonction dans l'api
    return result 


if __name__ == '__main__':
    app.run(host= "0.0.0.0", port=8081)
