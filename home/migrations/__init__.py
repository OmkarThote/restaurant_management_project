from flask import Flask, render_template_string

app = Flask(__name__)

# HTML with CSS styling embedded
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Styled Homepage</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        p {
            font-size: 18px;
            color: #555;
            line-height: 1.6;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Homepage</h1>
    <p>This is a simple page with basic CSS styling.</p>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(debug=True)