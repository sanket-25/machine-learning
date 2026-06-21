import cv2
import easyocr

reader = easyocr.Reader(['en'])
cap = cv2.VideoCapture(0)

detected_text = []

while True:
    ret, frame = cap.read()

    # Display previously detected text
    y = 30
    for text in detected_text:
        cv2.putText(
            frame,
            text,
            (10, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )
        y += 30

    cv2.putText(
        frame,
        "Press SPACE to Scan | ESC to Exit",
        (10, frame.shape[0] - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.imshow("OCR Camera", frame)

    key = cv2.waitKey(1) & 0xFF

    # SPACE pressed
    if key == 32:
        print("Scanning...")

        results = reader.readtext(frame)

        detected_text = []

        for bbox, text, confidence in results:
            detected_text.append(text)

        print("Detected:")
        print("\n".join(detected_text))

    # ESC pressed
    elif key == 27:
        break

cap.release()
cv2.destroyAllWindows()