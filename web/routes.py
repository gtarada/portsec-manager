from web import web

@web.route('/')
@web.route('/index')
def index():
    return "Hello, World!"
