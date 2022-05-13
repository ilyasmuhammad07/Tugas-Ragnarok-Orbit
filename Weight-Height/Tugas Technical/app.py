from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def weight_prediction():
    if request.method == 'GET':
        return render_template("Weight-Height.html")
    elif request.method == 'POST':
        print(dict(request.form))
        weight_prediction = dict(request.form).values()
        weight_prediction = np.array([float(x) for x in weight_prediction])
        model, std_scaler = joblib.load("model-development/Weight-Height-Linear-Regresion.pkl")
        weight_prediction = std_scaler.transform([weight_prediction])
        print(weight_prediction)
        result = model.predict(weight_prediction)
        gender = {
            '0': 'Gender',
            '1': 'Height',
            '2': 'Weight'
        }
        result = gender[str(result[0])]
        return render_template('"Weight-Height.html', result=result)
    else:
        return "Unsupported Request Method"


if __name__ == '__main__':
    app.run(port=5000, debug=True)