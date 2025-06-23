# generate a catpcha image use captcha lib
from captcha.image import ImageCaptcha
from PIL import Image
from io import BytesIO


def main():
    text: str = "Hello"
    cap = ImageCaptcha(
        width=280,
        height=90,
        fonts=["fonts/arial.ttf"],
        font_sizes=(80,),
    )  # width -> width of image, height -> height of image
    # cap.write(text, "data/captcha.png")

    data: BytesIO = cap.generate(text)
    image: Image.Image = Image.open(data)
    image.show()  # will open it with default image viewer
    # image.save("data/captcha.png")  # save image to file

    print("Captcha image generated successfully.")


if __name__ == "__main__":
    main()
