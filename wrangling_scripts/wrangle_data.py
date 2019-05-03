import pandas as pd
import plotly.graph_objs as go
import nltk, re, requests, oauth2, json
import pandas as pd
import plotly.plotly as py
import plotly.tools as tls
import matplotlib.pyplot as plt

from collections import Counter
from twython import Twython
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize


CONSUMER_KEY = 'MHK7n3fcuqePFfQ3bkwncspOp'
CONSUMER_SECRET = 'rTuDTaRBRveLxof2H6NzcFm5NbXKVVLwRRmLfirRKW1rSZwqbA'

twitter = Twython(app_key=CONSUMER_KEY,app_secret=CONSUMER_SECRET)
topics = ["dogs", "cats", "pizza", "beyonce", "dinosaurs", 
  "avengers", "summer", "hungry", "kanye", "ariana%20grande"]

stop_words = stopwords.words("english")
lemmatizer = WordNetLemmatizer()

def tokenize(text):
    # normalize case and remove punctuation
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    
    # tokenize text
    tokens = word_tokenize(text)
    
    # lemmatize andremove stop words
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    
    # manually handling of retweets and urls
    tokens = [ w for w in tokens if w not in ["rt", "http", "co"] ]

    return tokens

def get_most_common_words(q):
    results = twitter.search(q=q, count=100, result_type="mixed", lang="en")
    text = [ r["text"] for r in results["statuses"] ]

    all_text = []
    for t in text:
        all_text += tokenize(t)
    
    return Counter(all_text).most_common(10)

def plot_most_common_words(q):
    res = get_most_common_words(q)
    height = [ x[1] for x in res ]
    labels = [ x[0] for x in res ]

    graph = []

    graph.append(
      go.Bar(
      x = labels,
      y = height
      )
    )

    layout = dict(title = 'Most common words in "{}" tweets returned by Twitter API'.format(q),
                xaxis = dict(title = '',),
                yaxis = dict(title = 'Count'),
                titlefont = dict(size = 12)
                )

    return graph, layout


def load_data_from_twitter_api(topics=topics):
    results = [ twitter.search(q=topic, count=100, result_type="popular", lang="en") for topic in topics ]
    return results

def return_figures():
    """
    Creates six plotly visualizations

    Args:
      None

    Returns:
      list (dict): list containing the six plotly visualizations
    """
    results = load_data_from_twitter_api()

    # Compute statistics
    favorite_counts = [ [ t["favorite_count"] for t in r["statuses"]] for r in results ]
    retweet_counts = [ [ t["retweet_count"] for t in r["statuses"]] for r in results ]
    avg_favorite_count = [ sum(x) / len(x) for x in favorite_counts ]
    avg_retweet_count = [ sum(x) / len(x) for x in retweet_counts ]

    queries = ["dogs", "cats", "pizza", "beyonce", "dinosaurs", "avengers", "summer", "hungry", "kanye", "ariana grande"]
    colors = ['rgba(253,36,145,1)', 'rgba(145,36,253,1)',
               'rgba(253,36,253,1)', 'rgba(253,253,36,1)',
               'rgba(36,36,253,1)', 'rgba(255,40,40,1)',
               'rgba(253,145,36,1)', 'rgba(40,20,0,1)', 
               'rgba(36,253,36,1)', 'rgba(36,253,253,1)']

    sorted_fav_counts = sorted(zip(avg_favorite_count, queries, colors), key=lambda x: -x[0])
    sorted_rt_counts = sorted(zip(avg_retweet_count, queries, colors), key=lambda x: -x[0])

    fav_heights = [ x[0] for x in sorted_fav_counts ]
    fav_labels = [ x[1] for x in sorted_fav_counts ]
    fav_colors = [ x[2] for x in sorted_fav_counts ]
    rt_heights = [ x[0] for x in sorted_rt_counts ]
    rt_labels = [ x[1] for x in sorted_rt_counts ]
    rt_colors = [ x[2] for x in sorted_rt_counts ]

    # Visualization 1
    graph_one = []

    graph_one.append(
      go.Bar(
      x = fav_labels,
      y = fav_heights,
      marker=dict(
        color=rt_colors)
      )
    )

    layout_one = dict(title = 'Average favorite count for popular tweets returned by the Twitter API',
                xaxis = dict(title = 'Query',),
                yaxis = dict(title = 'Favorites'),
                titlefont = dict(size = 12)
                )

    # Visualization 2
    graph_two = []

    graph_two.append(
      go.Bar(
      x = rt_labels,
      y = rt_heights,
      marker=dict(
        color=rt_colors)
      )
    )

    layout_two = dict(title = 'Average retweet count for popular tweets returned by the Twitter API',
                xaxis = dict(title = 'Query',),
                yaxis = dict(title = 'Retweets'),
                titlefont = dict(size = 12)
                )

    # Visualization 3-6
    graph_three, layout_three = plot_most_common_words("avengers")
    graph_four, layout_four = plot_most_common_words("dogs")
    graph_five, layout_five = plot_most_common_words("pizza") 
    graph_six, layout_six = plot_most_common_words("dinosaurs")

    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))
    figures.append(dict(data=graph_five, layout=layout_five))
    figures.append(dict(data=graph_six, layout=layout_six))

    return figures




