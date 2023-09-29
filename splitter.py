from PIL import Image
import os

def split_image(image_file):
    with Image.open(image_file) as im:
        width, height = im.size
        mid_x = width // 2
        mid_y = height // 2
        top_left = im.crop((0, 0, mid_x, mid_y))
        top_right = im.crop((mid_x, 0, width, mid_y))
        bottom_left = im.crop((0, mid_y, mid_x, height))
        bottom_right = im.crop((mid_x, mid_y, width, height))
        return top_left, top_right, bottom_left, bottom_right

def process_images(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
            input_file = os.path.join(directory, filename)
            file_prefix = os.path.splitext(filename)[0]
            top_left, top_right, bottom_left, bottom_right = split_image(input_file)
            
            output_folder = os.path.join(directory, "output")
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            top_left.save(os.path.join(output_folder, file_prefix + "_top_left.png"))
            top_right.save(os.path.join(output_folder, file_prefix + "_top_right.png"))
            bottom_left.save(os.path.join(output_folder, file_prefix + "_bottom_left.png"))
            bottom_right.save(os.path.join(output_folder, file_prefix + "_bottom_right.png"))

if __name__ == "__main__":
    directory = "input"  # Change this to your input directory
    process_images(directory)
