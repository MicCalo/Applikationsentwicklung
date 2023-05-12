#!/usr/bin/env python3
# coding: utf8


from flask import Flask, redirect, request, session


app = Flask(__name__)
app.secret_key = 'wqQRHxsadfn5xRwhjogpLQ'


@app.route('/')
def handle_request():
    if 'username' in session:
        return f"Hello <b>{session['nick_name']}</b><br/>(Username {session['username']})<br/> <a href='/logout'>logout</a> "
    else:
        return """You are not logged in.<br/>
          <a href='/login'>click here to log in</a>"""


@app.route('/login', methods=['GET', 'POST'])
def login():    
    if request.method == 'POST':
        user_name = request.form['username']
        session['username'] = user_name
        session['nick_name'] = request.form['nickname']
        return redirect('/')
    else:    
        return """
      <form action="" method="post">
        <p>Username:<input type="text" name="username"/></p>
        <p>Nickname:<input type="text" name="nickname"/></p>
        <p><input type="submit" value="Login"/></p>
      </form></body></html>	
   """


@app.route('/logout')
def logout(): 
    # remove username from flask sessions
    del session['username']
    del session['nick_name']

    # redirect browser to index page (which will show 'please log in again')
    return redirect('/')


if __name__ == '__main__':
    # app.run(host='0.0.0.0') # per default, server only accepts clients from local host. Use '0.0.0.0' to accept all clients
    app.run()
