import re
import urllib.parse
import urllib.request


def get_vid(query):

    try:
        encoded = urllib.parse.quote(query)
