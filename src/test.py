import os


if __name__ == "__main__":
    print(os.environ)
    for name, value in os.environ.items():
        if "github" in name.lower():
            print(f"{name}:{value})"