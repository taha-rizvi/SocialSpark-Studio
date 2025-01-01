import pandas as pd
import random
from datetime import datetime, timedelta

# Helper function to generate random dates
def generate_dates(start_date, num_dates):
    dates = [start_date + timedelta(days=i) for i in range(num_dates)]
    return dates

# Simulate the dataset
post_types = ['Carousel', 'Reels', 'Static Image']
num_posts = 100  # Number of posts

# Generate random data
data = []
start_date = datetime(2025, 1, 1)

for i in range(num_posts):
    post_type = random.choice(post_types)

    # Adjust engagement based on post type
    if post_type == 'Carousel':
        likes = random.randint(300, 800)
        shares = random.randint(50, 150)
        comments = random.randint(100, 250)
    elif post_type == 'Reels':
        likes = random.randint(200, 600)
        shares = random.randint(40, 120)
        comments = random.randint(150, 300)
    else:  # Static Image
        likes = random.randint(50, 200)
        shares = random.randint(10, 50)
        comments = random.randint(20, 80)
    
    date = generate_dates(start_date, num_posts)[i]
    engagement = likes + shares + comments
    data.append([i+1, post_type, likes, shares, comments, date, engagement])

# Create DataFrame
df = pd.DataFrame(data, columns=["Post ID", "Post Type", "Likes", "Shares", "Comments", "Date", "Engagement"])

# Save to CSV
df.to_csv("social_media_engagement.csv", index=False)

# Display the first few rows
print(df.head())
