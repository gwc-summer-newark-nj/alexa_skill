from __future__ import print_function
import urllib
import json
import urllib
import re

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Hello. Welcome to the tv skill. " \
                    "I look forward to working with you."

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Hi, again. This is going to be a fun day!"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying out this fun new Alexa Skill. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def get_tv_show(intent, session):
    session_attributes = {}
    card_title = "TV Show"
    #You can change the below string any string you want.
    speech_output = "My favorite tv show is Silicon Valley. "

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Hi, again. "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_shows(show_name):
    data = urllib.parse.quote(show_name)
    print("encoded show name: " + data)
    url = "https://tvjan-tvmaze-v1.p.mashape.com/search/shows?q=" + data
    head = {"X-Mashape-Key": "759AC8LsObmshG4nM6DhorUzHhPVp1ictQfjsnjsJTALHjFdEi"}

    req = urllib.request.Request(url, headers=head)
    response = urllib.request.urlopen(req)
    respData = response.read()
    shows = json.loads(respData.decode("utf-8"))

    return shows
'''
"schedule": {
                "time": "22:00",
                "days": [
                    "Thursday"
                ]
            },
'''
def get_time(show_name):
    print("show_name: " + show_name)
    shows = get_shows(show_name)

    show_time = "Can't Find it"
    if len(shows) > 0:
        show = shows[0]
        schedule = show['show']['schedule']
        time = schedule['time']
        days = schedule['days']
        show_time = str(days) + " at " + time

    return show_time

def get_channel(show_name):
    print("show_name: " + show_name)
    shows = get_shows(show_name)

    channel = "Can't Find it"
    if len(shows) > 0:
        show = shows[0]
        channel = show['show']['network']['name']
    return channel

def clean_html(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def get_summary(show_name):
    shows = get_shows(show_name)

    summary = "Can't Find it"
    if len(shows) > 0:
        show = shows[0]
        summary = show['show']['summary']
    return summary


def get_show_name(intent):
    slots = intent['slots']
    show_name = slots['TV_SHOW']['value']
    return show_name


def get_tv_channel(intent, session):
    session_attributes = {}
    card_title = "TV Show Channel"

    # get slot data
    show_name = get_show_name(intent)
    channel = get_channel(show_name)

    speech_output = show_name + " can be found on " + channel

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Hi, again. "
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_tv_time(intent, session):
    session_attributes = {}
    card_title = "TV Show Time"

    # get slot data
    show_name = get_show_name(intent)
    tv_time = get_time(show_name)

    speech_output = show_name + " airs on " + tv_time

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Hi, again. "
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_tv_summary(intent, session):
    session_attributes = {}
    card_title = "TV Show Summary"

    show_name = get_show_name(intent)
    summary = get_summary(show_name)

    speech_output = show_name + " is about " + summary

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Hi, again. "
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))




# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "GetFavoriteTvShowIntent":
        return get_tv_show(intent, session)
    elif intent_name == "GetTvChannelIntent":
        return get_tv_channel(intent, session)
    elif intent_name == "GetTvTimeIntent":
        return get_tv_time(intent, session)
    elif intent_name == "GetTvSummaryIntent":
        return get_tv_summary(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])