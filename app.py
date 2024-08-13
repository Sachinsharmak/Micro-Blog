import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient
import os 
from dotenv import load_dotenv
load_dotenv()
def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGO_URI"))
    app.db = client.microblog
    entries = []

    @app.route("/", methods=["GET", "POST"])
    def home():
        # print([e for e in app.db.entries.find({})])
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%y-%m-%d")  # Two-digit year
            # entries.append((entry_content, formatted_date))
            app.db.entries.insert_one({"content":entry_content, "date":formatted_date})
        
        entries_with_date = [
            (
                entry["content"],
                entry["date"],
                datetime.datetime.strptime(entry["date"], "%y-%m-%d").strftime("%b %d")  # Two-digit year
            )
            for entry in app.db.entries.find({})
        ]
        
        return render_template("home.html", entries=entries_with_date)
    return app