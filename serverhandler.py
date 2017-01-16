import SimpleHTTPServer
import cgi

import jinja2

from movie import Movie


class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    # class to handle http requests of web browser

    movie_connector = None
    movie_list = []

    def do_GET(self):
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type']})

        # read input field of html page
        movie_information = self.movie_connector.get_movie_information(form.list[0].value)

        error = True
        if movie_information['Response'] == 'True':
            # if the response is not empty then fill movie object with retrieved information
            movie = Movie(movie_information['Title'], movie_information['Year'],
                          movie_information['Poster'], movie_information['Plot'])
            self.movie_list.append(movie)
            # set to prevent to show error message on html page
            error = False

        # initialise Jinja2 template engine
        template_loader = jinja2.FileSystemLoader(searchpath=".")
        template_env = jinja2.Environment(loader=template_loader)
        template = template_env.get_template('template.html')
        output_text = template.render(movie_list=self.movie_list, error=error)

        # send rendered template via http response
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(output_text)
