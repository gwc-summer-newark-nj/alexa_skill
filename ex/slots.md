# Update Interaction Model with Slots


## Overview

Sometime when we interact with Alexa we need to provide information, such as a City, Zipcode, or TV Show. To provide such information,
we specify this information in the interaction model. In the interaction model, we define `slots` which specify that when a user interacts
with the skill, a piece of information from the utterance needs to be treated differently. In this exercise, we will update our interaction
model to contain slots. The slots will be place holders for a TV Show.

The following is an example illustrating a slot named `{SHOW}`. Notice the `{}` around show. These are important!

> Alexa, when is {SHOW} on?
> Alexa, What time is {SHOW} on?
> What channel is {SHOW} on?
> What is {SHOW} about?

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

<a href="lambdaupdate.md"> Next: Extending lambda function</a>

## References
[https://developer.amazon.com/docs/custom-skills/create-intents-utterances-and-slots.html](https://developer.amazon.com/docs/custom-skills/create-intents-utterances-and-slots.html)