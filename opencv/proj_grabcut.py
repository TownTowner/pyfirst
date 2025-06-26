import cv2
import numpy as np


class GrabCut:
    def __init__(self, img):
        self.img = img
        self.mask = np.zeros(img.shape[:2], np.uint8)
        self.bgdModel = np.zeros((1, 65), np.float64)
        self.fgdModel = np.zeros((1, 65), np.float64)
        self.rect = (100, 100, 300, 300)
        self.iterCount = 5
        self.mode = cv2.GC_INIT_WITH_RECT
        self.rectFlag = False
        self.flags = self.mode
        self.colors = {
            "bg": (0, 0, 0),
            "fg": (255, 255, 255),
            "pr_bg": (128, 0, 0),
            "pr_fg": (0, 128, 0),
        }
        self.keyBindings = {
            "0": "bg",
            "1": "fg",
            "2": "pr_bg",
            "3": "pr_fg",
        }

        self.windowName = "img"
        cv2.namedWindow(self.windowName)
        cv2.setMouseCallback(self.windowName, self.mouseCallback)

    def show(self):
        while True:
            self.imgCopy = self.img.copy()
            if self.rectFlag:
                cv2.rectangle(self.imgCopy, self.rect, self.colors["pr_bg"], 2)
            else:
                cv2.rectangle(self.imgCopy, self.rect, self.colors["bg"], 2)

            cv2.imshow(self.windowName, self.imgCopy)

            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
            if k == ord("r"):
                self.rectFlag = False
            elif k == ord("n"):
                self.mode = cv2.GC_INIT_WITH_RECT
                self.rectFlag = False
            elif k == ord("e"):
                self.mode = cv2.GC_EVAL
            elif k == ord("c"):
                self.mode = cv2.GC_INIT_WITH_MASK
            elif k == ord("a"):
                self.rectFlag = True
            elif k == ord("s"):
                self.iterCount = self.iterCount + 1
            elif k == ord("d"):
                self.iterCount = self.iterCount - 1
            elif k in self.keyBindings:
                self.flags = self.mode | self.keyBindings[k]
            elif k == ord("g"):
                self.grabcut()
            elif k == ord("v"):
                self.showResult()
            elif k == ord("s"):
                self.saveResult()
            elif k == ord("l"):
                self.loadResult()
            elif k == ord("z"):
                self.undo()
            elif k == ord("x"):
                self.redo()
            elif k == ord("p"):
                self.printInfo()
            elif k == ord("h"):
                self.printHelp()
            elif k == ord("q"):
                break

        self.quit()

    def quit(self):
        cv2.destroyAllWindows()

    def printInfo(self):
        print(f"{self.iterCount = }")
        print(f"{self.mode = }")
        print(f"{self.flags = }")

    def printHelp(self):
        print(
            """
        GrabCut Demo
        -----------
        Keys:
        ----
        0: bg
        1: fg
        2: pr_bg
        3: pr_fg
        r: reset
        n: next
        e: eval
        c: change mode
        a: add rect
        s: iter +
        d: iter -
        g: grabcut
        v: show result
        s: save result
        l: load result
        z: undo
        x: redo
        p: print info
        h: print help
        q: quit
        """
        )

    def mouseCallback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.rectFlag = True
            self.rect = (x, y, 0, 0)
        elif event == cv2.EVENT_LBUTTONUP:
            self.rectFlag = False
            self.rect = self.calcuRect(self.rect, x, y)
            self.grabcut()
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.rectFlag:
                self.rect = self.calcuRect(self.rect, x, y)
                cv2.rectangle(self.imgCopy, self.rect, self.colors["pr_bg"], 2)

    def calcuRect(self, rect, x, y):
        return (min(rect[0], x), min(rect[1], y), abs(rect[0] - x), abs(rect[1] - y))

    def grabcut(self):
        if self.rect[3] == 0 or self.rect[2] == 0:
            return

        cv2.grabCut(
            self.imgCopy,
            self.mask,
            self.rect,
            self.bgdModel,
            self.fgdModel,
            self.iterCount,
            self.flags,
        )
        mask2 = np.where((self.mask == 2) | (self.mask == 0), 0, 1).astype("uint8")
        self.imgCopy = self.imgCopy * mask2[:, :, np.newaxis]

        # mask2 = np.where((self.mask == 1) | (self.mask == 3), 255, 0).astype("uint8")
        # self.imgCopy = cv2.bitwise_and(self.imgCopy, self.imgCopy, mask=mask2)

        cv2.imshow("result", self.imgCopy)


def main():
    img = cv2.imread("data/imgs/lena.png")
    grabcut = GrabCut(img)
    grabcut.show()


if __name__ == "__main__":
    main()
