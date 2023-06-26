#!/usr/bin/env python3
# -*- coding: utf-8 -*-

art = '''
 _____   ____  __  _    ___         ____  __ __  ______   ___   ___ ___   ____  ______  ____  ___   ____  
|     | /    ||  |/ ]  /  _]       /    ||  |  ||      | /   \ |   |   | /    ||      ||    |/   \ |    \ 
|   __||  o  ||  ' /  /  [_ _____ |  o  ||  |  ||      ||     || _   _ ||  o  ||      | |  ||     ||  _  |
|  |_  |     ||    \ |    _]     ||     ||  |  ||_|  |_||  O  ||  \_/  ||     ||_|  |_| |  ||  O  ||  |  |
|   _] |  _  ||     ||   [_|_____||  _  ||  :  |  |  |  |     ||   |   ||  _  |  |  |   |  ||     ||  |  |
|  |   |  |  ||  .  ||     |      |  |  ||     |  |  |  |     ||   |   ||  |  |  |  |   |  ||     ||  |  |
|__|   |__|__||__|\_||_____|      |__|__| \__,_|  |__|   \___/ |___|___||__|__|  |__|  |____|\___/ |__|__|
                                                                                                          
                                                                                                                                                                                                                                                                                    
                                                                                                        
                            DEVELOPED BY @DRAC0077. VERSION:1.0

This tool generates fake data including first name, last name, date of birth, gender, and a plausible username.
'''
print(art)

import random
from faker import Faker

faker = Faker()

def get_gender_from_name(name):
    """Get the gender based on the name using the last character of the first name."""
    last_char = name.strip()[-1].lower()

    if last_char in ['a', 'e', 'x']:
        return "Female"
    elif last_char in ['o', 'i', 'r', 'd', 'y']:
        return "Male"
    else:
        return random.choice(["Male", "Female"])

def generate_fake_data(num_entries):
    """Generate fake data with first name, last name, date of birth, gender, and username."""
    data = []
    for _ in range(num_entries):
        first_name = faker.first_name()
        last_name = faker.last_name()
        date_of_birth = faker.date_of_birth(minimum_age=18, maximum_age=70)
        gender = get_gender_from_name(first_name)
        username = f"{first_name.lower()}.{last_name.lower()}{random.randint(1, 100)}"
        data.append((first_name, last_name, date_of_birth, gender, username))
    return data

if __name__ == "__main__":
    num_entries = int(input("Enter the number of fake data entries to generate: "))

    fake_data = generate_fake_data(num_entries)

    print("Generated Data:")
    for entry in fake_data:
        first_name, last_name, date_of_birth, gender, username = entry
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Date of Birth: {date_of_birth}")
        print(f"Gender: {gender}")
        print(f"Username: {username}")
        print()
