from flask import Flask, render_template, request
from functions import functions, dbfunctions
from config import *

app = Flask(__name__)
funcs = functions()
db = dbfunctions()


@app.route('/')
def hello_poll():
    categories = db.select('category_table')
    info = {
        'title': 'Pace Polls',
        'categories': categories
    }
    return render_template('index.html', pg=info)


@app.route('/login')
def login():
    return render_template('login.html')


##########################################
@app.route('/create_poll', methods=['POST'])
def create_poll():
    title = category = ''
    questions = {}
    forms = {}
    key = ""
    c = 0
    poll_status = True
    msg = 'okk'
    for item in request.form:
        if funcs.empty(item):
            msg = f"{item} shouldn't be empty"
        elif item == 'poll-title_1':
            title = request.form[item]
        elif item == 'poll_category':
            category = request.form[item]
        elif item == 'poll_status':
            if request.form[item] == '0':
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
        if db.select('poll_table', f"where title = '{title}'", "title"):
            msg = "Title already exists"
        else:
            db_questions = funcs.python_to_json(forms)
            noww = datetime.now().strftime("%A %B %d, %Y | %H:%M:%S")
            msg = db.insert('poll_table', f"""'{title}', '{category}', "{db_questions}", '{noww}'""", "title, category, questions, date")
    except Exception as err:
        msg = "Questions Error: " + str(err)
        print(err)
    return msg


if __name__ == '__main__':
    app.run(debug=True)
