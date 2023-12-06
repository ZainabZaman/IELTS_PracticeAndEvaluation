#-------------- IMPORTING DEPENDENCIES -------------
import openai
import stt
import ielts_bands
import os
import pickle 
import pte_evaluation
#-------------- API KEYS -------------
openai.api_key = 'YOUR_OPENAI_API_KEY'
voice_name = 'en-US-JennyMultilingualNeural'

combined_dict = {}

class evaluation:
    user_dict = {}
    id = ''

    def __init__(self, id):
        self.id = id
        self.results_combined = {}
        self.user_input = '' 
        self.relevancy_score = 0.0
        self.score = 0.0
        self.user_dict = {}

    def create_user(self):
        user_ids = self.user_dict.values()
        if self.id not in user_ids:
            self.user_dict[self.id] = self.context
            return print("User created sucessfuly!")
        else:
            return print("User ID already exits!")
    
    def save_evaluation(self, evaluation):
        path = f'./{self.id}_listening.pkl'
        with open(path, 'wb') as fp:
            pickle.dump(evaluation, fp)

        return print(path)

    def load_saved_dict(self):
        if os.path.exists(f'./{self.id}_listening.pkl'):
           with open(f'./{self.id}_listening.pkl', 'rb') as fp:
            dict = pickle.load(fp)
            # print('Student Dictionary')
            # print(std)
            self.user_dict = dict
            # print(dict)
            return dict
        else:
            # self.create_user()
            return print('User not found!')
    
    def is_user(self):
        if os.path.exists(f'./{self.id}_listening.pkl'):
            # print('existing user')
            return self.load_saved_dict()
        else:
            return 0
        
    def delete_previous_context(self):
        context = self.context
        return context
    
    def evaluation_scores(self, audio_bot_text, user_input):
        # audio_asked_text = stt.recognize_from_microphone(audio_asked)
        # audio_asked_text = audio_asked_text.lower()
        user_input = user_input.lower()
        if user_input in audio_bot_text:
            # print('#####')
            relevancy_score = 1
            score = 1
        else: 
            # print('xxxx')
            relevancy_score = 0
            score = 0

        # if user_input == audio_bot_text:
        #     relevancy_score = 1
        #     score = 1
        # elif user_input != audio_bot_text:
        #     relevancy_score = 0
        #     score = 0
        print('Relevancy Score: ', relevancy_score)

        self.results_combined.update({'EvaluationScore': score})
        combined_dict[audio_bot_text] = (self.results_combined)

        return combined_dict[audio_bot_text]

def listening(id, audio_bot, user_input):
    user = evaluation(id)
    is_user = user.is_user()
    audio_bot_text = stt.recognize_from_microphone(audio_bot)
    audio_bot_text = audio_bot_text.lower()
    
    if is_user == 0:
        print('*****New User*****')
        #-------------- RETURNING accuracy, completeness, fluency, per_word_evaluation, pitch_per_word, overall_pitch, relevancy_score  -------------
        combined_dict[audio_bot_text] = user.evaluation_scores(audio_bot_text, user_input)
        print(combined_dict)
        user.save_evaluation(combined_dict)
        return combined_dict
        
    else:
        print('*****Existing User*****')
        score_list = []
        overall_score = 0.0
        band = 0.0
        pte_score = 0.0
        
        evaluation_dict = user.load_saved_dict()
        check_dictionary_len = len(list(evaluation_dict.values()))
        # print(check_dictionary_len)
        if check_dictionary_len < 40:
            print(evaluation_dict)
            evaluation_dict[audio_bot_text] = user.evaluation_scores(audio_bot_text, user_input)
            print(evaluation_dict)

            evaluation_dict_values = list(evaluation_dict.values())
            print(evaluation_dict_values)
            for i in evaluation_dict_values:
                score_list.append(i['EvaluationScore'])
        if check_dictionary_len == 40 or len(evaluation_dict_values) == 40:
            for i in range(len(score_list)):
                overall_score = overall_score + score_list[i]
            print(f'\n*****OverallScore*****: {overall_score}')
            band = ielts_bands.calculate_ielts_band(overall_score)
            print(f'\n*****IELTS_Band*****: {band}')
            pte_score = pte_evaluation.pte__evaluation(band)
            print(f'*****PTE_Score*****: {pte_score}\n')

        print(f'\nevaluation score list: {score_list}')
        user.save_evaluation(evaluation_dict)

        return band, pte_score

listening(4, 'D:\\GPT\\GPT\\ielts_evaluation\\why-hello-there-103596.wav', "well hello there")

# input -> id, bot_audio, user_response_text [there can be punctuation variation but the bot audio and the final user response string passed should be the same]
# output -> ielts_band