# AutoKey scripts for macOS-like shortcuts
A collection of scripts for Autokey that emulate macOS style keyboard shortcuts in Linux and X11.


## How to use
There are 2 different script packages available:
- For unmodified command keys layout (where <kbd>ctrl</kbd> outputs `control` and <kbd>cmd</kbd> outputs `super`)
- For modified command keys layout (where <kbd>ctrl</kbd> outputs `super` and <kbd>cmd</kbd> outputs `control`)

   ⮡ Learn how to [modify the layout](aaa).

### Using unmodified command keys layout
1. Install AutoKey using your package manager or following [AutoKey installation](https://github.com/autokey/autokey#installation) instructions.

2. Clone or download the `macOS-default` folder to `~/.config/autokey/data/`.

3. Modify individual scripts in AutoKey to prevent an interference with default terminal shortcuts:

   Replace the `'xfce4-terminal.Xfce4-terminal'` part with the terminal class name of your choice.

   *To get the class name, open terminal, then open AutoKey, click on `Window Filter -> Detect Window Properties -> click on terminal window` and AutoKey will show you the name as Window class. Don't forget to cancel the Window Filter settings.*  

4. Enable AutoKey at login: `AutoKey -> Edit -> Preferences -> Automatically start Autokey at login`.


### Using modified command keys layout
1. Install AutoKey using your package manager or following [AutoKey installation](https://github.com/autokey/autokey#installation) instructions.

2. Unbind AutoKey's configuration hotkey: `AutoKey -> Edit -> Preferences -> Special hotkeys -> Show configuration window using a hotkey -> Clear`

3. Clone or download the `macOS-switched` folder to `~/.config/autokey/data/`.

4. Modify individual scripts in AutoKey to prevent an interference with default terminal shortcuts:

   Replace the `'xfce4-terminal.Xfce4-terminal'` part with the terminal class name of your choice.

   *To get the class name, open terminal, then open AutoKey, click on `Window Filter -> Detect Window Properties -> click on terminal window` and AutoKey will show you the name as Window class. Don't forget to cancel the Window Filter settings.*  

5. Enable AutoKey at login: `AutoKey -> Edit -> Preferences -> Automatically start Autokey at login`.


## Limitations
- Command key input in terminals is troublesome, since macOS uses <kbd>ctrl</kbd> for all terminal operations. While the provided scripts provide a workaround for this, you won't be able to use these in built-in terminals (i.e. VS Code).
