def calculate_ielts_band(overall_score):
    overall_score = overall_score

    if 40 >= overall_score >= 39:
        ielts_band =  9
    elif 38 >= overall_score >= 37:
        ielts_band = 8.5
    elif 36 >= overall_score >= 35:
        ielts_band = 8.0
    elif 34 >= overall_score >= 32:
        ielts_band = 7.5
    elif 31 >= overall_score >= 30:
        ielts_band = 7.0
    elif 29 >= overall_score >= 26:
        ielts_band = 6.5
    elif 25 >= overall_score >= 23:
        ielts_band = 6.0
    elif 22 >= overall_score >= 18:
        ielts_band = 5.5
    elif 17 >= overall_score >= 16:
        ielts_band = 5.0
    elif 15 >= overall_score >= 13:
        ielts_band = 4.5
    elif 12 >= overall_score >= 11:
        ielts_band = 4.0
    elif 10 >= overall_score >= 9:
        ielts_band = 3.5
    elif 8 >= overall_score >= 7:
        ielts_band = 3.0
    elif 6 >= overall_score >= 5:
        ielts_band = 2.5
    elif 4 >= overall_score >= 3:
        ielts_band = 2.0
    elif 2 >= overall_score >= 1:
        ielts_band = 1.5
    elif 1 >= overall_score > 0:
        ielts_band = 1.0
    else:
        ielts_band = 0.0

    return ielts_band
