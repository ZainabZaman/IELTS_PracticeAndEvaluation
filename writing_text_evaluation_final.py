#-------------- IMPORTING DEPENDENCIES -------------
import openai
import relevancy
import ielts_bands
import os
import pickle 
import writing_text_evaluation
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
        path = f'./{self.id}_writing_text_eval.pkl'
        with open(path, 'wb') as fp:
            pickle.dump(evaluation, fp)

        return print(path)

    def load_saved_dict(self):
        if os.path.exists(f'./{self.id}_writing_text_eval.pkl'):
           with open(f'./{self.id}_writing_text_eval.pkl', 'rb') as fp:
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
        if os.path.exists(f'./{self.id}_writing_text_eval.pkl'):
            # print('existing user')
            return self.load_saved_dict()
        else:
            return 0
        
    def delete_previous_context(self):
        context = self.context
        return context
    
    def evaluation_scores(self, question, complete_essay):

        relevancy_score = relevancy.relevant(question, complete_essay)
        print('Relevancy Score: ', relevancy_score)

        if relevancy_score > 0.65:
            #-------------- GETTING EVALUATION SCORES -------------
            task_achievement, complete_response, clear_comprehensive_ideas, relevant_specific_examples, appropriate_word_count, coherence_and_cohesion, logical_structure,introduction_conclusion_present, supported_main_points, accurate_linking_words, variety_in_linking_words, lexical_resource, varied_vocabulary, accurate_spelling_word_formation, grammatical_range_and_accuracy, mix_of_complex_simple_sentences, clear_and_correct_grammar, overall_band_score, score = writing_text_evaluation.essay_assessment(question, complete_essay)
            
            #-------------- APPENDING PER ITERATION RESULTS INTO COMBINED RESULTS DICTIONARY -------------
            self.results_combined.update({'task_achievement': task_achievement})
            self.results_combined.update({'complete_response': complete_response})
            self.results_combined.update({'clear_comprehensive_ideas': clear_comprehensive_ideas})
            self.results_combined.update({'relevant_specific_examples': relevant_specific_examples})
            self.results_combined.update({'appropriate_word_count': appropriate_word_count})
            self.results_combined.update({'coherence_and_cohesion': coherence_and_cohesion})
            self.results_combined.update({'logical_structure': logical_structure})
            self.results_combined.update({'introduction_conclusion_present': introduction_conclusion_present})
            self.results_combined.update({'supported_main_points': supported_main_points})
            self.results_combined.update({'accurate_linking_words': accurate_linking_words})
            self.results_combined.update({'variety_in_linking_words': variety_in_linking_words})
            self.results_combined.update({'lexical_resource': lexical_resource})
            self.results_combined.update({'varied_vocabulary': varied_vocabulary})
            self.results_combined.update({'accurate_spelling_word_formation': accurate_spelling_word_formation})
            self.results_combined.update({'grammatical_range_and_accuracy': grammatical_range_and_accuracy})
            self.results_combined.update({'mix_of_complex_simple_sentences': mix_of_complex_simple_sentences})
            self.results_combined.update({'clear_and_correct_grammar': clear_and_correct_grammar})
            self.results_combined.update({'overall_band_score': overall_band_score})
            self.results_combined.update({'score': score})

            combined_dict[question] = (self.results_combined)

            return combined_dict[question]

def text_evaluation(id, question, complete_essay):
    # img_description = image_description.generate_image_description(image_path)
    question = question.lower()
    complete_essay = complete_essay.lower()
    print('*****QUESTION*****\n', question)
    print('*****USER RESPONSE*****\n', complete_essay)

    user = evaluation(id)
    is_user = user.is_user()
    
    if is_user == 0:
        print('\n*****New User*****')
        #-------------- RETURNING accuracy, completeness, fluency, per_word_evaluation, pitch_per_word, overall_pitch, relevancy_score -------------
        combined_dict[question] = user.evaluation_scores(question, complete_essay)
        # print(combined_dict)
        user.save_evaluation(combined_dict)
        return combined_dict
        
    else:
        print('*****Existing User*****')
        task_achievement = [] 
        complete_response = []
        clear_comprehensive_ideas = [] 
        relevant_specific_examples = [] 
        appropriate_word_count = [] 
        coherence_and_cohesion = [] 
        logical_structure = []
        introduction_conclusion_present = []
        supported_main_points = [] 
        accurate_linking_words = [] 
        variety_in_linking_words = [] 
        lexical_resource = [] 
        varied_vocabulary = [] 
        accurate_spelling_word_formation = [] 
        grammatical_range_and_accuracy = [] 
        mix_of_complex_simple_sentences = [] 
        clear_and_correct_grammar = [] 
        overall_band_score = [] 
        score = []
        overall_score = 0.0
        band = 0.0
        overall_score_20 = 0.0
        pte_score = 0.0
        
        evaluation_dict = user.load_saved_dict()
        check_dictionary_len = len(list(evaluation_dict.values()))
        print('*****loaded dict length*****: ',check_dictionary_len, '\n\n')
        if check_dictionary_len <= 10:
            # print('*****loaded dictionary*****\n',evaluation_dict, '\n\n')
            evaluation_dict[question] = user.evaluation_scores(question, complete_essay)
            # print('*****updated dictionary*****\n',evaluation_dict, '\n\n')

            evaluation_dict_values = list(evaluation_dict.values())
            # print('*****eval dict values*****\n',evaluation_dict_values, '\n')
            for i in evaluation_dict_values:

                task_achievement.append(i['task_achievement'])
                complete_response.append(i['complete_response'])
                clear_comprehensive_ideas.append(i['clear_comprehensive_ideas'])
                relevant_specific_examples.append(i['relevant_specific_examples'])
                appropriate_word_count.append(i['appropriate_word_count'])
                coherence_and_cohesion.append(i['coherence_and_cohesion'])
                logical_structure.append(i['logical_structure'])
                introduction_conclusion_present.append(i['introduction_conclusion_present'])
                # introduction_conclusion_present.append(i['introduction_conclusion_present'])
                supported_main_points.append(i['supported_main_points'])
                accurate_linking_words.append(i['accurate_linking_words'])
                variety_in_linking_words.append(i['variety_in_linking_words'])
                lexical_resource.append(i['lexical_resource'])
                varied_vocabulary.append(i['varied_vocabulary'])
                accurate_spelling_word_formation.append(i['accurate_spelling_word_formation'])
                grammatical_range_and_accuracy.append(i['grammatical_range_and_accuracy'])
                mix_of_complex_simple_sentences.append(i['mix_of_complex_simple_sentences'])
                clear_and_correct_grammar.append(i['clear_and_correct_grammar'])
                overall_band_score.append(i['overall_band_score'])
                score.append(i['score'])

            if check_dictionary_len == 10 or len(evaluation_dict_values) == 10:
                for i in range(len(score)):
                    overall_score = overall_score + score[i]
                    overall_score_20 = overall_score * 2
                print(f'*****Overall_Score*****: {overall_score}')
                print(f'*****Overall_Score_20*****: {overall_score_20}')
                band = ielts_bands.calculate_ielts_band(overall_score_20)
                print(f'*****IELTS_Band*****: {band}')
                pte_score = pte_evaluation.pte__evaluation(band)
                print(f'*****PTE_Score*****: {pte_score}\n')

            print(f'\ntask achievement score: {task_achievement} \ncompleteness score: {complete_response} \nclear and comprehensive ideas: {clear_comprehensive_ideas} \nrelevant and specific examples: {relevant_specific_examples} \nappropriate word count: {appropriate_word_count} \ncoherence and cohesion: {coherence_and_cohesion} \nlogical structure: {logical_structure} \nintroduction_conclusion_present: {introduction_conclusion_present} \nsupported_main_points: {supported_main_points} \naccurate_linking_words: {accurate_linking_words} \nvariety_in_linking_words: {variety_in_linking_words} \nlexical_resource: {lexical_resource} \nvaried_vocabulary: {varied_vocabulary} \naccurate_spelling_word_formation: {accurate_spelling_word_formation} \ngrammatical_range_and_accuracy: {grammatical_range_and_accuracy} \nmix_of_complex_simple_sentences: {mix_of_complex_simple_sentences} \nclear_and_correct_grammar: {clear_and_correct_grammar} \noverall_band_score: {overall_band_score} \nscore: {score}')
        
        elif check_dictionary_len > 10:
            print('Congratulations! You have completed both modules!')

        user.save_evaluation(evaluation_dict)
        return evaluation_dict, band, score, pte_score

text_evaluation(5, "Write a passage reflecting on the role of cars in your life, your favorite type of car, or any memorable experiences you've had with automobiles. What do cars mean to you, and how do they contribute to your daily life or sense of adventure? Take a moment to explore the fascinating world of cars through your own perspective.", "Cars, the modern marvels of transportation, have transformed the way we move, connect, and explore the world. From the early days of horseless carriages to the sleek, high-tech vehicles of today, the evolution of cars has been a testament to human innovation and engineering prowess. These four-wheeled machines have not only revolutionized our daily commute but have also become symbols of freedom, status, and style. In the 19th century, the invention of the automobile marked a pivotal moment in history. Karl Benz, often credited with creating the first true automobile, set in motion a chain of events that would reshape society. The simple, rattling contraptions of the past have given way to a diverse range of vehicles catering to every need and desire. Whether it's the efficient and eco-friendly electric cars, the powerful and adrenaline-pumping sports cars, or the sturdy and reliable SUVs, there is a car for every personality and lifestyle. The automotive industry has not only focused on improving the efficiency and performance of cars but has also embraced cutting-edge technologies. Advanced safety features, autonomous driving capabilities, and smart connectivity have become integral parts of modern cars. The intersection of artificial intelligence and automotive engineering has opened up new possibilities, promising a future where cars are not just means of transportation but intelligent companions on the road. Yet, the love for cars extends beyond their technical aspects. Car enthusiasts often find themselves immersed in the aesthetics, design, and history of automobiles. Classic cars, with their timeless charm, evoke a sense of nostalgia, while futuristic concept cars captivate our imagination and hint at the possibilities that lie ahead. As we continue to navigate the ever-changing landscape of transportation, cars remain at the forefront of innovation and societal progress. From reducing carbon emissions to redefining the concept of mobility, cars are poised to play a central role in shaping the future of our interconnected world.")

# input -> id, topic_for_writing_a_paragraph_on, TEXT_paragraph_by_user_on_the_given_topic
# output -> evaluation_dictionary, ielts_band, score_list