@app.route('/log/', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        return redirect(url_for('index'))
    return render_template('log.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

    <form method="post">
        <input type="text" name="username" placeholder="Имя">
        <input type="email" name="email" placeholder="E-mail">
        <input type="submit" value="Отправить">
    </form>

    {% if session.username %}
        <h1>Привет {{ session.username }}</h1>
        <a href="/logout">Log out</a>
    {% else %}
        <a href="/log">Login</a>
    {% endif %}