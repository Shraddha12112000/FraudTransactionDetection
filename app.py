from flask import Flask, render_template, request
import pickle
import numpy as np


app = Flask(__name__)
model = pickle.load(open('Model.pkl', 'rb'))
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def home():
    data_1 = float(request.form.get('Time'))
    data_2 = float(request.form.get('val1'))
    data_3 = float(request.form.get('val2'))
    data_4 = float(request.form.get('val3'))
    data_5 = float(request.form.get('val4'))
    data_6 = float(request.form.get('val5'))
    data_7 = float(request.form.get('val6'))
    data_8 = float(request.form.get('val7'))
    data_9 = float(request.form.get('val8'))
    data_10 = float(request.form.get('val9'))
    data_11 = float(request.form.get('val10'))
    data_12 = float(request.form.get('val11'))
    data_13= float(request.form.get('val12'))
    data_14= float(request.form.get('val13'))
    data_15= float(request.form.get('val14'))
    data_16= float(request.form.get('val15'))
    data_17= float(request.form.get('val16'))
    data_18= float(request.form.get('val17'))
    data_19= float(request.form.get('val18'))
    data_20= float(request.form.get('val19'))
    data_21= float(request.form.get('val20'))
    data_22= float(request.form.get('val21'))
    data_23= float(request.form.get('val22'))
    data_24= float(request.form.get('val23'))
    data_25 = float(request.form.get('val24'))
    data_26= float(request.form.get('val25'))
    data_27 = float(request.form.get('val26'))
    data_28= float(request.form.get('val27'))
    data_29= float(request.form.get('val28'))
    data_30= float(request.form.get('Amount'))

    arr = np.array([[data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_9,data_10, data_11, data_12, data_13, data_14,
                     data_15, data_16, data_17,
                     data_18, data_19,data_20,data_21,data_22, data_23, data_24, data_25, data_26, data_27,data_28,data_29,data_30]])
    pred = model.predict(arr)
    return render_template('result.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)