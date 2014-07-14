from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

STATUS_NORMAL = 0
STATUS_BLOCKED = 1

PENDING = 0
TIME_LIMIT_EXCEEDED = 1
MEM_LIMIT_EXCEEDED = 2
WRONG_ANSWER = 3
RUNTIME_ERROR = 4
COMPILE_ERROR = 5
PRESENTATION_ERROR = 6
OUTPUT_LIMIT_EXCEEDED = 7
ACCEPTED = 8

C = 0
CPP = 1
PYTHON = 2

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nickname = db.Column(db.String(64), index = True, unique = True)
	sid = db.Column(db.String(10), unique = True)
	email = db.Column(db.String(120), index = True, unique = True)
	password = db.Column(db.String(120))
	role = db.Column(db.SmallInteger, default = ROLE_USER)
	status = db.Column(db.SmallInteger, default = STATUS_NORMAL)
	last_seen = db.Column(db.DateTime)
	last_submition = db.Column(db.DateTime)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User %r>' % (self.nickname)

class Problem(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	problem_id = db.Column(db.Integer, unique = True)
	title = db.Column(db.String(100))
	time_limit = db.Column(db.Integer)
	memory_limit = db.Column(db.Integer)
	description = db.Column(db.Text)
	input_description = db.Column(db.Text)
	output_description = db.Column(db.Text)
	input_sample = db.Column(db.Text)
	output_sample = db.Column(db.Text)
	hint = db.Column(db.Text)

class Submit(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	problem = db.Column(db.Integer, db.ForeignKey('problem.id'))
	user = db.Column(db.Integer, db.ForeignKey('user.id'))
	status = db.Column(db.SmallInteger)
	time = db.Column(db.Integer)
	memory = db.Column(db.Integer)
	language = db.Column(db.SmallInteger)
	submit_time = db.Column(db.DateTime)
	code_file = db.Column(db.String(100))
	error_message = db.Column(db.Text)