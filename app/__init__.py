"""
Flask application.

Routes map to pages. The PAGES list at the top is what the navbar loops over,
so adding a route + a PAGES entry makes it appear in the menu automatically.
This satisfies "Add a menu bar that dynamically displays other pages in the app".
"""

import os

from dotenv import load_dotenv
from flask import Flask, render_template

from . import data

load_dotenv()

app = Flask(__name__)

# Anything secret/configurable comes from the environment, never hardcoded.
# See example.env. This satisfies the "use environment variables" tip.
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-only-change-me")

# The navbar renders from this list. (endpoint, label) pairs.
# Add a tuple here and the link shows up in the menu on every page.
PAGES = [
    ("index", "Home"),
    ("about", "About"),
    ("work", "Work"),
    ("projects", "Projects"),
    ("education", "Education"),
    ("skills", "Skills"),
    ("hobbies", "Hobbies"),
    ("places", "Map"),
]


@app.context_processor
def inject_globals():
    # Makes these available to every template without passing them each time.
    return {"profile": data.PROFILE, "pages": PAGES}


@app.route("/")
def index():
    return render_template("index.html", about=data.ABOUT)


@app.route("/about")
def about():
    return render_template("about.html", about=data.ABOUT, honors=data.HONORS)


@app.route("/work")
def work():
    return render_template("work.html", work=data.WORK)


@app.route("/projects")
def projects():
    return render_template("projects.html", projects=data.PROJECTS)


@app.route("/education")
def education():
    return render_template(
        "education.html", education=data.EDUCATION, publications=data.PUBLICATIONS
    )


@app.route("/skills")
def skills():
    return render_template("skills.html", skills=data.SKILLS)


@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html", hobbies=data.HOBBIES)


@app.route("/places")
def places():
    return render_template("places.html", places=data.PLACES)
