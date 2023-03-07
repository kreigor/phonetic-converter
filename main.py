import argparse
import sys


VERSION = "1.0.0"
NAME = "Phonetic converter"


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        epilog=f"{NAME} version {VERSION})",
        description="This will convert a single word to the phonetic alphabet.",
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"{NAME} version {VERSION}"
    )
    parser.add_argument(
        "word",
        type=str,
        help="Word to convert"
    )

    return parser


def convert(word):
    letter_to_word = {
        'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
        'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India',
        'J': 'Juliette', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November',
        'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra',
        'T': 'Tango',   'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey',
        'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'
    }

    return [letter_to_word[x] for x in [*word.upper()]]


def main() -> None:
    parser = init_argparse()

    if not len(sys.argv) > 1:
        parser.print_help()
        sys.exit(1)
    else:
        args = parser.parse_args()
        word = args.word

        if word.isalpha():
            print(*convert(word))
        else:
            print("Please enter letters only!")


if __name__ == "__main__":
    main()
