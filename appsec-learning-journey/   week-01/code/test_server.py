from flask import Flask, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'test_secret_key_12345'  # Required for sessions

@app.route('/')
def home():
    if 'username' in session:
        return f'<h1>Welcome, {session["username"]}!</h1><a href="/logout">Logout</a>'
    return '<h1>Not logged in</h1><a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', 'guest')
        session['username'] = username
        return redirect(url_for('home'))
    return '''
        <form method="post">
            Username: <input name="username" value="testuser">
            <button type="submit">Login</button>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
