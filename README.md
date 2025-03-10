# ChatGPT, prepare the library to be called on Rasa Action function

```
The purpose of this change is to prepare the library to be called inside the async run function in Rasa.
```

- __main__.py is just changed a little bit, nothing else.
- You can check example.py to see how to call the function.

# ChatGPT <img src="https://github.com/acheong08/ChatGPT/blob/main/logo.png?raw=true" width="7%"></img>

[![PyPi](https://img.shields.io/pypi/v/revChatGPT.svg)](https://pypi.python.org/pypi/revChatGPT)
[![PyPi](https://img.shields.io/pypi/dm/revChatGPT.svg)](https://pypi.python.org/pypi/revChatGPT)

Reverse Engineered ChatGPT by OpenAI. Extensible for chatbots etc.

Connect with me on [Linkedin](https://www.linkedin.com/in/acheong08/) to support this project. I'm graduating high school soon and knowing some people might help my chances at finding employment (in the far future). 
<br><br>
You can also follow me on [Twitter](https://twitter.com/GodlyIgnorance) to stay up to date.

### Related works
- API that scales: https://github.com/ChatGPT-Hackers/ChatGPT-API-server (By me as well)
- Lightweight version: https://github.com/acheong08/ChatGPT-lite (In collaboration with [Pawan](https://github.com/PawanOsman/))

*These are separate works and not part of this library*

# Usage

## Installation

`pip3 install --upgrade revChatGPT`

## Configuration

Refer to the setup [guide](https://github.com/acheong08/ChatGPT/wiki/Setup) for more information.

## Usage

`python3 -m revChatGPT`

```python
from revChatGPT.ChatGPT import Chatbot

chatbot = Chatbot({
  "session_token": "<YOUR_TOKEN>"
}, conversation_id=None, parent_id=None) # You can start a custom conversation

response = chatbot.ask("Prompt", conversation_id=None, parent_id=None) # You can specify custom conversation and parent ids. Otherwise it uses the saved conversation (yes. conversations are automatically saved)

print(response)
# {
#   "message": message,
#   "conversation_id": self.conversation_id,
#   "parent_id": self.parent_id,
# }
```

# Awesome ChatGPT

[My list](https://github.com/stars/acheong08/lists/awesome-chatgpt)

If you have a cool project you want added to the list, open an issue.

# Disclaimers

This is not an official OpenAI product. This is a personal project and is not affiliated with OpenAI in any way. Don't sue me

# Credits

- [rawandahmad698](https://github.com/rawandahmad698) - Reverse engineering Auth0
- [FlorianREGAZ](https://github.com/FlorianREGAZ) - TLS client
- [PyRo1121](https://github.com/PyRo1121) - Linting
- [Harry-Jing](https://github.com/Harry-Jing) - Async support
- [Ukenn2112](https://github.com/Ukenn2112) - Documentation
- [aliferouss19](https://github.com/aliferouss19) - Logo
- [All other contributors](https://github.com/acheong08/ChatGPT/graphs/contributors)
