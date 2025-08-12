from flask import Flask, render_template_string

app = Flask(__name__)

# Basic HTML template
contact_template = """
<DOCTYPE html>
<html>
<head>
    <title>Contact Us</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px; background-color: #f9f9f9; }
            .container { max-width: 600px; margin:auto; background: white; padding: 20px;
            border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0,1); }
            h1 { text-align: center; color: #333; }
            p { font-size: 16px; }
    </style>
</head>
<body>
    <div class="container">
    <h1>Contact Us</h1>
    <p><strong>Email:</strong>
    contact@example.com</p>
    <p><strong>Phone:</strong> +1 234 567 890</p>
    <p><strong>Address:</strong> 123 Main Street, City, Country</p>
    </div>
</body>
</html>
"""

@app.route("/contact")
def contact():
    return render_template_string(contact_template)

if __name__ == "__main__":
    app.run(debug=True)