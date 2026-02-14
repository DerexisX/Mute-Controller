# Audio Mute Controller

A Python script that lists all applications currently playing audio on your Windows machine and allows you to mute or unmute a selected application with a single key press.

## Features

- Lists all applications with active audio sessions.
- Allows you to select an application from the list.
- Toggle mute/unmute for the selected application.
- Refresh the list of applications.
- Simple command-line interface.

## Requirements

- Python 3.x
- The script will automatically install the following required Python packages using pip:
  - `pycaw`: for audio control on Windows.
  - `comtypes`: a dependency for `pycaw`.
  - `keyboard`: for global key press detection.

## How to Run

1.  Make sure you have Python installed.
2.  Save the code as a Python file (e.g., `audio_mute_controller.py`).
3.  Open a command prompt or terminal.
4.  Navigate to the directory where you saved the file.
5.  Run the script with administrator privileges:
    ```bash
    python audio_mute_controller.py
    ```
    _Administrator privileges may be required for the `keyboard` library to capture key presses and for `pycaw` to control system audio._

## Usage

1.  When you run the script, it will display a list of programs that are currently playing audio.
2.  Enter the number corresponding to the program you want to control and press `Enter`.

### Program Selection Menu

- **Enter a number**: Select the program to control.
- **'r'**: Refresh the list of programs.
- **'q'**: Quit the script.

### Control Mode

Once a program is selected, you can use the following keys:

- **'M'**: Toggle mute/unmute for the selected program.
- **'Home'**: Go back to the program selection menu.
- **'End'**: Exit the script.

## Creating an Executable

You can create a standalone executable from this script using `pyinstaller`.

1.  Install `pyinstaller`:
    ```bash
    pip install pyinstaller
    ```
2.  Navigate to the script's directory in your terminal.
3.  Run the following command:

    ```bash
    pyinstaller --onefile --noconsole audio_mute_controller.py
    ```

    - `--onefile`: Packages everything into a single executable.
    - `--noconsole`: Prevents the command prompt from appearing when you run the executable.

4.  The executable will be located in the `dist` folder. You can run this `.exe` file directly, preferably with administrator rights.
