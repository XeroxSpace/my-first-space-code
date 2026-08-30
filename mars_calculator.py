# --- MARS WEIGHT CALCULATOR ---

# 1. Ask the user for their weight on Earth (in kg)
earth_weight = float(input("Enter your weight on Earth (in kg): "))

# 2. Mars gravity is only about 38% of Earth's gravity
mars_gravity_ratio = 0.38

# 3. Calculate the weight on Mars
mars_weight = earth_weight * mars_gravity_ratio

# 4. Print the mind-blowing result!
print(f"🌌 On Mars, your pulling force changes! You would weigh only {mars_weight:.2f} kg!")
