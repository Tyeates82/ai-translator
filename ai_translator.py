# Import necessary modules
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.foundation_models import Model
import requests
import config  # Importing the configuration settings

# Use the config settings in your code
credentials = {
    "url": config.IBM_WATSON_URL,
    # "apikey": 'API_KEY'  # Uncomment and set your API key if needed
}

project_id = config.PROJECT_ID
model_id = ModelTypes[config.MODEL_ID]  # Assuming MODEL_ID is set to "FLAN_UL2" in config.py

parameters = {
    "decoding_method": config.DEFAULT_PARAMETERS["decoding_method"],
    "min_new_tokens": config.DEFAULT_PARAMETERS["min_new_tokens"],
    "max_new_tokens": config.DEFAULT_PARAMETERS["max_new_tokens"],
}

# Define the LLM
model = Model(
    model_id=model_id,
    params=parameters,
    credentials=credentials,
    project_id=project_id
)

def speech_to_text(audio_binary):
    # Set up Watson Speech-to-Text HTTP Api url using config
    api_url = config.SPEECH_TO_TEXT_URL + '/speech-to-text/api/v1/recognize'

    # Set up parameters for our HTTP request
    params = {
        'model': config.SPEECH_TO_TEXT_MODEL,
    }

    # Send a HTTP Post request
    response = requests.post(api_url, params=params, data=audio_binary).json()

    # Parse the response to get our transcribed text
    text = 'null'
    while bool(response.get('results')):
        print('Speech-to-Text response:', response)
        text = response.get('results').pop().get('alternatives').pop().get('transcript')
        print('Recognized text: ', text)
        return text

def text_to_speech(text, voice=""):
    # Set up Watson Text-to-Speech HTTP Api url using config
    api_url = config.TEXT_TO_SPEECH_URL + '/text-to-speech/api/v1/synthesize?output=output_text.wav'

    # Adding voice parameter in api_url if the user has selected a preferred voice
    if voice != "" and voice != "default":
        api_url += "&voice=" + voice

    # Set the headers for our HTTP request
    headers = {
        'Accept': 'audio/wav',
        'Content-Type': 'application/json',
    }

    # Set the body of our HTTP request
    json_data = {
        'text': text,
    }

    # Send a HTTP Post request to Watson Text-to-Speech Service
    response = requests.post(api_url, headers=headers, json=json_data)
    print('Text-to-Speech response:', response)
    return response.content

def watsonx_process_message(user_message):
    # Set the prompt for WatsonX API
    prompt = f"""You are an assistant helping translate sentences from English into Spanish.
    Translate the query to Spanish: ```{user_message}```."""
    
    # Generate response using the model
    response_text = model.generate_text(prompt=prompt)
    print("WatsonX response:", response_text)
    return response_text
