# sendtweetstomail
Send all public tweets from given users to your mail

## Requirements

1. First install the required packages

Python3

````
python3 -m venv myenv
source myenv/bin/activate // on MacOS
source myenv/Scripts/activate // on Windows
pip install -r requirements.txt
````

2. Api Key

You also need to have a API key working from https://developer.x.com/

Once you have it, put it into your env variables :
````
export TWITTER_API_KEY='AAAAAAAAAAAAAAAAAAAA'
````

## How to execute

Go in the same folder than the python script

````
$ python3 send_tweets_to_mail.py 'elonmusk' 
````

