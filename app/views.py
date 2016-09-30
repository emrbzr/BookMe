from app import app
from .decorators import *
from .models import *
#if 404 error render 404.html 
@app.errorhandler(404)
def not_found_error(error):
	return render_template('404.html')

#if 500 error render 500.html 
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

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
				return render_template('login.html',error=error)
		else:
			return render_template('login.html',error=error)
	return render_template('login.html')

#logout
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	session.clear()
	return redirect(url_for('index'))

#reservation
@app.route('/dashboard')
@login_required 
@nocache
def dashboard():
		return render_template('reservation.html')
	