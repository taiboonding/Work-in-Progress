import tornado.ioloop
import tornado.web


class CheckAccessIP(tornado.web.RequestHandler):
	def __init__(self):
		allowed_ips = ['127.0.0.1','50.4.81.111','45.56.120.82']
		
	def get(self):
		self.remote_ip = self.request.remote_ip if not self.request.headers.get("X-Real-IP") else self.request.headers.get("X-Real-IP")

	def allowed(self):
		if self.remote_ip in self.allowed_ips:
			check = True
		else: 
			check = False
		return check

		
class BaseHandler(tornado.web.RequestHandler):	
    def get_current_user(self):
		return self.get_secure_cookie("user")
		
		
class CheckAccessKey(BaseHandler):
	def get(self):
		fromurl = self.request.headers.get('Referrer')
		if not self.current_user:
			self.redirect(r"/login?source=%s" %str(fromurl))
			return
		
			
class MainHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect(r"/login")
            return
        x_real_ip = self.request.headers.get("X-Real-IP")
        remote_ip = self.request.remote_ip if not x_real_ip else x_real_ip
        self.write('Access key accepted.' + '<br>' + 'Welcome to Listeree.' + '<br>')
        self.write('Your IP Address is: %s' %repr(remote_ip))

		
class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')

    def post(self):
		allowed_keys = ['5SxENITfNKBCeh2A', 'dCYcWgfsujGUUGyI','tibyronMedforRulz', 
		'zhiqiGansta0rCop','joshPlayz2Winn','shawnTheeSage','pistontheclandestine',
		'ding']
		key = self.get_argument("key")
		if key in allowed_keys:
			self.set_secure_cookie("user", key, expires_days=None)
			self.redirect(r"/")
		else:
			self.write('Sorry, you have entered an invalid access key. Please contact Lu for an access key.')
			return
		
	

	
		

		
		
		


		

		
