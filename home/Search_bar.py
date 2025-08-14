from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template with a basic search bar
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Search Bar</title>
    <style>
        <body> {
            font-family: Ariak, sans-serif;
            text-align: center;
            padding-top: 50px;
        }
        input[type="text"] {
            width: 300px;
            padding: 10px;
            font-size: 16px;
        }
        button {
            padding: 10px 15px;
            font-size: 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h2>Search Menu Items</h2>
    <form method="GET">
        <input type="text" name="query"
        placeholder=" Search by name..." required>
            <button type="submit">Search</button>
    </form>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_template)

if __name__= "__main__":
    app.run(debug=True)