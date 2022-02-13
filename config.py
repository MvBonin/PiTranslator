##Deepl auth key
#To avoid putting it inside the code, set your auth key as an environment variable
#DEEPL_AUTH_KEY can be read from the code here. Or change it to the autk_key here directly.
deepl_auth_key = os.getenv("DEEPL_AUTH_KEY")

##The language, we want to translate from
lang_source = "de-DE"

##The language, we want to translate to
lang_output = "english"

voice_source = 'mb-de6'
voice_output = 'mb-pl1'

##The speech rate at output
speech_rate = 60
speech_volume = 1.0


##not yet used:
speech_pitch = 1.0
speech_word_gap = 1.0