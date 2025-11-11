# Emotion Detection Web Application

## Overview
This is a Flask-based web application that analyzes emotions in text using IBM Watson NLP's Emotion Predict service. The application processes text input and returns emotion scores for anger, disgust, fear, joy, and sadness, along with identifying the dominant emotion.

## Features
- Real-time emotion analysis using Watson NLP
- Web interface for text input
- Formatted output showing all emotion scores and dominant emotion
- Error handling for invalid or blank inputs
- Responsive design with HTML/CSS interface

## Prerequisites
- Python 3.6 or higher
- Flask
- requests library
- IBM Watson NLP access (provided through the API endpoint)

## Installation
1. Clone the repository
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   pip install flask requests
   ```
4. Ensure the EmotionDetection package is in the same directory

## Usage
1. Start the server:
   ```bash
   python server.py
   ```
2. Open your browser and navigate to `http://localhost:5000`
3. Enter text in the input field and submit to analyze emotions
4. View the emotion analysis results on the page

## API Endpoint
The application uses the Watson NLP Emotion Predict service at:
`https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict`

## Error Handling
- Blank or empty inputs return "Invalid text! Please try again."
- Invalid text that causes API errors returns the same message
- The system handles connection issues gracefully

## File Structure
- `server.py`: Flask application server
- `EmotionDetection/`: Package containing emotion detection logic
- `templates/index.html`: Web interface template
- `static/mywebscript.js`: Client-side JavaScript
- `README.md`: This file

## Testing
Unit tests are available in `test_emotion_detection.py` and can be run with:
```bash
python -m unittest test_emotion_detection.py
```

## License
[Apache License]
