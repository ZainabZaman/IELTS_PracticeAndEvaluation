import language_tool_python
import nltk

# example_text = "Cars, a ubiquitous aspects of contemporary live, symbolizes a harmonious blend of technology and conveniences. Beyond they're utilitarian role in transportations, car represents personal freedoms and choices. Ranging from compacts and efficiently models to luxurious and high-performance vehicle, they caters to diverse preference. Cars has not only transformed the ways we moves but also leaves an indelible marks on cultures and urban lifestyles. In essences, these four-wheeled innovations encapsulates modern mobility, influences the daily rhythms of our life."

def get_grammar_errors_and_grammar_scores(text):
    #-------------- LANGUAGE TOOL OBJECT -------------
    tool = language_tool_python.LanguageTool('en-US')

    #-------------- CHECKING FOR GRAMMAR ERRORS -------------
    matches = tool.check(text)

    #-------------- GET GRAMMAR ERRORS AND GRAMMAR SCORES -------------
    grammar_errors = len(matches)
    total_words = len(text.split())
    grammar_score = ((total_words - grammar_errors) / total_words)

    return grammar_errors, grammar_score

def lexical_diversity(text):
    words = nltk.word_tokenize(text)
    # diversity_score = (len(set(words)) / len(words)) * 100
    diversity_score = (len(set(words)) / len(words))
    return diversity_score

# #-------------- GRAMMAR ERRORS // GRAMMAR SCORE // LEXICAL DIVERSITY SCORE -------------
# grammar_errors, grammar_score = get_grammar_errors_and_grammar_scores(example_text)
# diversity_score = lexical_diversity(example_text)

# print(f"Grammar Errors: {grammar_errors}")
# print(f"Vocabulary Score: {grammar_score:.2f}%")
# print(f"NLTK Lexical Diversity Score: {diversity_score:.2f}%")

