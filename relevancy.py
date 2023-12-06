import transformers
import numpy as np
import torch

# Load the BERT model and tokenizer
model = transformers.BertModel.from_pretrained('bert-base-uncased')
tokenizer = transformers.BertTokenizer.from_pretrained('bert-base-uncased')

# text1 = "what is your favorite food."
# text2 = "i like to eat pasta"

def relevant(text1, text2):

    # Tokenize and encode the texts

    tokens1 = tokenizer(text1, return_tensors='pt', padding=True, truncation=True)
    tokens2 = tokenizer(text2, return_tensors='pt', padding=True, truncation=True)

    # Get the BERT embeddings
    with torch.no_grad():  # Use torch.no_grad() to disable gradient tracking
        embeddings1 = model(**tokens1)
        embeddings2 = model(**tokens2)

    # Flatten and convert the embeddings to numpy arrays
    embedding1_array = embeddings1.last_hidden_state.mean(dim=1).numpy()
    embedding2_array = embeddings2.last_hidden_state.mean(dim=1).numpy()

    # Calculate the cosine similarity between the embeddings
    similarity = np.dot(embedding1_array, embedding2_array.T) / (np.linalg.norm(embedding1_array) * np.linalg.norm(embedding2_array)
    )

    # Access the actual similarity value and convert it to a string
    similarity_value = similarity[0][0]
    # similarity_str = str(similarity_value)  # Convert similarity to a string

    print(similarity_value)
    return similarity_value

# relevant(text1, text2)

