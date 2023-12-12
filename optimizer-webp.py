import os
from PIL import Image

def convert_and_optimize_image(input_path, output_path, max_width=800, max_height=800, quality=100):
    try:
        # Open the image
        img = Image.open(input_path)

        # Resize the image to fit within the specified dimensions while preserving the aspect ratio
        img.thumbnail((max_width, max_height))

        # Save the resized image in WebP format
        img.save(output_path, "WEBP", quality=quality)

        print(f"Converted and optimized: {input_path}")

    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def convert_images_in_directory(input_directory, output_directory):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate through all files in the input directory
    for filename in os.listdir(input_directory):
        input_path = os.path.join(input_directory, filename)

        # Check if the file is an image
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
            # Construct the output path with the same filename but WebP extension
            output_path = os.path.join(output_directory, os.path.splitext(filename)[0] + ".webp")

            # Convert and optimize the image
            convert_and_optimize_image(input_path, output_path)

if __name__ == "__main__":
    # Specify the input and output directories
    input_directory = "ketusouthyouthsummit2023"
    output_directory = "ketusouthyouthsummit2023"

    # Convert images in the input directory and save the WebP images in the output directory
    convert_images_in_directory(input_directory, output_directory)
