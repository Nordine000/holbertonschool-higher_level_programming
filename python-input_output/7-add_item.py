#!/usr/bin/python3
"""
ajout d'arg a une liste python et enregistre dans un fcihier
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file = "add_item.json"

try:
    listes = load_from_json_file(file)
except FileNotFoundError:
    listes = []

listes.extend(sys.argv[1:])
save_to_json_file(listes, file)
