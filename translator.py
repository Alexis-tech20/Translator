import json 
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

api_key = "BYP_OekFgmJ3pzm0UediVxLlHcPYRt_jau_dQ4v5U0ic"
api_url = "https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/34104abe-15d8-44ea-ae5e-12e4675ee0f2"

authenticator = IAMAuthenticator(api_key)
translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
translator.set_service_url(api_url)

def translate_text(text, source_language, target_language):
    try:
        response = translator.translate(
            text=text,
            source=source_language,
            target=target_language
        ).get_result()
        translated_text = response["translations"][0]["translation"]
        return translated_text
    except Exception as e:
        print("Error:", str(e))
        return None

def main():
    source_language = input("Enter the source language code (e.g., en for English): ")
    target_language = input("Enter the target language code (e.g., es for Spanish): ")
    text_to_translate = input("Enter the text to translate: ")

    translated_text = translate_text(text_to_translate, source_language, target_language)
    if translated_text:
        print("Translated text:", translated_text)

if __name__ == "__main__":
    main()