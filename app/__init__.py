"""
Flask application.

Routes map to pages. The PAGES list at the top is what the navbar loops over,
so adding a route + a PAGES entry makes it appear in the menu automatically.
This satisfies "Add a menu bar that dynamically displays other pages in the app".
"""

import os

from dotenv import load_dotenv
from flask import Flask, render_template

from . import data, data_mh

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

# Mohammed Hossain pages
PAGES_MH = [
    ("mh_home", "Home"),
    ("mh_about", "About"),
    ("mh_work", "Work"),
    ("mh_projects", "Projects"),
    ("mh_education", "Education"),
    ("mh_skills", "Skills"),
    ("mh_hobbies", "Hobbies"),
    ("mh_places", "Map"),
]


@app.context_processor
def inject_globals():
    # Makes these available to every template without passing them each time.
    return {"profile": data.PROFILE, "pages": PAGES, "pages_mh": PAGES_MH, "profile_mh": data_mh.PROFILE}


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


@app.route("/mh/home")
def mh_home():
    return render_template("mh/home.html", profile_mh=data_mh.PROFILE, about_mh=data_mh.ABOUT, work=data_mh.WORK)

@app.route("/mh/about")
def mh_about():
    return render_template("mh/about.html", about_mh=data_mh.ABOUT, honors_mh=data_mh.HONORS)

@app.route("/mh/work")
def mh_work():
    return render_template("mh/work.html", work=data_mh.WORK)

@app.route("/mh/education")
def mh_education():
    return render_template("mh/eductaion.html", education_mh=data_mh.EDUCATION)

@app.route("/mh/skills")
def mh_skills():
    return render_template("mh/skills.html", skills=data_mh.SKILLS)

@app.route("/mh/projects")
def mh_projects():
    return render_template("mh/projects.html", projects=data_mh.PROJECTS)

@app.route("/mh/hobbies")
def mh_hobbies():
    return render_template("mh/hobbies.html", hobbies=data_mh.HOBBIES)

@app.route("/mh/places")
def mh_places():
    return render_template("mh/places.html", places=data_mh.PLACES)
