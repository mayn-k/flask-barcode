from flask import Flask, render_template, request

app = Flask(__name__)

previous_barcode = None

@app.route('/')
def index():
    return render_template('index.html', previous_barcode=previous_barcode)

@app.route('/scan', methods=['POST'])
def scan():
    global previous_barcode
    barcode_data = request.form['barcode_data']
    previous_barcode = barcode_data  # Store the current barcode in the global variable
    return render_template('scan.html', barcode_data=barcode_data)

if __name__ == '__main__':
    app.run(debug=True)
