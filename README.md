# LoverBoyFonts

**LoverBoyFonts** is a collection of terminal-based Python tools for generating fancy Unicode text styles and BBCode color gradients without requiring a browser or JavaScript.

The project is designed to work entirely from the command line, making it suitable for **privacy-conscious environments** (such as Whonix Workstations) where users may want to avoid browser-based text generators.

---

## What This Project Is For

* Generate **fancy Unicode text styles** (bold, script, monospace, etc.)
* Create **BBCode color gradients** for text
* Run everything **locally in the terminal**
* Avoid browser-based tools that may leak metadata or fingerprint users
* Keep dependencies isolated using a Python virtual environment

---

## Table of Contents

* [Installation](#installation)
* [Setup Instructions](#setup-instructions)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [License](#license)

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

    The setup script will:

    * Verify that **Python 3** is installed
    * Verify that the **Python venv module** is available
      (on Debian / Whonix: `python3-venv`)
    * Create a **local virtual environment** (`venv/`) if one does not exist
    * Install required Python packages from `requirements.txt`
    * Temporarily add the project’s `/bin` directory to your `$PATH` for the current terminal session

    > ⚠️ **Note:** Installing Python dependencies will access the network (via Tor on Whonix).
    > If any required dependency is missing, the script will stop and provide clear instructions on how to fix it.

2. **Install Noto Fonts** *(required for proper font rendering)*:

   In order to view the generated output correctly, you will likely need to install the **Noto** fonts (especially if you're using fancy or special Unicode characters).
   
   ```bash
   sudo apt install fonts-noto
   ```

   These fonts help ensure that all the Unicode characters render correctly in your terminal.

3. (Optional but recommended) Add the `/bin` directory to your `$PATH` permanently:

    * Temporary setup (for the current session only):

      The `setup.sh` script will add `/bin` to your `$PATH` for the current terminal session. When you close the terminal, this change will be lost.

    * Permanent setup:

      Add the following line to your `~/.bashrc` or `~/.zshrc` file:

      ```bash
      export PATH="$HOME/path/to/LoverBoyFonts/bin:$PATH"
      ```

      After adding the line, run:

      ```bash
      source ~/.bashrc
      # or
      source ~/.zshrc
      ```
      
    Adding `/bin` to your `$PATH` allows you to run the scripts from anywhere in your terminal without needing to navigate to the project folder.

---

## Usage

### **Available Scripts**:
    
* **`fancytext`**: This script generates **fancy text** in various styles and outputs it to the terminal. You can use it to create stylized text with fonts and effects.
* **`gradient`**: This script generates **gradient coloring** for input text and outputs it in **BBCode format** to the terminal. You can apply gradients with various directions (horizontal, vertical, diagonal), excluding spaces and blank characters from the BBCode output.

**Run the scripts directly from anywhere**:  
After running `setup.sh` and adding `/bin` to your `$PATH` (either temporarily or permanently), you can run the scripts from anywhere in your terminal.

### Fancy Text Generator

```bash
fancytext
```

* Prompts for input text
* Outputs multiple fancy Unicode text styles
* Runs entirely locally


### Gradient Generator

```bash
gradient
```

* Accepts multi-line input via standard input
* Prompts for gradient angle (horizontal, vertical, diagonal)
* Prompts for one or more hex colors
* Outputs BBCode-formatted text with color gradients
* Spaces and blank characters are preserved without BBCode tags

---

## Project Structure

```text
LoverBoyFonts/
├── bin/            # Shell wrappers (activate venv + run scripts)
├── scripts/        # Python scripts (fancy text, gradients)
├── venv/           # Local Python virtual environment
├── requirements.txt
├── setup.sh
└── README.md
```

* The `/bin` scripts handle virtual environment activation automatically
* Python scripts are never run against the system Python
* No global packages are installed

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
