from flask import Flask, render_template_string

app = Flask(__name__)

# common footer content
opening_hours = "Mon-Fri: 11am-9pm, Sat-Sun: 10am-10pm"

# base HTML template with footer
base_template = """
<!DOCTYPE html>
<html>
<head>
    <title> Restaurant Open </title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        main {
            flex: 1;
            padding: 20px;
            text-align: cenetr;
        }
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding : 10px 0;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <main>
        {% block content %}
        {%  endblock %}
    </main>
    <footer>
        {{ opening_hours }}
    </footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        "{% extends base %} {% block content %}
        <h1>Reservation Page</h1> 
        <p> \Coming soon!</p>
        {% endblock %}",
        base=base_template,
        title="Reservations",
        opening_hours=opening_hours
    )

if __name__== "__main__":
    app.run(debug=True)