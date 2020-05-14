directions = {
    "n": "Go North",
    "e": "Go East",
    "s": "Go South",
    "w": "Go West",
    "q": "Quit"
}

def main_direction():
    for key, value in directions.items():
        print(f'{key}: {value}')