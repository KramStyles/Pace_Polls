from flask import Flask, render_template, request
from functions import functions, dbfunctions
from config import *

app = Flask(__name__)
funcs = functions()
db = dbfunctions()


@app.context_processor
def showall():
    pg_vars = {
        'c_color': category_color,
        'replace': funcs.replacer,
    }
    return dict(baseurl=BASE_URL, pg_vars=pg_vars)


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
    info = {
        'title': 'Sign In',
    }
    return render_template('login.html', pg=info)


@app.route('/results/<title>')
def results(title):
    if not db.select('poll_table', f"where title = '{title}'", "title"):
        return not_found(title=title)
    else:
        try:
            def votePerc(vote, total, decimal=0):
                if decimal != 0:
                    percent = round((vote / total) * 100, decimal)
                else:
                    percent = round((vote / total) * 100)

                return percent

            file = open(f"static/files/{title}.km", 'r')
            file = funcs.json_to_python(file.read())
            total_votes = []
            for name in file['text']:
                votes = []
                for vote in file['text'][name]:
                    votes.append(vote[1])
                total_votes.append(sum(votes))
            info = {
                'title': title.title(),
                'questions': file,
                'total_votes': total_votes,
                'votePerc': votePerc,
                'main_total': sum(total_votes)
            }
            return render_template('results.html', pg=info)
        except Exception as err:
            print(str(err))
            return not_found(text="Result error occurred. Contact Admin!")


@app.route('/polls')
def polls():
    polls = db.select('poll_table', "ORDER BY id DESC LIMIT 15")
    info = {
        'title': 'All Polls',
    }
    return render_template('polls.html', polls=polls, pg=info)


@app.route('/polls/<title>')
def polls_title(title):
    if not db.select('poll_table', f"where title = '{title}'", "title"):
        return not_found(title=title)
    else:
        try:
            file = open(f"static/files/{title}.km", 'r')
            file = funcs.json_to_python(file.read())
            info = {
                'title': title.title(),
                'questions': file
            }
            return render_template('single-poll.html', pg=info)
        except Exception as err:
            print(str(err))
            return not_found(text="File for the question not found. Contact Admin!")


@app.route('/admin/polls')
def adminPolls():
    polls = db.select('poll_table', "ORDER BY id DESC LIMIT 15")
    info = {
        'title': 'Edit Polls Polls',
    }
    return render_template('admin/polls.html', polls=polls, pg=info)

##########################################

@app.route('/cast_votes', methods=['POST'])
def cast_votes():
    title = request.form['poll_parent_id']
    questions = request.form
    votes = len(questions) - 1
    try:
        file = open(f'static/files/{title}.km', 'r')
        raw = file.read()
        db_question = funcs.json_to_python(raw)
        for each in questions:
            if each != "poll_parent_id":
                for x in db_question['text'][each]:
                    if request.form[each] == x[0]:
                        x[1] += 1

        file.close()
        re_file = open(f'static/files/{title}.km', 'w')
        re_raw = funcs.python_to_json(db_question)
        re_file.write(re_raw)
        re_file.close()
        db_vote = db.select('poll_table', f"where title = '{title}'", 'votes')[0][0]
        votes += db_vote
        db.update('poll_table', f"votes = {votes}", f"where title='{title}'")
        return 'ok'
    except Exception as err:
        return f"Err msg: {err}"


@app.route('/create_poll', methods=['POST'])
def create_poll():
    title = category = ''
    forms = {}
    key = ""
    c = 0
    poll_status = True
    msg = 'okk'
    for item in request.form:
        if funcs.empty(item):
            msg = f"{item} shouldn't be empty"
        elif item == 'poll-title_1':
            title = request.form[item].strip()
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
            questions = {
                'title': title,
                'text': forms,
                'category': category
            }
            db_questions = funcs.python_to_json(questions)
            noww = datetime.now().strftime("%A %B %d, %Y | %H:%M:%S")
            msg = db.insert('poll_table', f"""'{title}', '{category}', '{noww}'""", "title, category, date")
            try:
                filename = f"{file_url}{title}.km"
                file = open(filename, 'a')
                file.write(db_questions)
                file.close()
            except Exception as err:
                msg = "File making error: " + str(err)
    except Exception as err:
        msg = "Questions Error: " + str(err)
        print(err)
    return msg


# ERROR HANDLING PAGES
@app.errorhandler(404)
def not_found(error='', title='', text=''):
    if not title:
        title = "error 404 | page not found"
    if not text:
        text = "Sorry that page cannot be found!"
    info = {
        'title': title.title(),
        'text': text
    }
    return render_template('404.html', pg=info)


# PAGE FUNCTIONS
def category_color(category):
    msg = db.select('category_table', f"where name = '{category}'", 'colour')
    return msg[0][0]


if __name__ == '__main__':
    app.run(debug=True)
