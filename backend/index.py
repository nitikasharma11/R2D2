from flask import Flask,render_template
import requests
app = Flask(__name__, template_folder='.')

@app.route('/<search>')
def searchMovie(search):

   x = "http://www.omdbapi.com/?t="+search+"&apikey=<apikey>"
   data = requests.get(x).json()
   return render_template('index.html', movies=data)


@app.route('/movies/<movie_id>')
def movieIdsearch(movie_id):
   y = "http://www.omdbapi.com/?i="+movie_id+"&apikey=<apikey>"
   movie = requests.get(y).json()
   return render_template('movies.html', movies=movie)

if __name__ == '__main__':

   app.run(host='0.0.0.0', debug=True)	
