commands = {
    "n": "Go North",
    "e": "Go East",
    "s": "Go South",
    "w": "Go West",
    "q": "Quit"
}

def key_commands():
    for key, value in commands.items():
        print(f'{key}: {value}')