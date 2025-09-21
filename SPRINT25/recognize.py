import cv2

#configurações
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trained_model.yml')

cap = cv2.VideoCapture(0)

scale_factor = 1.1
min_neighbors = 5

print("Iniciando reconhecimento")
print(f"Parâmetros atuais: scale_factor={scale_factor}, min_neighbors={min_neighbors}")
print(
    "Ajuste no código para ver impactos: scale_factor baixo -> mais detecções; min_neighbors alto -> detecções mais precisas")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors=min_neighbors)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        label, confidence = recognizer.predict(roi_gray)
        if confidence < 100:  #threshold ajustável (menor: mais rigoroso)
            text = "Usuário Identificado"
        else:
            text = "Desconhecido"

        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, f"{text} (Conf: {int(confidence)})", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                    (36, 255, 12), 2)

    cv2.imshow('Reconhecimento Facial', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()