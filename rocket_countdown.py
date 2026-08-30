# --- ROCKET LAUNCH COUNTDOWN ---
import time  # This tells Python to bring in the time-controlling tools

print("🚀 Preparing for launch... Mission Control is checking all systems.")
time.sleep(2)  # Tells the computer to pause for 2 seconds

# A loop that counts backward from 10 down to 1
for seconds in range(10, 0, -1):
    print(f"⏱️ T-minus {seconds}...")
    time.sleep(1)  # Forces the computer to wait exactly 1 second before the next line!

# The final countdown moment!
print("\n🔥 IGNITION!")
time.sleep(0.5)
print("🚀 LIFTOFF! We have a liftoff of the XeroxSpace rocket!")
