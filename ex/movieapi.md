```python

[
  {
    "score": 40.202457,
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
]

response = unirest.get("https://tvjan-tvmaze-v1.p.mashape.com/search/shows?q={query}",
  headers={
    "X-Mashape-Key": "759AC8LsObmshG4nM6DhorUzHhPVp1ictQfjsnjsJTALHjFdEi"
  }
)

```