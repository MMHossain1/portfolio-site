import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    experiences = [
        {"company": "MLH", "role": "Fellow", "year": "2026"},
        {"company": "Workday", "role": "Frontend Engineer", "year": "2025"}
    ]

    education = [
        {"school": "Trinity College Dublin", "degree": "Computer Science", "year": "2024"}
    ]

    hobbies = [
        {"name": "Reading", "description": "I enjoy books and articles."},
        {"name": "Photography", "description": "I love taking pictures."}
    ]

    return render_template(
        'index.html',
        experiences=experiences,
        education=education,
        hobbies=hobbies,
        title="MLH Fellow",
        url=os.getenv("URL")
        )
