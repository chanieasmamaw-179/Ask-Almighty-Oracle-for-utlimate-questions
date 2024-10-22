from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # Ensure both GET and POST are allowed
def index():
    answer = ""
    if request.method == 'POST':
        question = request.form['question']  # Get the user's question from the form

        # API request to GPT-4 via RapidAPI
        url = "https://gpt-4o.p.rapidapi.com/chat/completions"
        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        }
        headers = {
            "x-rapidapi-key": "9cab17a8a5msh7de5ccd2b34dc43p18bea4jsna1a001d1a4a1",
            "x-rapidapi-host": "gpt-4o.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            data = response.json()

            # Extract the AI's response from the API data
            answer = data['choices'][0]['message']['content']
        except Exception as e:
            answer = "Sorry, the Oracle is having trouble answering right now."
            print(f"Error: {e}")

    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
