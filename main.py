""" program reverses a string """
#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Nov 2022


def reverse_string(string: str) -> str:
    if string == "":
        return string
    else:
        return reverse_string(string[1:]) + string[0]


def main() -> None:
    a_string = input("Please input a string to reverse: ")

    print("")
    print(f"The original string is: {a_string}")
    print(f"The reversed string is: {reverse_string(a_string)}")

    print("\nDone")


if __name__ == "__main__":
    main()
