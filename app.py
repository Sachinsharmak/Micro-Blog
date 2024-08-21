import datetime
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGO_URI"))
    app.db = client.microblog

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%y-%m-%d")  # Two-digit year
            app.db.entries.insert_one({"content": entry_content, "date": formatted_date})

        entries_with_date = [
            {
                "_id": str(entry["_id"]),  # Convert ObjectId to string for template use
                "content": entry["content"],
                "date": entry["date"],
                "formatted_date": datetime.datetime.strptime(entry["date"], "%y-%m-%d").strftime("%b %d")
            }
            for entry in app.db.entries.find({})
        ]

        return render_template("home.html", entries=entries_with_date)

    @app.route("/delete/<id>", methods=["POST"])
    def delete_entry(id):
        app.db.entries.delete_one({"_id": ObjectId(id)})
        return redirect(url_for("home"))

    @app.route("/update/<id>", methods=["GET", "POST"])
    def update_entry(id):
        if request.method == "POST":
            new_content = request.form.get("content")
            app.db.entries.update_one({"_id": ObjectId(id)}, {"$set": {"content": new_content}})
            return redirect(url_for("home"))

        entry = app.db.entries.find_one({"_id": ObjectId(id)})
        return render_template("update.html", entry=entry)

    @app.route("/view/<id>", methods=["GET"])
    def view_entry(id):
        entry = app.db.entries.find_one({"_id": ObjectId(id)})
        entry_with_date = {
            "content": entry["content"],
            "date": entry["date"],
            "formatted_date": datetime.datetime.strptime(entry["date"], "%y-%m-%d").strftime("%b %d")
        }
        return render_template("view.html", entry=entry_with_date)

    return app
