from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
prediction_val = 0

model = pickle.load(open('model_random.pkl', 'rb'))

@app.route('/', methods=['GET','POST'])
def predict():
    global prediction_val
    # data = request.get_json()  
    if request.method == 'POST':
        pm25 = request.form.get('PM2.5')
        pm10 = request.form.get('PM10')
        no = request.form.get('NO')
        no2 = request.form.get('NO2')
        co = request.form.get('CO')
        so2 = request.form.get('SO2')
        o3 = request.form.get('O3')
        prediction_val = model.predict([[pm25, pm10, no, no2, co, so2, o3]])
        print(prediction_val)
    
    return render_template('index.html', prediction= prediction_val)

if __name__ == '__main__':
    app.run(debug = True)
