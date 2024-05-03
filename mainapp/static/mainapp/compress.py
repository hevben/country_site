from PIL import Image
import PIL
import os

#quality = int(input("Pick quality: "))


def compress_and_save(input_img, output_img):
    image = Image.open(input_img)
    new_image = image.resize((50,50),Image.NEAREST)
    image.save(output_img, "jpg")


if __name__ == "__main__":
    source_path = "img"
    output_path = "img/compressed"

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for filename in os.listdir(source_path):
        if filename.endswith(".svg"):
            input_img = os.path.join(source_path, filename)
            output_img = os.path.join(output_path, filename)

            compress_and_save(input_img, output_img)

    print("All compression completed")