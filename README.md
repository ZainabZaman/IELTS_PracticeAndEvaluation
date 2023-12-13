# IELTS_PracticeAndEvaluation
IELTS is a globally recognized English language proficiency test designed to assess the language skills of individuals who aim to study, work, or migrate in English-speaking countries. The test consists of four main modules: **Listening, Reading, Writing, and Speaking,** each evaluating different language abilities to provide a comprehensive overview of a candidate's English proficiency. The scores obtained in these modules contribute to an overall IELTS band score, ranging from 1 to 9, with 9 being the highest proficiency level.

Similarly PTE a.k.a Pearson Test of English, is an English language proficiency test similar to IELTS, recognized globally for academic and immigration purposes. PTE assesses candidates through Speaking and Writing, Reading, and Listening modules. Both tests serve as reliable measures of English language proficiency, but PTE is known for its computer-based format and quicker result turnaround compared to IELTS.
This project evaluates user responses for each IELTS module and calculates an overall score, IELTS band, and it's corresponding PTE score based on the responses.

This project contains five modules i.e.
- Listening evaluation
- Speaking evaluation
- Reading evaluation
- Writing evaluation [Image based]
- Writing evaluation [Text based]

## Getting Started 
- Clone the repository:
  ```python
  git clone https://github.com/ZainabZaman/IELTS_PracticeAndEvaluation.git
  ```
- Install the required dependencies:
  ```python
  pip install -r requirements.txt
  ```
- While executing any of the file replace 'YOUR_OPENAI_API_KEY' in the code with your OpenAI API key and 'YOUR_AZURE_SPEECH_STUDIO_API_KEY' with your azure speech studio key.

## User Class
The user class contains the following functionalities 
- `create_user`: Creates a new user if the user ID does not exist.
- `save_evaluation`: Saves the evaluation results for a user.
- `load_saved_dict`: Loads the saved evaluation dictionary for a user.
- `is_user`: Checks if the user exists.
- `delete_previous_context`: Deletes the previous context for a user.
- `evaluation_scores`: Computes the relevancy score and updates the evaluation results.

## IELTS Listening Module
IELTS listening evaluation can be executed by passing user_ID, audio_file_from_the_bot, user_response_text in the listening function in the listening_final.py file such that there can be punctuation variation but the bot audio and the final user response string passed should be the same.
```python
listening(4, '.\why-hello-there-103596.wav', "well hello there")
```
```python
py listening_final.py
```

## IELTS Speaking Module
IELTS speaking evaluation can be executed by passing user_ID, topic_based_text_from_the_bot, user_audio_response in the speaking function in the speaking_final.py. The speaking evaluation is a conversational assessment where the bot evaluates responses from the user through a conversation on a partiular topic. 
```python
speaking(2, "How often do you like to travel?", '.\i_like_to_travel_once_or_twice_a_year.wav')
```
```python
py speaking_final.py
```

## IELTS Reading Module
IELTS reading evaluation can be executed by passing user_ID, question_shown_to_user_by_bot, user_text_response in the reading function in the reading_final.py such that the user response should is a sub-string of the bot's text.
```python
reading(1, 'a hot cup of coffee', "COFFEE")
```
```python
py reading_final.py
```

## IELTS Writing Module [Image based]
IELTS writing evaluation [image based] can be executed by passing user_ID, image_path_for_image_to_be_explained, TEXT_image_description_by_user in the writing_image_evaluation function in the writing_image_evaluation_final.py.
```python
writing_image_evaluation(6, ".\img01.jpg", "This is an artistic picture showing a blue car floating in the sky among the clouds. The sky looks nice with light and fluffy clouds. The image has a dreamy feel because cars do not fly in real life. There are words on the bottom that say “FAST CAR PIANO MAGE. DREAM. MIDNIGHTS.” It looks like an edit or a fantasy picture because the car is in the air like a big airplane. The colors are soft and give a calm feeling.")
```
```python
py writing_image_evaluation_final.py
```

## IELTS Writing Module [text based]
IELTS writing evaluation [text based] can be executed by passing user_ID, topic_for_writing_a_paragraph_on, TEXT_paragraph_by_user_on_the_given_topic in the text_evaluation function in the writing_text_evaluation_final.py.
```python
text_evaluation(5, "Write a passage reflecting on the role of cars in your life, your favorite type of car, or any memorable experiences you've had with automobiles. What do cars mean to you, and how do they contribute to your daily life or sense of adventure? Take a moment to explore the fascinating world of cars through your own perspective.", "Cars, the modern marvels of transportation, have transformed the way we move, connect, and explore the world. From the early days of horseless carriages to the sleek, high-tech vehicles of today, the evolution of cars has been a testament to human innovation and engineering prowess. These four-wheeled machines have not only revolutionized our daily commute but have also become symbols of freedom, status, and style. In the 19th century, the invention of the automobile marked a pivotal moment in history. Karl Benz, often credited with creating the first true automobile, set in motion a chain of events that would reshape society. The simple, rattling contraptions of the past have given way to a diverse range of vehicles catering to every need and desire. Whether it's the efficient and eco-friendly electric cars, the powerful and adrenaline-pumping sports cars, or the sturdy and reliable SUVs, there is a car for every personality and lifestyle. The automotive industry has not only focused on improving the efficiency and performance of cars but has also embraced cutting-edge technologies. Advanced safety features, autonomous driving capabilities, and smart connectivity have become integral parts of modern cars. The intersection of artificial intelligence and automotive engineering has opened up new possibilities, promising a future where cars are not just means of transportation but intelligent companions on the road. Yet, the love for cars extends beyond their technical aspects. Car enthusiasts often find themselves immersed in the aesthetics, design, and history of automobiles. Classic cars, with their timeless charm, evoke a sense of nostalgia, while futuristic concept cars captivate our imagination and hint at the possibilities that lie ahead. As we continue to navigate the ever-changing landscape of transportation, cars remain at the forefront of innovation and societal progress. From reducing carbon emissions to redefining the concept of mobility, cars are poised to play a central role in shaping the future of our interconnected world.")
```
```python
writing_text_evaluation_final.py
```


