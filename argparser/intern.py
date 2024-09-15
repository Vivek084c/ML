import matplotlib.pyplot as plt
import random

class Rectangle:
    def __init__(self, width, height, id):
        self.width = width
        self.height = height
        self.id = id
        self.x = None
        self.y = None
        self.rotated = False

    def rotate(self):
        self.width, self.height = self.height, self.width
        self.rotated = not self.rotated

def recursive_partitioning(space_width, space_height, rectangles, x_offset=0, y_offset=0):
    if len(rectangles) == 0:
        return True

    current_rectangle = rectangles[0]

    # Try to fit the rectangle without rotation
    if current_rectangle.width + 1 <= space_width and current_rectangle.height + 1 <= space_height:
        current_rectangle.x = x_offset
        current_rectangle.y = y_offset
        if recursive_partitioning(space_width - current_rectangle.width - 1, space_height, rectangles[1:], x_offset + current_rectangle.width + 1, y_offset):
            return True

    # Try to rotate and fit
    current_rectangle.rotate()
    if current_rectangle.width + 1 <= space_width and current_rectangle.height + 1 <= space_height:
        current_rectangle.x = x_offset
        current_rectangle.y = y_offset
        if recursive_partitioning(space_width - current_rectangle.width - 1, space_height, rectangles[1:], x_offset + current_rectangle.width + 1, y_offset):
            return True

    # Try partitioning vertically
    if current_rectangle.width + 1 <= space_width and current_rectangle.height + 1 <= space_height:
        if recursive_partitioning(current_rectangle.width, space_height - current_rectangle.height - 1, rectangles[1:], x_offset, y_offset + current_rectangle.height + 1):
            return True

    # If all options fail, backtrack and return False
    return False

def plot_rectangles(rectangles):
    fig, ax = plt.subplots()
    for rect in rectangles:
        color = (random.random(), random.random(), random.random())
        ax.add_patch(plt.Rectangle((rect.x, rect.y), rect.width, rect.height, fill=True, edgecolor='black', facecolor=color))
        ax.text(rect.x + rect.width / 2, rect.y + rect.height / 2, f'{rect.id}', color='black', ha='center', va='center')
        if rect.rotated:
            ax.text(rect.x + rect.width / 2, rect.y + rect.height / 2 - 2, 'Rotated', color='red', ha='center', va='center')

    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()

def main():
    # Define 5 random rectangles
    rectangles = [Rectangle(random.randint(10, 30), random.randint(10, 30), i+1) for i in range(5)]
    
    # Try to place rectangles
    if not recursive_partitioning(100, 100, rectangles):
        raise ValueError("Placement not possible")
    
    # Plot the result
    plot_rectangles(rectangles)

if __name__ == "__main__":
    main()