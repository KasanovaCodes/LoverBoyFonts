import re
import sys
import math

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')  # Remove the leading '#' if it exists
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    """Convert RGB tuple to hex color in lowercase"""
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2]).lower()

def interpolate_color(start_color, end_color, factor):
    """Interpolate between two RGB colors based on the factor"""
    start_rgb = hex_to_rgb(start_color)
    end_rgb = hex_to_rgb(end_color)
    interpolated_rgb = tuple(
        round(start_rgb[i] + (end_rgb[i] - start_rgb[i]) * factor) for i in range(3)
    )
    return rgb_to_hex(interpolated_rgb)

def apply_gradient_to_text(text, colors, angle):
    """Apply a color gradient with the specified angle to each character in the text"""
    result = ''
    lines = text.splitlines()  # Split the input into lines
    num_lines = len(lines)
    num_cols = max(len(line) for line in lines)  # Find the maximum number of columns

    num_colors = len(colors)
    non_space_count = sum(1 for char in text if char != ' ' and char != '⠀')  # Count non-space characters

    # Calculate the gradient factor for each character based on the angle
    gradient_index = 0
    for row in range(num_lines):
        for col in range(len(lines[row])):
            char = lines[row][col]
            # Exclude spaces and "blank" characters like U+2800 (Braille Pattern Blank)
            if char.isspace() or char == '⠀':  # Exclude spaces and "blank" characters
                result += char  # Keep them as they are
                continue

            # Normalize the position (row, col) based on the angle
            # For horizontal (0 degrees), we just use the column position
            # For vertical (90 degrees), we just use the row position
            # For diagonal gradients (45 degrees), we combine row and col position
            if angle == 0:  # Horizontal
                factor = col / num_cols
            elif angle == 90:  # Vertical
                factor = row / num_lines
            else:  # Diagonal or other angles (45 degrees)
                # Diagonal gradient: Treat the position in the grid as part of a smooth transition
                dist = (row + col) / (num_lines + num_cols)  # Use normalized row+col for smooth diagonal
                factor = dist  # Normalize the factor between 0 and 1 for diagonal

            # Interpolate between colors
            color_index_1 = int(factor * (num_colors - 1))
            color_index_2 = min(color_index_1 + 1, num_colors - 1)
            interp_factor = (factor * (num_colors - 1)) - color_index_1

            color = interpolate_color(colors[color_index_1], colors[color_index_2], interp_factor)
            result += f'[color={color}]{char}[/color]'

            gradient_index += 1

        result += '\n'  # Add newline after each line to preserve the structure

    return result

def get_colors_from_input():
    """Prompt user to input an array of colors and return as a list of hex color strings"""
    input_colors = input("Enter colors for the gradient (e.g., [#ff0000, #00ff00, #0000ff]): ").strip()

    # Check if the input is wrapped in brackets
    if input_colors.startswith('[') and input_colors.endswith(']'):
        # Remove brackets and handle the rest
        input_colors = input_colors[1:-1].strip()
        # Split by commas or spaces
        colors = re.split(r'[,\s]+', input_colors)  # Split by both commas and spaces
    else:
        # Handle the case where colors are just space/comma separated
        colors = re.split(r'[,\s]+', input_colors)  # Split by both commas and spaces

    # Normalize the color list (strip any leading '#' and ensure consistent formatting)
    normalized_colors = []
    for color in colors:
        color = color.strip()  # Strip any extra whitespace
        color = color.lstrip('#')  # Remove leading '#'

        # Validate and add leading '#' if necessary
        if len(color) == 6 and all(c in '0123456789abcdefABCDEF' for c in color):
            normalized_colors.append('#' + color.lower())  # Ensure each color has a leading '#'
        else:
            print(f"Invalid hex color: {color}. Skipping.")
            return []

    return normalized_colors

def main():
    """Main function to run the script"""
    # Get multi-line input text
    print("Enter text (press Ctrl+D on new line to finish):")
    input_text = sys.stdin.read().strip()

    # Check if there's more than one line
    num_lines = input_text.count('\n') + 1  # Count the number of lines

    # If it's a single line, default to horizontal gradient
    if num_lines == 1:
        angle = 0  # Set angle to horizontal by default
    else:
        # Get the gradient angle from the user
        angle = input("Enter gradient angle (0 for horizontal, 90 for vertical, 45 for diagonal): ").strip()

        # Convert angle to integer
        try:
            angle = int(angle)
        except ValueError:
            print("Invalid angle entered. Exiting.")
            return

    # Get the colors for the gradient as an array
    colors = get_colors_from_input()

    if not colors:
        print("No valid colors entered. Exiting.")
        return

    # Generate the gradient and output it
    output_text = apply_gradient_to_text(input_text, colors, angle)
    print("\nGenerated BBCode with gradient:")
    print(output_text)

# Run the program
if __name__ == "__main__":
    main()
