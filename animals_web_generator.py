import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def main():
    animals = load_data("animals_data.json")

    # 1) Template oku
    with open("animals_template.html", "r", encoding="utf-8") as f:
        template_html = f.read()


    output = ""

    for animal in animals:
        output += '<li class="cards__item">\n'

        if "name" in animal:
            output += f"Name: {animal['name']}<br/>\n"

        characteristics = animal.get("characteristics", {})

        if "diet" in characteristics:
            output += f"Diet: {characteristics['diet']}<br/>\n"

        if "locations" in animal and animal["locations"]:
            output += f"Location: {animal['locations'][0]}<br/>\n"

        if "type" in characteristics:
            output += f"Type: {characteristics['type']}<br/>\n"

        output += "</li>\n"


    final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", output)


    with open("animals.html", "w", encoding="utf-8") as f:
        f.write(final_html)

    print("animals.html başarıyla oluşturuldu")


if __name__ == "__main__":
    main()
