import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from PIL import Image

def crop_image(input_path, output_path, dimensions):
    try:
        image = Image.open(input_path)
        width, height = image.size
        left, upper, right, lower = dimensions
        cropped_image = image.crop((left, upper, right, lower))
        cropped_image.save(output_path)
        return True
    except Exception as e:
        print("Error:", str(e))
        return False

def select_images():
    file_paths = filedialog.askopenfilenames(title="Select Images to Crop")
    return file_paths

def process_images():
    file_paths = select_images()
    if not file_paths:
        print("No images selected. Exiting...")
        return
    
    dimensions = simpledialog.askstring("Input", "Enter cropping dimensions (left, upper, right, lower):")
    if not dimensions:
        print("Invalid dimensions. Exiting...")
        return
    
    dimensions = tuple(map(int, dimensions.split(',')))

    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if not output_folder:
        print("No output folder selected. Exiting...")
        return

    print("Cropping images...")
    for file_path in file_paths:
        file_name = file_path.split("/")[-1]
        output_path = output_folder + "/" + file_name
        if crop_image(file_path, output_path, dimensions):
            print(f"{file_name} cropped and saved to {output_path}")
        else:
            print(f"Failed to crop {file_name}")
    print("Image cropping complete.")

# Create the main window
root = tk.Tk()
root.title("Automatic Image Cropper")

# Create buttons to trigger image selection and cropping
select_button = tk.Button(root, text="Select Images", command=process_images)
select_button.pack()

# Start the Tkinter main loop
root.mainloop()
