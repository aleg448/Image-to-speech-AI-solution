K.Wolf's Image-to-Text-to-Speech!
Are you blind and received an image? Would you like to know if it is a cute dog or a chair?
Upload the image, and we'll tell you!!

If you are the intended recipient, Hi to the folks at ☆, This app was developed in 8 hours including lunch break and I managed to get it working just in time!
I had a few issues getting a mLLM like LLava and scaled back to a more manageable model "vit-gpt2-image-captioning"
This model unfortunately was not able to run the imaginative part of the task and so we only get an imaginative description.
With more time my next approach would be to get  a more imaginative LLM running with the text input to create a story, Cheers!


This application is built using Python and Flask to create a web framework.

We'll be using:
- The "nlpconnect/vit-gpt2-image-captioning" model from Hugging Face for image-to-text generation
- Pyttsx3 for Text-to-Speech conversion (works offline unlike gTTS)


1. Uploading an image to our web framework
2. The image and a prompt are passed to the Hugging Face model
3. The model generates a text response describing the image
4. The generated text is converted to speech with pyttsx3
5. The speech is saved as an audio file with a unique filename
6. The text response and the audio file are displayed to the user on the web framework

You can install the requirements for this project with:
"pip install -r requirements.txt"

To run the application locally:
1. Install the required packages: `pip install -r requirements.txt`
2. Run the Flask app: `python app.py`
3. Access the application in your web browser at `http://localhost:5000`