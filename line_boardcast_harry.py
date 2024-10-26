import random
import pprint
import os
from dotenv import load_dotenv
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    TextMessage,
    ImageMessage,
    BroadcastRequest
)

load_dotenv()  # Load environment variables from .env file

# Access the LINE_CHANNEL_ACCESS_TOKEN from the .env file
line_channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')

configuration = Configuration(
    access_token=line_channel_access_token,
)
api_client = ApiClient(configuration)
line_bot_api = MessagingApi(api_client)


# generate function to random house in Harry potter and boardcast using BroadcastRequest 
# send ImageMessage contain house png image from https://storage.googleapis.com/gemini-code-assist-beat/
# send TextMessage contain house name and house description 
