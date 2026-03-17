from alchemy import create_fire, create_water
import alchemy

print("\n=== Sacred Scroll Mastery ===\n")

print("Testing direct module access:")

fire = create_fire()
water = create_water()
earth = alchemy.elements.create_earth()
air = alchemy.elements.create_air()

print("alchemy.elements.create_fire():", fire)
print("alchemy.elements.create_water():", water)
print("alchemy.elements.create_earth():", earth)
print("alchemy.elements.create_air():", air) 


fire = alchemy.create_fire()
water = alchemy.create_water()


print("\nTesting package-level access (controlled by __init__.py):")
print("alchemy.create_fire(): ", fire) 
print("alchemy.create_water(): ", water)

try:
    alchemy.create_earth()
except AttributeError:
    print("alchemy.create_earth(): AttributeError - not exposed")
try:
    alchemy.create_air()
except AttributeError:
    print("alchemy.create_air(): AttributeError - not exposed")


print("\nPackage metadata:")
print("Version:", alchemy.__version__)
print("Author:", alchemy.__author__)
