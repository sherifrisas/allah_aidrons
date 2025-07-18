# Example: Enforcing Drone Altitude Limits with DroneKit
# This code checks the drone's altitude and triggers a failsafe if it exceeds set limits.
# Replace 'trigger_failsafe' with your actual failsafe/RTL/landing logic.

from dronekit import connect, VehicleMode
import time

# Set your altitude limits (in meters)
MAX_ALTITUDE = 120  # Maximum allowed altitude
MIN_ALTITUDE = 2    # Minimum allowed altitude

# Connect to the vehicle (adjust connection string as needed)
vehicle = connect('udp:127.0.0.1:14550', wait_ready=True)

def trigger_failsafe(reason):
    print(f"Failsafe triggered: {reason}")
    # Example: switch to RTL (Return to Launch)
    vehicle.mode = VehicleMode('RTL')

try:
    while True:
        altitude = vehicle.location.global_relative_frame.alt
        print(f"Current Altitude: {altitude:.2f} m")
        if altitude > MAX_ALTITUDE:
            trigger_failsafe("Altitude too high!")
            break
        elif altitude < MIN_ALTITUDE:
            trigger_failsafe("Altitude too low!")
            break
        time.sleep(1)
finally:
    vehicle.close() 