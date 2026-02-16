import json
import os

def merge_json_files(directory, output_file):
    merged_data = {}
    
    # List all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".json") and filename != output_file:
            file_path = os.path.join(directory, filename)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                    # Use the filename (without extension) as the key
                    key = os.path.splitext(filename)[0]
                    
                    # Special handling for "openings (1).json" or similar
                    # If you want to clean up the key name:
                    key = key.split(' (')[0]
                    
                    merged_data[key] = data
                    print(f"Successfully merged: {filename}")
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    # Write the merged result to a file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, indent=4)
    
    print(f"\nMerge complete! All files saved into '{output_file}'.")

if __name__ == "__main__":
    # Current directory where the script is located
    current_dir = os.getcwd()
    output_filename = "merged.json"
    
    merge_json_files(current_dir, output_filename)