## What is an Alexa Skill?

Alexa is Amazon’s voice service and the brain behind tens of millions of devices like the Echo family of devices including Echo Show and Echo Spot. 
Alexa provides capabilities, or skills, that enable customers to create a more personalized experience. 

Did you know that 30000 Alexa skills exist today and that is 29000 more than existed two years ago.
At that rate, how many Alexa skill will be developed by 2020?




## Overview of Creating an Alexa Skill
Alexa Skills can be implemented to do many things like ordering a pizza, telling you the weather, playing a game,
turning on your lights, or any other thing you can imagine! There is a ton of information on the web to teach how to create an Alexa skill. 
Check out the [Alexa Skills Kit](https://developer.amazon.com/alexa-skills-kit) after this workshop to dig deeper into Alexa skill development.

To get started today, we are going to learn some new terminology, and then learn how to create an Alexa skill.


Writing an Alexa skill involves some new terminology:
1. `Interaction Model` or `Voice UI`: defines the words and phrases users can say to make the skill do what they want. This model determines how Alexa communicates with your users.
2. `Utterance`: A set of likely spoken phrases mapped to the intents. This should include as many representative phrases as possible.
3. `Intent`: An intent represents an action that fulfills a user's spoken request. Intents can optionally have arguments called slots.
4. `Invocation` name: the name used by the user to invoke an Alexa  skill. For example, Alexa ask the weather channel, what is the weather? The `weather channel` is the invocation name.  
5. `Lambda function`: AWS Lambda is a service that allows code to run in the cloud. The user does not manage the server. A Lambda function is required to handle requests from Alexa, process them and return a response that Alexa understands. 



There are four main steps to creating an Alexa skill.
1. Define an `interaction model`.
2. Implement code to handle and respond to the users `utterance` in a `lambda function`.
3. Configure the `Alexa skill` to talk to the `lambda function`
4. Test your Alexa skill

## Getting Started

Our workshop today involves implementing an Alexa skill. The goal by the end of the workshop is to implement the steps required for creating an Alexa skill. We will guide you through the process via a series of exercises, each containing a set of steps to be followed. Then you will customize your skill to make it unique! 
We hope you enjoy learning about Alexa skills today!

To begin, log into a couple of Amazon related websites. Open up new tabs by clicking on the links below.
- [https://aws.amazon.com](https://aws.amazon.com)
- [https://developer.amazon.com](http://developer.amazon.com)

## Building an Alexa Skill

- [Exercise 1: Alexa skill: Hello World!](ex/ex1.md)
- [Exercise 2: Alexa skill: TV Show Finder](ex/ex2.md)
- [Exercise 3: Alexa skill: Customize TV Show Finder](ex/ex3.md)

## References
* [Youtube video](https://www.youtube.com/watch?v=ei_q4saWwcE)
* [Alexa Skills Kit](https://developer.amazon.com/docs/ask-overviews/build-skills-with-the-alexa-skills-kit.html)
* [Alexa Design Guide](http//alexa.design/guide)
