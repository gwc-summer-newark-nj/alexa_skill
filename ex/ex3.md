# Exercise 3

## Overview

This exercise is open-ended. It is time for you to customize your Alexa skill. Is there other information you want to return? Should Alexa respond differently? Be creative?
Ask questions? Is there something you want your skill to do but you don't know how to get started, then also please ask! 

The following are some ideas if you are stuck, otherwise, you are free to come up with other ideas and implement them!

1. The summary response contains html tags. Can you clean up the response? Hint: There is a function `clean_html` contained in the python lambda code. 
2. The summary doesn’t always sound good or it is too long. How could you fix it?
3. How could you clean up  the tv times? Can you convert the time to 12 hour time instead of military time? 
4. Some shows are on everyday of the week. Can your skill handle that case?
5. Customize the responses to how you think Alexa should respond, what makes sense to you?
6. Do the interaction model sample utterance make sense? Are there additional utterances that you think would be better?
7. Alexa can understand SSML, which is voice mark up language. In the function `build_speechlet_response`, the `outputSpeech` `type` is referenced as `plainText`. Alter the `type` to be `SSML`, and `text` to `ssml`,  for example: 
```
"outputSpeech": {
    "type": "SSML",
    "ssml": "<speak>This output speech uses SSML.</speak>"
}
```

8. Update a function where the output text is constructed. You will need to add speech tags. For example, check out the code below. For more speech tags, check out: [SSML](https://developer.amazon.com/docs/custom-skills/speech-synthesis-markup-language-ssml-reference.html) and for different audio sounds, check out: [Sounds](https://developer.amazon.com/docs/custom-skills/ask-soundlibrary.html)

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

