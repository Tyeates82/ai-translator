# config.py

# WatsonX API Credentials
WATSONX_API = "Your WatsonX API"
PROJECT_ID = "Your Project ID"

# IBM Watson Machine Learning URL
IBM_WATSON_URL = "https://us-south.ml.cloud.ibm.com"

# Model Configuration
MODEL_ID = "FLAN_UL2"

# Default Parameters for the Model
DEFAULT_PARAMETERS = {
    "decoding_method": "greedy",  # You can set this to "beam_search" or others as per your requirement
    "min_new_tokens": 1,
    "max_new_tokens": 1024
}

# Watson Speech-to-Text Configuration
SPEECH_TO_TEXT_MODEL = "en-US_Multimedia"
SPEECH_TO_TEXT_URL = "https://your-speech-to-text-url"

# Watson Text-to-Speech Configuration
TEXT_TO_SPEECH_URL = "https://your-text-to-speech-url"

# Default Voice for Text-to-Speech (optional)
DEFAULT_VOICE = "en-US_AllisonVoice"  # You can customize this or leave it blank for default
