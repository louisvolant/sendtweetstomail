# weather.py

import os
import logging
import argparse
import tweepy

# README
# execute with
# python3 -m venv myenv
# source myenv/bin/activate # on MacOS
# source myenv/Scripts/activate # on Windows
# pip install -r requirements.txt
# python3 send_tweets_to_mail.py 'elonmusk'
# Once finished, simply desactivate the virtual environment using "deactivate"


# Function to get user tweets
def get_user_tweets(client, username, max_results=100):
    # Get user ID
    user = client.get_user(username=username)
    user_id = user.data.id

    # Get tweets
    tweets = client.get_users_tweets(
        id=user_id,
        max_results=max_results,
        tweet_fields=['created_at', 'public_metrics']
    )

    return tweets.data


def main():
    parser = argparse.ArgumentParser(description='Retrieve tweets for a given username.')
    parser.add_argument('username', type=str, help='The user on X you wish to see the latest tweets')
    args = parser.parse_args()

    TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')

    # Create a client instance
    client = tweepy.Client(bearer_token=TWITTER_API_KEY)

    tweets = get_user_tweets(client, args.username)

    # Print tweets
    for tweet in tweets:
        logging.info(f"Tweet ID: {tweet.id}")
        logging.info(f"Text: {tweet.text}")
        logging.info(f"Created at: {tweet.created_at}")
        logging.info(f"Retweets: {tweet.public_metrics['retweet_count']}")
        logging.info(f"Likes: {tweet.public_metrics['like_count']}")
        logging.info("---")


if __name__ == '__main__':
    ## Initialize logging before hitting main, in case we need extra debuggability
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')
    main()
