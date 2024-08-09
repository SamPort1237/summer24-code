import cv2
import mediapipe as mp
import time


class FaceMeshDetector():

    def __init__(self, staticmode=False, maxface=1, refinelm=False, detectioncon=0.5, trackingcon=0.5):
        self.staticmode = staticmode
        self.maxface = maxface
        self.refinelm = refinelm
        self.detectioncon = detectioncon
        self.trackingcon = trackingcon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticmode, self.maxface, self.refinelm, self.detectioncon, self.trackingcon)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=int(0.5))


    def findfacemesh(self, img, draw = True):
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)
        faces = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_CONTOURS, self.drawSpec, self.drawSpec)

                face = []
                for id, lm in enumerate(faceLms.landmark):
                    #print(lm)
                    ih, iw, ic = img.shape
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    #print(id, x, y)
                    face.append([id,x,y])
                faces.append(face)
        return img, face, faces

def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector=FaceMeshDetector()

    while True:
        success, img = cap.read()
        img, face, faces = detector.findfacemesh(img)
        if len(face) != 0:
            print(face)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()