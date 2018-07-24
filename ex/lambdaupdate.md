# Update lambda function to use slots

Now when our lambda function is invoked, we can access the slot, which contains information about a specific show to query.
Our lambda function will invoke a TV Show API, which will return information about the TV show. We will create a response containing the
information obtained from the TV Show API.

The TV Show API we are using is from: [Marketplace Mashape](https://market.mashape.com/dashboard). This is a site that provides a searchable listing of APIs for all sorts of things, like Movie listings, random quotes, food nutrition. I choose to use the TV Show API, however, we could be using any external api from our lambda function.   
The TV Show API provides an interface that allows the user to query shows, actors, and schedules. 

For this exercise, we are going to explore the TV Show API and update our lambda function to invoke the TV Show API, parse the response, and construct a response that ALExa understands. 


## Exercise
1. Try out the TV Show API: [TV Show API]({https://market.mashape.com/tvjan/tvmaze). Type in a TV Show name and click `TEST ENDPOINT`. A JSON response will be returned. Look through the response to get an idea of what an API returns. 
1. Go to [https://aws.amazon.com/lambda](https://aws.amazon.com/lambda)
2. Copy new Lambda function into editor: [https://github.com/gwc-summer-newark-nj/gwc-summer-newark-nj.github.io/blob/master/ex/lambda2.py](https://github.com/gwc-summer-newark-nj/gwc-summer-newark-nj.github.io/blob/master/ex/lambda2.py)
3. Check out the new intents that are now recognized, `GetTvChannelIntent`, `GetTvTimeIntent`, `GetTvSummaryIntent`. Each intent invokes a corresponding function that invokes the TV Show API, and then parses the response, and then constructs a response for Alexa. Can you follow the flow? 
4. Make sure you saved your Lambda Function in the AWS editor. Then you can move on to the next step.

[Next: Test your latest Alexa skill](test2.md)
