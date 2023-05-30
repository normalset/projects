import requests
import json

# Set up the API request headers and data
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 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',
}

data = {
    'prompt': 'Generate a sentence about a fictional character.',
    'model': 'davinci-codex',
    'temperature': 0.7,
    'max_tokens': 50,
    'n': 1,
}

# Send a GET request to the ChatGPT API
response = requests.post(
    'https://api.openai.com/v1/engines/davinci-codex/completions', headers=headers, data=json.dumps(data))

# Check if the response was successful
if response.ok:
    # Extract the generated sentence from the API response
    sentence = response.json()['choices'][0]['text'].strip()
    print(sentence)
else:
    # Print an error message if the API call failed
    print('Failed to generate sentence:', response.text)
