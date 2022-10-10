from flask import Flask, request, render_template
from model.model import Translator
import os
import logging

app = Flask(__name__, template_folder='website')  

# create instance
model = Translator('./model/final_model.h5')
logging.basicConfig(level=logging.INFO)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['GET', 'POST'])
def predict():
    english_sentence = request.form["input"]
    french_sentence = model.translate(english_sentence)
    return render_template('index.html', translation=french_sentence)

def main():
    """Run the Flask app."""
    port=int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=port, debug=True) 

if __name__ == "__main__":
    main()