from flask import Flask, request, jsonify
import argostranslate.package
import argostranslate.translate
import os

app = Flask(__name__)

# Load models from models/ folder
model_dir = "models"
for file in os.listdir(model_dir):
    if file.endswith(".argosmodel"):
        argostranslate.package.install_from_path(os.path.join(model_dir, file))

# Get installed languages
installed_languages = argostranslate.translate.get_installed_languages()
en_lang = next(lang for lang in installed_languages if lang.code == "en")
bn_lang = next(lang for lang in installed_languages if lang.code == "bn")

@app.route('/')
def home():
    return "🌍 SiXGPT Phase 2 is Running!"

# English -> Bengali
@app.route('/en-to-bn', methods=['POST'])
def en_to_bn():
    data = request.get_json()
    text = data.get("text", "")
    try:
        translation = en_lang.get_translation(bn_lang).translate(text)
        return jsonify({"translatedText": translation})
    except Exception as e:
        return jsonify({"error": str(e)})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
