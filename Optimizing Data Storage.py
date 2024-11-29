 __author__="Kudzanai Mautsa"
"""
Description: You are optimizing the data storage for a machine learning project.
You have two datasets of image files for training. One dataset contains 4000 images, 
and the other contains 3000 images. Each image is 256KB in size.
Additionally, you receive a new storage device with 2048MB capacity.
"""
 

# Sizes of datasets (in images) 
dataset1_size = 4000
dataset2_size = 3000

# Size of each image in KB  
image_size_kb = 256 

# Calculate total storage needed (in KB)
total_storage_kb = ((4000*256)+(3000*256))

# Convert total storage needed to MB
total_storage_mb = total_storage_kb / 1024
print(f"Total storage needed: {total_storage_mb:.2f} MB")

# Storage device capacity (in MB)
device_capacity_mb = 2048

# Calculate leftover storage in MB
leftover_storage_mb =(2048-total_storage_mb)
print(f"Storage left after storing all images: {leftover_storage_mb:.2f} MB")
