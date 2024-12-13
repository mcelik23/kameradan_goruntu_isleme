import cv2


class Streamer:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def read_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            raise Exception("Kamera görüntüsü alınamadı")

        #(Ayna görüntüsü)
        frame = cv2.flip(frame, 1)

        return frame

    def release(self):
        self.cap.release()
