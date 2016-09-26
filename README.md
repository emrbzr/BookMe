# SOEN 343 Project

This is the repository that contains the code, documentation, issues and much more related to reserving a classroom for a school project.
<br />

<h1>How to setup Flask</h1>
-Download the latest python3.5 version<br />
-follow this <a href="http://flask.pocoo.org/docs/0.11/installation/">Flask installation</a><br />

Finally to activate the venv:<br />
cd to project directory<br />
source venv/bin/activate<br />
pip install the necessary modules: <br />
$ pip install flask flask-security flask-sqlalchemy<br />
<h2>Database guide</h2>
Install <a href="https://www.postgresql.org/download/">postgresql</a><br />
install psycopg2 on the venv, the installation of this depends on your os<br />
<h3>Mac osX</h3>
install <a href="http://brew.sh/">brew</a>
insert the following command on your terminal: <br />
$ brew install postgresql<br />
then in your venv enter the following command on your terminal:<br />
$ pip install psycopg2 <br />

<h3>Windows</h3>
go into the project directory<br />
cd venv/lib/python3.5/site-packages <br />
pip install psycopg2-2.6.1-cp35-none-win32.whl<br />

<h3>Create reservation database through the postgresl GUI</h3>
Insert user and pass seperate by ":" -> app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/development'<br />
$ python<br />
>>> from app import db<br />
>>> db.create_all()<br />

<h2>To start server</h2>
$ python app.py <br />

<h2>to deactivate server</h2>
$ deactivate <br />

## Team Members

Ahmad Hyjaz Loudin <br />
Emir Bozer <br />
Leo Yu <br />
Nikolas De vigne Blanchet<br />
Mary Psaroudis<br />
