import json
import os
import sys
from typing import Dict, List

# Configuration parameters
INPUT_BUNDLE_PATH = "Example ValueSets from OCL Staging.json"
OUTPUT_DIRECTORY = "C:/Users/jamlung/Documents/GitHub/WHO-SMART-Guidelines/FHIR Bundle Parser/"

def process_fhir_bundle(bundle_path: str, output_dir: str) -> None:
    """
    Process a FHIR R4 bundle and save individual resources as JSON files.

    Args:
    bundle_path (str): Path to the FHIR bundle JSON file
    output_dir (str): Directory to save individual resource JSON files
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Read the FHIR bundle
    try:
        with open(bundle_path, 'r') as f:
            bundle = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file {bundle_path} was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: The file {bundle_path} is not a valid JSON file.")
        return

    # Ensure it's a FHIR bundle
    if bundle.get('resourceType') != 'Bundle':
        print("Error: The provided JSON is not a FHIR bundle")
        return

    # Process each entry in the bundle
    for entry in bundle.get('entry', []):
        resource = entry.get('resource')
        if resource:
            resource_type = resource.get('resourceType')
            resource_id = resource.get('id')

            if resource_type and resource_id:
                filename = f"{resource_type}_{resource_id}.json"
                file_path = os.path.join(output_dir, filename)

                # Save the resource as a JSON file
                with open(file_path, 'w') as f:
                    json.dump(resource, f, indent=2)
                print(f"Saved {filename}")

    print(f"Processing complete. Output saved to {output_dir}")

if __name__ == "__main__":
    # Use command-line arguments if provided, otherwise use the configured paths
    input_path = sys.argv[1] if len(sys.argv) > 1 else INPUT_BUNDLE_PATH
    output_dir = sys.argv[2] if len(sys.argv) > 2 else OUTPUT_DIRECTORY

    print(f"Processing FHIR bundle: {input_path}")
    print(f"Output directory: {output_dir}")

    process_fhir_bundle(input_path, output_dir)