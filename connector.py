import logging
import urllib
import string
import json


class MovieConnector:
    # Helper class for retrieving information about a movie via REST webservice.

    def __init__(self):
        connection_url_template = r"http://www.omdbapi.com/?t=${movie_name}&y=&plot=full&r=json"
        self.template = string.Template(connection_url_template)

    def get_movie_information(self, title):
        # Gets back a json object which contains information for given title.
        substituted_string = self.template.substitute(movie_name=title)  # substitute movie title for the URL
        response = urllib.urlopen(substituted_string)
        logging.info(response)
        return json.load(response)
