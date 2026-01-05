# LoverBoyFonts

Simple Python tools for generating fancy text using various styles and creating BBCode text color gradients. This project allows you to easily generate fancy text and color gradients directly from the terminal.

---

## Table of Contents
- [Installation](#installation)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [License](#license)

---

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/KasanovaCodes/LoverBoyFonts.git
    cd LoverBoyFonts
    ```

2. Make the `setup.sh` script executable (only if necessary):

    ```bash
    chmod +x setup.sh
    ```

---

## Setup Instructions

To get the project up and running, follow these steps:

1. Run the `setup.sh` script to create a virtual environment and install the required dependencies:

    ```bash
    ./setup.sh
    ```

    This script will:
    - Check if a virtual environment exists, and create one if not.
    - Install all the necessary dependencies listed in `requirements.txt`.
    - Optionally add the `/bin` directory to your `$PATH` for the current session.

2. **Install Noto Fonts** *(required for proper font rendering)*:

   In order to view the generated output correctly, you will likely need to install the **Noto** fonts (especially if you're using fancy or special Unicode characters).
   
   ```bash
   sudo apt install fonts-noto
   ```

   These fonts help ensure that all the Unicode characters render correctly in your terminal.

3. (Optional but recommended) Add the `/bin` directory to your `$PATH` permanently:

    - Temporary setup (for the current session only):

      The `setup.sh` script will add `/bin` to your `$PATH` for the current terminal session. When you close the terminal, this change will be lost.

    - Permanent setup:

      Add the following line to your `~/.bashrc` or `~/.zshrc` file:

      ```bash
      export PATH="$HOME/path/to/yourproject/bin:$PATH"
      ```

      After adding the line, run:

      ```bash
      source ~/.bashrc  # or source ~/.zshrc for zsh
      ```
      
    Adding `/bin` to your `$PATH` allows you to run the scripts from anywhere in your terminal without needing to navigate to the project folder.


---

## Usage

1. **Run the scripts directly from anywhere**:  
   After running `setup.sh` and adding `/bin` to your `$PATH` (either temporarily or permanently), you can run the scripts from anywhere in your terminal. For example:

    ```bash
    fancytext
    ```
    or
    ```bash
    gradient
    ```

2. **Available Scripts**:
    - **`fancytext`**: This script generates **fancy text** in various styles and outputs it to the terminal. You can use it to create stylized text with fonts and effects.
    - **`gradient`**: This script generates **gradient coloring** for input text and outputs it in **BBCode format** to the terminal. You can apply gradients with various directions (horizontal, vertical, diagonal), excluding spaces and blank characters from the BBCode output.

---


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
