import requests
from sys import argv

def main():
# Get the user number from the command line
    user_num = argv[1]

# Get the user info from the API as a dictionary
    user_info = get_user_info(user_num)
    if user_info:

# Get the title and body text strings for PasteBin
        pb_strings = get_title_and_text(user_info)

# Post the title and body text to PasteBin
        pb_url = post_to_pastebin(pb_strings[0], pb_strings[1])

# Print the URL of the new PasteBin paste
        print(pb_url)

def get_user_info(user_num):
    print("Getting user information...", end='')
    URL = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(URL + str(user_num))

    if response.status_code == 200:
        print('success')
        return response.json() # Convert response body to a dictionary
    else:
        print('failed. Response code:', response.status_code)
        return

def get_title_and_text(user_dict):
    title = user_dict['name'] + "'s information"
    body_text = "Name: " + user_dict['name'] + "\n"
    body_text += "Abilities: " + user_dict['abilities']['ability']['name']
    return (title, body_text)

def post_to_pastebin(title, body_text):
    print("Posting to PasteBin...", end='')

    params = {
        'api_dev_key': "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title
    }
    URL = 'https://pastebin.com/api/api_post.php'
    response = requests.post(URL, data=params)

    if response.status_code == 200:
        print('success')
        return response.text # Converts response body to a string
    else:
        print('failed. Response code:', response.status_code)
        return response.status_code

main()