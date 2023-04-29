import torch
from transformers import RobertaTokenizer, RobertaForSequenceClassification

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


# Load tokenizer and model RoBERTa
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaForSequenceClassification.from_pretrained('roberta-base')


# Function to get Sentiment
def get_sentiment(text):

    # Tokenize and convert to input features
    inputs = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=512,
        return_tensors='pt'
    )

    # Sentiment Analysis
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1)

    # Map the predicted class
    sentiments = ['Negative', 'Positive']
    predicted_sentiments = sentiments[predicted_class]

    return {text: predicted_sentiments}


text_1 = 'I am happy'
text_2 = 'I am sad'
print(get_sentiment(text_1))
print(get_sentiment(text_2))


"""
    Output:
        {'I am happy': 'Positive'}
        {'I am sad': 'Negative'}
"""