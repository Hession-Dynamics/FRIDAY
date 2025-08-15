from verahession.api import vera_interface, tts_interface

API_KEY = "FDa-DO8KKIrzj1YpPszS8-Qg4yp-KdhxU3mp4hqEFF4"
AGENT_NAME = "FRIDAY"
GENDER = "female"
ACCENT = "irish"

sentence = input("You: ")
vera_llm = vera_interface(API_KEY, AGENT_NAME)
vera_tts = tts_interface(API_KEY, GENDER, ACCENT)

response = vera_llm.send(sentence)

print(response)

vera_tts.tts(response.get("response"))
