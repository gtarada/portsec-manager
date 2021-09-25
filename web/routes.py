# https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04-ru
# https://code.visualstudio.com/docs/containers/quickstart-python
# https://code.visualstudio.com/docs/python/tutorial-flask
# https://developer.cisco.com/docs/iox/#!tutorial-build-sample-docker-type-python-simple-app/tutorial-build-sample-docker-type-python-simple-app
# https://docs.docker.com/language/python/
# https://lab.github.com/githubtraining/github-actions:-write-docker-container-actions
# https://pythonspeed.com/articles/base-image-python-docker-images/
# https://www.docker.com/blog/containerized-python-development-part-1/

from web import web


@web.route("/")
@web.route("/index")
def index():
    return "Hello, World!"
