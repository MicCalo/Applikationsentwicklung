#!/usr/bin/env python3
# coding: utf8


from flask import Flask, render_template, redirect, request, session
import a3_functions as functions

# Logging should be configured before app is started
functions.setup_logging()


app = Flask(__name__)
app.secret_key = 'yxcv4eergyxwd3wewe'

all_sessions = {}
server_info = functions.get_server_infos()


@app.route('/')
def handle_request():
    functions.increment_served_requests_counter(server_info)
    if 'username' in session:
        # if username is present in session, user is logged in  -> first, update 'last seen' timestamp
        session['login_last_request'] = functions.get_current_time_str()

        # collect data
        all_data = []
        all_data.append({'title': 'Session Information', 'data': session})
        all_data.append({'title': 'Request Information',
                        'data': functions.get_infos_from_request(request)})
        all_data.append({'title': 'Request Arguments',
                        'data': request.args.to_dict()})
        all_data.append({'title': 'All sessions',        'data': all_sessions})
        all_data.append({'title': 'server info',         'data': server_info})

        # pass user name and data to template renderer
        return render_template('sessions_advanced.html.jinja', name=session['username'], all_data=all_data, with_logout=True)
    else:
        return """You are not logged in.<br/>
          <a href='/login'>click here to log in</a>"""


@app.route('/login', methods=['GET', 'POST'])
def login():
    functions.increment_served_requests_counter(server_info)
    info = ''
    if request.method == 'POST':
        user_name = request.form['username']
        if request.form['password'] == '1234':
            # set some data in session dictionary
            session['username'] = user_name
            session['login_datetime'] = functions.get_current_time_str()
            session['login_last_request'] = functions.get_current_time_str()

            # update 'our' infos
            all_sessions[user_name] = f"started: {session['login_datetime']}, client ip: {request.remote_addr}"
            server_info['sessions_count'] = str(len(all_sessions))

            app.logger.info(
                f"user '{user_name}' logged in. Currently, there are {len(all_sessions)} users logged in")
            return redirect('/')
        else:
            app.logger.info(
                f"user '{user_name}' failed to log in (wrong password)")
            info = "password incorrect. Please try again<br/>"
    return info + """
      <form action="" method="post">
        <p>Username:<input type="text" name="username"/></p>
        <p>Password:<input type="password" name="password"/></p>
        <p><input type="submit" value="Login"/></p>
      </form></body></html>	
   """


@app.route('/logout')
def logout():
    functions.increment_served_requests_counter(server_info)
    user_name = session['username']
    app.logger.info(f"user '{user_name}' logged out")

    # update 'our' infos
    if user_name in all_sessions:
        del all_sessions[user_name]
    server_info['sessions_count'] = str(len(all_sessions))

    # remove it from flask sessions
    session.pop('username', None)

    # redirect browser to index page (which will show 'please log in again')
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0') # per default, server only accepts clients from local host. Use '0.0.0.0' to accept all clients
    #app.run()
