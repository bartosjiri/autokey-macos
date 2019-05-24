if window.get_active_class() != 'xfce4-terminal.Xfce4-terminal':
    keyboard.send_keys("<ctrl>+v")
else:
    keyboard.send_keys("<ctrl>+<shift>+v")