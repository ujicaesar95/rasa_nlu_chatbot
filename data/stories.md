## affirm happy path

* greet
    - utter_greet
* booking_doctor_intent
    - utter_ask_confirm_doctor
* affirm
    - utter_explain_doctor_available
    - action_save_confirm_doctor
    - slot{"confirm_doctor_entity": "confirm_doctor_entity"}
    - utter_ask_name
    - action_save_user_name
    - slot{"user_name_entity":"user_name_entity"}
    - utter_ask_symptomps
* symptomp_intent
    - action_save_symptomp
    - slot{"symptomp_entity":"symptomp_entity"}
    - utter_ask_symptompsDuration
* symtompDuration_intent
    - action_save_symptomp_duration
    - slot{"symptompDuration_entity":"symptompDuration_entity"}
    - utter_ask_appointmentSchedule
* appointmentSchedule_intent
    - action_save_appointment_schedule
    - slot{"appointmentSchedule_entity":"appointmentSchedule_entity"}
    - utter_ask_appointmentPlace
* appointmentPlace_intent
    - action_save_appointment_place
    - slot{"appointmentPlace_entity":"appointmentPlace_entity"}
    - utter_submit
    - utter_slots_values
* thankyou
    - utter_noworries