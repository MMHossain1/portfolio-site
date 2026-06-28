import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    experiences = [
        {"company": "MLH", "role": "Fellow", "year": "2026", "description": "• Gaining hands-on experience in production engineering with Meta & Major Leage Hacking"},
        {"company": "Workday", "role": "Software Engineer", "year": "2026", "description": "• Developed frontend architecture using Next.js and TypeScript"},
        {"company": "HackEurope", "role": "Associate", "year": "2026", "description": "• Supporting Operations and Sponsor Engagement"}
    ]

    education = [
        {"university": "Trinity College Dublin", "degree": "Computer Science", "year": "2024"}
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
