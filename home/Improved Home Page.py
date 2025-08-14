from flask import Flask, render_template_string,
url_for

app = Flask(__name__)

# HTML template with CSS styling
html_template = """ 
<!DOCTYPE html>
<html>
<head>
    <title>Restaurant Homepage</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            background-color: #f8f8f8;
            margin: 0;
            padding: 0; 
        }
        header {
            background-color: #ff6347;
            color: white;
            padding: 20px;
            font-size: 28px;
            font-width: bold;
        }
        img {
            max-width: 250px;
            height: auto;
            margin-top: 30px;
        }
        .container {
            margin: 40px auto;
            width: 60%;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0,1);
        }
        p {
            font-size: 18px;
            color: #333;
        }
    </style>
<body>
    <header>Welcome to Our Restaurant</header>
    <div class="container">
        <img src="{{ url_for('static', filename='logo.png') }}" alt="Restaurant Logo">
        <p>Enjoy the best food in town with a warm and welcoming atmosphere.</p>
        </div>
    </body>
    </html>
    """

    @app.route("/)
    def home():
        return render_template_string(html_template)
    
    if __name__= "__main__":
        app.run(debug=True)