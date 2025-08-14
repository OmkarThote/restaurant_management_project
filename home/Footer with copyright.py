from flask import Flask, render_template_string
from datetime import datetime

app = flask( __name__)

# Common data
restaurant_name = "Tasty Bites"
year = datetime.now().year

# Base HTML template
base_template = """
<!DOCTYPE html>
<html>
<head>
    <title> {{ Copyright }} </title>
    <style>
        <body> {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            min-height: 100vh;
            flex-direction: column;
        } 
        main{
            flex: 1;
            padding: 20px;
            text-align: center;
        }
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        {{ restaurant_name }} &copy;
        {{ year }}.
    All right reserved.
    </footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        "{% extends base %}{% block content %}
        <h1>Welcome to {{ restaurant_name }}</h1>
        {% endblock %}",
        base=base_template,
        title="Home",
        restaurant_name=restaurant_name,
        year=year
    )
if __name__= "__main__":
    app.run(debug=True)
    