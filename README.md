The website shows information like title, storyline and poster image of a given movie.
It allows you to dynamically add movies to the website by a given movie title.
The Information will automatically retrieved via webservice.

The Movie Website project is part of the _Python programming foundations_ course.

## Dependencies

The project uses **Jinja2** as template engine.

## Known issues
There is no link to the youtube trailers for the movies. The reason is that I did not want order a google API key
to get the link of the youtube video automatically via webservice.

## Run website
Go to the folder where the project files are located and run:
```
python main.py
```
After that you can open the url http://localhost:8000 in a web browser and add movies through the input field.