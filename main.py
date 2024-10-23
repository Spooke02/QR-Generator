from flask import Flask, request, render_template, send_file
import qrcode
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    qr_type = request.form['qrType']
    qr_code = None

    # Handle URL QR Code
    if qr_type == 'url':
        url = request.form['url']
        qr_code = qrcode.make(url)
    
    # Handle VCard QR Code
    elif qr_type == 'vcard':
        vcard_data = f"""
BEGIN:VCARD
VERSION:3.0
N:{request.form['name']}
FN:{request.form['fullname']}
TEL:{request.form['phone']}
EMAIL:{request.form['email']}
END:VCARD
"""
        qr_code = qrcode.make(vcard_data)
    
    # Handle App Store Link QR Code
    elif qr_type == 'appstore':
        appstore_link = request.form['appstore_link']
        qr_code = qrcode.make(appstore_link)
    
    # Handle Image QR Code (placeholders)
    elif qr_type == 'image':
        image_file = request.files['image_file']
        if image_file:
            image_path = os.path.join('static', image_file.filename)
            image_file.save(image_path)
            qr_code = qrcode.make(image_path)  # Placeholder for processing image
    
    # Handle PDF QR Code (placeholders)
    elif qr_type == 'pdf':
        pdf_file = request.files['pdf_file']
        if pdf_file:
            pdf_path = os.path.join('static', pdf_file.filename)
            pdf_file.save(pdf_path)
            qr_code = qrcode.make(pdf_path)  # Placeholder for processing PDF

    # Save generated QR code image
    qr_code_path = 'static/qr_code.png'
    qr_code.save(qr_code_path)
    return render_template('show_qr.html', qr_code_path=qr_code_path)

if __name__ == '__main__':
    app.run(debug=True)
