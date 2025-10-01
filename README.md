# 🤖 AI Chatbot (Python)

An intelligent Python-based AI Chatbot capable of handling conversations, telling jokes, giving time & date, fetching **real-time weather**, and performing **Wikipedia searches**.  

---

## ✨ Features  
- 🗨️ **Small Talk** – Handles greetings & basic chat  
- ⏰ **Time & Date** – Tells current time and date  
- 😂 **Jokes** – Random jokes generator  
- 🌦 **Weather** – Real-time weather updates using OpenWeather API  
- 📖 **Wikipedia Search** – Fetches short summaries of any topic  
- 🖥 **GUI Version** – Interactive Tkinter window with scrollable chat history  
- 🚪 **Exit Option** – Type `exit` to quit  

---

## 🛠️ Technologies Used  
- **Python 3**  
- **Requests** (for APIs)  
- **Wikipedia** (Python library)  
- **Tkinter** (GUI)  
- **OpenWeather API** (for real-time weather data)  

---

## 📂 Installation  

1. Clone the repository or download the files:  
   ```bash
   git clone https://github.com/your-username/ai-chatbot.git
   cd ai-chatbot
   
2.Install required libraries:-
 pip install requests wikipedia
 
3. Get a free API key from OpenWeather and replace it in both files:-
API_KEY = "your_api_key_here"

4.Run the chatbot:-
python gui_chatbot.py


💻 Usage
CLI Example:-
You: hi
Bot: Hello!

You: time
Bot: ⏰ Current time is 15:42:10

You: weather Delhi
Bot: 🌍 Weather in Delhi: 30°C, clear sky

You: search Python
Bot: 📖 Wikipedia: Python is a high-level programming language...

You: tell me a joke
Bot: Why don’t scientists trust atoms? Because they make up everything!

GUI Version:

Type your message in input box

Click Send

Scrollable chat area shows conversation

📌 Future Improvements

Voice input & output

Machine learning for smarter responses

Web-based version using Flask

High-score / analytics for interactions

Type exit or bye to quit.
