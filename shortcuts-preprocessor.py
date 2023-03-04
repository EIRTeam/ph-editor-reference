import json
import sys
import re
from typing import Dict, Any

pattern = re.compile(r"{{(.+)}}\((.+)\)")

def process_item(item: Dict[str, Any], shortcuts):
    if item["Chapter"]:
        m = re.search(pattern, item["Chapter"]["content"])
        
        while m:
            text = m.group(1)
            action = m.group(2)

            bindings = [shortcut["shortcut"] for shortcut in shortcuts if shortcut["action"] == action]
            bindings_text = "Shortcuts: " if len(bindings) >= 2 else "Shortcut: "
            bindings_text += ", ".join(bindings)

            generated_text = f"[{text}](/manual/settings/shortcuts.md '{bindings_text}')"
            item["Chapter"]["content"] = item["Chapter"]["content"][:m.start()] + generated_text + item["Chapter"]["content"][m.end():] 
            
            m = re.match(pattern, item["Chapter"]["content"])
        
        for subitem in item["Chapter"]["sub_items"]:
            process_item(subitem, shortcuts)


if __name__ == '__main__':
    if len(sys.argv) > 1: # we check if we received any argument
        if sys.argv[1] == "supports": 
            # then we are good to return an exit status code of 0, since the other argument will just be the renderer's name
            sys.exit(0)

    # load both the context and the book representations from stdin
    context, book = json.load(sys.stdin)

    # load the shortcuts map
    with open("./src/ShortcutMapper/sources/ph-editor/intermediate/ph_editor_og_format.json", mode="r") as f:
        shortcuts = json.load(f)

        for item in book["sections"]:
            process_item(item, shortcuts)

    # we are done with the book's modification, we can just print it to stdout, 
    print(json.dumps(book))
