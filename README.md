# AI-Tutor
An Application that uses AI to teach ML Topics and much more.

AI Tutor is a web-based chatbot that utilizes OpenAI's GPT-3 language model to provide automated tutoring to students on various topics related to machine learning. The chatbot can generate questions related to different subtopics and summarize the ideas related to that subtopic. The chatbot can also track student engagement and move on to the next subtopic once the student has demonstrated sufficient understanding.

### Requirements
- Python 3.6 or higher
- Flask
- OpenAI API key

### Installation
- Clone the repository: git clone https://github.com/absterjr/AI-Tutor.git
- Install the required packages: pip install -r requirements.txt
- Set up the OpenAI API key: https://platform.openai.com/account/api-keys
- Run the app: flask --app app run
(After Clicking on "Start Conversation" on the webpage, move on back to the terminal to continue the conversation, as you can see from the image below.)
![alt text](https://github.com/absterjr/AI-Tutor/blob/main/AI%20Tutor.png?raw=true)
Type Yes to continue on to the next topic.
#### Or you can use this command or your command line:
  - ##### (Linux, make sure you have python and git installed):
```bash
   git clone https://github.com/absterjr/AI-Tutor.git && pip install -r requirements.txt && python3 env.py && flask --app app run
```
  - ##### (Windows, make sure you have python and git installed):
```powershell
  git clone https://github.com/absterjr/AI-Tutor.git && pip install -r requirements.txt && python env.py && flask --app app run
```

### Usage
Once the app is running, navigate to http://127.0.0.1:5000 in your web browser to access the chatbot. You can start a conversation by typing your response in the input box at the bottom of the page and pressing Enter. The chatbot will respond with a question related to a particular subtopic and a summary of the ideas related to that subtopic. Once the chatbot determines that you have demonstrated sufficient understanding of the current subtopic, it will move on to the next subtopic. 
You can see an example below.
![alt text](https://github.com/absterjr/AI-Tutor/blob/main/Doubt.png?raw=true)


### Contributing
Contributions to AI Tutor are welcome! If you find a bug or have an idea for a new feature, please open an issue or submit a pull request. 


#### Note: replace "YOUR_API_KEY" with your actual OpenAI API key. Also, make sure to install the necessary packages (flask and openai)
The number of topics can be increased by simply adding the topic names into the list defined at the beginning.
