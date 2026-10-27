import sys


def main():
    # Kullanıcı hiç komut yazmadıysa
    if len(sys.argv) < 2:
        print("Kullanim: python task_cli.py <komut> [argumanlar]")
        return

    command = sys.argv[1]

    if command == "add":
        print("add komutu calisti")
    elif command == "list":
        print("list komutu calisti")
    else:
        print(f"Bilinmeyen komut: {command}")


if __name__ == "__main__":
    main()