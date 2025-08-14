from flask import Flask, render_template_string

app = Flask(__name__)

#HTML template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Error Handling</title>
</head>
<body>
    <h2>{{ message }}</h2>
</body>
</html>
"""

@app.route("/")
def home():
    try:
        # Simulating database access
        result = get_data_from_db()
        message = f"Data fetched successfully: {result}"
        except Exception as e:
            message = f"An error occurred: {str(e)}"
        return render_template_string(html_template, message=message)

def get_data_from_db():
    # Simulating a database error
    raise ConnectionError("Unable to connect to the database")

if __name__= "__main__":
    app.run(debug=True)