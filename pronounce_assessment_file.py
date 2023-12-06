import azure.cognitiveservices.speech as speechsdk
import threading 
import wave 
import time
import string
import json
import intonation as intonate

# weatherfilename = 'output.wav'
speech_key = "YOUR_AZURE_SPEECH_STUDIO_API_KEY"
service_region = "eastus"
# filename='D:\\GPT\\GPT\\reading_evalaution\\zz.wav'
# # filename = r'F:\chatbot_keyboard\user_audio.wav'
# language = 'en-US'
# reference_text = 'The image shows a bar graph displaying the number of coffee and manufacturing sales in the United States from 2016 to 2018. The graph shows that there was a steady increase in sales from 2016 to 2018, with the highest sales occurring in August 2018. The graph also shows that there was a slight decrease in sales in December 2017 and January 2018.'

def pronunciation_assessment_configured_with_json(filename, language, reference_text):

    average_intonation = 0
    """Performs pronunciation assessment asynchronously with input from an audio file.
        See more information at https://aka.ms/csspeech/pa"""

    # Creates an instance of a speech config with specified subscription key and service region.
    # Replace with your own subscription key and service region (e.g., "westus").
    # Note: The sample is for en-US language.
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    audio_config = speechsdk.audio.AudioConfig(filename=filename)

    reference_text = reference_text
    # Create pronunciation assessment config with json string (JSON format is not recommended)
    enable_miscue, enable_prosody = True, True
    config_json = {
        "GradingSystem": "HundredMark",
        "Granularity": "Phoneme",
        "Dimension": "Comprehensive",
        "ScenarioId": "",  # "" is the default scenario or ask product team for a customized one
        "EnableMiscue": enable_miscue,
        "EnableProsodyAssessment": enable_prosody,
        "NBestPhonemeCount": 0,  # > 0 to enable "spoken phoneme" mode, 0 to disable
    }
    pronunciation_config = speechsdk.PronunciationAssessmentConfig(json_string=json.dumps(config_json))
    pronunciation_config.reference_text = reference_text

    # Create a speech recognizer using a file as audio input.
    language = 'en-US'
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, language=language, audio_config=audio_config)
    # Apply pronunciation assessment config to speech recognizer
    pronunciation_config.apply_to(speech_recognizer)

    result = speech_recognizer.recognize_once_async().get()

    # Check the result
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print('pronunciation assessment for: {}'.format(result.text))
        pronunciation_result = json.loads(result.properties.get(speechsdk.PropertyId.SpeechServiceResponse_JsonResult))
        # print('assessment results:\n{}'.format(json.dumps(pronunciation_result, indent=4)))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
    per_word_pronounciation_assessment_result = []
    final_pronounciation_assessment_result = []
    pronunciation_result_parsed_01 = pronunciation_result['NBest'][0]
    pronounciation_assessment_result = pronunciation_result_parsed_01['PronunciationAssessment']

    # print(pronounciation_assessment_result)
    final_pronounciation_assessment_result.append(pronounciation_assessment_result)
    length = len(pronunciation_result_parsed_01['Words'])
    for i in range(len(pronunciation_result_parsed_01['Words'])):

        # del pronunciation_result_parsed_01['Words'][i]['Syllables']
        del pronunciation_result_parsed_01['Words'][i]['Phonemes']

        # print(pronunciation_result_parsed_01['Words'][i])
        intonation_results = pronunciation_result_parsed_01['Words'][i]['PronunciationAssessment']['Feedback']['Prosody']['Intonation']
        # print(intonation_results)
        intonation = pronunciation_result_parsed_01['Words'][i]['PronunciationAssessment']['Feedback']['Prosody']['Intonation']['Monotone']['SyllablePitchDeltaConfidence']
        average_intonation = (average_intonation + intonation) 
        # print(intonation)
        per_word_pronounciation_assessment_result.append(pronunciation_result_parsed_01['Words'][i])
        per_word_pronounciation_assessment_result.append(intonation_results)
        # per_word_pronounciation_assessment_result.append(pitch_per_word[i])

        del pronunciation_result_parsed_01['Words'][i]['PronunciationAssessment']['Feedback']
    final_pronounciation_assessment_result.append(per_word_pronounciation_assessment_result)

    # print(per_word_pronounciation_assessment_result)
    # print(f'\n\n')

    average_intonation = average_intonation / length
    accuracy = pronounciation_assessment_result['AccuracyScore']/100
    fluency = pronounciation_assessment_result['FluencyScore']/100
    prosody_score = pronounciation_assessment_result['ProsodyScore']/100
    completeness = pronounciation_assessment_result['CompletenessScore']/100
    avg_pro_score = pronounciation_assessment_result['PronScore']/100

    # print(f'Accuracy: {accuracy} \nFluency: {fluency} \nProsody Score: {prosody_score} \nCompleteness: {completeness} \nAverage Pronounciation Score: {avg_pro_score} \nIntonation: {average_intonation} \n\n')
    # final_pronounciation_assessment_result.append(pitch_per_word)
    # final_pronounciation_assessment_result.append(('overall_pitch: ' + str(overall_pitch)))

    # print(final_pronounciation_assessment_result)

    return accuracy, fluency, prosody_score, completeness, avg_pro_score, average_intonation, final_pronounciation_assessment_result

# accuracy, fluency, prosody_score, completeness, avg_pro_score, average_intonation, pitch_per_word, overall_pitch, final_pronounciation_assessment_result = pronunciation_assessment_configured_with_json(filename, language, reference_text)

# pronunciation_assessment_configured_with_json(filename, language, reference_text)
