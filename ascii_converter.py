from PIL import Image

ASCII_CHARS = "@%#*+=-:. "
MAX_WIDTH = 100  # Resize image width

def resize_image(image, new_width=MAX_WIDTH):
    width, height = image.size
    ratio = height / width / 1.65  # Adjust height scaling for terminal
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    chars = "".join(ASCII_CHARS[pixel * len(ASCII_CHARS) // 256] for pixel in pixels)
    return chars

def convert_image_to_ascii(path):
    try:
        image = Image.open(path)
    except Exception as e:
        return f"Error: {e}"

    image = resize_image(image)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    img_width = image.width
    ascii_lines = [ascii_str[i:i + img_width] for i in range(0, len(ascii_str), img_width)]
    return "\n".join(ascii_lines)

def save_to_file(ascii_art, output_path="output.txt"):
    with open(output_path, "w") as f:
        f.write(ascii_art)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python ascii_converter.py <image_path>")
        sys.exit(1)

    path = sys.argv[1]
    ascii_art = convert_image_to_ascii(path)
    print(ascii_art)
    save_to_file(ascii_art)
