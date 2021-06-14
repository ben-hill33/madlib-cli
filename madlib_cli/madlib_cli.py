import re

def read_template(path):

    with open(path) as f:
        return f.read().strip()


def parse_template(template):

    stripped = ""
    parts = []
    current_part = ""
    capturing_part = False

    for ch in template:

        if ch == "{":
            stripped += ch
            capturing_part = True
            current_part = ""
        elif ch == "}":
            stripped += ch
            capturing_part = False
            parts.append(current_part)
        elif capturing_part:
            current_part += ch
        else:
            stripped += ch

    return stripped, tuple(parts)

def parse_template_alt_regex(template):

    pattern = r"(?<=\{).[^\}]+"
    parts = tuple(re.findall(pattern, template))
    stripped = re.sub(pattern, "", template)

    return stripped, parts

def merge(stripped_template, parts):
    return stripped_template.format(*parts)


def collect_input(parts):
    responses = []
    for part in parts:
        response = input(f"Enter a {part} ")
        responses.append(response)

    return responses


def save_madlib(merged, path):
    with open(path, "w") as f:
        f.write(merged)


def main(path):
    print("MadLib CLI edition!")

    template = read_template(path)

    stripped, parts = parse_template(template)

    responses = collect_input(parts)

    merged = merge(stripped, responses)

    print(merged)

    out_path = path.replace(".txt", ".completed.txt")

    save_madlib(merged, out_path)


if __name__ == "__main__":
    path = "assets/dark_and_stormy_night.txt"
    main(path)