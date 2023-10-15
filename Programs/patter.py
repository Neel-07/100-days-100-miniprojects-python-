import numpy as np
import matplotlib.pyplot as plt

def generate_artistic_pattern():
    # Create a canvas
    canvas = np.zeros((500, 500, 3), dtype=np.uint8)
    
    # Generate your artistic pattern
    # Example: Create a colorful gradient pattern
    for i in range(500):
        for j in range(500):
            canvas[i, j] = [i % 256, j % 256, (i + j) % 256]
    
    # Display the pattern
    plt.imshow(canvas)
    plt.axis('off')
    plt.show()
    
    # Save the pattern as an image
    plt.imsave("artistic_pattern.png", canvas)

# Main function
if __name__ == "__main__":
    generate_artistic_pattern()
