import cv2
import numpy as np
from PIL import Image
import os

def analyze_proof(file_path: str, category: str):
    score = 0
    reasons = []


    if category.lower() == "road pothole":
        score += 0.2
        reasons.append("Category supported")
    else:
        reasons.append("Unknown category")

    
    try:
        img = cv2.imread(file_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except:
        return {
            "verdict": "INVALID",
            "confidence": 0.2,
            "reason": "Unreadable image"
        }

    
    blur_score = cv2.Laplacian(gray, cv2.CV_64F).var()
    if blur_score > 100:
        score += 0.25
        reasons.append("Image is sharp")
    else:
        reasons.append("Image is blurry")


    edges = cv2.Canny(gray, 50, 150)
    edge_density = np.sum(edges > 0) / edges.size

    if 0.01 < edge_density < 0.15:
        score += 0.35
        reasons.append("Irregular road damage detected")
    else:
        reasons.append("No pothole-like structure")


    if score >= 0.6:
        verdict = "VALID"
    else:
        verdict = "INVALID"

    return {
        "verdict": verdict,
        "confidence": round(score, 2),
        "reason": ", ".join(reasons)
    }
