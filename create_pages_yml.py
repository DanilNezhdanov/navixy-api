import os

def create_pages_yml(dir_path):
    for root, dirs, files in os.walk(dir_path):
        print(f"Scanning {root}...")  # Debug message to see which directory is being processed
        # Check if .pages.yml exists in the current directory
        if '.pages.yml' not in files:
            print(f"Creating .pages.yml in {root}")  # Debug message to confirm creation
            # Create .pages.yml file
            with open(os.path.join(root, '.pages.yml'), 'w') as yml_file:
                yml_file.write("nav:\n")
                for file in files:
                    if file.endswith('.md'):
                        yml_file.write(f"  - {file.replace('.md', '').replace('_', ' ').title()}: {file}\n")
                for dir in dirs:
                    yml_file.write(f"  - {dir.replace('_', ' ').title()}: {dir}\n")
            print(f"Created .pages.yml in {root}")

# Set the path to your documentation root directory
doc_root = os.path.expanduser('~/IdeaProjects/navixy-api/docs')
create_pages_yml(doc_root)