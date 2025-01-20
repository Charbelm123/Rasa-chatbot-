Restaurant Chatbot
A Rasa-powered conversational AI bot that helps users find and book restaurants based on their preferences.

Features
  Interactive restaurant search and booking
  Form-based information collection:
    -Cuisine preferences
    -Number of people
    -Outdoor seating requirements
    -Additional preferences
    -Feedback collection

    
Project Structure
.
├── actions/             # Custom action code
├── data/               # Training data
│   ├── nlu.yml        # NLU training examples
│   ├── rules.yml      # Conversation rules
│   └── stories.yml    # Conversation paths
├── models/             # Trained model files
├── tests/             # Test stories
├── config.yml         # Pipeline configuration
├── credentials.yml    # Channel credentials
├── domain.yml         # Bot domain definition
├── endpoints.yml      # Endpoint configuration
└── restaurants_db.py  # Restaurant database utilities

Setup
1-Install dependencies:
  pip install -r requirements.txt
2-Train the model:
  rasa train
3-Start the action server:
  rasa run actions
4-Start the Rasa server:
  rasa shell


Usage

The bot supports:
  -Natural conversations about restaurant bookings
  -Multiple intents including greetings, restaurant requests, chitchat
  -Slot filling for restaurant preferences
  -Feedback collection
  -Basic chitchat
  
Development
  -Use rasa train to retrain the model
  -Add training examples in nlu.yml
  -Define conversation flows in stories.yml
  -Configure pipeline in config.yml
  


