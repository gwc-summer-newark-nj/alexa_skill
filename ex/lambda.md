# Creating a Lambda Function

## Overview
An AWS lambda function let's you run code without having a server. It is also known as a server-less function.
We are going to write a lambda function that will be invoked when a user utters one of the phrases entered
in the previous section. The lambda function will know how to handle the response from Alexa and return a response.


## Exercise
1. Go to [https://aws.amazon.com/lambda](https://aws.amazon.com/lambda).
2. Login with the credentials provided.
3. Click the orange `Create function` on the right hand side fo the screen.
4. Next fill in the form with the follow information:
![alt text](../img/lambda_create_function.png "Create Lambda Function")
* Name: `alexa-tv-skill`
* Runtime: `Python 3.6`
* Role: `Create a custom role.` Next screen click `Allow`.
5. Click `Create function`
6. Scroll down to the `Function Code` section. Go to [https://github.com/gwc-summer-newark-nj/gwc-summer-newark-nj.github.io/blob/master/ex/ex1.py](https://github.com/gwc-summer-newark-nj/gwc-summer-newark-nj.github.io/blob/master/ex/ex1.py)
7. The python code for the lambda function should appear. Click on Raw.
8. Copy the python code and paste in the aws lambda editor.
9. Once you pasted the code, find the method for `get_tv_show` and change the `speech_output` variable to be your favorite show.

```python

def get_tv_show(intent, session):

    card_title = "TV Show"
    #You can change the below string any string you want.
    speech_output = "My favorite tv show is Silicon Valley. "

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Hi, again. "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

```

7. Scroll up in the `Designer` section. Add a trigger. Click `Alexa Skills Kit`. Then click on configure Alexa Skill.
Need to copy Skill Id from [https://developer.amazon.com/alexa](https://developer.amazon.com/alexa)
8. Click Save.

[Next: link together model and lambda function](link.md)


