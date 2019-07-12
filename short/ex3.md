# Exercise 3

## Overview

This exercise will explore SSML and Alexa.  SSML is Speech Synthesis Markup Language, where a markup language is a system for annotating a document in a way that is syntactically distinguishable from the text. Some markup langauges you might be familiar with are HTML and XML. SSML is a markup language that provides a standard way to mark up text for the generation of synthetic speech. Alexa understands SSML and it can be used to alter the way she sounds. 


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


8. Update the function where the output text is constructed. You will need to add speech tags. For example, check out the code below. For more speech tags, check out: [SSML](https://developer.amazon.com/docs/custom-skills/speech-synthesis-markup-language-ssml-reference.html) and for different audio sounds, check out: [Sounds](https://developer.amazon.com/docs/custom-skills/ask-soundlibrary.html)

[Supported SSML] (
https://developer.amazon.com/docs/custom-skills/speech-synthesis-markup-language-ssml-reference.html#ssml-supported)


9. Save your changes, and test.

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

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Hi, again. "
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

``` 

