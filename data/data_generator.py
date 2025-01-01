import csv
import random
import uuid

# Define post types and engagement ranges
post_types = ["Carousel", "Reels", "Static Image"]
likes_range = (50, 200)
shares_range = (10, 50)
comments_range = (20, 80)

# Number of entries to generate
num_entries = 1000

# Generate dataset
dataset = []
for _ in range(num_entries):
    post_id = str(uuid.uuid4())  # Unique ID for each post
    post_type = random.choice(post_types)
    likes = random.randint(*likes_range)
    shares = random.randint(*shares_range)
    comments = random.randint(*comments_range)
    dataset.append([post_id, post_type, likes, shares, comments])

# Write to CSV
csv_file = "engagement_data.csv"
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Post ID", "Post Type", "Likes", "Shares", "Comments"])
    writer.writerows(dataset)

print(f"Dataset created and saved as {csv_file}")