# (1.) Train the nlu model
		''' python nlu_model.py ''' old version
		''rasa train --config ./config/config.yml --domain ./config/domain.yml'' new version
		
		trains NLU Model and saves the model under nlu/default/chatter folder 
		

# (2.) Train the core Model
		## Start the custom action server by running
				''' python -m rasa_core_sdk.endpoint --actions actions '''
				
		## Open a new terminal and train the Rasa Core model by running:
				''' python dialogue_management_model.py  '''
		
		saves the dialogue management model under models/dialogue
				
# (3.) Online training
			'''  python -m rasa_core.train --online -d config/domain.yml -s data/stories.md -o models/dialogue -u models/nlu/default/chatter --epochs 250 --endpoints endpoints.yml  ''' old version

			'' rasa interactive -m models/<update models>.tar.gz --endpoints endpoints.yml '' new version
			
			Note-Make sure the custom action server is running


# (4.) Test the assistant by running:
    ```
    rasa run actions
    ```
    This will load the assistant in your command line for you to chat.

# (5.) Talking to bot
			''' python bot.py ''' old version
			''rasa shell -m models --endpoints endpoints.yml'' new version