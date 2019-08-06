# PART 3: Start the Bot

from rasa.core.agent import Agent
from rasa.nlu.model import Trainer, Metadata
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.utils.endpoints import EndpointConfig

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/chatter')
action_endpoint = EndpointConfig("http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

# Part 4:Talk to Bot
print("start the conversation")
print()
print("Hi! How can I help you today? ")
while True:
    a=input()
    if a == 'stop' :
        break
    responses = agent.handle_message(a)
    for response in responses:
        print(response['text'])
