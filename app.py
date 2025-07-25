from flask import Flask,request,jsonify,render_template
import tensorflow as tf
from utils import preprocess_text

model=tf.keras.models.load_model('model/fake_news_model1.keras')
app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    data=request.get_json()
    if 'text' not in data:
        return jsonify({"error":"missing text in request",}),400
    processed=preprocess_text(data['text'])
    prediction=model.predict(processed)
    label='Fake news' if prediction[0][0]>=0.5 else 'Real news'
    return jsonify({"prediction": label, "confidence": float(prediction[0][0])})

if __name__ == "__main__":
    app.run(debug=True)