# import requests
# url = "https://api.yelp.com/v3/businesses/search"
# headers = {"Authorization": "Bearer mUOoEuwbg4In0FAGUm041a9Std20NoqFWNgw1i36aP8pnVuFYFn5RcKqTcamjM21niuNO9oYfjGexB2zOxGlgGBy8Vd1KfqOXKi6b2SvU2Coy5hzIprEWYW3OgreYXYx" }
# params = {"term": "gyms", "location": "San Jose"}
# results = requests.get(url, params=params, headers=headers)

# results_dict = results.json()
# businesses = results_dict["businesses"]

# bus1 = businesses[1]

{% for location in businesses %}
    {% if location["categories"] %}
        {% for index in range(len(categories)) %}   
            <p>Categories: {{categories[index]["title"]}}</p>
{% endfor %}
{% endif %}
{% endfor %}

<p><u><b><a href="/fav_location">Click</a></u></b> to save this result as your favorite gym</p>


def sentence_length(sentence):
    words = sentence.split(" ")
    for word in words:
        print (len(word))
        
    