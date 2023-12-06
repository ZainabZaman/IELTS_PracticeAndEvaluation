import parselmouth
import numpy as np
import tts

# per_word_pitch = []
# input_sentence = 'nothing much what about you'
# input_words = input_sentence.split(' ')
# print(type(input_sentence))
# output = 'D:\\GPT\\GPT\\reading_evalaution\\nothing_much_what_about_you.wav'
# tts.text_to_speech_wav(tts.voice_name, input_sentence, output)

def pitch(input_words, output):
    per_word_pitch = []
# Load the recorded audio using parselmouth
    sound = parselmouth.Sound(output)

    # Calculate pitch
    pitch = sound.to_pitch()
    # print(pitch)

    # Extract pitch values
    pitch_values = pitch.selected_array['frequency']
    pitch = [x for x in pitch_values if x != 0]
    for i in range(len(input_words)):
        # print(f"{input_words[i]} = Pitch: {pitch[i]:.2f}")
        per_word_pitch.append(f'{input_words[i]}: {pitch[i]} Hz')
    # print(per_word_pitch)
    # Calculate the overall average pitch
    overall_average_pitch = np.mean(pitch)

    # Define a range or threshold for pitch values (adjust as needed)
    min_pitch_threshold = 60   # minimum pitch threshold
    max_pitch_threshold = 300   # maximum pitch threshold

    # Map overall average pitch to a percentage within the defined range
    percentage_pitch = (
        (overall_average_pitch - min_pitch_threshold) /
        (max_pitch_threshold - min_pitch_threshold)
    )*100

    # Print the overall average pitch value
    # print(f"Overall Pitch: {overall_average_pitch:.2f} Hz")

    return per_word_pitch, overall_average_pitch, percentage_pitch

# per_word_pitch, overall_average_pitch, percentage_pitch = pitch(input_words, output)

# print(f"Overall Average Pitch: {per_word_pitch}")
# print(f"Overall Average Pitch: {overall_average_pitch:.2f} Hz")
# print(f"Overall Average Pitch as Percentage: {percentage_pitch:.2f}%")