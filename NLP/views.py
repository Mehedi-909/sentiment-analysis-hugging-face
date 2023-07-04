from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import  TextSerializer
from transformers import pipeline


def map_sentiment_label(label):

    if label in ["1 star", "2 stars"]:
        return "Negative"
    elif label in ["4 stars", "5 stars"]:
        return "Positive"
    else:
        return "Neutral"


def analyze_sentiment(text):
    
    # Load the sentiment analysis model
    sentiment_classifier = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

    # Perform sentiment analysis on the input text
    sentiment = sentiment_classifier(text)[0]

    # Retrieve the sentiment label
    sentiment_label = sentiment['label']
    return map_sentiment_label(sentiment_label)


# Class based APIView
class API(APIView):

    def get(self, request, format=None):
        return Response({"text" : "Welcome"},status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TextSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text_to_analyze = serializer.data.get('text')
        sentiment = analyze_sentiment(text_to_analyze)
        response = {"sentiment" : sentiment}
        return Response(response, status=status.HTTP_200_OK)


