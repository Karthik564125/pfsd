# Import necessary modules
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

# Import the Profile model
from your_app.models import Profile

# Retrieve all profile objects from the database
profiles = Profile.objects.all()

# Display data for each profile
for profile in profiles:
    print("Username:", profile.user.username)
    print("Date of Birth:", profile.dob)
    print("City:", profile.city)
    print("Address:", profile.address)
    print("Contact:", profile.contact)
    print("User Type:", profile.user_type)
    print("Status:", profile.status)
    print("Image:", profile.image.url if profile.image else "No image")
    print("\n")

