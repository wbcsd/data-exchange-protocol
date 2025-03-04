import sys
import yaml
import logging
import json
import jsonref
import jsonschema 
import urllib.parse

# Show the difference between the two OpenAPI files. Only show the differences in the data model.
# For a given type, create a list of properties which are new, removed, or changed.
# For properties which are changed, show the old and new values.
# For properties which are new, show the new value.

def load_openapi_file(path):
    with open(path, encoding="utf-8") as file:
        schema = yaml.safe_load(file)
    schema = jsonref.replace_refs(schema, merge_props=True, proxies=False)
    return schema

def dump_schema(schema):
    return yaml.safe_dump(schema)

def navigate_to(schema, path):
    # Iterate over the parts and select the item from the schema
    for part in path.split('/'):
        part = urllib.parse.unquote(part)
        schema = schema[part]
    return schema


def validate_json_data(schema_path, data_path):
    """
    Validates JSON data against a specified schema.
    Args:
        schema_path (str): The path to the schema file, including an internal path separated by '#'.
        data_path (str): The path to the JSON data file to be validated.
    Raises:
        jsonschema.exceptions.ValidationError: If the JSON data does not conform to the schema.
        FileNotFoundError: If the schema or data file cannot be found.
        json.JSONDecodeError: If the data file contains invalid JSON.
    Example:
        validate_json_data('schema.yaml#/components/schemas/ExampleSchema', 'data.json')
    """

    # Split the schema into file and internal path filename + '#' + internal path
    schema_path, schema_internal_path = schema_path.split('#')

    # Load the schema from the file
    schema = load_openapi_file(schema_path)

    # Load the data to be validated from the file
    logging.info(f"Validating {data_path} against {schema_path}#{schema_internal_path}")
    with open(data_path, 'r') as file:
        data = json.load(file)
    
    # Get the relevant part in the schema
    schema = navigate_to(schema, schema_internal_path)
    # Validate the data against the schema
    jsonschema.validate(instance=data, schema=schema)


def get_data_models(openapi_spec):
    return openapi_spec.get('components', {}).get('schemas', {})

def compare_properties(old_props, new_props):
    new_props = {k: v for k, v in new_props.items() if not v.get('obsolete')}
    old_props = {k: v for k, v in old_props.items() if not v.get('obsolete')}

    old_keys = set(old_props.keys())
    new_keys = set(new_props.keys())
    
    added = new_keys - old_keys
    removed = old_keys - new_keys
    common = old_keys & new_keys
    
    changes = {}
    for key in common:
        if old_props[key].get('type') != new_props[key].get('type') or \
           old_props[key].get('obsolete') != new_props[key].get('obsolete'):
        # if old_props[key] != new_props[key]:
            changes[key] = {'old': old_props[key], 'new': new_props[key]}
    
    return {
        'added': {key: new_props[key] for key in added},
        'removed': {key: old_props[key] for key in removed},
        'changed': changes
    }

def compare_data_models(old_models, new_models):
    old_keys = set(old_models.keys())
    new_keys = set(new_models.keys())
    
    added = new_keys - old_keys
    removed = old_keys - new_keys
    common = old_keys & new_keys
    
    changes = {}
    for key in common:
        changes[key] = compare_properties(old_models[key].get('properties', {}), new_models[key].get('properties', {}))
    
    return {
        'added': {key: new_models[key] for key in added},
        'removed': {key: old_models[key] for key in removed},
        'changed': changes
    }

def schema_diff(old_file_path, new_file_path):
    old_spec = load_openapi_file(old_file_path)
    new_spec = load_openapi_file(new_file_path)
    
    old_models = get_data_models(old_spec)
    new_models = get_data_models(new_spec)
    
    differences = compare_data_models(old_models, new_models)
    
    print(yaml.dump(differences, default_flow_style=False))

    def summary(diffs, level = 0):
        indent = " " * (level * 2)
        if not 'added' in diffs and not 'removed' in diffs and not 'changed' in diffs:
            return
        for key,item in diffs['added'].items():
            print(f"{indent}Added: {key}")
            if item.get('properties'):
                for prop in item.get('properties'):
                    print(f"  {prop}")
        for key,item in diffs['removed'].items():
            print(f"{indent}Removed: {key}")
            if item.get('properties'):
                for prop in item.get('properties'):
                    print(f"  {prop}")
        for key,item in diffs['changed'].items():
            print(f"{indent}Changed: {key}")
            summary(item, level + 1)
        
    summary(differences)
        

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff.py <old_openapi_file> <new_openapi_file>")
        sys.exit(1)
    
    old_file_path = sys.argv[1]
    new_file_path = sys.argv[2]
    
    schema_diff(old_file_path, new_file_path)