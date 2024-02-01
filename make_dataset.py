# ##L24

# import os
# import shutil
# from tqdm import tqdm
# from PIL import Image

# def main():
#     image_dir = r"C:\Users\mehrdad\L24_CLiP\data\classified_images"
#     label_dict = {}  # To map class names to numeric labels
#     label_counter = 0
#     label_data = []
#     img_size = 256
    
#     if not os.path.exists("output"):
#         os.makedirs("output")
    
#     new_folder = ""
#     counter = 0
#     index = 0
    
#     for class_name in tqdm(os.listdir(image_dir), desc="Processing classes"):
#         class_path = os.path.join(image_dir, class_name)
#         if os.path.isdir(class_path):
#             if class_name not in label_dict:
#                 label_dict[class_name] = label_counter
#                 label_counter += 1
#             for filename in os.listdir(class_path):
#                 if filename.endswith('.png'):
#                     numeric_label = label_dict[class_name]
                    
#                     if counter % 1000 == 0:
#                         new_folder = f"{index:04d}"
#                         os.makedirs(os.path.join("output", new_folder))
#                         index += 1
                    
#                     new_filename = f"img{counter:08d}.png"
                    
#                     src_path = os.path.join(class_path, filename)
#                     dest_path = os.path.join("output", new_folder, new_filename)
                    
#                     # Resize and save the image uncompressed
#                     with Image.open(src_path) as img:
#                         img_resized = img.resize((img_size, img_size))
#                         img_resized.save(dest_path, compress_level=0)
                    
#                     label_data.append([f"{new_folder}/{new_filename}", numeric_label])
                    
#                     counter += 1

#     # Convert the inner lists to strings
#     label_strings = [f'        ["{item[0]}", {item[1]}]' for item in label_data]
    
#     # Join the strings with commas and newlines
#     labels_str = ',\n'.join(label_strings)
    
#     # Create the final formatted string
#     formatted_json_str = f'{{\n    "labels": [\n{labels_str}\n    ]\n}}'
    
#     # Write JSON file
#     with open('output/dataset.json', 'w') as f:
#         f.write(formatted_json_str)
        
#     # Create a zip file
#     shutil.make_archive("dataset", 'zip', "output")

# if __name__ == "__main__":
#     main()

# ## Diospyros
# import os
# import shutil
# from tqdm import tqdm
# from PIL import Image

# def filename_tokenizer(filename):
#     tokens = filename.split("_")
#     return tokens

# def main():
#     image_dir = '/home/me/Dios/Data/Tiles_C3_256/train/'
#     label_dict = {}  # To map species names to numeric labels
#     label_counter = 0
#     label_data = []
#     img_size = 256
#     output_dir = "~/datasets/Diospyros_C3_256"

#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)

#     new_folder = ""
#     counter = 0
#     index = 0

#     for filename in tqdm(os.listdir(image_dir), desc="Processing images"):
#         src_path = os.path.join(image_dir, filename)
#         if filename.endswith('.png'):
#             species, _,_,_,_,_,_,_ = filename_tokenizer(filename)
            
#             if species not in label_dict:
#                 label_dict[species] = label_counter
#                 label_counter += 1

#             numeric_label = label_dict[species]

#             if counter % 1000 == 0:
#                 new_folder = f"{index:04d}"
#                 os.makedirs(os.path.join(output_dir, new_folder))
#                 index += 1

#             new_filename = f"img{counter:08d}.png"
#             dest_path = os.path.join(output_dir, new_folder, new_filename)

#             # Resize and save the image uncompressed
#             with Image.open(src_path) as img:
#                 img_resized = img.resize((img_size, img_size))
#                 img_resized.save(dest_path, compress_level=0)

#             label_data.append([f"{new_folder}/{new_filename}", numeric_label])
#             counter += 1

#     # Convert inner lists to strings
#     label_strings = [f'        ["{item[0]}", {item[1]}]' for item in label_data]
    
#     # Join strings with commas and newlines
#     labels_str = ',\n'.join(label_strings)
    
#     # Make final formatted string
#     formatted_json_str = f'{{\n    "labels": [\n{labels_str}\n    ]\n}}'
    
#     # Write JSON file
#     with open(os.path.join(output_dir, 'dataset.json'), 'w') as f:
#         f.write(formatted_json_str)
        
#     # # Make a zip file
#     # shutil.make_archive("dataset", 'zip', "output")

#     # Write label map
#     with open(os.path.join(output_dir,'label_map.txt'), 'w') as f:
#         for species, numeric_label in label_dict.items():
#             f.write(f"{species} {numeric_label}\n")

# if __name__ == "__main__":
#     main()

import os
import shutil
from tqdm import tqdm
from PIL import Image
import csv

def main():
    image_dir = '/home/me/Dios/Data/Tiles_C3_256/train/'
    label_dict = {}  # To map class names to numeric labels
    label_counter = 0
    label_data = []
    img_size = 256
    output_dir = "~/datasets/Diospyros_C3_256"
    
    # Create output directories if they do not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    new_folder = ""
    counter = 0
    index = 0
    
    # Process each class in the image directory
    for class_name in tqdm(os.listdir(image_dir), desc="Processing classes"):
        class_path = os.path.join(image_dir, class_name)
        if os.path.isdir(class_path):
            if class_name not in label_dict:
                label_dict[class_name] = label_counter
                label_counter += 1
            for filename in os.listdir(class_path):
                if filename.endswith('.JPG') or filename.endswith('.jpg') or filename.endswith('.png'):
                    numeric_label = label_dict[class_name]
                    
                    if counter % 1000 == 0:
                        new_folder = f"{index:04d}"
                        new_folder_path = os.path.join(output_dir, new_folder)
                        os.makedirs(new_folder_path, exist_ok=True)
                        index += 1
                    
                    # new_filename = f"img{counter:08d}.png"
                    new_filename = f"{class_name}_{counter:08d}.png"
                    src_path = os.path.join(class_path, filename)
                    dest_path = os.path.join(new_folder_path, new_filename)
                    
                    # Resize and save the image uncompressed
                    with Image.open(src_path) as img:
                        img_resized = img.resize((img_size, img_size))
                        img_resized.save(dest_path, compress_level=0)
                    
                    label_data.append([new_folder + "/" + new_filename, numeric_label])
                    
                    counter += 1
    
    # Write label data CSV file
    label_strings = [f'        ["{item[0]}", {item[1]}]' for item in label_data]
    labels_str = ',\n'.join(label_strings)
    formatted_json_str = f'{{\n    "labels": [\n{labels_str}\n    ]\n}}'
    
    # Write JSON file
    with open(os.path.join(output_dir, 'dataset.json'), 'w') as f:
        f.write(formatted_json_str)
    
    # Write label dictionary CSV file
    with open(os.path.join(output_dir, 'label_dict.csv'), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["class_name", "numeric_label"])
        for class_name, numeric_label in label_dict.items():
            writer.writerow([class_name, numeric_label])

    # Print a success message
    print(f"Processed {counter} images. Label mapping saved to {os.path.join(output_dir, 'label_dict.csv')}")

if __name__ == "__main__":
    main()
