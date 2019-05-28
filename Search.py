from Extensions import extensions
import os

def run(init_path):
    for dirPath, dirs, files in os.walk(init_path):
        for _file in files:
            path_name = os.path.join(dirPath, _file)
            absolutePath = os.path.abspath(path_name)
            ext = absolutePath.split('.')[-1]

            if ext in extensions:
                yield absolutePath


if __name__ == "__main__":
    result = run(os.path.abspath(os.path.join(os.getcwd(), 'test')))
    for i in result:
        print(i)
