from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotionDetector():
    if request.method == 'POST':
        statement = request.form.get('textToAnalyze')
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
    
    response_text = f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    
    return response_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)