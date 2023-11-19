# HealthMate Chat 🏥

Welcome to HealthMate Chat, a personalized health advice application powered by OpenAI's GPT-3.5 Turbo! This application allows users to interact with a virtual health advisor, providing health advice based on user input and personalized health data.

## Getting Started

### Prerequisites
Before running the application, make sure you have Python installed. You can install the required packages using:

```bash
pip install -r requirements.txt
```

### OpenAI API Key
You need to obtain an OpenAI API key to use the language model. Create a copy of `.env.example` and rename it to `.env`. Replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key.

## Running the Application
To run the HealthMate Chat application, execute the following command:

```bash
python chat_app.py
```

## Usage

### Health Data Entry
In the sidebar, you can enter your health data manually or choose to read it from an Arduino device.

#### Enter Manually
If you choose "Enter Manually," you can input various health metrics, such as heart rate and temperature.

#### Read from Arduino
If you have an Arduino device, you can integrate it to read health data. (Integration details to be added)

### Add Field
You can add new health data fields by providing a name and value. Fields must not already exist to be added.

### Remove Field
To remove an existing health data field, select the field name from the dropdown and click "Remove."

### Chat
Interact with the HealthMate Chat by entering your messages in the input box. The application will generate responses based on your input and provide personalized health advice.

### Clear Chat
Clear the chat history by clicking the "Clear Chat" button. This action will reset the conversation to the initial system message.

## Screenshots
**Screenshot 1: Initial Chat Interface**
    ![image](https://github.com/0aaryan/healthMate/assets/73797587/72958a67-68d5-40f3-81e4-5090a65db1ba)
    ![image](https://github.com/0aaryan/healthMate/assets/73797587/d3c915b7-11d4-4e6b-91e6-a25b83063f45)
    ![image](https://github.com/0aaryan/healthMate/assets/73797587/f5a32340-d440-43b9-8d8e-0ce615681b53)

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [OpenAI](https://platform.openai.com/)

Feel free to contribute to this project or provide feedback!
