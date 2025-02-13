import os
import sys
import yaml
import json
import jsonref

# Show the difference between the two OpenAPI files. Only show the differences in the data model.
# For a given type, create a list of properties which are new, removed, or changed.
# For properties which are changed, show the old and new values.
# For properties which are new, show the new value.

def load_openapi_file(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

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
    
    #print(json.dumps(differences, indent=2))
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
    
    main(old_file_path, new_file_path)