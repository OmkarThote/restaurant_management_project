from django.shortcuts import render
from django.conf import settings


# Create your views here.
from flask import Flask, render_template

app = Flask(__name__)

def home():
    return()'''
    <h1>Welcome to Our Restaurant</h1>
    <p><a href="/about">About Us</a></p>
    '''

    def about():
        return'''
        <h1>About Us</h1>
        <p>Welcome to Gourmet Haven - where taste meets tradition! We serve freshly
        prepared dishes made from the finest ingredients, ensuring every bite is a delightful experience.</p>
        <img src="https://via.placeholder.com/400*250
        alt="Restaurant Image" />
        <p><a href="/">Back to Home</a></p>

    if __name__== '__main__':
        app.run(debug=True)

