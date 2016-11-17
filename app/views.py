from app import app
from .decorators import *
from .models import *
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
		user = User.query.filter(db.or_(User.username == request.form['username'])).first()
		password = User.query.filter(db.or_(User.password == request.form['password'])).first()
		if user:
			if password:
				session['logged_in'] = True
				return redirect(url_for('dashboard',user=request.form['username']))
			else:
				return render_template('login.php',error=error)
		else:
			return render_template('login.php',error=error)
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
def month():
	return render_template('month.php')

@app.route('/january')
def january():
	return render_template('january.php')

@app.route('/february')
def february():
	return render_template('february.php')

@app.route('/march')
def march():
	return render_template('march.php')

@app.route('/april')
def april():
	return render_template('april.php')

@app.route('/may')
def may():
	return render_template('may.php')

@app.route('/june')
def june():
	return render_template('june.php')

@app.route('/july')
def july():
	return render_template('july.php')

@app.route('/august')
def august():
	return render_template('august.php')

@app.route('/september')
def september():
	return render_template('september.php')

@app.route('/october')
def october():
	return render_template('october.php')

@app.route('/november')
def november():
	return render_template('november.php')

@app.route('/december')
def december():
	return render_template('december.php')

@app.route('/january/add')
def addJanuary():
	return render_template('add.php')

@app.route('/february/add')
def addFebruary():
	return render_template('add.php')

@app.route('/march/add')
def addMarch():
	return render_template('add.php')

@app.route('/april/add')
def addApril():
	return render_template('add.php')

@app.route('/may/add')
def addMay():
	return render_template('add.php')

@app.route('/june/add')
def addJune():
	return render_template('add.php')

@app.route('/july/add')
def addJuly():
	return render_template('add.php')

@app.route('/august/add')
def addAugust():
	return render_template('add.php')

@app.route('/september/add')
def addSeptember():
	return render_template('add.php')

@app.route('/october/add')
def addOctober():
	return render_template('add.php')

@app.route('/november/add')
def addNovember():
	return render_template('add.php')

@app.route('/december/add')
def addDecember():
	return render_template('add.php')