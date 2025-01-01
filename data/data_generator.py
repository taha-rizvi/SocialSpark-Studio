import pandas as pd
import random
from datetime import datetime, timedelta

# Helper function to generate random dates
def generate_dates(start_date, num_dates):
    dates = [start_date + timedelta(days=i) for i in range(num_dates)]
    return dates

# Simulate the dataset
post_types = ['Carousel', 'Reels', 'Static Image']
user_types = ['Popular', 'Unpopular']
content_quality = ['High-Quality', 'Average']
num_posts = 1000  # Number of posts

data = []
start_date = datetime(2025, 1, 1)

for i in range(num_posts):
    post_type = random.choice(post_types)
    user_type = random.choice(user_types)
    quality = random.choice(content_quality)
    
    # Base engagement ranges
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
    
    # Adjustments for user type and content quality
    if user_type == 'Popular':
        likes = int(likes * 1.5)  # Popular users typically get more likes
        shares = int(shares * 1.2)  # Slightly more shares
        comments = int(comments * 1.3)  # Higher comments
    if quality == 'High-Quality':
        likes = int(likes * 1.3)  # High-quality content attracts more likes
        shares = int(shares * 1.5)  # High-quality content is more shareable
        comments = int(comments * 1.2)  # Slightly higher comments

    date = generate_dates(start_date, num_posts)[i]
    engagement = likes + shares + comments
    data.append([i+1, post_type, user_type, quality, likes, shares, comments, date, engagement])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "Post ID", "Post Type", "User Type", "Content Quality", 
    "Likes", "Shares", "Comments", "Date", "Engagement"
])

# Save to CSV
df.to_csv("realistic_social_media_engagement.csv", index=False)

# Display the first few rows
print(df.head())
