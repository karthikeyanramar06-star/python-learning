noun = input("Give me a noun: ")
verb = input("Give me a verb: ")
adjective = input("Give me an adjective: ")
print(f"The {adjective} {noun} decided to {verb} all day long.")

#Area of the house
def area (length,width):
    return length*width

def main():
    House = (50,50)
    Yard = (20,70)
    total_sq = House * Yard
    print(str(total_sq) + "square feet")