from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    # Get the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)
    
    # Check if the dominant emotion is found
    if result['dominant_emotion'] is not None:
        # Format the response as requested
        response_text = f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
        
        return response_text
    else:
        return "Invalid text! Please try again."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)