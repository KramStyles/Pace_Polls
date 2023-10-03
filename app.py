from flask import Flask, render_template, request
from flask_login import (
    login_required,
    login_user,
    logout_user,
    LoginManager,
    current_user,
)
from functions import functions, dbfunctions
from users import User
from secrets import token_urlsafe
from config import *

app = Flask(__name__)
app.secret_key = token_urlsafe(18)
funcs = functions()
db = dbfunctions()
logManager = LoginManager(app)


@logManager.user_loader
def load_user(username):
    return User(username)


@app.context_processor
def showall():
    pg_vars = {
        "c_color": category_color,
        "replace": funcs.replacer,
        "user": current_user.get_id(),
        "fulldate": funcs.fulldate,
    }
    return dict(baseurl=BASE_URL, pg_vars=pg_vars)


@app.route("/create")
@login_required
def hello_poll():
    categories = db.select("category_table")
    info = {"title": "Pace Polls", "categories": categories}
    return render_template("index.html", pg=info)


@app.route("/login")
def login():
    info = {
        "title": "Sign In",
    }
    return render_template("login.html", pg=info)


@app.route("/elections")
def elections():
    info = {"title": "Elections"}
    return render_template("elections.html", pg=info)


@app.route("/logout")
def logout():
    logout_user()
    return login()


@app.route("/results/<title>")
def results(title):
    title = title.replace("%20", " ")

    if not db.select("poll_table", f'where title = "{title}" ', "title"):
        print("title", title)
        return not_found(title=title)
    else:
        try:

            def votePerc(vote, total, decimal=0):
                if decimal != 0:
                    percent = round((vote / total) * 100, decimal)
                else:
                    percent = round((vote / total) * 100)

                return percent

            file = open(f"static/files/{title}.km", "r")
            file = funcs.json_to_python(file.read())
            total_votes = []
            for name in file["text"]:
                votes = []
                for vote in file["text"][name]:
                    votes.append(vote[1])
                total_votes.append(sum(votes))
            info = {
                "title": title.title(),
                "questions": file,
                "total_votes": total_votes,
                "votePerc": votePerc,
                "main_total": sum(total_votes),
            }
            return render_template("results.html", pg=info)
        except Exception as err:
            print(str(err))
            return not_found(text="Result error occurred. Contact Admin!")


@app.route("/polls")
@app.route("/")
def polls():
    polls = db.select("poll_table", "ORDER BY id DESC LIMIT 15")
    info = {
        "title": "All Polls",
    }
    return render_template("polls.html", polls=polls, pg=info)


@app.route("/temp")
def temp_poll():
    info = {"title": "Pacesetter Polls"}
    return render_template("temp.html", pg=info)


@app.route("/polls/<title>")
def polls_title(title):
    title = title.replace("%20", " ")

    if not db.select("poll_table", f'where title = "{title}" ', "title"):
        return not_found(title=title)
    else:
        try:
            file = open(f"static/files/{title}.km", "r")
            file = funcs.json_to_python(file.read())
            info = {"title": title.title(), "questions": file}
            return render_template("single-poll.html", pg=info)
        except Exception as err:
            print(str(err))
            return not_found(text="File for the question not found. Contact Admin!")


@app.route("/admin/polls")
def adminPolls():
    polls = db.select("poll_table", "ORDER BY id DESC LIMIT 15")
    info = {
        "title": "All Polls",
    }
    return render_template("admin/polls.html", pg=info, polls=polls)


@app.route("/admin/polls/<title>")
def adminEditPolls(title):
    title = title.replace("%20", " ")
    if not db.select("poll_table", f"""where title = "{title}" """):
        return not_found("Incorrect Poll Item")
    else:
        categories = db.select("category_table")
        file = open(f"static/files/{title}.km", "r")
        poll = funcs.json_to_python(file.read())
        info = {"title": f"Edit Polls: {title}", "categories": categories}
    return render_template("admin/edit_poll.html", pg=info, poll=poll)


##########################################


@app.route("/admin_delete_poll", methods=["POST"])
def admin_delete_poll():
    idd = request.form["data_id"]
    msg = db.delete("poll_table", f"where id = {idd}")
    return msg


@app.route("/cast_votes", methods=["POST"])
def cast_votes():
    title = request.form["poll_parent_id"]
    questions = request.form
    votes = len(questions) - 1
    try:
        file = open(f"static/files/{title}.km", "r")
        raw = file.read()
        db_question = funcs.json_to_python(raw)
        for each in questions:
            if each != "poll_parent_id":
                for x in db_question["text"][each]:
                    if request.form[each] == x[0]:
                        x[1] += 1

        file.close()
        re_file = open(f"static/files/{title}.km", "w")
        re_raw = funcs.python_to_json(db_question)
        re_file.write(re_raw)
        re_file.close()
        db_vote = db.select("poll_table", f'where title = "{title}" ', "votes")[0][0]
        votes += db_vote
        db.update("poll_table", f"votes = {votes}", f'where title="{title}" ')
        return "ok"
    except Exception as err:
        return f"Err msg: {err}"


@app.route("/create_poll", methods=["POST"])
def create_poll():
    title = category = ""
    forms = {}
    key = ""
    c = 0
    poll_status = True
    msg = "okk"
    for item in request.form:
        if funcs.empty(item):
            msg = f"{item} shouldn't be empty"
        elif item == "poll-title_1":
            title = request.form[item].strip()
        elif item == "poll_category":
            category = request.form[item]
        elif item == "poll_status":
            if request.form[item] == "0":
                poll_status = False
        else:
            if item.find("question") >= 0:
                key = request.form[item]
                forms[request.form[item]] = []
                c = 0
            if item.find("option") >= 0:
                forms[key].append([request.form[item], 0])
            if item.find("colour") >= 0:
                forms[key][c].append([request.form[item]][0])
                c += 1
    try:
        if db.select("poll_table", f'where title = """{title}"""', "title"):
            msg = "Title already exists"
        else:
            questions = {"title": title, "text": forms, "category": category}
            db_questions = funcs.python_to_json(questions)

            noww = datetime.now().strftime("%A %B %d, %Y | %H:%M:%S")
            msg = db.insert(
                "poll_table",
                f'"{title}", "{category}", "{noww}" ',
                "title, category, date",
            )
            try:
                filename = f"{file_url}{title}.km"
                file = open(filename, "a")
                file.write(db_questions)
                file.close()
            except Exception as err:
                msg = "File making error: " + str(err)
    except Exception as err:
        msg = "Questions Error: " + str(err)
        print(err)
    return msg


@app.route("/admin_edit_poll", methods=["POST"])
def admin_edit_poll():
    # TODO: Work on editing polls
    return "hello"


@app.route("/admin_sign_in", methods=["POST"])
def admin_sign_in():
    username = request.form["username"]
    password = request.form["password"]
    msg = ""
    try:
        if db.select("admin_table", f"where username = '{username}'", "password"):
            db_password = db.select(
                "admin_table", f"where username = '{username}'", "password"
            )[0][0]
            if funcs.verify(password, db_password):
                user = User(username)
                login_user(user, remember=True)
                msg = "ok"
            else:
                msg = "Invalid Authentication"
        else:
            msg = "User not Found"
    except Exception as err:
        print("Login Error:", err)
        msg = "Login Error: " + str(err)
    return msg


# ERROR HANDLING PAGES
@app.errorhandler(404)
def not_found(error="", title="", text=""):
    if not title:
        title = "error 404 | page not found"
    if not text:
        text = "Sorry that page cannot be found!"
    info = {"title": title.title(), "text": text}
    return render_template("404.html", pg=info)


@app.errorhandler(401)
def no_permission(error="", title="", text=""):
    if not title:
        title = "access denied"
    if not text:
        text = "You are not supposed to be here! You should login (Admin)"
    info = {
        "title": title.title(),
        "text": text,
        "link_text": "Login",
        "link": "/login",
    }
    return render_template("404.html", pg=info)


# PAGE FUNCTIONS
def category_color(category):
    msg = db.select("category_table", f"where name = '{category}'", "colour")
    return msg[0][0]


if __name__ == "__main__":
    app.run(debug=True)
