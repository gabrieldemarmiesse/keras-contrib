import os

strings_to_replace = [('import keras', 'import tensorflow.python.keras'),
                      ('from keras.', 'from tensorflow.python.keras.'),
                      ('from keras import', 'from tensorflow.python.keras import')]


def replace_imports(file_path):
    if not file_path.endswith('.py') or file_path.endswith('convert_imports.py'):
        return
    with open(file_path, 'r') as f:
        text = f.read()

    for str_to_replace, str_to_insert in strings_to_replace:
        text = text.replace(str_to_replace, str_to_insert)

    with open(file_path, 'w+') as f:
        f.write(text)


if __name__ == '__main__':
    for root, dirs, files in os.walk("."):
        for name in files:
            replace_imports(os.path.join(root, name))
