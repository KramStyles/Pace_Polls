from app import app, render_template, make_response, request, User, login_user, datetime, login_required \
    , logout_user, current_user, timedelta, force, redirect
from config import *
from functions import functions, dbfunctions

funcs = functions()
DB = dbfunctions()


@app.context_processor
def my_utility_processor():
    status = current_user.get_id()
    user = ''
    info = DB.select('admin', f"where username = '{status}'")
    if status is not None and info != []:
        user = DB.select('admin', f"where username = '{status}'")[0]
    return dict(getYear=funcs.getYear, Official=OFFICIAL, admin_user=user, emptyV=funcs.emptyValue,
                baseURL=BASE_URL, menu=adminmenu, numbComma=funcs.numbComma)


"""
VIEW ENDPOINTS START
"""


@app.route('/log_on')
def logon():
    status = current_user.get_id()
    if status is not None:
        return redirect('/users')
    else:
        scripts = """<script src="static/dashboard/js/pages/custom/login/login-general62fd.js?v=7.2.3"></script>"""
        css = """<link href="static/dashboard//css/pages/login/login-162fd.css?v=7.2.3" rel="stylesheet" type="text/css" />"""
        pageInfo = ['Admin Login', css, scripts]
        response = make_response(render_template('admin/logon.html', pageInfo=pageInfo))
    return response


@app.route('/admin_dashboard')
@login_required
def admin_dashboard():
    status = current_user.get_id()
    type = DB.select('admin', f"where username = '{status}'", "type")
    sum = {}
    admintype = None
    if type:
        admintype = type[0][0]
        countUsers = DB.count_sql('users', 'username')[0][0]
        countNotify = DB.count_sql('notifications', 'seen', f"where receiver='{status}' and seen = 0")[0][0]
        sumNaira = DB.sum_sql('users', 'bal', 'where country = "NG"')[0][0]
        sumDollar = DB.sum_sql('users', 'bal', 'where country != "NG"')[0][0]
        newUsers = DB.select('users', 'ORDER BY id DESC LIMIT 5', 'username, firstname, lastname, mobile, email, country')
        sum = {
            'users': countUsers,
            'sum_naira': sumNaira,
            'sum_dollar': sumDollar,
            'notify': countNotify,
            'newUsers': newUsers,
            'status': status
        }
    pageInfo = ['Dashboard', css, scripts, status, admintype]
    response = make_response(render_template('admin/dashboard.html', pageInfo=pageInfo, sum=sum))
    return response


@app.route('/users')
@login_required
def users():
    status = current_user.get_id()
    type = DB.select('admin', f"where username = '{status}'", "type")
    admintype = None
    if type:
        admintype = type[0][0]
    pageInfo = ['All Users', css, scripts, status, admintype]
    users = DB.select('users')
    response = make_response(render_template('admin/users.html', pageInfo=pageInfo, users=users))
    return response


@app.route('/investments')
@login_required
def investments():
    status = current_user.get_id()
    type = DB.select('admin', f"where username = '{status}'", "type")
    admintype = None
    if type:
        admintype = type[0][0]
    pageInfo = ['Investments', css, scripts, status, admintype]
    users = DB.select('wallet_recharge')
    response = make_response(render_template('admin/investments.html', pageInfo=pageInfo, users=users))
    return response


@app.route('/notifications')
@login_required
def notifications():
    status = current_user.get_id()
    type = DB.select('admin', f"where username = '{status}'", "type")
    admintype = None
    if type:
        admintype = type[0][0]
    pageInfo = ['Notifications', css, scripts, status, admintype]
    # DB.update('notifications', "seen = 1", "where receiver = '{}'".format(status))
    users = DB.select('notifications', f"where sender='{status}' or receiver = '{status}' ORDER BY regdate ASC")
    response = make_response(render_template('admin/notifications.html', pageInfo=pageInfo, users=users))
    return response


@app.route('/withdrawals')
@login_required
def withdrawals():
    status = current_user.get_id()
    type = DB.select('admin', f"where username = '{status}'", "type")
    admintype = None
    if type:
        admintype = type[0][0]
    pageInfo = ['Withdrawals', css, scripts, status, admintype]
    users = DB.select('withdraw')
    response = make_response(render_template('admin/withdrawals.html', pageInfo=pageInfo, users=users))
    return response


@app.route('/admin_logout')
def admin_logout():
    logout_user()
    return redirect('/log_on')


"""
VIEW ENDPOINTS END
ENDPOINTS FOR ACTION START
"""


@app.route('/admin_login', methods=['POST'])
def admin_login():
    username = request.form['username']
    passwd = request.form['password']
    rememberMe = request.form.get('remember')
    retain = msg = ''
    if not username or not passwd:
        msg = "Fill all fields"
    else:
        if rememberMe != None:
            retain = True
        else:
            retain = False
        if DB.select('admin', "where username = '{}'".format(username), "username"):
            logdata = DB.select('admin', 'where username = "{}" limit 1'.format(username), 'username,password')
            dbpass = logdata[0][1]
            if funcs.verify(str(passwd), dbpass):
                user = User(username)
                login_user(user, remember=retain)
                msg = 'ok'
            else:
                msg = 'Invalid Account Details'
        else:
            msg = "User not found"
    return msg


@app.route('/getWallet', methods=['POST'])
def getWallet():
    wid = request.form['wid']
    info = DB.select('users', f'Where username = "{wid}"', 'account_name, account_number, bank_name')
    info = funcs.python_to_json(info)
    return info


@app.route('/adminfundcancel', methods=['POST'])
def adminfundcancel():
    msg = userz = ""
    status = current_user.get_id()
    idd = request.form.get('idd')
    transid = request.form.get('transid')
    userz = request.form.get('userz')
    admin = funcs.selector('admin', "where username = '{}'".format(status), 'id')
    adminid = admin[0][0]
    cancelmsg = request.form.get('cancelmsg')
    noww = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if idd and transid:
        try:
            DB.update('wallet_recharge', "status = 'cancelled'", "where id = '{}' and transaction_id = '{}'".format(idd, transid))
            msg = DB.insert('notifications', f"'{status}','{userz}','error','{cancelmsg}','{noww}'", "sender,receiver,notification_type,description,regdate")
        except Exception as err:
            msg = str(err)
    else:
        msg = 'An error occured'
    return msg


@app.route('/adminwithdrawcancel', methods=['POST'])
def adminwithdrawcancel():
    status = current_user.get_id()
    status = 'sam'
    idd = request.form.get('idd')
    amount = float(request.form.get('amount'))
    user = request.form.get('userz')
    info = DB.select('users', f'where username = "{user}"', 'bal, password')[0]
    bal = float(info[0])
    cancelmsg = request.form.get('cancelmsg')
    noww = datetime.now().strftime("%A %B %d, %Y | %H:%M:%S")
    if idd and amount:
        bal += amount
        DB.insert('notifications', f"'{user}','{status}','error','{cancelmsg}','{noww}'", "receiver,sender,notification_type,description,regdate")
        DB.update('users', "bal = {}".format(bal), "where username = '{}'".format(user))
        msg = DB.update('withdraw', "status = 'cancelled'", "where id = '{}'".format(idd))
    else:
        msg = 'An error occured'
    return msg


@app.route('/adminwithdrawconfirm', methods=['POST'])
def adminwithdrawconfirm():
    status = current_user.get_id()
    status = 'sam'
    idd = request.form.get('idd')
    amount = float(request.form.get('amount'))
    user = request.form.get('userz')
    accDetails = request.form.get('accDetails')
    # info = DB.select('users', f'where username = "{user}"', 'bal, password')[0]
    # bal = float(info[0])
    message = f"{amount} has been deposited into {accDetails}. Thank you for been patient"
    noww = datetime.now().strftime("%A %B %d, %Y | %H:%M:%S")
    try:
        DB.insert('notifications', f"'{user}','{status}','confirmation','{message}','{noww}'", "receiver,sender,notification_type,description,regdate")
        msg = DB.update('withdraw', "status = 'confirmed'", "where id = '{}'".format(idd))
    except Exception as err:
        msg = str(err)

    return msg


@app.route('/adminfundconfirm', methods=['POST'])
def adminfundconfirm():
    status = current_user.get_id()
    msg = ""
    plan = request.form.get('plan')
    user = request.form.get('user')
    cid = request.form.get('cid')
    todayy = datetime.today()
    transid = request.form.get('transid')
    profit = DB.select('users', f"where username = '{user}' limit 1", "profits")[0][0]
    amount = float(request.form.get('amount'))
    noww = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if plan == 'Monthly':
        due = (todayy + timedelta(days=32)).strftime("%A, %B %d, %Y")
        percent = 0.05
        profit = (percent * amount) + amount
    elif plan == 'Weekly':
        due = (todayy + timedelta(days=8)).strftime("%A, %B %d, %Y")
        percent = 0.29
        profit = (percent * amount) + amount

    amount += float(profit)
    message = f"Your {plan} subscription has been activated successfully. You will be able to withdraw your investment returns after {due}"
    try:
        DB.update('wallet_recharge', f"status = 'started', profit = {profit}, due_date='{due}'", f"where id = {cid} and transaction_id = '{transid}'")
        DB.update('users', f"profits = {amount}", f"where username = '{user}'")
        msg = DB.insert('notifications', f"'{status}','{user}','confirmation','{message}','{noww}'", "sender,receiver,notification_type,description,regdate")
    except Exception as err:
        msg = str(err)
    return msg


@app.route('/adminfundincomplete', methods=['POST'])
def adminfundincomplete():
    msg = userz = ""
    status = current_user.get_id()
    idd = request.form.get('idd')
    transid = request.form.get('transid')
    userz = request.form.get('userz')
    cancelmsg = request.form.get('cancelmsg')
    cancelmsg += ". Your money is saved in your balance"
    bal = DB.select('users', "where username = '{}' limit 1".format(userz), "bal")[0][0]
    amount = float(request.form.get('amount'))
    amount = amount + float(bal)
    noww = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if idd and transid:
        DB.update('wallet_recharge', "status = 'cancelled'", "where id = '{}' and transaction_id = '{}'".format(idd, transid))
        DB.update('users', f"bal = {amount}", f"where username = '{userz}'")
        msg = DB.insert('notifications', f"'{status}','{userz}','error','{cancelmsg}','{noww}'", "sender,receiver,notification_type,description,regdate")

    else:
        msg = 'An error occured'
    return msg


@app.route('/admineditusers', methods=['POST'])
def admineditusers():
    msg = ''
    user = request.form['user']
    email = request.form['email']
    investment = float(funcs.inpck(request.form['investment']))
    balance = float(funcs.inpck(request.form['balance']))
    if not investment:
        investment = 0.0
    if not balance:
        balance = 0.0
    if not email or not user:
        msg = "No fields should be left empty!"
    elif not funcs.emailCheck(email):
        msg = f"{email} is not an email"
    else:
        msg = DB.update('users', f"email = '{email}', bal={balance}, profits={investment}", f"where username = '{user}'")
    return msg


@app.route('/adminnotifyusers', methods=['POST'])
@login_required
def adminnotifyusers():
    status = current_user.get_id()
    msg = ''
    notifyType = funcs.inpck(request.form['notifyType'])
    message = funcs.inpck(request.form['message'])
    noww = datetime.now().strftime("%A, %B %d %Y | %H:%M:%S")
    if not message:
        msg = "You cannot send an empty notification"
    else:
        try:
            sql = DB.insert('notifications', f"'Everyone','admin','{notifyType}','{message}','{noww}'", "receiver,sender,notification_type,description,regdate")
            msg = str(sql)
        except Exception as err:
            msg = str(err)
    return msg


@app.route('/admin_change_password', methods=['POST'])
def admin_change_password():
    status = current_user.get_id()
    passmsg = ''
    existPassword = request.form.get('exist')
    password = request.form.get('passwd')
    confirm = request.form.get('confirm')
    dbpass = DB.select('admin', f"where username = '{status}' limit 1", 'password')[0][0]
    print(dbpass)
    if not existPassword or not password or not confirm:
        passmsg = 'Fill all fields'
    elif len(password) < 6:
        passmsg = "Password must be more than 6 letters"
    elif password != confirm:
        passmsg = "Passwords must match"
    elif funcs.verify(str(existPassword), dbpass):
        encrypt = funcs.password(password)
        passmsg = DB.update('admin', "password = '{}'".format(encrypt),
                      "where username = '{}'".format(status))
    else:
        passmsg = "Incorrect password"
    return passmsg


@app.route('/admin_complete_investment', methods=['POST'])
def admin_complete_investment():
    status = current_user.get_id()
    amount = funcs.inpck(request.form['amount'])
    user = funcs.inpck(request.form['user'])
    transid = funcs.inpck(request.form['transid'])
    cid = funcs.inpck(request.form['cid'])
    additional = funcs.inpck(request.form['additional'])

    if not amount.isdigit():
        msg = "Amount must contain numbers"
    else:
        noww = datetime.now().strftime("%A %B %d, %Y | %H:%M:%S")
        info = DB.select('users', f'where username = "{user}"', 'bal')[0]
        bal = float(info[0])
        amount = float(amount)
        bal = bal + amount
        msg = bal
        message = f"Dear {user}, Your investment (ID: {transid}) is complete. {amount} has been added to your balance. You can use it to reinvest and make more or withdraw it. " + additional
        try:
            DB.update('users', f"bal = {bal}", f"where username = '{user}'")
            DB.update('wallet_recharge', f"status = 'completed', ready = 2, profit = {amount}", f"where transaction_id = '{transid}'")
            msg = DB.insert('notifications', f"'{user}', '{status}', 'confirmation', '{message}', '{noww}'", "receiver, sender, notification_type, description, regdate")
        except Exception as err:
            msg = f"Error while confirming: {err}"
    return msg


"""
ACTION ENDPOINTS END
"""
