crop_tips = {
    "wheat": "Sow wheat seeds in well-drained soil; irrigate every 10-15 days.",
    "rice": "Rice requires plenty of water and thrives in flooded fields.",
    "maize": "Maize grows best in warm temperatures; ensure good soil fertility."
}

def get_crop_tip(crop):
    return crop_tips.get(crop.lower(), "Sorry, no tips available for this crop.")
