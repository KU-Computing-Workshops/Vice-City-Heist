"""
THE VICE CITY HEIST  (a Git practice repo)
=========================================
This file is broken on purpose. Every MISSION below has a bug or is unfinished.
Fix the code in your editor, save, then run:   python heist.py
When a mission says PASS, save your progress with Git.
"""

# ---- Crew settings (we fight over these in the team exercises) ----
CREW_NAME = "The Vice City Crew"
HIDEOUT = "Leonida Keys"

CARS = [
    ("Sultan", 150),
    ("Infernus", 190),
    ("Sanchez", 120),
    ("Stallion", 140),
]
MAX_STARS = 5


# MISSION 1 (easy): Welcome to Vice City
def welcome(name):
    """Return the text: Welcome to Vice City, Lucia!  (use the name that is passed in)"""
    # TODO: this function is unfinished.
    # Hint: an f-string looks like f"Hello {name}"
    pass


# MISSION 2 (easy): Wanted level stars
def show_stars(stars):
    """Return one '*' for every wanted star. 3 stars -> '***'"""
    # TODO: this function is unfinished.
    # Hint: in Python, "*" * 3 gives "***"
    return ""


# MISSION 3 (easy): The payout
def payout(base, bonus):
    """Total cash = the base pay PLUS the bonus."""
    return base - bonus


# MISSION 4 (easy): WASTED?
def is_wasted(health):
    """Return True when health has run out (0 or less), otherwise False."""
    return health < 0


# MISSION 5 (medium): Heat cap
def add_heat(stars, heat):
    """Add heat to the wanted level, but never go above MAX_STARS."""
    return stars + heat


# MISSION 6 (medium): The getaway car
def fastest_car(cars):
    """Return the NAME of the car with the highest top speed."""
    return min(cars, key=lambda car: car[1])[0]


# MISSION 7 (medium): Splitting the Jewel Store Job
def split_the_take(total, crew_size):
    """Michael, Franklin and Trevor split the take. Return each person's share
    in whole dollars. 9000 split 3 ways -> 3000"""
    # Hint: // divides and rounds down
    return total * crew_size


# ---------------------------------------------------------------------------
# Don't edit below this line. This just checks your missions.
# ---------------------------------------------------------------------------
CHECKS = [
    ("Mission 1: welcome", lambda: welcome("Lucia") == "Welcome to Vice City, Lucia!"),
    ("Mission 2: show_stars", lambda: show_stars(3) == "***" and show_stars(0) == ""),
    ("Mission 3: payout", lambda: payout(5000, 1500) == 6500),
    ("Mission 4: is_wasted", lambda: bool(is_wasted(0)) and not is_wasted(40)),
    ("Mission 5: add_heat", lambda: add_heat(3, 1) == 4 and add_heat(4, 3) == MAX_STARS),
    ("Mission 6: fastest_car", lambda: fastest_car(CARS) == "Infernus"),
    ("Mission 7: split_the_take", lambda: split_the_take(9000, 3) == 3000),
]


def run_checks():
    print(f"\nCrew: {CREW_NAME}   |   Hideout: {HIDEOUT}\n")
    passed = 0
    for name, check in CHECKS:
        try:
            ok = bool(check())
        except Exception:
            ok = False
        print(("PASS  " if ok else "FAIL  ") + name)
        passed += ok
    print(f"\n{passed}/{len(CHECKS)} missions complete.")
    if passed == len(CHECKS):
        print("MISSION PASSED. Respect +")


if __name__ == "__main__":
    run_checks()
