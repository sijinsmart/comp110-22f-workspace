"""Example of importing Python."""


from lessons import helpers

def main() -> None:
    """Entrypoint of program."""
    #cannot directly use powerful but should include the module's name 
    print(helpers.powerful(2,4))
    print(f"The answer: {helpers.THE_ANSWER}")

if __name__ == "__main__":
    main()