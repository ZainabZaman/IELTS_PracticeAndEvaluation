#-------------- IMPORTING DEPENDENCIES -------------
import openai
import relevancy
import grammar_vocabulary_evaluation
import ielts_bands
import os
import pickle 
import image_description
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
        path = f'./{self.id}_writing_image_eval.pkl'
        with open(path, 'wb') as fp:
            pickle.dump(evaluation, fp)

        return print(path)

    def load_saved_dict(self):
        if os.path.exists(f'./{self.id}_writing_image_eval.pkl'):
           with open(f'./{self.id}_writing_image_eval.pkl', 'rb') as fp:
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
        if os.path.exists(f'./{self.id}_writing_image_eval.pkl'):
            # print('existing user')
            return self.load_saved_dict()
        else:
            return 0
        
    def delete_previous_context(self):
        context = self.context
        return context
    
    def evaluation_scores(self, img_description, user_response):

        relevancy_score = relevancy.relevant(img_description, user_response)
        print('Relevancy Score: ', relevancy_score)

        if relevancy_score > 0.65:
            #-------------- GETTING EVALUATION SCORES -------------
            grammar_errors, grammar_score = grammar_vocabulary_evaluation.get_grammar_errors_and_grammar_scores(user_response)
            lexical_diversity_score = grammar_vocabulary_evaluation.lexical_diversity(user_response)

            score = (relevancy_score + grammar_score + lexical_diversity_score) / 3
            if score >= 0.5:
                score = 1
            elif score < 0.5:
                score = 0
            
            #-------------- APPENDING PER ITERATION RESULTS INTO COMBINED RESULTS DICTIONARY -------------
            self.results_combined.update({'GrammarErrors': grammar_errors})
            self.results_combined.update({'ContentRelevancyScore': round(relevancy_score,2)})
            self.results_combined.update({'GrammarCorrectnessScore': round(grammar_score,2)})
            self.results_combined.update({'LexicalDiversityScore': round(lexical_diversity_score,2)})
            self.results_combined.update({'EvaluationScore': round(score,2)})

            combined_dict[img_description] = (self.results_combined)

            return combined_dict[img_description]

def writing_image_evaluation(id, image_path, user_response):
    img_description = image_description.generate_image_description(image_path)
    user_response = user_response.lower()
    img_description = img_description.lower()
    print('*****IMAGE DESCRPTION*****\n', img_description)
    print('*****USER RESPONSE*****\n', user_response)

    user = evaluation(id)
    is_user = user.is_user()
    
    if is_user == 0:
        print('\n*****New User*****')
        #-------------- RETURNING accuracy, completeness, fluency, per_word_evaluation, pitch_per_word, overall_pitch, relevancy_score -------------
        combined_dict[img_description] = user.evaluation_scores(img_description, user_response)
        # print(combined_dict)
        user.save_evaluation(combined_dict)
        return combined_dict
        
    else:
        print('*****Existing User*****')
        grammar_errors = []
        grammar_correctness_score = []
        lexical_diversity_score = []
        relevancy_score = []
        score_list = []
        overall_score = 0.0
        band = 0.0
        overall_score_20 = 0.0
        pte_score = 0.0
        
        evaluation_dict = user.load_saved_dict()
        check_dictionary_len = len(list(evaluation_dict.values()))
        print('*****loaded dict length*****: ',check_dictionary_len, '\n\n')
        if check_dictionary_len <= 10:
            # print('*****loaded dictionary*****\n',evaluation_dict, '\n\n')
            evaluation_dict[img_description] = user.evaluation_scores(img_description, user_response)
            # print('*****updated dictionary*****\n',evaluation_dict, '\n\n')

            evaluation_dict_values = list(evaluation_dict.values())
            # print('*****eval dict values*****\n',evaluation_dict_values, '\n')
            for i in evaluation_dict_values:
                relevancy_score.append(i['ContentRelevancyScore'])
                grammar_errors.append(i['GrammarErrors'])
                grammar_correctness_score.append(i['GrammarCorrectnessScore'])
                lexical_diversity_score.append(i['LexicalDiversityScore'])
                score_list.append(i['EvaluationScore'])

            if check_dictionary_len == 10 or len(evaluation_dict_values) == 10:
                for i in range(len(score_list)):
                    overall_score = overall_score + score_list[i]
                    overall_score_20 = overall_score * 2
                print(f'*****Overall_Score*****: {overall_score}')
                print(f'*****Overall_Score_20*****: {overall_score_20}')
                band = ielts_bands.calculate_ielts_band(overall_score_20)
                print(f'*****IELTS_Band*****: {band}')
                pte_score = pte_evaluation.pte__evaluation(band)
                print(f'*****PTE_Score*****: {pte_score}\n')
                
            
            print(f'\ncontent relevancy score: {relevancy_score} \ngrammar errors: {grammar_errors} \ngrammar correctness score: {grammar_correctness_score} \nlexical diversity score: {lexical_diversity_score} \nevaluation score list: {score_list}')

        elif check_dictionary_len > 10:
            print('Image evaluation module complete, Attempt the text evaluation module')
            # print(f'\nexisating Scores: {evaluation_dict}')

        user.save_evaluation(evaluation_dict)

        return evaluation_dict, band, score_list, pte_score

writing_image_evaluation(6, "D:\\GPT\\GPT\\ielts_evaluation\\img01.jpg", "This is an artistic picture showing a blue car floating in the sky among the clouds. The sky looks nice with light and fluffy clouds. The image has a dreamy feel because cars do not fly in real life. There are words on the bottom that say “FAST CAR PIANO MAGE. DREAM. MIDNIGHTS.” It looks like an edit or a fantasy picture because the car is in the air like a big airplane. The colors are soft and give a calm feeling.")

# input -> id, image_path_for_image_to_be_explained, TEXT_image_description_by_user
# output -> evaluation_dictionary, ielts_band, score_list