# Next-Word Text Prediction with LSTM

## Project Overview

The **Next-Word Text Prediction with LSTM** project is an application that predicts the next word in a sequence based on user input, leveraging Long Short-Term Memory (LSTM) models. This project supports dynamic writing styles such as **Casual**, **Formal**, **Technical**, and **Email**, offering personalized suggestions. By predicting the next word as you type, the application helps enhance productivity, particularly in drafting emails, technical documents, or casual conversations.

### Key Features:
- **Real-time word prediction**: As users type, the application predicts the next word based on the provided text, enhancing typing speed.
- **Dynamic layout**: The interface changes depending on the selected writing style, providing a unique experience for Casual, Formal, Technical, or Email writing.
- **Interactive word suggestions**: Users can click on any predicted word, and it gets appended to the input text, enabling easy text completion.
- **Model-specific tokenization**: Each writing style has its own trained tokenizer, which ensures that predictions align with the vocabulary and structure of that style.
- **Adaptive UI**: The layout adapts to the selected writing style, reflecting different text formatting and functionality according to each use case (e.g., professional emails or informal chat).

## Technology Stack:
- **Python**: Backend development using Python.
- **Flask**: Web framework for backend API development and serving the frontend.
- **TensorFlow/Keras**: For training and utilizing LSTM models for word prediction.
- **JavaScript**: Handles real-time frontend interaction and AJAX calls to the backend for predictions.
- **HTML5**: Structure of the web interface.
- **CSS3**: Styling for a responsive and user-friendly layout.
- **Pickle**: Saving and loading tokenizers specific to each writing style.
- **JQuery**: For easy DOM manipulation and handling AJAX requests.

## Project Structure:
<pre>
nextword-prediction/ │
                     ├── app.py # Flask app that serves the backend and handles predictions 
                     ├── predictor.py # Contains functions to load models and make predictions 
                     ├── models/ # Directory containing model files and tokenizers 
                     │ ├── casual_model.h5 
                     │ ├── formal_model.h5 
                     │ ├── technical_model.h5 
                     │ ├── email_model.h5 
                     │ ├── casual_tokenizer.pickle 
                     │ ├── formal_tokenizer.pickle 
                     │ ├── technical_tokenizer.pickle 
                     │ └── email_tokenizer.pickle 
                     ├── templates/ 
                     │ └── index.html # Frontend HTML for the web interface 
                     ├── static/ 
                     │ ├── css/ 
                     │ │ └── style.css # Styling for the app's frontend 
                     │ └── js/ 
                     │ └── script.js # JavaScript to handle predictions and UI behavior 
                     ├── requirements.txt # Python dependencies for the project
</pre>
## How the Application Works:

### 1. **User Interaction**:
   - The user starts typing a sentence or phrase into a text input field.
   - As the user types, the application dynamically predicts the next possible word.
   - The user can select any of the predicted words by clicking on them, and the word is appended to the input field.
   - The application continuously updates predictions based on the latest word typed.

### 2. **Backend (Flask)**:
   - The Flask app serves the main HTML frontend and handles the communication between the user input and the trained models.
   - When a user types in the input field, the Flask backend receives the request through an AJAX call and uses the LSTM model to predict the next word.
   - Each writing style (Casual, Formal, Technical, Email) has a separate LSTM model, and Flask loads the corresponding model for each type of prediction.
   - The Flask app sends the predictions back to the frontend where the JavaScript displays them for the user to select.

### 3. **Machine Learning Models**:
   - The project uses pre-trained **LSTM models** for each writing style, such as `casual_model.h5`, `formal_model.h5`, etc. These models are trained using a large corpus of text for each category to understand the word patterns and language structure.
   - The models take the text typed by the user, process it using the tokenizer specific to the style, and predict the next word.
   - **Tokenizer**: Each writing style (Casual, Formal, Technical, Email) uses a **unique tokenizer** that was trained alongside the respective LSTM model. This ensures that the predictions are specific to the type of content being written.

### 4. **Frontend (HTML, CSS, JavaScript)**:
   - The frontend is built using **HTML5** and **CSS3** to create a responsive, user-friendly interface.
   - **JavaScript/jQuery** is used to handle the real-time interaction and make AJAX requests to the Flask backend when the user types.
   - **Predictions**: As the user types, the JavaScript fetches the next-word predictions from the backend and displays them on the UI. When the user clicks a prediction, the text input field is updated with the selected word.

## Detailed Explanation of Files:

### `app.py`:
- This is the core Flask application file that initializes the server, handles incoming requests, and returns predictions.
- It loads the pre-trained models and tokenizers, and sends the appropriate predictions based on the selected writing style.

### `predictor.py`:
- **`load_trained_model()`**: This function loads the pre-trained LSTM model for each writing style from the file system using Keras.
- **`predict_next_word()`**: This function takes the user’s input, processes it using the relevant tokenizer, and predicts the next word using the LSTM model.

### `models/`:
- Contains all the pre-trained models and tokenizers for each writing style:
  - `casual_model.h5`, `formal_model.h5`, `technical_model.h5`, `email_model.h5`: These are the LSTM models trained on different corpora for each style.
  - `casual_tokenizer.pickle`, `formal_tokenizer.pickle`, `technical_tokenizer.pickle`, `email_tokenizer.pickle`: These tokenizers are used to transform input text into sequences that the LSTM models can process.

### `index.html`:
- The main HTML file that structures the frontend interface. It contains a text input field, prediction display area, and dropdown for selecting the writing style.
- The layout changes dynamically based on the style selected, using CSS classes applied by JavaScript.

### `style.css`:
- This file contains the CSS to style the web interface. It ensures the layout is responsive and adapts based on the selected writing style.
- Custom styles for different writing styles, buttons, and predictions are applied here.

### `script.js`:
- Contains JavaScript code that handles the real-time prediction feature. It listens for user input and triggers AJAX requests to the Flask backend for word predictions.
- It updates the UI with the predicted words and allows users to select words for auto-completion.

## Installation Instructions

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/nextword-prediction.git
cd nextword-prediction
