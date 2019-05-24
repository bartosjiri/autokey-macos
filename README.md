# AutoKey scripts for macOS-like shortcuts
A collection of scripts for Autokey that emulate macOS style keyboard shortcuts in Linux and X11.


## How to use
1. Install AutoKey using your package manager or following [AutoKey installation](https://github.com/autokey/autokey#installation) instructions.

2. Download one of the provided script folders to `~/.config/autokey/data/` depending on your settings:
- If you are using default Linux keyboard settings (where <kbd>ctrl</kbd> is `<ctrl>` and <kbd>cmd</kbd> is `<super>`), select `macos-default`.
- If you are using modified keyboard settings (i.e. where <kbd>ctrl</kbd> is `<super>` and <kbd>cmd</kbd> is `<ctrl>`), select `macos-switched`.

3. Modify individual scripts in AutoKey to prevent an interference with default terminal shortcuts:

   Replace the `'xfce4-terminal.Xfce4-terminal'` part with the terminal emulator of your choice.

   *To get the exact name, open terminal, open AutoKey, click on `Window Filter -> Detect Window Properties -> click on terminal window` and AutoKey will show you the name as Window class. Don't forget to cancel the Window Filter settings.*  

4. Enable AutoKey at login: `AutoKey -> Edit -> Preferences -> Automatically start Autokey at login`.


## Limitations
- Copy & paste in terminals are troublesome, since custom shortcuts can interfere with default terminal shortcut. While the provided scripts provide a workaround for this, you won't be able to use these in built-in terminals (i.e. VS Code).
