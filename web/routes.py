
# https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04-ru

from web import web

@web.route('/')
@web.route('/index')
def index():
    return "Hello, World!"
