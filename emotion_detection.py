import requests
import json

# define emotion detection using Emotion Predict function of the Watson NLP Library
def emotion_detector(text_to_analyse):
    # url for emotion predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # set a header requirements
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # create a dictionary with the text to be analyzed
    obj = { "raw_document": { "text": text_to_analyse } }

    # Send post request to the API with text and header
    response = requests.post(url, json = obj, headers = headers )

    # Return the response from the API
    formatted_response = json.loads(response.text)

    return (formatted_response)

emotion_detector('The Weather is too good. I feel Like going to play soccer.')
