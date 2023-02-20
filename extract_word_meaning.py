import requests
from bs4 import BeautifulSoup

# Read in list of words from file
with open('word_list.txt', 'r') as f:
    words = f.read().splitlines()

# Set up base URLs for Merriam-Webster and Etymology Online
mw_base_url = 'https://www.merriam-webster.com/dictionary/'
eo_base_url = 'https://www.etymonline.com/word/'

# Loop over words and get their meanings and origins
results = []
for word in words:
    # Get meaning from Merriam-Webster website
    response = requests.get(f'{mw_base_url}{word}')
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            meaning = soup.find(class_='dtText').text
        except AttributeError:
            meaning = ''
    else:
        meaning = ''

    # Get origin from Etymology Online website
    response = requests.get(f'{eo_base_url}{word}')
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            origin = soup.find('section', {'id': 'etymology'}).find('p').text
        except AttributeError:
            origin = ''
    else:
        origin = ''

    # Add word, meaning, and origin to results list
    results.append(f'{word}: {meaning}: {origin}')

# Write results to file
with open('word_results.txt', 'w') as f:
    f.write('\n'.join(results))
