K.Wolf's image to speech!
Are you blind and received an image? would you like to know if it is a cute dog or a chair? 
Upload the image and well tell you!!

This application is built using Python and Flask to create a web framework

We'll be using: 
OpenCV for image processing
The "HuggingFaceM4/idefics2-8b" model from Hugging Face for image-text-to-text generation
Pyttsx3 for Text-to-speech conversion (works offline unlike gTTS)

The workflow for the user will be the following:

Uploading an image to our web framework
The image is preprocessed with OpenCV
The Image and prompt are run on the Idefics2-8B model
The model generates a text response
The generated text is converted to speech with pyttsx3
The speech is saved as an audio file
The Speech audio file is displayed to the use on the web framework

