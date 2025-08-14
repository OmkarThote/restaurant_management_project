from flask import Flask, render_template_string,
url_for

app = Flask(__name__)

# HTML template with Restaurant Logo
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Restaurant Homepage</title>
    <style>
        body {
            text-align: center;
            font-family: Arial, sans-serif;
            margin-top: 50px;
        }
        img {
            max-width: 300px;
            height: auto;
        }
    </style>
</head>
<body> 
    <h1>Welcome to Our Restaurant</h1>
    <img src="{{ url_for('static', filename='logo.png') }}" alt="Restaurant Logo">
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_template)

if __name__= "__main__"
    app.run(debug=True)