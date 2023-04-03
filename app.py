from flask import Flask, request, jsonify
import openai
import nltk

# Initialize the Flask application
app = Flask(__name__)

# Define the topics and subtopics as a list or a tree data structure
topics = ["Intro to ML training", "Steps in Training", "Data Collection", "Preprocessing", "Training", "Evaluation"]

# Define the OpenAI API key and model
openai.api_key = "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"
model_engine = "text-davinci-002"

# Define the natural language processing (NLP) tools
nltk.download('punkt')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')


# Define the main conversation function
def run_conversation():
    # Initialize the subtopic index and engagement flag
    subtopic_index = 0
    engaged = False
    
    while subtopic_index < len(topics):
        # Retrieve the current subtopic from the list
        subtopic = topics[subtopic_index]
        
        # Use the OpenAI GPT API to generate a question related to the current subtopic
        question = openai.Completion.create(
            engine=model_engine,
            prompt=subtopic,
            temperature=0.5,
            max_tokens=100,
            n=1,
            stop=None,
            timeout=15
        ).choices[0].text
        
        # Use the OpenAI GPT API to summarize the ideas related to the current subtopic
        summary = openai.Completion.create(
            engine=model_engine,
            prompt=subtopic + "\n\nPlease summarize the ideas related to this topic.",
            temperature=0.5,
            max_tokens=100,
            n=1,
            stop=None,
            timeout=15
        ).choices[0].text
        
        # Display the question and summary to the student
        message = "AI Tutor: " + question + "\n\n" + summary + "\n\n"
        
        # Check if the student has engaged sufficiently in the conversation so far in relation to the current topic/subtopic
        if engaged:
            subtopic_index += 1
            engaged = False
            message += "AI Tutor: Great job! Let's move on to the next subtopic: " + topics[subtopic_index] + "\n\n"
        else:
            message += "AI Tutor: Do you understand the topic? Please type your answer below."
        
        # Wait for the student's response
        response = input(message)
        
        # Use NLP tools to extract features from the student's response
        response_features = tokenizer.tokenize(response)
        
        # Use OpenAI GPT API to classify the response as engaged or not
        classification = openai.Completion.create(
            engine=model_engine,
            prompt=response,
            temperature=0.5,
            max_tokens=100,
            n=1,
            stop=None,
            timeout=15
        ).choices[0].text
        
        if "engaged" in classification.lower():
            engaged = True
        
    return "Thanks for learning with us!"


# Define the Flask API endpoint
@app.route('/', methods=['GET', 'POST'])
def conversation_endpoint():
    if request.method == 'POST':
        # Call the conversation function
        return run_conversation()
    else:
        # Display the HTML form for the student to begin the conversation
        return '''
            <form method="post">
                <input type="submit" value="Start Conversation">
            </form>
        '''
