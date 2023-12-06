#-------------- IMPORTING DEPENDENCIES -------------
import openai
import pronounce_assessment_file
import intonation
import relevancy
import stt
import grammar_vocabulary_evaluation
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
        self.accuracy = ''
        self.completeness = ''
        self.fluency = ''
        self.pitch_per_word = ''
        self.overall_pitch = ''
        self.user_response = '' 
        self.relevancy_score = 0.0
        self.band = 0.0
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
        path = f'./{self.id}_speaking.pkl'
        with open(path, 'wb') as fp:
            pickle.dump(evaluation, fp)

        return print(path)

    def load_saved_dict(self):
        if os.path.exists(f'./{self.id}_speaking.pkl'):
           with open(f'./{self.id}_speaking.pkl', 'rb') as fp:
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
        if os.path.exists(f'./{self.id}_speaking.pkl'):
            # print('existing user')
            return self.load_saved_dict()
        else:
            return 0
        
    def delete_previous_context(self):
        context = self.context
        return context
    
    def evaluation_scores(self, lesson_entry, filename):
        user_response_audio = filename
        user_response = stt.recognize_from_microphone(user_response_audio)
        user_response = user_response.lower()
        lesson_entry = lesson_entry.lower()
        # if user_response == lesson_entry:
        #     relevancy_score = 1
        # elif user_response != lesson_entry:
        #     relevancy_score = 0
        relevancy_score = relevancy.relevant(lesson_entry, user_response)
        print('Relevancy Score: ', relevancy_score)
        # if relevancy_score != 1:
        #     print('Provide an accurate response!')
        #     exit()

        if relevancy_score > 0.65:
            user_response_words = user_response.split(' ')

            #-------------- GETTING EVALUATION SCORES -------------
            pitch_per_word, overall_pitch, percentage_pitch = intonation.pitch(user_response_words, user_response_audio)
            accuracy, fluency, prosody_score, completeness, avg_pro_score, average_intonation,final_pronounciation_assessment_result = pronounce_assessment_file.pronunciation_assessment_configured_with_json(user_response_audio, 'en-US', user_response)
            grammar_errors, grammar_score = grammar_vocabulary_evaluation.get_grammar_errors_and_grammar_scores(user_response)
            lexical_diversity_score = grammar_vocabulary_evaluation.lexical_diversity(user_response)
            overall_pitch = overall_pitch/300

            score = (accuracy + fluency + prosody_score + completeness + avg_pro_score + average_intonation + overall_pitch + percentage_pitch + grammar_score + lexical_diversity_score) / 10
            if score >= 0.5:
                score = 1
            elif score < 0.5:
                score = 0
            
            #-------------- APPENDING PER ITERATION RESULTS INTO COMBINED RESULTS DICTIONARY -------------
            self.results_combined.update({'Accuracy': round(accuracy,2)})
            self.results_combined.update({'Fluency': round(fluency,2)})
            self.results_combined.update({'ProsodyScore': round(prosody_score,2)})
            self.results_combined.update({'Completeness': round(completeness,2)})
            self.results_combined.update({'AveragePronounciationScore': round(avg_pro_score,2)})
            self.results_combined.update({'Intonation': round(average_intonation,2)})
            self.results_combined.update({'PerWordPitch': pitch_per_word})
            self.results_combined.update({'OverallPitch': round(overall_pitch,2)})
            self.results_combined.update({'PercentagePitch': round(percentage_pitch,2)})
            self.results_combined.update({'GrammarErrors': grammar_errors})
            self.results_combined.update({'GrammarCorrectnessScore': round(grammar_score,2)})
            self.results_combined.update({'LexicalDiversityScore': round(lexical_diversity_score,2)})
            self.results_combined.update({'EvaluationScore': round(score,2)})

            combined_dict[lesson_entry] = (self.results_combined)

            return combined_dict[lesson_entry]

def speaking(id, lesson_entry, filename):
    user = evaluation(id)
    is_user = user.is_user()
    
    if is_user == 0:
        print('*****New User*****')

        #-------------- GETTING ENTRIES FROM LESSON ARRAY -------------
        print('Tutor: ', lesson_entry)

        #-------------- RETURNING accuracy, completeness, fluency, per_word_evaluation, pitch_per_word, overall_pitch, relevancy_score  -------------
        combined_dict[lesson_entry] = user.evaluation_scores(lesson_entry, filename)
        # print(combined_dict)
        user.save_evaluation(combined_dict)
        return combined_dict
        
    else:
        print('*****Existing User*****')
        print('Tutor: ', lesson_entry)
        accuracy = []
        fluency = []
        prosody_score = []
        completeness = []
        avg_pro_score = []
        intonation = []
        overall_pitch = []
        percentage_pitch = []
        grammar_errors = []
        grammar_correctness_score = []
        lexical_diversity_score = []
        score_list = []
        overall_score = 0.0
        band = 0.0
        pte_score = 0.0
        
        evaluation_dict = user.load_saved_dict()
        check_dictionary_len = len(list(evaluation_dict.values()))
        # print(check_dictionary_len)
        if check_dictionary_len < 40:
        # print(evaluation_dict)
            evaluation_dict[lesson_entry] = user.evaluation_scores(lesson_entry, filename)
            # print(evaluation_dict)

            evaluation_dict_values = list(evaluation_dict.values())
            print(evaluation_dict_values)
            for i in evaluation_dict_values:
                accuracy.append(i['Accuracy'])
                fluency.append(i['Fluency'])
                prosody_score.append(i['ProsodyScore'])
                completeness.append(i['Completeness'])
                avg_pro_score.append(i['AveragePronounciationScore'])
                intonation.append(i['Intonation'])
                overall_pitch.append(i['OverallPitch'])
                percentage_pitch.append(i['PercentagePitch'])
                grammar_errors.append(i['GrammarErrors'])
                grammar_correctness_score.append(i['GrammarCorrectnessScore'])
                lexical_diversity_score.append(i['LexicalDiversityScore'])
                score_list.append(i['EvaluationScore'])
        if check_dictionary_len == 40 or len(evaluation_dict_values) == 40:
            for i in range(len(score_list)):
                overall_score = overall_score + score_list[i]
            print(f'\n*****Overall_Score*****: {overall_score}')
            band = ielts_bands.calculate_ielts_band(overall_score)
            print(f'\n*****IELTS_Band*****: {band}')
            pte_score = pte_evaluation.pte__evaluation(band)
            print(f'*****PTE_Score*****: {pte_score}\n')
                
        print(f'\naccuracy: {accuracy} \nfluency: {fluency} \nprosody score: {prosody_score} \ncompleteness: {completeness} \navg pro score: {avg_pro_score} \nintonation: {intonation} \noverall pitch: {overall_pitch} \npercentage pitch: {percentage_pitch} \ngrammar errors: {grammar_errors} \ngrammar correctness score: {grammar_correctness_score} \nlexical diversity score: {lexical_diversity_score} \nevaluation score list: {score_list}')
        user.save_evaluation(evaluation_dict)

        return band, pte_score

speaking(2, "hey! how can i assist you today", 'D:\\GPT\\GPT\\ielts_evaluation\\why-hello-there-103596.wav')

# input -> id, lesson_entry_from_bot, user_audio_input
# output -> ielts_band