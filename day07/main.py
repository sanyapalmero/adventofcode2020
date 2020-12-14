def read_file():
    with open("input.txt") as file:
        return file.read().splitlines()


class Bag:
    def __init__(self, color, contained_colors=[], contained_colors_with_nums=[]):
        self.color = color
        self.contained_colors = contained_colors
        self.contained_colors_with_nums = contained_colors_with_nums
    

def part_1():
    lines = read_file()

    bags = []
    for line in lines:
        bag_color, contain = line.split("bags contain")
        bag_color = bag_color.strip()
        contain = contain.strip()

        bag = Bag(color=bag_color)

        contained_colors_list = []
        if "no other bags" not in contain:
            contained_colors = contain.split(",")
            for color in contained_colors:
                color = color.strip()
                splitted_str = color.split(" ")
                color = " ".join([splitted_str[1], splitted_str[2]])
                contained_colors_list.append(color)
        else:
            contained_colors_list.clear()
        
        bag.contained_colors = contained_colors_list
        bags.append(bag)

    def _find_color(search_color):
        contains = set()
        for bag in bags:
            if search_color in bag.contained_colors:
                contains.add(bag.color)
                contains.update(_find_color(bag.color))
        return contains
    
    contains = _find_color("shiny gold")
    print(len(contains))


def part_2():
    lines = read_file()

    bags = []
    for line in lines:
        bag_color, contain = line.split("bags contain")
        bag_color = bag_color.strip()
        contain = contain.strip()

        bag = Bag(color=bag_color)

        contained_colors_list = []
        contained_colors_with_nums = []
        if "no other bags" not in contain:
            contained_colors = contain.split(",")
            for color in contained_colors:
                color = color.strip()
                splitted_str = color.split(" ")
                color = " ".join([splitted_str[1], splitted_str[2]])
                contained_colors_list.append(color)
                contained_colors_with_nums.append({
                    "color": color,
                    "count": int(splitted_str[0]),
                })
        else:
            contained_colors_list.clear()
            contained_colors_with_nums.clear()
        
        bag.contained_colors = contained_colors_list
        bag.contained_colors_with_nums = contained_colors_with_nums
        bags.append(bag)

    def _find_color(search_color):
        total_bags = 0
        for bag in bags:
            if search_color == bag.color:
                for contained_color in bag.contained_colors_with_nums:
                    total_bags += contained_color["count"]
                    total_bags += contained_color["count"] * _find_color(contained_color["color"])
        return total_bags
    
    total_bags = _find_color("shiny gold")
    print(total_bags)

if __name__ == "__main__":
    part_1()
    part_2()
