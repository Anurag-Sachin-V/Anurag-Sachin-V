import pickle
from flask import Flask, render_template, request

app= Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods= ['GET','POST'])
def predict():
    try:
        data = request.form #stores data as strings
        features = [float(data[i]) for i in data] #converts data to float inlisg
    # (features)print

    #passing features list into model

        prediction = model.predict([features])
        output = round(prediction[0],2)

        return render_template('index.html', prediction_text= f'price of the house is {output}/-')
    
    except:
        return render_template('index.html', prediction_text= 'Something went wrong!')

if __name__=='__main__':
    app.run(debug=True)