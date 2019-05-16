# Sample Twitter API Data Dashboard

This repository contains files I used in order to build a simple visualization dashboard for some sample Twitter data on Heroku.

## Installations
Libraries used in this data analysis include [pandas](https://pandas.pydata.org/), [nltk](https://www.nltk.org/), [plotly](https://plot.ly/python/), and [matplotlib/pyplot](https://matplotlib.org/api/pyplot_api.html). These are all super well-known Python libraries, and further installation instructions can be found on their respective websites (linked). The Twitter API library [Twython](https://twython.readthedocs.io/en/latest/) was used to obtain data. App was built using [Flask](http://flask.pocoo.org/) and deployed on [Heroku](https://dashboard.heroku.com/login). 

## Motivation
The primary motivation for this project was to complete an optional component of the Udacity Data Scientist Nanodegree. I chose to complete this project to gain experience creating and deploying apps with Flask and Heroku. 

## File descriptions
- working_notebook.ipynb - This is the Jupyter notebook where wrangling work was done and prepared prior to setting everything up in wrangling.py.
- wrangling_scripts/wrangling.py - This is the primary file for data wrangling, where data is pulled through the Twitter API and then transformed into a form suitable for plotting with Plotly.
- myapp (directory), myapp.py - These are files for the Flask app set-up, including routes.py, which connects the wrangled data to the front-end for visualization through index.html.
- Procfile, nltk.txt, requirements.txt - These are files required by Heroku, to locate the app, specify NLTK libraries to download, and specify Python library requirements.

## Summary of results
The completed dashboard can be seen at https://dsnd-twitter-api-dashboard.herokuapp.com/. It should be dynamically updated with updates (as possible) from the Twitter API whenever the app reloads.

## Authors
Data is provided through the Twitter API, and much of the boilerplate code for the index.html file is provided through the Udacity Data Scientist Nanodegree. The author of the Jupyter notebook and wrangle_data.py (which is most of the rest of the meaningful content in this repo) is me.

## Acknowledgements
Thanks to Twitter for providing the [API](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html) to obtain tweet data for this analysis. Thanks to Udacity for including this project as part of their Data Scientist Nanodegree. I gained some experience with the Flask framework and deploying my first app on Heroku through this. Cool stuff.
