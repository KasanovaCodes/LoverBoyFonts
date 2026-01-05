#!/bin/bash

# Get the directory of the current script (absolute path)
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Path to the virtual environment
VENV_DIR="$SCRIPT_DIR/../venv"

# Path to the requirements.txt
REQUIREMENTS_FILE="$SCRIPT_DIR/../requirements.txt"

# Path to the bin directory
BIN_DIR="$SCRIPT_DIR/../bin"

# Step 1: Check if the virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found. Creating it now..."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists."
fi

# Step 2: Install dependencies
echo "Installing dependencies from requirements.txt..."
source "$VENV_DIR/bin/activate"
pip install -r "$REQUIREMENTS_FILE"
deactivate

# Step 3: Add /bin to $PATH temporarily for the session (if it's not already included)
if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    echo "Adding $BIN_DIR to your current \$PATH for this session."
    export PATH="$BIN_DIR:$PATH"
    echo "This change is temporary and will last only for this terminal session."
fi

# Step 4: Display instructions for the user
echo "Setup complete!"
echo "To use the scripts, you can now run them directly from the terminal."
echo "If you want to make the /bin directory addition permanent, add this to your ~/.bashrc or ~/.zshrc:"
echo "  export PATH=\"$BIN_DIR:\$PATH\""
echo "Then run 'source ~/.bashrc' or 'source ~/.zshrc' to apply the change."
