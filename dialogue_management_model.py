# Part 2:Adding dialogue capabilities

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging
import tensorflow
import asyncio

import rasa.core
from rasa.core import config 
from rasa.core.agent import Agent
from rasa.core.policies import FallbackPolicy, KerasPolicy, MemoizationPolicy
from rasa.core.run import serve_application
from rasa.utils.endpoints import EndpointConfig
from rasa.core.interpreter import RasaNLUInterpreter

logger = logging.getLogger(__name__)

def train_dialogue(domain_file = './config/domain.yml',
                    model_path = './models/dialogue',
                    training_data_file = './data/stories.md'):
    policies = config.load("./config/config.yml")
    agent = Agent(domain_file, policies=policies)
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(agent.load_data(training_data_file))
    agent.train(data)
    agent.persist(model_path)
    return agent

def run_dialogue(serve_forever = True):
    interpreter = RasaNLUInterpreter('./models/nlu/default/chatter')
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent.load('./models/dialogue', interpreter = interpreter, action_endpoint=action_endpoint)
    rasa_core.run.serve_application(agent, channel=cmdline)
    return agent

if __name__ == '__main__':
    train_dialogue()