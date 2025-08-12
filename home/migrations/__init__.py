from flask import Flask, render_template_string

app = Flask(__name__)

# HTML with CSS styling embedded
HTML_PAGE = ""
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