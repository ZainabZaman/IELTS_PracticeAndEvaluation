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
IELTS listening evaluation can be executed by passing user_ID, topic_based_text_from_the_bot, user_audio_response in the speaking function in the speaking_final.py. The speaking evaluation is a conversational assessment where the bot evaluates responses from the user through a conversation on a partiular topic. 
```python
speaking(2, "How often do you like to travel?", '.\i_like_to_travel_once_or_twice_a_year.wav')
```
```python
py speaking_final.py
```
