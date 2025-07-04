import cv2
import numpy as np
import face_recognition as fr
import os


def get_best_encoding_and_location(img, known_locations=None, same_as_locations=False):
    locations = fr.face_locations(img)
    known_locations = locations if same_as_locations else known_locations
    encodings = fr.face_encodings(img, known_locations)
    location = locations[0] if len(locations) > 0 else None
    encoding = encodings[0] if len(encodings) > 0 else None
    return location, encoding


def get_encodings_and_locations(img, known_locations=None, same_as_locations=False):
    locations = fr.face_locations(img)
    known_locations = locations if same_as_locations else known_locations
    encodings = fr.face_encodings(img, known_locations)
    return locations, encodings


def findEncodings(imgs):
    encodeList = []
    for img in imgs:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def face_test():
    img = fr.load_image_file("data/imgs/faces/k_ElonMusk.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgTest = fr.load_image_file("data/imgs/faces/ElonMusk2.png")
    imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

    imgLoc, imgEncode = get_best_encoding_and_location(img)
    imgTestLoc, imgTestEncode = get_best_encoding_and_location(imgTest)
    results = fr.compare_faces([imgEncode], imgTestEncode)
    faceDis = fr.face_distance([imgEncode], imgTestEncode)

    print(results, faceDis)

    cv2.rectangle(img, (imgLoc[3], imgLoc[0]), (imgLoc[1], imgLoc[2]), (255, 0, 255), 2)
    pt1Test, pt2Test = (imgTestLoc[3], imgTestLoc[0]), (imgTestLoc[1], imgTestLoc[2])
    cv2.rectangle(imgTest, pt1Test, pt2Test, (255, 0, 255), 2)

    fnt = cv2.FONT_HERSHEY_COMPLEX
    if results[0]:
        cv2.putText(imgTest, f"Match", (50, 50), fnt, 1, (0, 255, 0), 2)

    cv2.imshow("face", img)
    cv2.imshow("face2", imgTest)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def face_recog():
    path = "data/imgs/faces/"
    imgs = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        # only load known(starts with 'k_')
        if not cl.startswith("k_"):
            continue

        curImg = cv2.imread(f"{path}/{cl}")
        imgs.append(curImg)
        classNames.append(os.path.splitext(cl)[0].strip("k_"))
    print(classNames)

    encodeListKnown = findEncodings(imgs)
    print("Encoding Complete")

    fnt = cv2.FONT_HERSHEY_COMPLEX
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        if not success:
            break

        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        locations, encodings = get_encodings_and_locations(imgS, same_as_locations=True)
        for location, encoding in zip(locations, encodings):
            matches = fr.compare_faces(encodeListKnown, encoding)
            faceDis = fr.face_distance(encodeListKnown, encoding)

            matchIndex = np.argmin(faceDis)
            print(matchIndex, matches, faceDis)
            # 2 [False, False, False] [0.89848412 0.8080555  0.67921771]
            # 2 [False, False, True] [0.89301426 0.86035318 0.41269662]

            if not matches[matchIndex]:
                continue

            name = classNames[matchIndex]
            print(name)  # JackMa

            y1, x2, y2, x1 = np.array(location) * 4  # multiply back for resized before
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, name, (x1, y1 - 6), fnt, 1, (255, 255, 255), 2)

        cv2.imshow("face", img)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


def main():
    try:
        fr.load_image_file("data/imgs/faces/ElonMusk2.png")
    except Exception as e:
        import face_recognition_models

        print(f"face_recognition版本: {fr.__version__}")
        print(f"face_recognition_models版本: {face_recognition_models.__version__}")
        print(e)
        return

    face_test()
    # face_recog()


if __name__ == "__main__":
    main()
