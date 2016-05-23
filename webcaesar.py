from flask import Flask, render_template, request
import pycaesar

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        # TODO: sanitize input
        cipher_text = pycaesar.encrypt(request.form.get('plain_text'), request.form.get('key'))
        return render_template('index.html', cipher_text=cipher_text)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
