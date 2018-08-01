# Update lambda function to use slots

For this exercise, we are going to explore an API (Application Programming Interface), update our lambda function to use the slot we added to our interaction model and invoke an API, 
parse the response from the API, and construct a response that Alexa understands. Wow that sounds complicated. Don't worry there are instructions for each step. 

The API we are going to use is from: [Marketplace Mashape](https://market.mashape.com/dashboard). This is a site that provides a searchable listing of APIs for all sorts of things, like Movie listings, random quotes, food nutrition. I choose to use a `TV Show API`, however, we could be using any external api from our lambda function.
The `TV Show API` provides an interface that allows the user to query shows, actors, and tv schedules.

We are going to use the value of the slot in our lambda function and pass that value to the `TV Show API`.

## Exercise
1. Try out the  [TV Show API](https://market.mashape.com/tvjan/tvmaze). Type in a TV Show name and click `TEST ENDPOINT`. A `JSON` response will be returned. Look through the response to get an idea of what an API can return. 
1. Go to [https://aws.amazon.com/lambda](https://aws.amazon.com/lambda)
2. Copy new Lambda function into editor: [https://github.com/gwc-summer-newark-nj/gwc-summer-newark-nj.github.io/blob/master/ex/lambda2.py](https://github.com/gwc-summer-newark-nj/gwc-summer-newark-nj.github.io/blob/master/ex/lambda2.py)
3. Check out the new intents that are now recognized, `GetTvChannelIntent`, `GetTvTimeIntent`, `GetTvSummaryIntent`. Each intent invokes a corresponding function that invokes the `TV Show API`, and then parses the response, and then constructs a response for Alexa. Can you follow the flow?
5. Can you find where the slot is obtained in the code?  
4. Make sure you saved your `Lambda Function` in the AWS editor. Then you can move on to the next step.

[Next: Test your latest Alexa skill](test2.md)
