from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route("/")
def init_browser():    
    executable_path = {'executable_path': ChromeDriverManager().install()}    
    return Browser('chrome', **executable_path, headless=False)

@app.route("/scrape")
def scrape():    
    mars_dict={}    
    browser = init_browser()

if __name__ == "__main__":
    app.run(debug=True)   