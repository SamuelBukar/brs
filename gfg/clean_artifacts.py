import os
import glob

# Path to the artifacts3 directory
artifacts_path = "artifacts3"

# Delete all pickle files in the artifacts3 directory
pickle_files = glob.glob(os.path.join(artifacts_path, "*.pkl"))
for file in pickle_files:
    os.remove(file)

print("All pickle files deleted successfully!")
