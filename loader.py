import os
import re
import yaml
from antlr4 import CommonTokenStream, InputStream
from validator import RootSchema
from SCLangLexer import SCLangLexer
from SCLangParser import SCLangParser
from SCLangVisitor import SCLangVisitor


class Loader(yaml.SafeLoader):
    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        super(Loader, self).__init__(stream)

    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        with open(filename, 'r') as f:
            return yaml.load(f, Loader)

Loader.add_constructor('!include', Loader.include)


def preprocess_imports(input_text, base_dir='', imported_files=None):
    """
    Preprocess the input text, replacing #import statements with the content of the files they refer to.
    Handles recursive imports.

    Args:
    - input_text: The input text containing #import statements.
    - base_dir: The base directory to resolve relative paths for imports.
    - imported_files: A set to track already imported files to avoid recursion.

    Returns:
    - The preprocessed text with #import statements replaced by file content.
    """
    if imported_files is None:
        imported_files = set()

    # Regex to match #import statements
    import_pattern = re.compile(r'#\s*import\s+"?([^"]+)"?')

    # Function to replace each #import with the content of the specified file
    def replace_import(match):
        file_path = match.group(1)  # Extract the file path from the match
        full_path = os.path.join(base_dir, file_path)

        # Avoid importing the same file more than once
        if full_path in imported_files:
            return ''  # Return an empty string if file has already been imported
        imported_files.add(full_path)

        try:
            with open(full_path, 'r') as file:
                file_content = file.read()
                # Recursively process imports within the file
                return preprocess_imports(file_content, base_dir, imported_files)
        except FileNotFoundError:
            print(f"Warning: File not found '{full_path}'. Skipping import.")
            return ''  # Return an empty string if file is not found

    # Replace all #import statements in the input text
    return re.sub(import_pattern, replace_import, input_text)


def load_yaml(yaml_path):
    with open(yaml_path, 'r') as f:
        data = yaml.load(f, Loader)
    validated = RootSchema(**data)
    return validated


def load_script(script_path):
    with open(script_path, 'r') as f:
        in_str = preprocess_imports(f.read())
    input_stream = InputStream(in_str)
    lexer = SCLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SCLangParser(stream)
    tree = parser.script()
    return tree
    vinterp = SCLangVisitor()
    return vinterp.visit(tree)