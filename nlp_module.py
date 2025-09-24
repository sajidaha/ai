import spacy

nlp = spacy.load("en_core_web_sm")

def get_response_nlp(user_input):
    doc = nlp(user_input.lower())
    crops = ["wheat", "rice", "maize", "barley"]
    crop_mentioned = None
    for token in doc:
        if token.text in crops:
            crop_mentioned = token.text
            break
    if crop_mentioned:
        return f"I can give you tips on {crop_mentioned}. What would you like to know?"
    elif "weather" in user_input:
        return "Please provide your location for weather updates."
    else:
        return "Can you please provide more details?"

# Reuse main loop from previous code with get_response replaced by get_response_nlp
