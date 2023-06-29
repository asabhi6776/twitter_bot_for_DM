# Twitter DM Automation Script

This script automates the process of sending direct messages (DMs) to users who have commented "dm me" under a specific post on Twitter.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed on your system.
- The Tweepy library installed. You can install it using the command `pip install tweepy`.
- Twitter API credentials: consumer key, consumer secret, access token, and access token secret. You can obtain these by creating a Twitter developer account and creating an app.

## Setup

1. Clone this repository or download the script file (`twitter_dm_automation.py`) to your local machine.

2. Open the script file in a text editor or integrated development environment (IDE) of your choice.

3. Replace the placeholder values in the script with your actual Twitter API credentials. Modify the following lines with your credentials:

   ```python
   consumer_key = "YOUR_CONSUMER_KEY"
   consumer_secret = "YOUR_CONSUMER_SECRET"
   access_token = "YOUR_ACCESS_TOKEN"
   access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
   ```

Replace the SPECIFIC_POST_ID placeholder with the ID of the specific post where users have commented "dm me". You can find the post ID by looking at the URL of the tweet, which will end with a numeric value.

Save the changes to the script file.

## Usage

1. Open a terminal or command prompt and navigate to the directory where the script file is located.

2. Run the script using the command:

    ```bash
    python twitter_dm_automation.py
    ```

    The script will authenticate with your Twitter account, retrieve the comments under the specified post, and send DMs to users who have commented "dm me".

3. Monitor the terminal or command prompt for the script's output. It will display the status of each DM sent or any errors that occur during the process.

## Important Notes

- Use this script responsibly and in compliance with Twitter's terms of service and developer guidelines.

- Be cautious when automating actions on social media platforms. Ensure that you are not violating any platform policies or engaging in spammy behavior.

- The Tweepy library provides powerful features for Twitter automation. Feel free to explore the library's documentation (<https://docs.tweepy.org/>) for more functionality or customization options.

- Remember to keep your Twitter API credentials secure and not share them publicly or commit them to version control systems.

## Contributing

Contributions to this script are welcome. If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)
