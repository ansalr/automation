import os
import shutil

def merge_yolo_datasets(input_dir, output_dir):
   
    dirs = ['images', 'labels']
    file_counters = {'images': 0, 'labels': 0}
    
    for d in dirs:
        os.makedirs(os.path.join(output_dir, d), exist_ok=True)

    for subfolder in os.listdir(input_dir):
        subfolder_path = os.path.join(input_dir, subfolder)
        if os.path.isdir(subfolder_path):
            for d in dirs:
                src_dir = os.path.join(subfolder_path, d)
                dest_dir = os.path.join(output_dir, d)

                if not os.path.exists(src_dir):
                    continue

                for filename in os.listdir(src_dir):
                    if d == 'images' and not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                        continue
                    if d == 'labels' and not filename.endswith('.txt'):
                        continue

                    new_name = f"{file_counters[d]}_{filename}"
                    shutil.copy(os.path.join(src_dir, filename), os.path.join(dest_dir, new_name))
                    print(f"{filename} moved to {output_dir}")
                    file_counters[d] += 1

    print(f"Merged datasets saved to: {output_dir}")


if __name__ == "__main__":
    input_dir = "dataset"           
    output_dir = "mergeDataset"
    merge_yolo_datasets(input_dir, output_dir)
