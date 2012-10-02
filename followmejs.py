import cgi
import datetime
import urllib
import webapp2
import jinja2
import os

from google.appengine.ext import db
from google.appengine.api import users


jinja_environment = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
    def get(self):
        
        template_values = {
            'url': ''
        }
        
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))


class MobileRemote(webapp2.RequestHandler):
	def get(self):

		template_values = {
			'url': ''
			}

		template = jinja_environment.get_template('remote.html')
		self.response.out.write(template.render(template_values))
		

class ChatPage(webapp2.RequestHandler):
	def get(self):

		template_values = {
			'url': ''
			}

		template = jinja_environment.get_template('chat.html')
		self.response.out.write(template.render(template_values))
		

class VideoPage(webapp2.RequestHandler):
	def get(self):

		template_values = {
			'url': ''
			}

		template = jinja_environment.get_template('video.html')
		self.response.out.write(template.render(template_values))
		
		
		
app = webapp2.WSGIApplication([('/', MainPage),
						       ('/r', MobileRemote),
							   ('/chat', ChatPage),
							   ('/video', VideoPage)],
                              debug=True)