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

## Exercise

1. Go to [https://developer.amazon.com/lambda](https://developer.amazon.com/lambda)
2. Go to the `JSON Editor` under the Buld tab.
3. Update the interaction model to include an additional intent. You can copy and paste the entire interaction model from repo:
[https://github.com/gwc-summer-newark-nj/gwc-summer-newark-nj.github.io/blob/master/ex/model2.json](https://github.com/gwc-summer-newark-nj/gwc-summer-newark-nj.github.io/blob/master/ex/model2.json)



```java

{
    "name": "GetTvShowChannelIntent",
    "slots" : [
     {
      "name": "SHOW",
      "type": "AMAZON.SearchQuery"",
     }

    ]
    "samples" : [
      "What channel is {SHOW} on",
      "What network can I find my {SHOW}""
     ]

}

```

[Next: Extending our lambda function](lambdaupdate.md)

## References
[https://developer.amazon.com/docs/custom-skills/create-intents-utterances-and-slots.html](https://developer.amazon.com/docs/custom-skills/create-intents-utterances-and-slots.html)