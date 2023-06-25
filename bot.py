import tweepy

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# ID of the specific post where users have commented "dm me"
post_id = "SPECIFIC_POST_ID"

# Retrieve the comments under the post
comments = api.search(q=f"to:{api.me().screen_name}", since_id=post_id)

# Iterate over the comments and send DMs
for comment in comments:
    user_id = comment.user.id_str
    username = comment.user.screen_name
    comment_text = comment.text.lower()

    if "dm me" in comment_text:
        message = "Hello! I noticed your comment, and I'm here to assist you. How can I help?"

        try:
            api.send_direct_message(user_id, message)
            print(f"DM sent to {username} successfully.")
        except tweepy.TweepError as e:
            print(f"Error sending DM to {username}: {str(e)}")
