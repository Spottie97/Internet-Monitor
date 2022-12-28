import requests

def test_internet_connection(url):
    try:
        response = requests.get(url)
        return True
    except:
        return False

def send_push_notification(title, message):
    # Replace YOUR_APP_TOKEN and YOUR_USER_KEY with your Pushover API keys
    app_token = "YOUR_APP_TOKEN"
    user_key = "YOUR_USER_KEY"
    
    # Send the push notification using the Pushover API
    requests.post("https://api.pushover.net/1/messages.json", data = {
        "token": app_token,
        "user": user_key,
        "title": title,
        "message": message
    })

# Test connection to Google
is_connected = test_internet_connection("http://www.google.com")
if is_connected:
    print("Connected to the internet!")
else:
    print("Not connected to the internet :(")
    send_push_notification("Internet Connection Down", "The internet connection is down!")
