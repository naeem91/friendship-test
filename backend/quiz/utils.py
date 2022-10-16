import string
import secrets

from django.conf import settings


def generate_random_code():
    """
    Generate a short, easy to type link
    e.g, xjv-jho-lqm
    """
    link_length = settings.RANDOM_LINK_LENGTH
    char_set = string.ascii_lowercase 

    random_chars = []
    for i in range(1, link_length + 1):
        char = secrets.choice(char_set)
        if i%3 == 0 and i < link_length:
            char += '-'
        random_chars.append(char)
    
    return ''.join(random_chars)
