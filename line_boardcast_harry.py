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
def random_house():
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    house = random.choice(houses)
    if house == "Gryffindor":
        house_description = "Brave, daring, and chivalrous"
        image_url = "https://storage.googleapis.com/gemini-code-assist-beat/Gryffindor.png"
    elif house == "Hufflepuff":
        house_description = "Hard-working, loyal, and patient"
        image_url = "https://storage.googleapis.com/gemini-code-assist-beat/Hufflepuff.png"
    elif house == "Ravenclaw":
        house_description = "Intelligent, witty, and creative"
        image_url = "https://storage.googleapis.com/gemini-code-assist-beat/Ravenclaw.png"
    elif house == "Slytherin":
        house_description = "Ambitious, cunning, and resourceful"
        image_url = "https://storage.googleapis.com/gemini-code-assist-beat/Slytherin.png"
    return house, house_description, image_url

# call random_house function and get house, house_description, image_url
house, house_description, image_url = random_house()

# create ImageMessage and TextMessage
image_message = ImageMessage(
    type="image",
    original_content_url=image_url,
    preview_image_url=image_url
)
text_message = TextMessage(
    text=f"You are in {house}! {house_description}"
)

# broadcast message using BroadcastRequest
response = line_bot_api.broadcast(
    BroadcastRequest(messages=[image_message, text_message])

)

# print response
pprint.pprint(response)

