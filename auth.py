import tornado.ioloop
import tornado.web

		
class BaseHandler(tornado.web.RequestHandler):	
    def get_current_user(self):
		return self.get_secure_cookie("user")
		
			
class CheckAccess(BaseHandler):
	def __init__(self):
		allowed_ips = ['127.0.0.1','50.4.81.111','45.56.120.82']
		
	def get(self):
		self.remote_ip = self.request.remote_ip if not self.request.headers.get("X-Real-IP") else self.request.headers.get("X-Real-IP")
		self.user = self.current_user

	def allowed(self):
		# if self.remote_ip in self.allowed_ips:
			# check = False (True)
		if self.user:
			check = True
		else:
			check = False
			
		return check

		
class LoginHandler(BaseHandler):	
    def get(self):
        self.render('login.html')
		
    def post(self):
		allowed_keys = ['5SxENITfNKBCeh2A', 'dCYcWgfsujGUUGyI','tibyronMedforRulz', 
		'zhiqiGansta0rCop','joshPlayz2Winn','shawnTheeSage','pistontheclandestine',
		'ding']
		key = self.get_argument("key")
		if key in allowed_keys:
			source = self.get_query_argument("source")
			self.set_secure_cookie("user", key, expires_days=None)
			self.redirect(r"%s" %self.source)
		else:
			self.write('Sorry, you have entered an invalid access key. Please contact Lu for an access key.')
			return
		
	
