import yaml
import sys
from pathlib import Path

REPLACEMENTS =  { 
    "NegativeOrZeroDecimal": "Decimal",
    "PositiveOrZeroDecimal": "Decimal",
    "PositiveDecimal": "Decimal",
    "PositiveNonZeroDecimal": "Decimal",
    "NegativeDecimal": "Decimal",
    "NonEmptyString": "string",
    "FloatBetween1And3": "number",
    "Percent": "number"
}

ATOMIC_TYPES = {
    "string", "number", "integer", "boolean", "null", "Decimal", "Uri", "Urn"
}

def get_standard_type(type_name: str) -> str:
    return REPLACEMENTS.get(type_name, type_name)

def load_openapi(path: str) -> dict:
    with open(path, encoding="utf-8") as file:
        schema = yaml.safe_load(file)
    return schema

def openapi_to_mermaid(openapi: dict) -> str:
    """Convert OpenAPI schemas to a Mermaid class diagram."""
    schemas = openapi.get("components", {}).get("schemas", {})
    lines = ["classDiagram"]

    for name, schema in schemas.items():
        # Skip non-object schemas (enums, primitives, etc.)
        if schema.get("type") != "object" and "properties" not in schema:
            continue

        lines.append(f"    class {name} {{")
        props = schema.get("properties", {})
        for prop_name, prop in props.items():
            if prop_name == "$ref":
                continue

            prop_type = prop.get("type", "object")
            # handle array types
            if prop_type == "array":
                items = prop.get("items", {})
                item_type = items.get("$ref", items.get("type", "any"))
                if isinstance(item_type, str) and item_type.startswith("#/components/schemas/"):
                    item_type = item_type.split("/")[-1]
                    item_type = get_standard_type(item_type)
                prop_type = f"List[{item_type}]"
            # handle $ref types
            if "$ref" in prop:
                ref_type = prop["$ref"].split("/")[-1]
                prop_type = ref_type

            # Standardize certain types
            prop_type = get_standard_type(prop_type)
            if not (prop_name in schema.get("required", [])):
                prop_type = f"{prop_type}?"
 
            lines.append(f"        {prop_type} {prop_name}")
        lines.append("    }")

    # Add associations for $ref and arrays
    for name, schema in schemas.items():
        if "$ref" in schema:
            base_type = schema["$ref"].split("/")[-1]
            lines.append(f"    {base_type} <|-- {name}")
        props = schema.get("properties", {})
        for prop_name, prop in props.items():
            if prop_name == "$ref":
                continue
            if "$ref" in prop:
                ref_type = prop["$ref"].split("/")[-1]
                ref_type = get_standard_type(ref_type)
                if ref_type not in ATOMIC_TYPES:
                    lines.append(f"    {name} --> {ref_type}")
            elif prop.get("type") == "array" and "$ref" in prop.get("items", {}):
                ref_type = prop["items"]["$ref"].split("/")[-1]
                ref_type = get_standard_type(ref_type)
                if ref_type not in ATOMIC_TYPES:
                    lines.append(f"    {name} --> {ref_type}")

    return "\n".join(lines)

def openapi_to_mermaid_file(input_path: str, output_path: str):
    openapi = load_openapi(input_path)
    mermaid = openapi_to_mermaid(openapi)
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(mermaid)

def main():
    if len(sys.argv) != 3:
        print("Usage: python openapi_to_mermaid.py <openapi.yaml> <output.mmd>")
        sys.exit(1)

    openapi_to_mermaid_file(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()