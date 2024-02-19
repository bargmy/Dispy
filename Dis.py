print("Starting DisPy...")
import requests

def format_message(message):
    author = message['author']['username']
    content = message['content']
    return f"{author}\n  :  {content}"

def send_discord_message(token, channel):
    headers = {"authorization": token}
    url = f"https://discord.com/api/v9/channels/{channel}/messages?limit=50"
    response = requests.get(url, headers=headers)
    data = response.json()
    data.reverse()
    print("converting messages...")
    formatted_messages = [format_message(message) for message in data]
    print("\n \n \n \n \n \n \n \n \n \n \n \n ")
    for message in formatted_messages:
        print("\n", message)
    message = input("Message ( empty  for refresh ) : ")
    headers8 = {"authorization": token}
    data8 = {"content": message}
    url8 = f"https://discord.com/api/v9/channels/{channel}/messages"
    response8 = requests.post(url8, headers=headers8, data=data8)
    return

print("     Welcome to DisPy")
print("this client is based on requests on python to send and get messages using api urls...\n and requires a discord token. client is open source it means you can be sure we will not get your token.")
print(" \n \n")
token = input("Enter Your Discord Token: ")
print(" \n \n")
print("this client will not be logged in into your account..\n just use your token as authorization header for sending messages")
print(" \n \n")
channel = input("Enter Any Channel/DM ID : ")
print(" \n \n")
print("forcing discord api to load messages...")

send_discord_message(token=token, channel=channel)
