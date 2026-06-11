import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL of the sentiment analysis service 
    myobj = { "raw_document": { "text": text_to_analyze } } # Create a dictionary with the text to be analyzed 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Set the headers required for the API request 
    response = requests.post(url, json = myobj, headers=header) # Send a POST request to the API with the text and headers 
    
    #Parsing the JSON response from the API 
    formatted_response = json.loads(response.text)

    # Extracting emotions label and score from the response 
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Returning a dictionary containing sentiment analysis results 
    return {'anger': emotions['anger'], 'disgust': emotions['disgust'],'fear': emotions['fear'], 'joy': emotions['joy'], 'sadness': emotions['sadness'], 'dominant_emotion': max(emotions, key=emotions.get)}

