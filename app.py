from flask import Flask, request, render_template
from ner_recognition import ner_recognition
from flask import jsonify
from ner_recognition import ner_recognition



app = Flask(__name__)

@app.route('/')
def home():
       return render_template('home.html')
       
@app.route('/predict',methods=['POST'])

def predict():
	if request.method == 'POST':
		data = request.form['oraciones'] ## extrae el input
		response = ner_recognition(data) ## funcion para extraer los NER y generar el diccionario final.
	return jsonify(response) # aplica jsonify para regresar un str


if __name__ == '__main__':
	app.run(debug=True)
    #app.run(host='0.0.0.0', debug=True)
app.config['JSON_AS_ASCII'] = False