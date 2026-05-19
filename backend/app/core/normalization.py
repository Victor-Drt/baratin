import re
import unicodedata


def normalize_product_name(name: str) -> str:
    name = name.lower().strip()

    name = unicodedata.normalize("NFKD", name)
    name = "".join(c for c in name if not unicodedata.combining(c))

    name = re.sub(r"[^a-z0-9\s]", "", name)

    return name