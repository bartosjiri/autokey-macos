# AutoKey scripts for macOS-like shortcuts
A collection of scripts for Autokey that emulate macOS style keyboard shortcuts in Linux and X11.

## Included shortcuts
Command | Key combination
--- | ---
Copy | <kbd>cmd</kbd>+<kbd>c</kbd>
Cut | <kbd>cmd</kbd>+<kbd>x</kbd>
Find | <kbd>cmd</kbd>+<kbd>f</kbd>
Go to | <kbd>cmd</kbd>+<kbd>l</kbd>
New | <kbd>cmd</kbd>+<kbd>n</kbd>
New tab | <kbd>cmd</kbd>+<kbd>t</kbd>
Paste | <kbd>cmd</kbd>+<kbd>v</kbd>
Quit | <kbd>cmd</kbd>+<kbd>q</kbd>
Redo | <kbd>cmd</kbd>+<kbd>shift</kbd>+<kbd>z</kbd>
Replace | <kbd>cmd</kbd>+<kbd>r</kbd>
Save | <kbd>cmd</kbd>+<kbd>s</kbd>
Select all | <kbd>cmd</kbd>+<kbd>a</kbd>
Undo | <kbd>cmd</kbd>+<kbd>z</kbd>

*Note: Commands can have different actions across various applications.*


## How to use
1. Install AutoKey using your package manager or following [AutoKey installation](https://github.com/autokey/autokey#installation) instructions.

2. Clone or download the provided scripts folder to `~/.config/autokey/data/`.


3. Modify individual scripts in AutoKey to prevent an interference with default terminal shortcuts:

   Replace the `'xfce4-terminal.Xfce4-terminal'` part with the terminal class name of your choice.

   *To get the class name, open terminal, then open AutoKey, click on `Window Filter -> Detect Window Properties -> click on terminal window` and AutoKey will show you the name as Window class. Don't forget to cancel the Window Filter settings.*  

4. Enable AutoKey at login: `AutoKey -> Edit -> Preferences -> Automatically start Autokey at login`.


## Limitations
- Copy & paste in terminals are troublesome, since custom shortcuts can interfere with default terminal shortcut. While the provided scripts provide a workaround for this, you won't be able to use these in built-in terminals (i.e. VS Code).
