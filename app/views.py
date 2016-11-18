from app import app
from .decorators import *
from .models import *
from flask import render_template, request
from app.TDG import UserTDG
from app.core.user import User
#if 404 error render 404.html
@app.errorhandler(404)
def not_found_error(error):
	return render_template('404.php')

#if 500 error render 500.html
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.php'), 500

@app.route('/')
def home():
	return redirect(url_for('index'))
#login
@app.route('/login', methods=['GET', 'POST'])
def index():
    error = 'Invalid credentials. Please try again'
    if request.method == 'POST':
        data = UserTDG.find(request.form['username'])
        if data[0][0] is int(request.form['username']):
            if data[0][2] == request.form['password']:
                session['logged_in'] = True
                return redirect(url_for('dashboard',user=data[0][1]))
            else:
                return render_template('login.php',error=error)
        else:
            return render_template('login.php',error=error)
    else:
        return render_template('login.php')

#logout
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	session.clear()
	return redirect(url_for('index'))

#reservation
@app.route('/dashboard/<string:user>')
@login_required
@nocache
def dashboard(user):
	session['user'] = user
	return render_template('index.php',user=user)

@app.route('/month')
@login_required
@nocache
def month():
	return render_template('month.php')

@app.route('/january')
@login_required
@nocache
def january():
	return render_template('january.php')

@app.route('/february')
@login_required
@nocache
def february():
	return render_template('february.php')

@app.route('/march')
@login_required
@nocache
def march():
	return render_template('march.php')

@app.route('/april')
@login_required
@nocache
def april():
	return render_template('april.php')

@app.route('/may')
@login_required
@nocache
def may():
	return render_template('may.php')

@app.route('/june')
@login_required
@nocache
def june():
	return render_template('june.php')

@app.route('/july')
@login_required
@nocache
def july():
	return render_template('july.php')

@app.route('/august')
@login_required
@nocache
def august():
	return render_template('august.php')

@app.route('/september')
@login_required
@nocache
def september():
	return render_template('september.php')

@app.route('/october')
@login_required
@nocache
def october():
	return render_template('october.php')

@app.route('/november')
@login_required
@nocache
def november():
	return render_template('november.php')

@app.route('/december')
@login_required
@nocache
def december():
	return render_template('december.php')

@app.route('/january/add')
@login_required
@nocache
def addJanuary():
	return render_template('add.php')

@app.route('/february/add')
@login_required
@nocache
def addFebruary():
	return render_template('add.php')

@app.route('/march/add')
@login_required
@nocache
def addMarch():
	return render_template('add.php')

@app.route('/april/add')
@login_required
@nocache
def addApril():
	return render_template('add.php')

@app.route('/may/add')
@login_required
@nocache
def addMay():
	return render_template('add.php')

@app.route('/june/add')
@login_required
@nocache
def addJune():
	return render_template('add.php')

@app.route('/july/add')
@login_required
@nocache
def addJuly():
	return render_template('add.php')

@app.route('/august/add')
@login_required
@nocache
def addAugust():
	return render_template('add.php')

@app.route('/september/add')
@login_required
@nocache
def addSeptember():
	return render_template('add.php')

@app.route('/october/add')
@login_required
@nocache
def addOctober():
	return render_template('add.php')

@app.route('/november/add')
@login_required
@nocache
def addNovember():
	return render_template('add.php')

@app.route('/december/add')
@login_required
@nocache
def addDecember():
	return render_template('add.php')