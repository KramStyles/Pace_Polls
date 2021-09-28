import json, string, urllib, urllib.request, calendar, datetime, pymysql, random, re, sqlite3

from passlib import hash

# from flask_wtf import Form
# from wtforms import PasswordField, SubmitField, validators, StringField, TextAreaField
# from wtforms.fields.html5 import EmailField, TelField, URLField


"""
BITLY INFORMATION
"""

ROOT_URL = "https://api-ssl.bitly.com/v4/bitlinks"
SHORTEN = "/v4/shorten?access_token={}&longUrl={}"
ROOT = "https://bitly.com/oauth/authorize?client_id={}&client_secret={}&redirect_uri={}"
CLIENT_ID = "b2133124d547e7a5dca5cd33fa138c94bd1a47af"
CLIENT_SEC = "8c17c5bcf98e8648f15b597e63884cc94631a773"
"""https://bitly.com/oauth/authorize?client_id=b2133124d547e7a5dca5cd33fa138c94bd1a47af&client_secret=8c17c5bcf98e8648f15b597e63884cc94631a773&redirect_uri=http://127.0.0.1:5000"""

uploadFolder = '/static/uploads'
allowedExtensions = {'pdf', 'png', 'jpg', 'jpeg'}
allowedImageExtensions = {'png', 'jpg', 'jpeg'}

DBFile = 'static/site/db.sqlite'


class dbfunctions:
    def select(self, table, conditions='', what='*'):
        db = sqlite3.connect(DBFile, check_same_thread=False)
        cursor = db.cursor()
        sql = f"SELECT {what} FROM {table} {conditions};"
        try:
            result = cursor.execute(sql)
            msg = result.fetchall()
            print(sql)
            db.close()
        except Exception as err:
            print("SQL CODE: ", sql)
            print("Selection Error: ", err)
            msg = 'Selection Error. Contact Admin'
        finally:
            return msg

    def update(self, table, update, where=''):
        db = sqlite3.connect(DBFile, check_same_thread=False)
        cursor = db.cursor()
        sql = f"UPDATE {table} SET {update} {where}"
        try:
            cursor.execute(sql)
            db.commit()
            db.close()
            msg = 'ok'
        except Exception as err:
            print("SQL CODE: ", sql)
            print("Updating Error: ", err)
            msg = 'Error While Updating. Contact Admin'
        finally:
            return msg

    def delete(self, table, conditions=''):
        db = sqlite3.connect(DBFile, check_same_thread=False)
        cursor = db.cursor()

        sql = f"DELETE FROM {table} {conditions};"
        try:
            cursor.execute(sql)
            db.commit()
            db.close()
            msg = 'ok'
        except Exception as err:
            print("SQL CODE: ", sql)
            print("Delection Error: ", err)
            msg = 'Error While Deleting. Contact Admin'
        finally:
            return msg

    def insert(self, table, data, where=''):
        db = sqlite3.connect(DBFile, check_same_thread=False)
        cursor = db.cursor()
        sql = f"""INSERT INTO {table} ({where}) VALUES ({data})"""
        try:
            cursor.execute(sql)
            db.commit()
            db.close()
            msg = 'ok'
        except Exception as err:
            print("SQL CODE: ", sql)
            print("Insertion Error: ", err)
            msg = 'Error While Saving. Contact Admin'
        finally:
            return msg

    def count_sql(self, table, row, conditions=''):
        db = sqlite3.connect(DBFile, check_same_thread=False)
        cursor = db.cursor()
        sql = f"SELECT COUNT({row}) FROM {table} {conditions};"
        try:
            result = cursor.execute(sql)
            msg = result.fetchall()
            db.close()
        except Exception as err:
            print("SQL CODE: ", sql)
            print("Selection Error: ", err)
            msg = 'Selection Error. Contact Admin'
        finally:
            return msg

    def sum_sql(self, table, row, conditions=''):
        db = sqlite3.connect(DBFile, check_same_thread=False)
        cursor = db.cursor()
        sql = f"SELECT SUM({row}) FROM {table} {conditions};"
        try:
            result = cursor.execute(sql)
            msg = result.fetchall()
            db.close()
        except Exception as err:
            print("SQL CODE: ", sql)
            print("Selection Error: ", err)
            msg = 'Selection Error. Contact Admin'
        finally:
            return msg


class functions:
    def connect(self, database='delldb'):
        return pymysql.connect(host='localhost', user='root', passwd='', db=database)
        # def connect(self, database='prempfom_premiumgamesdb'):
        # return pymysql.connect(host='localhost', user='prempfom_admin', passwd='@GAMEZONE12345', db=database)

    def selector(self, table, condition='', what='*'):
        conn = self.connect()
        try:
            sql = "SELECT {} FROM {} {};".format(what, table, condition)
            print(sql)

            with conn.cursor() as con:
                con.execute(sql)
            return con.fetchall()
        finally:
            conn.close()

    def countsql(self, table, row, condition=''):
        conn = self.connect()
        try:
            sql = "SELECT COUNT({}) FROM {} {};".format(row, table, condition)
            print(sql)

            with conn.cursor() as con:
                con.execute(sql)
            return con.fetchall()
        finally:
            conn.close()

    def sumsql(self, table, row, condition=''):
        conn = self.connect()
        try:
            sql = "SELECT SUM({}) FROM {} {};".format(row, table, condition)
            print(sql)

            with conn.cursor() as con:
                con.execute(sql)
            return con.fetchall()
        finally:
            conn.close()

    def inserter(self, table, data, where=''):
        conn = self.connect()
        sql = "INSERT INTO " + table + " " + where + " values (" + data + ");"
        try:
            sql = "INSERT INTO " + table + " " + where + " values (" + data + ");"
            print(sql)
            with conn.cursor() as con:
                con.execute(sql)
                conn.commit()
                msg = 'ok'
        except Exception as err:
            msg = err
            print(err)
        finally:
            conn.close()  # CRUD CREATE, REVIEW, UPDATE, DELETE
        return msg

    def add_months(self, sourcedate, months):
        month = sourcedate.month - 1 + months
        year = sourcedate.year + month // 12
        month = month % 12 + 1
        day = min(sourcedate.day, calendar.monthrange(year, month)[1])
        return datetime.date(year, month, day)

    def deleter(self, table, condition=''):
        conn = self.connect()
        try:
            sql = "DELETE FROM {} {}".format(table, condition)
            print(sql)
            with conn.cursor() as con:
                con.execute(sql)
                conn.commit()
                msg = 'ok'
        except Exception as err:
            msg = err
            print(err)
        finally:
            conn.close()
        return msg

    def updater(self, table, update, where=''):
        conn = self.connect()
        try:
            sql = "UPDATE {} SET {} {}".format(table, update, where)
            print(sql)
            with conn.cursor() as con:
                con.execute(sql)
                conn.commit()
                msg = 'ok'
        except Exception as err:
            msg = err
            print(err)
        finally:
            conn.close()
        return msg

    def seckey(self, a, b):
        rand = random.randint(a, b)
        return rand

    def sanitizeString(self, input):
        whiteList = string.ascii_letters + string.digits + " !?$.,;:-'()&"
        filters = filter(lambda x: x in whiteList, input)
        return filters

    def htmlEn(self, input):
        if "<" in input or ">" in input:
            message = input.replace("<", "&lt;")
            message = message.replace(">", "&gt;")
            both = message
        else:
            both = input
        return both

    def htmlDe(self, input):
        if "&lt;" in input or "&gt;" in input:
            message = input.replace("&lt;", "<")
            message = message.replace("&gt;", ">")
            both = message
        else:
            both = input
        return both

    def password(self, password):
        password = hash.apr_md5_crypt.encrypt(password)
        return password

    def verify(self, password, dbpass):
        newpass = str(password)
        return hash.apr_md5_crypt.verify(newpass, dbpass)

    def inpck(self, data):
        if data:
            return self.htmlEn(data.strip())
        # elif not data.strip():
        #     return False

    def lowerInpck(self, data):
        if data:
            data = data.strip()
            return data.lower()

    def empty(self, vars):
        for items in vars:
            if not items:
                return True

    def formatDateTime(self, value):
        if type(value) == 'str':
            day = datetime.datetime.strptime(value, '%d/%m/%y')
            time = datetime.datetime.strptime(value, '%H:%M:%S')
        else:
            day = value.strftime("%Y-%m-%d")
            time = value.strftime("%H:%M:%S")
        result = [day, time]
        return result

    def calculateAge(self, birthDate):
        if type(birthDate) == str:
            birthDate = datetime.datetime.strptime(birthDate, "%Y-%m-%d")
        today = datetime.date.today()
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        return age

    def emptyValue(self, value):
        if value is None:
            value = ''
        return value

    def numbComma(self, val):
        if val is None:
            val = 0
        return "{:,}".format(val)

    def myfilter(self, myList):
        unique_list = []
        for x in myList:
            if x not in unique_list:
                unique_list.append(x)
        return unique_list

    def typeOf(self, value):
        return type(value)

    def telValidate(self, data):
        if data:
            if not data.isdigit():
                return "Only Numbers allowed. Remove '+'"
            elif len(data) != 11:
                if len(data) != 13:
                    return "11 Digits Allowed. 234 Allowed Too"
                else:
                    return 'ok'
            else:
                return 'ok'

    def username(self, data):
        if data:
            data = data.lower()
            data = data.strip()
            username = False
            if " " not in data:
                username = True
            return username

    def emailCheck(self, data):
        if data:
            email = False
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', data)
            if match != None:
                email = True
            return email

    def shorten(self, longURL):
        try:
            url = ROOT_URL + SHORTEN.format(CLIENT_ID, longURL)
            response = urllib.request.urlopen(url).read()
            jsonLoads = json.loads(response)
            return jsonLoads
        except Exception as err:
            print(err)

    def python_to_json(self, data):
        try:
            return json.dumps(data)
        except Exception as err:
            print(err)
            return err

    def mylist(self, data):
        newarray = []
        for item in data:
            item = item.__str__()
            newarray.append(item)
        # print(f"new is: {newarray}")
        return json.dumps(newarray)

    def printArray(self, array):
        resp = 'Response is: '
        for item in array:
            resp += f"{item}, "
        return resp

    def printForm(self, form):
        resp = "<center><b>Form elements:</b></center><br> "
        for item in form:
            resp += f"{item} = {form[item]} <br>"
        return resp

    def json_to_python(self, data):
        try:
            return json.loads(data)
        except Exception as err:
            print(err)
            return err

    def allowedFile(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowedImageExtensions

    def gen_string(self, size=7, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def fulldate(self):
        current_ = datetime.datetime.now()
        day = current_.strftime("%A")
        date = current_.strftime("%d")
        month = current_.strftime("%b")
        year = current_.strftime("%Y")
        msg = f"{day}, {month} {date} {year}"
        return msg

    def getYear(self):
        current_ = datetime.datetime.now()
        return current_.strftime("%Y")

    def greetings(self):
        current_ = datetime.datetime.now()
        current_hour = current_.hour
        if current_hour == 0 or current_hour <= 11:
            msg = "Good Morning"
        elif current_hour <= 16:
            msg = "Good Afternoon"
        else:
            msg = "Good Evening"
        return msg

    def total(self, one, two):
        if one == None:
            one = 0
        if two == None:
            two = 0
        result = one + two
        return "{:.2f}".format(result)

    def namestr(self, obj, namespace):
        return [name for name in namespace if namespace[name] is obj]

    def checkImportant(self, Arrays):
        msg = ''
        for x in Arrays:
            if self.inpck(x) == '':
                VAR = self.namestr(x, globals())
                msg += f"<br>{VAR} is Empty"
        return msg

    # def login(self, username, passwd, rem=None):
    #     retain = False
    #     if not username or not passwd:
    #         msg = "Fill all fields"
    #     else:
    #         if rem != None:
    #             retain = True
    #         if self.selector('users', "where username = '{}'".format(username), "username"):
    #             logdata = self.selector('users', 'where username = "{}" limit 1'.format(username),
    #                                          'username,password')
    #             dbpass = logdata[0][1]
    #             if self.verify(str(passwd), dbpass):
    #                 msg = 'ok'
    #             else:
    #                 msg = 'Invalid Account Details'
    #         else:
    #             msg = "User not found"
    #     return msg

# class contactFunctions(Form):
#     fullname = StringField('fullnames', validators=[validators.DataRequired()])
#     subject = StringField('subject', validators=[validators.DataRequired()])
#     email = EmailField('email', validators=[validators.DataRequired(), validators.Email()])
#     telephone = TelField('telephone', validators=[validators.DataRequired()])
#     textarea = TextAreaField('textarea', validators=[validators.DataRequired])
#     website = URLField('url')
#     submit = SubmitField('submit', [validators.DataRequired()])
#
#
# class loginFunctions(Form):
#     username = StringField('logUser', validators=[validators.DataRequired()])
#     password = PasswordField('logPassword', validators=[validators.DataRequired(), validators.Length(min=6,
#                                                                                                      message='Choose password of 6 or more characters')])
#     login = SubmitField('submit', [validators.DataRequired()])
#
#
# class regFunctions(Form):
#     username = StringField('regUser')
#     email = EmailField('regEmail', validators=[validators.DataRequired(), validators.Email()])
#     password = PasswordField('regPassword', validators=[validators.DataRequired(), validators.Length(min=6,
#                                                                                                      message='Choose password of 6 or more characters')])
#     cpassword = PasswordField('cpassword', validators=[validators.DataRequired(),
#                                                        validators.EqualTo(password, message='Passwords must match')])
#     register = SubmitField('submit', [validators.DataRequired()])
