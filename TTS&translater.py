from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os

def get_language_code(prompt, languages):
    print(prompt)
    for language, code in sorted(languages.items()):
        print(f"{language.title()}: {code}")

    language_code = input("Enter the language code: ")
    return language_code

def translate_text(text, dest_language):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text

def text_to_speech(text, googletrans_code):
    # Mapping between googletrans codes and gtts codes
    gtts_codes = {
        'af': 'af', 'sq': 'sq', 'ar': 'ar', 'hy': 'hy', 'ca': 'ca',
        'zh-cn': 'zh', 'zh-tw': 'zh-tw', 'hr': 'hr', 'cs': 'cs',
        'da': 'da', 'nl': 'nl', 'en': 'en', 'eo': 'eo', 'fi': 'fi',
        'fr': 'fr', 'de': 'de', 'el': 'el', 'ht': 'ht', 'hi': 'hi',
        'hu': 'hu', 'is': 'is', 'id': 'id', 'ga': 'ga', 'it': 'it',
        'ja': 'ja', 'ko': 'ko', 'la': 'la', 'lv': 'lv', 'lt': 'lt',
        'mk': 'mk', 'no': 'no', 'pl': 'pl', 'pt': 'pt', 'ro': 'ro',
        'ru': 'ru', 'sr': 'sr', 'sk': 'sk', 'sl': 'sl', 'es': 'es',
        'sw': 'sw', 'sv': 'sv', 'ta': 'ta', 'th': 'th', 'tr': 'tr',
        'vi': 'vi', 'cy': 'cy'
    }

    gtts_lang_code = gtts_codes.get(googletrans_code, 'en')  # Default to English if not found
    tts = gTTS(text=text, lang=gtts_lang_code)
    filename = "translated_speech.mp3"
    tts.save(filename)
    print(f"Translated speech saved as '{filename}'")
    # Uncomment the 1st line to play the audio automatically on macOS and 2nd line for macOS
    # os.system(f"open {filename}")
    # os.system(f"start {filename}")
# Example usage
text_to_translate = input("Enter the text to translate: ")
print("\n--- Language Selection for Translation ---")
translation_language = get_language_code("Available translation languages:", LANGUAGES)

translated_text = translate_text(text_to_translate, translation_language)
print(f"\nOriginal: {text_to_translate}")
print(f"Translated: {translated_text}")

# Convert translated text to speech
text_to_speech(translated_text, translation_language)
