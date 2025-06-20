from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded credentials
VALID_USERNAME = 'admin'
VALID_PASSWORD = '123456'

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    flag = None
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            flag = 'flag{bruteforce_success}'
        else:
            message = 'Invalid credentials.'

    return render_template('login.html', flag=flag, message=message)

@app.route('/level2')
def level2():
    user_id = request.args.get('user_id')

    # Simulate unsafe SQL behavior
    if user_id is None:
        profile = "You must provide a user_id."
    elif user_id == "1":
        profile = "User ID: 1 — Name: Alice"
    elif "'1'='1" in user_id or "1=1" in user_id:
        # Simulate SQLi success
        flag = "flag{sql_injection_unlocked}"
        return render_template("level2.html", profile="All users loaded!", flag=flag)
    else:
        profile = f"User ID: {user_id} not found."

    return render_template("level2.html", profile=profile)

@app.route('/level3')
def level3():
    is_admin = request.cookies.get('is_admin', 'false')

    if is_admin == 'true':
        flag = "flag{cookie_monster}"
        return render_template("level3.html", access_granted=True, flag=flag)
    else:
        return render_template("level3.html", access_granted=False)
    
@app.route('/level4')
def level4():
    return render_template('level4.html') 

if __name__ == '__main__':
    app.run(debug=True)