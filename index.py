import cv2
import mediapipe as mp

# Inisialisasi MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Fungsi untuk mendeteksi jari-jari terangkat
def fingers_up(hand_landmarks):
    fingers = []
    finger_tips = [
        mp_hands.HandLandmark.INDEX_FINGER_TIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_hands.HandLandmark.RING_FINGER_TIP,
        mp_hands.HandLandmark.PINKY_TIP
    ]
    
    for tip in finger_tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(True)
        else:
            fingers.append(False)
    
    return fingers

# Fungsi untuk menampilkan teks kustom pada frame
def draw_custom_text(image, text, position, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, color=(0, 255, 0), thickness=2):
    cv2.putText(image, text, position, font, font_scale, color, thickness, cv2.LINE_AA)

# Buka kamera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingers = fingers_up(hand_landmarks)
            
            # Deteksi gerakan tertentu
            if fingers == [True, False, False, False]:  # Hanya jari telunjuk terangkat
                draw_custom_text(image, 'aku ganteng', (10, 30))
            elif fingers == [True, True, False, False]:  # Jari telunjuk dan jari tengah terangkat
                draw_custom_text(image, 'V', (10, 30))
            elif all(fingers):  # Semua jari terangkat
                draw_custom_text(image, '5', (10, 30))
            # Tambahkan logika lain sesuai kebutuhan untuk gerakan tangan lainnya

    cv2.imshow('Hand Gesture Detection with Custom Text', image)

    if cv2.waitKey(5) & 0xFF == 27:  # Tekan 'Esc' untuk keluar
        break

cap.release()
cv2.destroyAllWindows()
