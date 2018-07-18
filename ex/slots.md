# Update Interaction Model with Slots

> Alexa, when is <SHOW> on?

> Alexa, What time is <SHOW> on?

> What channel is <SHOW> on?

> What is <SHOW> about?

```java
{
    "interactionModel": {
        "languageModel": {
            "invocationName": "tv show finder",
            "intents": [
                {
                    "name": "AMAZON.FallbackIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.CancelIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.HelpIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.StopIntent",
                    "samples": []
                },
                {
                    "name": "GetFavoriteTvShowIntent",
                    "samples" : [
                      "What is your favorite show",
                      "What is your favorite tv show",
                      "What show do you like the best"

                    ]
                }
            ],
            "types": []
        }
    }
}



```


## References
[https://developer.amazon.com/docs/custom-skills/create-intents-utterances-and-slots.html](https://developer.amazon.com/docs/custom-skills/create-intents-utterances-and-slots.html)