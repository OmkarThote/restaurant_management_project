from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/reservations")
def reservations():
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Reservations</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
                text-align: center;
                margin-top 100px;
            }
            .placeholder {
                font-size: 20px;
                color: #555;
                border" 2px dashed #bbb;
                padding: 20px;
                display: inline-block;
                border-radius: 10px;
            }
        </style>
        </head>
        <body>
            <h1>Reservation Page</h1>
            <div class="placeholder">
                This is a placeholder for the Reservations page. Content coming soon!
            </div>
        </body>
    </html>
    """
    return render_template_string(html_template)

    if __name__== "__main__":
        app.run(debuug=True)