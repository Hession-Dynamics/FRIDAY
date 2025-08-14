# IMPORT LIBRARIES

from verahession.api import vera_interface, tts_interface
from dotenv import load_dotenv
import os

# IMPORT ENVIRONMENT VARIABLES

load_dotenv()

API_KEY = os.getenv("API_KEY")
AGENTNAME = os.getenv("AGENTNAME")

# CHAT TO API

sentence = input("You: ")

vera_llm = vera_interface(API_KEY, AGENTNAME)
response = vera_llm.send(sentence)

print(response)

# Give 'FRIDAY' an actual voice!

vera_tts = tts_interface(API_KEY, "female", "irish")

vera_tts.tts(response.get('response'))

