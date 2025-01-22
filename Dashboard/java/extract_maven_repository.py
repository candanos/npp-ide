import os
import shutil
from pathlib import Path
import argparse
from packaging import version
import re

def get_version_from_filename(filename):
    """Extract version number from filename using regex."""
    # Match version patterns like: 1.2.3, 1.2.3.Final, 1.2.3-SNAPSHOT, etc.
    version_pattern = r'[\d.]+(?:[-.](?:RELEASE|FINAL|SNAPSHOT|Alpha|Beta|RC\d*|M\d+|GA))?'
    match = re.search(version_pattern, filename, re.IGNORECASE)
    if match:
        try:
            # Clean up version string to make it compatible with packaging.version
            ver_str = match.group(0)
            # Replace non-numeric endings with standard pre-release syntax
            ver_str = re.sub(r'[-.]SNAPSHOT', 'a0', ver_str, flags=re.IGNORECASE)
            ver_str = re.sub(r'[-.]RELEASE|[-.]FINAL|[-.]GA', '', ver_str, flags=re.IGNORECASE)
            ver_str = re.sub(r'[-.]Alpha', 'a', ver_str, flags=re.IGNORECASE)
            ver_str = re.sub(r'[-.]Beta', 'b', ver_str, flags=re.IGNORECASE)
            ver_str = re.sub(r'[-.]RC(\d*)', lambda m: f'rc{m.group(1) or "0"}', ver_str, flags=re.IGNORECASE)
            ver_str = re.sub(r'[-.]M(\d+)', lambda m: f'a{m.group(1)}', ver_str, flags=re.IGNORECASE)
            return version.parse(ver_str)
        except version.InvalidVersion:
            return version.parse("0.0.0")
    return version.parse("0.0.0")

def find_latest_versions(source_dir):
    """Find the latest version of each unique JAR."""
    jar_versions = {}
    
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.jar'):
                # Get base name without version
                base_name = re.sub(r'-[\d.]+(?:[-.].*)?\.jar$', '.jar', file)
                ver = get_version_from_filename(file)
                full_path = os.path.join(root, file)
                
                if base_name not in jar_versions or ver > jar_versions[base_name][0]:
                    jar_versions[base_name] = (ver, full_path, file)
    
    return jar_versions

def copy_latest_jars(source_dir, dest_dir):
    """Copy only the latest version of each JAR."""
    # Create destination directory if it doesn't exist
    Path(dest_dir).mkdir(parents=True, exist_ok=True)
    
    # Find latest versions
    latest_jars = find_latest_versions(source_dir)
    
    # Copy files
    copied_count = 0
    for base_name, (_, source_path, original_name) in latest_jars.items():
        dest_path = os.path.join(dest_dir, original_name)
        try:
            shutil.copy2(source_path, dest_path)
            copied_count += 1
            print(f"Copied: {original_name}")
        except Exception as e:
            print(f"Error copying {original_name}: {str(e)}")
    
    print(f"\nTotal JAR files copied: {copied_count}")

def main():
    # Get the .m2 repository path
    m2_path = os.path.join(str(Path.home()), '.m2', 'repository')
    destination = r'C:\java\external-jars'
    # Confirm with user
    print(f"Source directory: {m2_path}")
    print(f"Destination directory: {destination}")
    proceed = input("Proceed with copying JAR files? (y/n): ")
    
    if proceed.lower() == 'y':
        copy_latest_jars(m2_path, destination)
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()