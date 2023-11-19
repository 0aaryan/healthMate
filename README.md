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
python your_script_name.py
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

- **Screenshot 1: Initial Chat Interface**
  - Description: This screenshot shows the initial chat interface with the system message and the user's input box.

  ![Initial Chat Interface](path/to/screenshot1.png)

- **Screenshot 2: Health Data Entry Sidebar**
  - Description: This screenshot illustrates the sidebar where users can enter their health data manually or choose to read it from an Arduino device.

  ![Health Data Entry Sidebar](path/to/screenshot2.png)

- **Screenshot 3: Chat History**
  - Description: This screenshot displays the chat history with alternating user and AI messages.

  ![Chat History](path/to/screenshot3.png)

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [OpenAI](https://platform.openai.com/)

Feel free to contribute to this project or provide feedback!