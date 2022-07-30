from deepface import DeepFace
import cv2 as cv

def getInformation(img):
    analysis = DeepFace.analyze(img, actions = ['race', 'emotion', 'gender'])

    data = {'gender' : analysis['gender'], 'race' : analysis['dominant_race'], 'emotion' : analysis['dominant_emotion']}

    return data

image = cv.imread("./data/tymur.jpg")

print(getInformation(image))
# prints {'gender': 'Man', 'race': 'white', 'emotion': 'neutral'}