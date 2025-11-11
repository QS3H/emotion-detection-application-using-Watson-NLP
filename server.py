"""
Flask application for emotion detection.
This module provides a web interface for analyzing emotions in text.
"""
from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_route():
    """
    Route to handle emotion detection requests.

    Args:
        None directly, but uses request data from GET/POST

    Returns:
        str: Formatted response with emotion scores or error message
    """
    if request.method == 'POST':
        statement = request.form.get('textToAnalyze', '')
    else:
        statement = request.args.get('textToAnalyze', '')

    result = emotion_detector(statement)

    if result is None or result['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return response_text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    