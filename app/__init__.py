"""
Flask application.

Routes map to pages. The PAGES list at the top is what the navbar loops over,
so adding a route + a PAGES entry makes it appear in the menu automatically.
This satisfies "Add a menu bar that dynamically displays other pages in the app".
"""

import os
import datetime

from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from peewee import *
from playhouse.shortcuts import model_to_dict

from . import data, data_mh

load_dotenv()

app = Flask(__name__)

if os.getenv("TESTING") == "true":
    # In-memory SQLite database used only when running tests, so tests do not
    # depend on a running MySQL instance.
    mydb = SqliteDatabase(":memory:")
else:
    mydb = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306,
    )


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


if os.getenv("MYSQL_DATABASE") or os.getenv("TESTING") == "true":
    mydb.connect(reuse_if_open=True)
    mydb.create_tables([TimelinePost])

@app.route("/api/timeline_post", methods=["POST"])
def post_timeline_post():
    name = request.form.get("name")
    email = request.form.get("email")
    content = request.form.get("content")

    if not name:
        return "Invalid name", 400
    if not content:
        return "Invalid content", 400
    if not email or "@" not in email:
        return "Invalid email", 400

    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)


@app.route("/api/timeline_post", methods=["GET"])
def get_timeline_post():
    return {
        "timeline_posts": [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }


@app.route("/api/timeline_post/<int:post_id>", methods=["DELETE"])
def delete_timeline_post(post_id):
    deleted = TimelinePost.delete().where(TimelinePost.id == post_id).execute()
    if deleted == 0:
        return {"error": "post not found"}, 404
    return {"deleted": post_id}


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
    ("timeline", "Timeline"),
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
    return render_template("mh/home.html", profile_mh=data_mh.PROFILE, about_mh=data_mh.ABOUT, work=data_mh.WORK)


@app.route('/mh/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")


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
    return render_template("mh/education.html", education_mh=data_mh.EDUCATION)


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