import sys

try:
    import fancytexts
except ImportError:
    print("Error: 'fancytexts' is not installed.")
    print("Please run the project setup script and ensure the virtual environment is active.")
    sys.exit(1)

def get_user_input():
    """Function to prompt for user input."""
    return input("Enter the text you want to convert: ")

def print_fancy_text_options(text):
    """Function to print different fancy text styles using the style codes."""
    style_codes = {
    "Bold": 'bfds',
    "Italic": 'ifds',
    "Bold Italic": 'bifd',
    "Monospace": 'mofd',
    "Small Caps": 'scf',
    "Double Struck": 'dsf',
    "Bubble": 'bf',
    "Fraktur": 'ff',
    "Bold Fraktur": 'bff',
    "Script": 'hwfd',
    "Bold Script": 'bsfd',
    "Currency": 'cf',
    "Block": 'bfd',
    "Smooth": 'sfd',
    "Rusify": 'rfd',
    "Manga": 'mfd',
    "Black Bubble": 'bbfd',
    "Sorcerer": 'sofd',
    "Spacing": 'spfd',
    "Square": 'sqfd',
    "Blurry": 'blfd',
    "Tiny Caps": 'ticfd',
    "Antrophobia": 'af',
    "Flaky": 'ffd',
    "High Above": 'hiafd',
    "Blacksquare": 'blsfd',
    "Fancystyle1": 'fs1f',
    "Fancystyle2": 'fs2f',
    "Fancystyle3": 'fs3f',
    "Symbols": 'syfd'
    }

    print("\nHere are your fancy text options:")

    # Iterate over the style codes and display the converted text
    for style_name, style_code in style_codes.items():
        try:
            fancy_text = fancytexts.fancytext(style_code, text)
            print(f"{style_name}: {fancy_text}")
        except Exception as e:
            print(f"Error: Could not apply style '{style_name}'. Error: {e}")

def main():
    try:
        text = get_user_input()
        print_fancy_text_options(text)
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting.")
        sys.exit(130)

if __name__ == "__main__":
    main()
