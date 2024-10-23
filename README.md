# QR Code Generator

## Overview
This project is a web-based QR Code generator that allows users to create QR Codes for various types of data including URLs, VCards, App Store links, images, and PDFs. The application is built using Flask, a lightweight web framework for Python, and utilizes the `qrcode` library for generating QR Codes.

## Features
- Generate QR Codes for:
  - URLs
  - VCards
  - App Store links
  - Images
  - PDFs
- Dynamic input fields based on selected QR Code type.
- Simple and attractive user interface.

## Prerequisites
Before running the application, make sure you have the following installed:
- Python 3.x
- pip (Python package installer)

## Installation Steps

1. **Clone the Repository**
   Clone this repository to your local machine using the following command:
   ```bash
   git clone <repository_url>
   cd <repository_name>
2. Create a Virtual Environment (Optional but recommended) Create a virtual environment to manage dependencies:
   python -m venv venv
   Activate the virtual environment:

   - For Windows:
    venv\Scripts\activate
   - For macOS/Linux:
    source venv/bin/activate
3. Install Required Packages Install the required packages using pip:

    - pip install Flask qrcode[pil]
4. Project Structure The project structure should look like this:
```
    QR_Code_Generator/
    ├── main.py
    ├── templates/
    │   ├── index.html
    │   └── show_qr.html
    └── static/
        └── qr_code.png (will be generated dynamically)
```
5. Create HTML Templates

   - index.html: The main form for inputting data to generate QR Codes. Includes dynamic input fields that show based on the selected QR Code type.
   - show_qr.html: Displays the generated QR Code.

    Example index.html:
```
      <!DOCTYPE html>
      <html lang="en">
      <head>
          ...
      </head>
      <body>
          <h1>QR Code Generator</h1>
          <form action="/generate" method="POST" enctype="multipart/form-data">
              ...
          </form>
          <script>
              function showFields() {
                  ...
              }
          </script>
      </body>
      </html>
```

6. Create the Flask Application In main.py, set up a basic Flask application:

      from flask import Flask, request, render_template, send_file
      import qrcode
      import os
      
      app = Flask(__name__)
      ...
7. Run the Application To run the application, use the following command:

     python main.py

     Access the application by navigating to http://127.0.0.1:5000/ in your web browser.

## Usage
1. Select the type of QR Code you want to generate from the dropdown menu.
2. Fill in the relevant fields based on the selected type.
3. Click the "Generate QR Code" button.
4. The generated QR Code will be displayed, and you can generate another if needed.

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to create an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
