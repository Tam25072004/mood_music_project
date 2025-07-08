import cv2
from deepface import DeepFace
import pygame
import time
import os
import random

# Initialize pygame mixer
pygame.mixer.init()

# Define music paths
mood_music = {
    'happy': ['music/happy1.mp3', 'music/happy2.mp3'],
    'sad': ['music/sad1.mp3', 'music/sad2.mp3'],
    'angry': ['music/angry1.mp3'],
    'neutral': ['music/neutral1.mp3']
}

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        print("Mood Detected:", emotion)

        if emotion in mood_music:
            music_file = random.choice(mood_music[emotion])
            if os.path.exists(music_file):
                pygame.mixer.music.load(music_file)
                pygame.mixer.music.play()
                print(f"Playing: {music_file}")
                time.sleep(10)  # Let the song play for 10 seconds
                pygame.mixer.music.stop()
            else:
                print(f"Music file not found: {music_file}")
        break

    except Exception as e:
        print("Error:", e)

    cv2.imshow("Mood Detection", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
