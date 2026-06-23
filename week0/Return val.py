#Area of the house
def area (length,width):
    print(length*width)
    return length*width

def main():
    House_area = area (50,50)
    Yard_area = area (20,70)
    total_sq = House_area * Yard_area
    print(str(total_sq) + "square feet") 

main()