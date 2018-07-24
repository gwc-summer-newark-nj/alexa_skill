# Update Interaction Model with Slots


## Overview

Sometime when we interact with Alexa we need to provide information, such as a City, Zipcode, or TV Show. To provide such information,
we specify this information in the interaction model through the use of slots. A `slot` is used to capture a piece of information from the user when they interact
with the skill. A slot can be though of as a parameter in a function.  In this exercise, we will update our interaction
model to contain slots. The slots will be place-holders for a TV Show.

The following is an example illustrating a slot named `{SHOW}`. Notice the `{}` around show. These are important!

> Alexa, when is {SHOW} on? <br>
> Alexa, what time is {SHOW} on? <br>
> Alexa, what channel is {SHOW} on? <br>
> Alexa, what is {SHOW} about?

## Exercise

1. Go to [https://developer.amazon.com/lambda](https://developer.amazon.com/lambda)
2. Go to the `JSON Editor` under the Buld tab.
3. Update the `interaction model` to include a few additional `intents`, where each intent contains `slots`. You can copy and paste the entire interaction model from the repo:
[https://github.com/gwc-summer-newark-nj/gwc-summer-newark-nj.github.io/blob/master/ex/model2.json](https://github.com/gwc-summer-newark-nj/gwc-summer-newark-nj.github.io/blob/master/ex/model2.json)



```java
                {
                    "name": "GetTvChannelIntent",
                    "slots": [
                        {
                            "name": "TV_SHOW",
                            "type": "AMAZON.SearchQuery"
                        }
                    ],
                    "samples": [
                        "What channel is {TV_SHOW}",
                        "What network is {TV_SHOW}",
                        "Where can I find {TV_SHOW}",
                        "What station is {TV_SHOW}"
                    ]
                },
                {
                    "name": "GetTvTimeIntent",
                    "slots": [
                        {
                            "name": "TV_SHOW",
                            "type": "AMAZON.SearchQuery"
                        }
                    ],
                    "samples": [
                        "What time is {TV_SHOW} on",
                        "When is {TV_SHOW} on",
                        "What day is {TV_SHOW} on"
                    ]
                },
                {
                    "name": "GetTvSummaryIntent",
                    "slots": [
                        {
                            "name": "TV_SHOW",
                            "type": "AMAZON.SearchQuery"
                        }
                    ],
                    "samples": [
                        "What is {TV_SHOW} about",
                        "Tell me about {TV_SHOW} "
                    ]
                }

```

[Next: Extending our lambda function](lambdaupdate.md)

## References
[https://developer.amazon.com/docs/custom-skills/create-intents-utterances-and-slots.html](https://developer.amazon.com/docs/custom-skills/create-intents-utterances-and-slots.html)
