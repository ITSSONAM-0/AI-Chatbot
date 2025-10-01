import tkinter as tk
from tkinter import scrolledtext
import random
import datetime
import requests
import wikipedia

# --- Chatbot Functions ---
def get_time():
    return f"⏰ Current time is {datetime.datetime.now().strftime('%H:%M:%S')}"

def get_date():
    return f"📅 Today's date is {datetime.date.today()}"

def tell_joke():
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the computer go to the doctor? Because it caught a virus!",
        "Why do Java developers wear glasses? Because they can’t C#!"
    ]
    return random.choice(jokes)

def get_weather(city):
    API_KEY = "b1c6ce7cc28827950fc02983f2f6b9a1"   # Replace with your OpenWeather API Key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        condition = data['weather'][0]['description']
        return f"🌍 Weather in {city}: {temp}°C, {condition}"
    else:
        return "❌ Sorry, I couldn't fetch weather."

def search_wiki(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return f"📖 Wikipedia: {result}"
    except:
        return "❌ Sorry, I couldn't find anything on Wikipedia."

# --- Chatbot Response Logic ---
def chatbot_response(user):
    user = user.lower()

    if "hi" in user or "hello" in user:
        return random.choice(["Hello!", "Hi there!", "Hey!"])
    elif "how are you" in user:
        return "I'm good! How about you?"
    elif "time" in user:
        return get_time()
    elif "date" in user:
        return get_date()
    elif "joke" in user:
        return tell_joke()
    elif "weather" in user:
        city = user.replace("weather", "").strip()
        if city == "":
            return "Please tell me which city 🌆"
        return get_weather(city)
    elif "search" in user:
        query = user.replace("search", "").strip()
        if query == "":
            return "Please tell me what to search 🔍"
        return search_wiki(query)
    elif "bye" in user or "exit" in user:
        return "Goodbye 👋"
    else:
        return "Sorry, I don't understand that."

# --- GUI Setup ---
def send_message():
    user_input = entry.get()
    if user_input.strip() != "":
        chat_area.insert(tk.END, "You: " + user_input + "\n")
        response = chatbot_response(user_input)
        chat_area.insert(tk.END, "Bot: " + response + "\n\n")
        entry.delete(0, tk.END)

# Window
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("500x600")
root.config(bg="#222")

# Chat Display
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=25, bg="#111", fg="white", font=("Arial", 12))
chat_area.pack(pady=10)
chat_area.insert(tk.END, "🤖 Chatbot is ready! Type your message...\n\n")

# Input Field
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

# Send Button
send_button = tk.Button(root, text="Send", command=send_message, bg="#4CAF50", fg="white", font=("Arial", 12))
send_button.pack()

root.mainloop()
