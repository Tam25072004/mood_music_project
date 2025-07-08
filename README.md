# 🎵 Mood-Based Music Player 🎭

This project is an AI-powered desktop application that detects your **facial emotion in real time** using your webcam and plays music that matches your current mood — happy, sad, angry, or neutral.

---

## 📸 How It Works

1. Opens your webcam and scans your face.
2. Uses `DeepFace` to detect emotion (e.g., 😃 Happy, 😢 Sad, 😠 Angry).
3. Automatically plays a corresponding `.mp3` song from a local folder using `pygame`.

---

## 🧠 Technologies Used

| Purpose             | Library/Tool     |
|---------------------|------------------|
| Emotion Detection   | [DeepFace](https://github.com/serengil/deepface) |
| Webcam Input        | OpenCV           |
| Audio Playback      | pygame           |
| Language            | Python 3.9       |
