# STEPS TO USE THIS CODE
# 1. Install Python (version 3) - make sure you include pip in the install
#    - pip is the package installer for Python. We can write a lot with basic Python,
#       but it's useful to use packages that other people have written. That way we
#       don't have to write everything from scratch ourselves.
# 2. Double check python has installed successfully. In a terminal, type in "python --version".
#    If that doesn't work, try "python3 --version". You should see a version number output e.g.
#    Python 3.10.8
# 3. Install and open Visual Studio Code - https://code.visualstudio.com/
# 4. Open the python_demo folder in VS Code.
# 5. Click on "Terminal" in the taskbar, then "New Terminal". In that terminal, 
# type in the following command: "pip install requests"

# TO RUN THIS CODE, EITHER:
# - Right click on the code in VS Code, and select "Run Python File in Terminal"
# - Click the play button in the top right of VS Code

# GETTING NEWS FROM OUR API
# Source: https://newsapi.org/docs

# These are the packages we want to use so we don't have to reinvent the wheel.
# We import packages using the import keyword
import requests, pprint

pp = pprint.PrettyPrinter(indent=4)

# We're creating a variable called API_KEY. This key proves we're allowed to send requests
# and receive responses from the News API. Don't change it!
API_KEY = 'c0f1891a789e4278b8f8bf4d3895f891'

# We'll also create a variable called BASE_URL. This just saves us repeating the same url over
# and over each time we want to make a new request
BASE_URL = 'https://newsapi.org/v2'

# Let's make our first request!
# This one's a demo. We'll make a request to the url. We can make the request to the
# /everything endpoint - that tells the API we want to get back all the data.
# We're also going to add a query parameter to only get Insider articles back.
request_url = str.format(f"{BASE_URL}/everything?apiKey={API_KEY}&sources=business-insider-uk")

# Every request returns a response - if the request is valid we should get some data back!
# The data is returned as JSON - short for JavaScript Object Notation. It's the way most data
# is transmitted on the web via HTTP.
response = requests.get(request_url).json()

# You can uncomment this code by deleting the hash (#) in front of the line. Try uncommenting the
# line below and running the code. The output is pretty big!
# print(response)

# Let's just look at the first article. To get data out of the article, we need to look at what's in the
# JSON. We'll get the first item in the articles list using the square bracket notation.
first_article = response['articles'][0]
pp.pprint(first_article)

# Yay! We've got some data. But it still looks a bit gross. Let's print it out in a nice way!
print("\n---- NEWS ARTICLE ---- \n")
print(f"Title: {first_article['title']} \n")
print(f"Author: {first_article['author']} \n")

# TASK - Print out the publish time (publishedAt) and the URL of the article (url) as well.


# QUESTION - what happens if we try and use a key that doesn't exist?

# TASK - Print out the article's source name? HINT: Look at the nested dictionaries examples!


# TASK - Now it's your turn! Try changing the request in some way and seeing what the results are.
# Try looking at the JSON response and printing a few bits of the data.
# You could try changing the endpoint, or changing the query parameters.
# Use the code up above as a starting point.