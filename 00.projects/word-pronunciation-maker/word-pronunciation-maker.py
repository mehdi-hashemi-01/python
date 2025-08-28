from gtts import gTTS
import os
import time

# List of words with their English meanings and example sentences
words_info = [
    {
        "word": "mandatory",
        "English meaning": "required by law or rules",
        "Example": "Wearing a helmet is mandatory for all motorcyclists."
    },
    {
        "word": "struggle",
        "English meaning": "to try hard to do something difficult",
        "Example": "She struggled to finish her homework on time."
    },
    {
        "word": "compulsory",
        "English meaning": "required by law or authority; obligatory",
        "Example": "Education is compulsory for children in many countries."
    },
    {
        "word": "heterogeneous",
        "English meaning": "consisting of different or diverse parts",
        "Example": "The classroom was filled with a heterogeneous group of students."
    },
    {
        "word": "homogeneous",
        "English meaning": "consisting of parts that are all the same",
        "Example": "The village is quite homogeneous in terms of culture."
    },
    {
        "word": "hypothermias",
        "English meaning": "medical conditions where body temperature drops dangerously low",
        "Example": "Hikers risk hypothermias in freezing weather."
    },
]

# Create a folder for storing generated MP3 files
os.makedirs("audio_words", exist_ok=True)

# Loop through each word in the list and generate an MP3 file
for i, item in enumerate(words_info, start=1):
    # Combine word, meaning, and example into a single text
    text = f"{item['word']}. English meaning: {item['English meaning']}. Example: {item['Example']}."

    # Convert text to speech (English)
    tts = gTTS(text=text, lang='en')

    # Define filename format: 001_word.mp3, 002_word.mp3, etc.
    filename = f"audio_words/{i:03d}_{item['word']}.mp3"

    # Save the MP3 file
    tts.save(filename)

    # Print confirmation message
    print(f"Created: {filename}")

    # Short delay between file generations (to avoid API rate limits)
    time.sleep(0.5)
