import json
from jinja2 import Environment, FileSystemLoader


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def main():
    animals = load_data("animals_data.json")

    # Jinja2 ortamı
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("animals_template.html")

    # HTML üret
    rendered_html = template.render(animals=animals)

    # animals.html yaz
    with open("animals.html", "w", encoding="utf-8") as f:
        f.write(rendered_html)

    print("animals.html başarıyla oluşturuldu")


if __name__ == "__main__":
    main()
