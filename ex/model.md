# Creating an Interaction Model

## Overview

1. Go to: [https://developer.amazon.com/alexa](https://developer.amazon.com/alexa) This is the Amazon developer site providing access to a set of tools
used to develop programs that interact with Amazon. For example, have you ever gone to a web-site or app that allows you to login with your amazon
credentials? This is the site developers need to go to set up that access for users. For our case, we will be using [https://developer.amazon.com](https://developer.amazon.com)
to create our Alexa skill.
2. Login into [https://developer.amazon.com/alexa](https://developer.amazon.com/alexa) using the credentials we have supplied.
3. Click on the Toolbar on the top right that says Your Alexa Consoles and click on Skills.
![alt text](img/alexa_skills_console.png "Your Alexa Consoles")
4. Click the button on the right that says Create Skill.
5. Enter skill name: TV Show Findeas the model for your skill.
6. Click Create Skill button on the right.
![alt text](img/alexa_dashboard.png "Custom Model Dashboard")
7. Now we need to tell Alexa how to invoke our skill. Click Invocation. Type: `tv show finder` (notice only lower case letters). <br>
Users will invoke our skill as follows:
 >  User: Alexa, ask TV Show Finder what station can I find Silicon Valley.
8. Next we need to tell Alexa how we expect users to interact with our Skill and what to do when Alexa hears those phrases.
> What phrases will users say to interact with our skill?
> What should Alexa do once hearing those phrases?
For now, we are going to make it super simple. Click JSON Editor on the left column.
Select the entire interaction model that shows up in the editor, and delete it. Then copy our interaction model below and paste into
JSON editor.

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
9. Click `Save Model` at the top of the page. If there are any errors, try to figure out the problem or ask a volunteer to help you out.
10. Once your have saved successfully, then click `Build Model`. This will take a couple of minutes to complete.
11. Click on `Endpoint` from the left-hand side menu. This is where we will specify what Lambda function to call when a user interacts with our Alexa Skill.
For now, just click `Copy to Clipboard` next to your `Your Skill ID`.


<a href="lambda.md"> Next implement a lambda function</a>

