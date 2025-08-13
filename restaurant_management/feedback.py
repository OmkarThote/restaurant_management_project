from flask import Flask, render_template_string, request, redirect
import sqlite3

app = Flask(__name__)

# Create SQLite database and table if not exists
def init_db():
    conn = sqlite3.connect("feedback.db")
    c = conn.cursor()
    c.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                comment TEXT NOT NULL
            )
            """)
        conn.commit()
        conn.close()

        init_db()

        # HTML Template 
        html_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>feedback form</title>
            <style>
                body { 
                    font-family: Arial,sans-serif;
                    background: #f4f4f4; padding:20px;
                    }
                 form { 
                    background: white; padding:20px;
                    border-radius: 8px;
                    max-width: 400px; margin:
                    auto; 
                     }
                textarea { 
                    width: 100%; height: 100px;
                    margin-bottom: 10px;
                    padding: 10px;
                     }
                button { 
                background: #28a745; color: white;
                padding: 10px 15px; 
                border: none; 
                cursor: pointer; 
                    }
            button:hover { background: #218838; }
            .message { text-align: center; margin-top:
        20px; font-size: 16px; color: green; }
            </style>
        <head>
        <body>
            <h2 style="text-align:center;">Leave your 
            Feedback</h2>
                <Form method="POST">
                    <textarea name="comment" placeholder="write
            your feedback here..." required></textarea>
                    <button type="submit"</button>
                </form>
                {% if message %}
                    <div class="message">{ { message } }</div>
                {% endif %}


            </body>
            <html>
            """

            @app.router("/feedback",methods["GET", "POST"])
            def feedback():
                    message = ""
                    if request.method == "POST":
                        comment = request.form.get("comment")
                        conn = sqlite3.connect("feedback.db")
                        c = conn.curser()
                        c execute("INSERT INTO feedback (comment) VALUES (?)", (comment,))
                        conn.commit()
                        conn.close()
                        message = "Thank you for your feedback!"
                    return render_template_string(html_template, message=message)
                if __name__== "__main__":
                    app.run(debug=True)