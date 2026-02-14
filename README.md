# Audio Mute Controller

A simple Windows utility to list all applications currently playing audio and allow you to mute or unmute a selected application with a single key press.

## Features

- Lists all applications with active audio sessions.
- Allows you to select an application from the list to control.
- Toggle mute/unmute for the selected application using a hotkey.
- Refresh the list of applications without restarting the script.
- Simple and lightweight command-line interface.

## How to Use (Executable)

1.  Download the `audio_mute_controller.exe` from the latest release.
2.  Run the executable. It is recommended to run it with **administrator privileges** for it to function correctly.
3.  A terminal window will appear, listing all programs currently making sound.
4.  Enter the number of the program you wish to control and press `Enter`.

### Program Selection Menu

- **Enter a number**: Select the program to control.
- **'r'**: Refresh the list of programs.
- **'q'**: Quit the script.

### Control Mode

Once a program is selected, you can use the following keys:

- **'M'**: Toggle mute/unmute for the selected program.
- **'Home'**: Go back to the program selection menu.
- **'End'**: Exit the script.

---

<details>
<summary><b>For Developers (Running from Source)</b></summary>

### Requirements

- Python 3.x
- The script will automatically attempt to install the following required Python packages using pip:
  - `pycaw`: for audio control on Windows.
  - `comtypes`: a dependency for `pycaw`.
  - `keyboard`: for global key press detection.

### How to Run from Source

1.  Make sure you have Python installed.
2.  Save the code as a Python file (e.g., `audio_mute_controller.py`).
3.  Open a command prompt or terminal.
4.  Navigate to the directory where you saved the file.
5.  Run the script:
    ```bash
    python audio_mute_controller.py
    ```
    _Administrator privileges may be required for the `keyboard` library to capture key presses and for `pycaw` to control system audio._
