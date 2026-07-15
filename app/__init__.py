"""
Flask application.

Routes map to pages. The PAGES list at the top is what the navbar loops over,
so adding a route + a PAGES entry makes it appear in the menu automatically.
This satisfies "Add a menu bar that dynamically displays other pages in the app".
"""

import os
import datetime
import importlib
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from peewee import *
from playhouse.shortcuts import model_to_dict

from . import data, data_mh

# pymysql = importlib.import_module("pymysql")
# pymysql.install_as_MySQLdb()

# # Always load .env from the project root, even when Flask is started elsewhere.
# PROJECT_ROOT = Path(__file__).resolve().parents[1]
# load_dotenv(PROJECT_ROOT / ".env")

app = Flask(__name__)

# mysql_database = os.getenv("MYSQL_DATABASE")
# if not mysql_database:
#     raise RuntimeError("MYSQL_DATABASE is not set. Create .env from example.env and fill MYSQL_* values.")

# my_db = MySQLDatabase(mysql_database,
#             user=os.getenv("MYSQL_USER"), 
#             password=os.getenv("MYSQL_PASSWORD"), 
#             host=os.getenv("MYSQL_HOST"),
#             port=3306
#         )

# print(my_db)

# class TimelinePost(Model):
#     name = CharField()
#     email = CharField()
#     content = TextField()
#     created_at = DateTimeField(default=datetime.datetime.now)

#     class Meta:
#         database = my_db

# my_db.connect()
# my_db.create_tables([TimelinePost])

# @app.route('/api/timeline_post', methods=['POST'])
# def post_timeline_post():
#     name = request.form.get('name')
#     email = request.form.get('email')
#     content = request.form.get('content')

#     timeline_post = TimelinePost.create(name=name, email=email, content=content)
#     return model_to_dict(timeline_post)


# @app.route('/api/timeline_post', methods=['GET'])
# def get_timeline_post():
#     timeline_posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
#     return {"timeline_posts": [model_to_dict(post) for post in timeline_posts]}


# @app.route('/api/timeline_post/<int:post_id>', methods=['DELETE'])
# def delete_timeline_post(post_id):
#     deleted_count = TimelinePost.delete_by_id(post_id)
#     if deleted_count:
#         return {"ok": True, "deleted_id": post_id}
#     return {"ok": False, "error": "Timeline post not found", "deleted_id": post_id}, 404


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
