# Update lambda function to use slots

Now when our lambda function is invoked, we can access the slot, which contains information about a specific show to query.
Our lambda function will invoke a TV show API, which will return information about the TV show. We will create a response containing the
information obtained about the TV show API.

ADD EXAMPLE HERE that contains example request and response.


## Exercise

1. Go to [https://aws.amazon.com/lambda](https://aws.amazon.com/lambda)
2. Copy new Lambda function into editor: [https://github.com/gwc-summer-newark-nj/gwc-summer-newark-nj.github.io/blob/master/ex/lambda2.py](https://github.com/gwc-summer-newark-nj/gwc-summer-newark-nj.github.io/blob/master/ex/lambda2.py)
3. Check out the function named `TODO`. This is where we will add some code to remove the slot parameter and pass the value to `get_tv_show_info`.
4. Construct a speech response from the map value returned from `get_tv_show_info`.


The JSON map below illustrates the response returned from `get_tv_show_info`.

```python

{
    "show": {
        "schedule": {
            "time": "20:30",
            "days": [
              "Thursday"
            ]
        },
        "network": {
            "id": 2,
            "name": "CBS",
             "country": {
                "name": "United States",
                "code": "US",
                "timezone": "America/New_York"
             }
        }
        "summary": "<p>For 9-year-old Sheldon Cooper, it isn't easy growing up in East Texas. Being a once-in-a-generation mind capable of advanced mathematics and science isn't always helpful in a land where church and football are king. And while the vulnerable, gifted and somewhat naïve Sheldon deals with the world, his very normal family must find a way to deal with him. His father, George, is struggling to find his way as a high school football coach and as father to a boy he doesn't understand. Sheldon's mother, Mary, fiercely protects and nurtures her son in a town where he just doesn't fit in. Sheldon's older brother, Georgie, does the best he can in high school, but it's tough to be cool when you're in the same classes with your odd 9-year-old brother. Finally, there's Sheldon's twin sister, Missy, who sometimes resents all the attention Sheldon gets, but also remains the one person who can reliably tell Sheldon the truth. For 10 years on THE BIG BANG THEORY, audiences have come to know the iconic, eccentric and extraordinary Sheldon Cooper. This single-camera, half-hour comedy gives us the chance to meet him in childhood, as he embarks on his innocent, awkward and hopeful journey toward the man he will become.</p>",
     }
}
```

[Next: Test your latest Alexa skill](test2.md)
