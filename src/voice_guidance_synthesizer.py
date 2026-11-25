"""
Third Eye: Spatial Voice Guidance Synthesizer
Converts spatial detection results into clear, concise, actionable auditory cues
for visually impaired users with urgency prioritization.
"""

class SpatialVoiceGuidanceSynthesizer:
    def __init__(self):
        pass

    def generate_speech_prompt(self, detections):
        """Translates detections into spoken navigation commands."""
        if not detections:
            return "Path clear ahead."
            
        # Prioritize immediate obstacles in center path
        critical = [d for d in detections if d["urgency"] == "High" or d["estimated_distance_meters"] < 2.0]
        if critical:
            top_hazard = critical[0]
            return f"Caution: {top_hazard['label']} directly {top_hazard['zone']} at {top_hazard['estimated_distance_meters']} meters. Step slightly {'Right' if top_hazard['zone']=='Center' else 'Left'}."
            
        secondary = detections[0]
        return f"{secondary['label']} detected on {secondary['zone']} at {secondary['estimated_distance_meters']} meters."

if __name__ == "__main__":
    from object_detection_pipeline import VisionAssistanceDetector
    dummy_tensor = __import__("numpy").zeros((640, 640, 3))
    detector = VisionAssistanceDetector()
    results = detector.detect_and_localize(dummy_tensor)
    
    synthesizer = SpatialVoiceGuidanceSynthesizer()
    spoken_command = synthesizer.generate_speech_prompt(results)
    
    print("\n--- AUDITORY NAVIGATION OUTPUT ---")
    print(f"Spoken Prompt: \"{spoken_command}\"")
