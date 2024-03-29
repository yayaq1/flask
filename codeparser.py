from tree_sitter import Language, Parser

# Load the Tree-sitter Python grammar
Language.build_library(
    # Store the library in the `build` directory
    'tree-sitter-python/build/my-languages.so',
    # Include the path to the Python grammar repository
    ['tree-sitter-python']
)

PYTHON_LANGUAGE = Language('tree-sitter-python/build/my-languages.so', 'python')
parser = Parser()
parser.set_language(PYTHON_LANGUAGE)

# Example: Parse a single Python file from Flask
with open('src/flask/app.py', 'rb') as file:
    source_code = file.read()

tree = parser.parse(source_code)
root_node = tree.root_node
print(root_node.sexp())
