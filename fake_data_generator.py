#!/usr/bin/env python3
# -*- coding: utf-8 -*-

art = '''
"""
.%%%%%%...%%%%...%%..%%..%%%%%%...........%%%%...%%..%%..%%%%%%...%%%%...%%...%%...%%%%...%%%%%%..%%%%%%...%%%%...%%..%%.
.%%......%%..%%..%%.%%...%%..............%%..%%..%%..%%....%%....%%..%%..%%%.%%%..%%..%%....%%......%%....%%..%%..%%%.%%.
.%%%%....%%%%%%..%%%%....%%%%....%%%%%%..%%%%%%..%%..%%....%%....%%..%%..%%.%.%%..%%%%%%....%%......%%....%%..%%..%%.%%%.
.%%......%%..%%..%%.%%...%%..............%%..%%..%%..%%....%%....%%..%%..%%...%%..%%..%%....%%......%%....%%..%%..%%..%%.
.%%......%%..%%..%%..%%..%%%%%%..........%%..%%...%%%%.....%%.....%%%%...%%...%%..%%..%%....%%....%%%%%%...%%%%...%%..%%.
.........................................................................................................................
                                                                                                                                                                                                                                                                                    
                                                                                                        
                            DEVELOPED BY DRAC00. VERSION:1.0

This script generates fake data including first name, last name, date of birth, gender, and username.

"""
'''
print(art)

import random
from faker import Faker

faker = Faker()

def generate_fake_data(num_entries):
    """Generate fake data with first name, last name, date of birth, gender, and username."""
    data = []
    for _ in range(num_entries):
        first_name = faker.first_name()
        last_name = faker.last_name()
        date_of_birth = faker.date_of_birth(minimum_age=18, maximum_age=70)
        gender = random.choice(["Male", "Female"])
        username = f"{first_name.lower()}.{last_name.lower()}{random.randint(1, 100)}"
        data.append((first_name, last_name, date_of_birth, gender, username))
    return data

if __name__ == "__main__":
    num_entries = int(input("Enter the number of fake data entries to generate: "))

    fake_data = generate_fake_data(num_entries)

    print("Generated Fake Data:")
    for entry in fake_data:
        first_name, last_name, date_of_birth, gender, username = entry
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Date of Birth: {date_of_birth}")
        print(f"Gender: {gender}")
        print(f"Username: {username}")
        print()
