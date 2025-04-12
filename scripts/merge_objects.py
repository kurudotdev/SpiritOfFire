import os
import xml.etree.ElementTree as ET
import argparse

def merge_objects(folder_path, output_path):
    root = ET.Element("Objects")

    for filename in sorted(os.listdir(folder_path)):
        if not filename.endswith(".xml"):
            continue
        if not filename.startswith("objects-"):
            continue

        file_path = os.path.join(folder_path, filename)
        try:
            tree = ET.parse(file_path)
            for obj in tree.getroot():
                root.append(obj)
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

    tree = ET.ElementTree(root)
    tree.write(output_path, encoding="utf-8", xml_declaration=True)
    print(f"Merged to: {output_path}")

def main(data_path):
    folder_path = os.path.join(data_path, ".objects")
    output_path = os.path.join(data_path, "objects.xml")

    if not os.path.exists(folder_path):
        print(f"No .objects folder found at: {folder_path}")
        return

    merge_objects(folder_path, output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge .objects/*.xml into objects.xml")
    parser.add_argument("--data-path", type=str, required=True, help="Path to ModData/data")
    args = parser.parse_args()
    main(args.data_path)
