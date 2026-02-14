"""
Audio Mute Controller
Lists all programs with audio and allows muting a selected one with the 'M' key.
"""

import sys
import subprocess

# Install required packages if not present
def install_packages():
    packages = ['pycaw', 'comtypes', 'keyboard']
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

install_packages()

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume, IAudioEndpointVolume
import keyboard
import os

def get_audio_sessions():
    """Get all active audio sessions (programs with audio)."""
    sessions = AudioUtilities.GetAllSessions()
    audio_programs = []
    
    for session in sessions:
        if session.Process:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            audio_programs.append({
                'name': session.Process.name(),
                'pid': session.Process.pid,
                'session': session,
                'volume': volume
            })
    
    return audio_programs

def display_programs(programs):
    """Display the list of programs with audio."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 60)
    print("        AUDIO MUTE CONTROLLER")
    print("=" * 60)
    print("\nPrograms with active audio:\n")
    
    if not programs:
        print("  No programs with audio found.")
        return
    
    for i, prog in enumerate(programs, 1):
        muted = prog['volume'].GetMute()
        status = "[MUTED]" if muted else "[PLAYING]"
        print(f"  {i}. {prog['name']:<30} {status}")
    
    print("\n" + "=" * 60)

def select_program(programs):
    """Let user select a program to control."""
    while True:
        display_programs(programs)
        print("\nEnter the number of the program to control (or 'r' to refresh, 'q' to quit):")
        
        choice = input("\n> ").strip().lower()
        
        if choice == 'q':
            return None
        elif choice == 'r':
            return 'refresh'
        
        try:
            index = int(choice) - 1
            if 0 <= index < len(programs):
                return programs[index]
            else:
                print("Invalid selection. Please try again.")
                input("Press Enter to continue...")
        except ValueError:
            print("Please enter a valid number.")
            input("Press Enter to continue...")

def toggle_mute(program):
    """Toggle mute state for the selected program."""
    volume = program['volume']
    current_mute = volume.GetMute()
    volume.SetMute(not current_mute, None)
    return not current_mute

def main():
    print("=" * 60)
    print("        AUDIO MUTE CONTROLLER")
    print("=" * 60)
    print("\nScanning for programs with audio...\n")
    
    while True:
        programs = get_audio_sessions()
        
        if not programs:
            print("No programs with audio found.")
            print("Make sure some programs are playing audio.")
            input("\nPress Enter to refresh or Ctrl+C to exit...")
            continue
        
        selected = select_program(programs)
        
        if selected is None:
            print("\nExiting...")
            break
        elif selected == 'refresh':
            continue
        
        # Control mode
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print("        AUDIO MUTE CONTROLLER")
        print("=" * 60)
        print(f"\nControlling: {selected['name']}")
        print(f"PID: {selected['pid']}")
        
        muted = selected['volume'].GetMute()
        print(f"Current status: {'MUTED' if muted else 'UNMUTED'}")
        
        print("\n" + "-" * 60)
        print("  Press 'M' to toggle mute/unmute")
        print("  Press 'START' to go back to program selection")
        print("  Press 'END' to exit")
        print("-" * 60)
        
        running = True
        while running:
            try:
                # Check if the process still exists
                try:
                    current_mute = selected['volume'].GetMute()
                except:
                    print(f"\n{selected['name']} is no longer available.")
                    input("Press Enter to go back to selection...")
                    break
                
                # Wait for key press
                event = keyboard.read_event(suppress=False)
                
                if event.event_type == keyboard.KEY_DOWN:
                    if event.name == 'm':
                        new_state = toggle_mute(selected)
                        status = "MUTED" if new_state else "UNMUTED"
                        print(f"\r  >> {selected['name']} is now {status}          ", end='')
                    
                    elif event.name == 'home':
                        print("\nReturning to program selection...")
                        running = False
                    
                    elif event.name == 'end':
                        print("\n\nExiting...")
                        return
                        
            except KeyboardInterrupt:
                print("\n\nExiting...")
                return

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...")
    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure you're running this script as Administrator")
        print("if you encounter permission issues.")
        input("\nPress Enter to exit...")
