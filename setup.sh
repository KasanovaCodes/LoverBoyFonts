#!/bin/bash
set -euo pipefail

# Helpers
error() {
    echo "ERROR: $1" >&2
    exit 1
}

info() {
    echo "INFO: $1"
}

# Get the directory of the current script (absolute path)
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Path to the virtual environment
VENV_DIR="$SCRIPT_DIR/venv"
VENV_FILE="$VENV_DIR/bin/activate"

# Path to the requirements.txt
REQUIREMENTS_FILE="$SCRIPT_DIR/requirements.txt"

# Path to the bin directory
BIN_DIR="$SCRIPT_DIR/bin"

# Step 1: Pre-flight Checks
# Check for python3
if ! command -v python3 >/dev/null 2>&1; then
    error "python3 is not installed or not on PATH. Please install Python 3."
fi

# Check that requirements.txt exists
if [ ! -f "$REQUIREMENTS_FILE" ]; then
    error "requirements.txt not found at $REQUIREMENTS_FILE"
fi

# Check that venv module is available
if ! python3 -m venv --help >/dev/null 2>&1; then
    error "Python venv module is not available.
On Debian/Whonix, run:
  sudo apt update && sudo apt install python3-venv"
fi

#  Step 2: Create virtual environment
if [ ! -f "$VENV_FILE" ]; then
    echo "Virtual environment not found. Creating it now..."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists."
fi

# Step 3: Install dependencies
info "Installing Python dependencies (this will access the network via Tor)."
source "$VENV_DIR/bin/activate"

# Ensure pip exists and is up to date
if ! command -v pip >/dev/null 2>&1; then
    error "pip is not available inside the virtual environment."
fi

python -m pip install --upgrade pip
python -m pip install -r "$REQUIREMENTS_FILE"

deactivate

# Step 4: Add /bin to $PATH temporarily for the session (if it's not already included)
if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    echo "Adding $BIN_DIR to your current \$PATH for this session."
    export PATH="$BIN_DIR:$PATH"
    echo "This change is temporary and will last only for this terminal session."
fi

# Step 5: Display instructions for the user
echo "Setup complete!"
echo "To use the scripts, you can now run them directly from the terminal."
echo "If you want to make the /bin directory addition permanent, add this to your ~/.bashrc or ~/.zshrc:"
echo "  export PATH=\"$BIN_DIR:\$PATH\""
echo "Then run 'source ~/.bashrc' or 'source ~/.zshrc' to apply the change."
