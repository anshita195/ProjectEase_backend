import secrets


def generate_unique_colour():
    color = '#'+secrets.token_hex(3)
    return color