# Exercise 3

## Overview

This exercise will explore SSML and Alexa.  SSML is Speech Synthesis Markup Language, where a markup language is a computer language that uses tags to define elements within a document. Some markup langauges you might be familiar with are HTML and XML. SSML is a markup language that provides a standard way to mark up text for the generation of synthetic speech. Alexa understands SSML and it can be used to alter Alexa's voice. 


###  How to use SSML

To use SSML, construct your output speech using the supported SSML tags. When sending back a response from your service, you must indicate that it is using SSML rather than plain text.  

For example, in our function `build_speechlet_response`, 
the `outputSpeech` `type` is referenced as `plainText`. Alter the `type` to be `SSML`, and `text` to `ssml`: 
```
"outputSpeech": {
    "type": "SSML",
    "ssml": "<speak>This output speech uses SSML.</speak>"
}
```


### Steps for Exercise 3
1. Update the `outputSpeech` values as shown above. 

1. Update the function where the output text is constructed. You will need to add speech tags around the constructed output. It is up to you how you want Alexa to respond and sound. For example, the code below illustrates using `<amazon:effect >` tag and an `<emphasis level/>` tag within the `speech_output`. 
For more speech tags, check out: [Supported SSML](https://developer.amazon.com/docs/custom-skills/speech-synthesis-markup-language-ssml-reference.html#ssml-supported) and for different audio sounds, check out: [Sounds](https://developer.amazon.com/docs/custom-skills/ask-soundlibrary.html)

1. Save your changes and test the results. You can alter the SSML and try out different sounds and effects. 


### Example code
 
```python
def get_tv_summary(intent, session):
    session_attributes = {}
    card_title = "TV Show Summary"

    show_name = get_show_name(intent)
    summary = get_summary(show_name)

    speech_output =
         '<speak>' +
             'Silicon valley is a show about ' +
             '<amazon:effect name="whispered">' + summary + '</amazon:effect>.' +
             '<emphasis level="strong">Can you believe it?</emphasis>' +
         '</speak>'


    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

``` 

