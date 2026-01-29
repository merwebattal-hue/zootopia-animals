import json
from jinja2 import Template

# JSON verisini oku
with open("animals_data.json", "r", encoding="utf-8") as f:
    animals = json.load(f)

# HTML template'i oku
with open("animals_template.html", "r", encoding="utf-8") as f:
    template_content = f.read()

template = Template(template_content)

# Template'i JSON ile doldur
rendered_html = template.render(animals=animals)

# Çıktıyı yaz
with open("animals.html", "w", encoding="utf-8") as f:
    f.write(rendered_html)

print("animals.html başarıyla oluşturuldu")
