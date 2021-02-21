import secrets


def generate_shortcode(selection_list: list):
    while True:
        code = secrets.token_urlsafe(8)
        if code not in selection_list:
            break
        continue
    return code
