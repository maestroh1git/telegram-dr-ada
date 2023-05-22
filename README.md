# Medical Advice Telegram Bot

## Overview

The Medical Advice Telegram Bot is a Telegram bot that uses OpenAI's advanced language model GPT-3 to answer medical questions. The bot can interpret natural language queries and provide responses based on the vast amount of medical knowledge that the GPT-3 model is trained on. 

**NOTE:** The information provided by the bot is based on an AI model and doesn't replace professional medical advice, diagnosis, or treatment. Always seek the advice of your healthcare provider with any questions you may have regarding a medical condition.

## Prerequisites

- Python 3.7 or later
- pip (Python Package Installer)
- A Telegram account
- OpenAI API key

## Installation

Follow these steps to get the bot running on your local machine for development and testing purposes.

1. **Clone the Repository**

    ```
    git clone https://github.com/<your-username>/telegram-dr-ada.git
    ```

2. **Navigate to the Project Directory**

    ```
    cd telegram-dr-ada
    ```

3. **Install Dependencies**

    The required Python packages can be installed using pip. Run:

    ```
    pip install -r requirements.txt
    ```

4. **Setup Environment Variables**

    We use environment variables to store sensitive information. 

    Create or rename the `botfather.env.example` file to `botfather.env` and fill in your OpenAI API key and Telegram token.

    ```
    TELEGRAM_TOKEN=<your-telegram-bot-token>
    OPENAI_KEY=<your-openai-key>
    ```

## Usage

After setting up the environment variables, you can run the bot using:

```
python main.py
```

Now you can interact with your bot on Telegram by searching for it (`<your-bot-username>`) in the search bar. The bot should be ready to answer your medical queries.

## Testing

You can run the tests for the bot using the following command:

```
python -m unittest discover tests
```

## Deployment
[] ToDo

For instructions on how to deploy the bot to a live system, refer to the `DEPLOYMENT.md` file in the repository.

## Contributing

If you would like to contribute to this project, please feel free to fork the repository, create a feature branch, and then submit a pull request to propose your changes.

## Acknowledgments

- Thanks to OpenAI for providing the powerful GPT-3 model.
- Thanks to the developers of the python-telegram-bot wrapper, which makes interacting with the Telegram Bot API straightforward and intuitive.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for more details.

---

Remember, you'll need to create `DEPLOYMENT.md`, `LICENSE.md`, and `assets/demo_image.png` (a screenshot or some image representing your bot) in your repository.
