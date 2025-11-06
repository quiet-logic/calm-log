#full_name(first,last)

def full_name(first: str, last: str | None = None) -> str:
    """
    Accepts either:
      - first and last name separately, OR
      - a single string containing both names together.
    Cleans punctuation and spacing.
    """

    # Case 1: user passed ONE string with both names
    if last is None:
        # Split into words
        parts = first.replace(",", " ").replace(".", " ").split()

        if len(parts) < 2:
            raise ValueError("Not enough name parts to split full name.")

        # First word is first name, last word is surname
        first = parts[0]
        last = parts[-1]

    # Case 2: user provided first and last separately
    first = first.strip().title()
    last = last.strip().title()

    return f"{first} {last}"

print(full_name(" Sinead", ", Smith "))   
