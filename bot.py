# Dependencies
import numpy as np
import tweepy
import time
import json

consumer_key = 'NV4AmQgzwJzWnBaSWa5unbbnR'
consumer_secret = 'm4DOPZ7mos87XPljxZCBvnqXe29MDlKvo6wisuPN5R8r2cUBSx'
access_token = '979170021992677376-sG0j4sW3J3pY9C95f1twdsQiRxmeioa'
access_token_secret = 'rezwjR90ZDjf9m4bEjajVZUrbMjb5h0bLSNmmFKqlS76T'

# Target Term
target_term = "@929_grace"

# Opening message
print("We're going live!")

# Create Thank You Function
def ThankYou():

    # Twitter Credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Search for all tweets
    public_tweets = api.search(target_term, count=100, result_type="recent")

    # Loop through all tweets
    for tweet in public_tweets["statuses"]:

        # Get ID and Author of most recent tweet directed to me
        tweet_id = tweet["id"]
        tweet_author = tweet["user"]["screen_name"]

        # Print the tweet_id
        print(tweet_id)

        # Use Try-Except to avoid the duplicate error
        try:
            # Respond to tweet
            api.update_status(
                "Thank you @%s! Come again!" %
                tweet_author,
                in_reply_to_status_id=tweet_id)

            # Print success message
            print("Successful response!")

        except Exception:            # Print message if duplicate
            print("Already responded to this one!")

        # Print message to signify complete cycle
        print("We're done for now. I'll check again in 60 seconds.")

# Set timer to run every minute
while(True):
    ThankYou()
    time.sleep(60)

