from msilib.schema import Error
from tkinter import EXCEPTION
from flask import Flask, render_template, request, redirect, send_file
from scrapper_copy_remote import extract_inform_remote
from scrapper_wework import extract_inform_wework
from save import save_to_file
app = Flask("SuperScrapper")


db = {}


def get_jobs(name):
    remote_result = extract_inform_remote(name)
    wework_result = extract_inform_wework(name)
    return remote_result + wework_result

@app.route("/")
def home():
    return render_template("support.html")
    return "Hello! Welcome to mi casa!"

@app.route('/report')
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
        #print(jobs)
    else:
        return redirect("/")
    return render_template("report.html", 
    searchingBy=word,
    resultsNumber = len(jobs),
    jobs=jobs
    )
    return f"You are looking for a job in {word}"

@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs =db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")


app.run(host="0.0.0.0")