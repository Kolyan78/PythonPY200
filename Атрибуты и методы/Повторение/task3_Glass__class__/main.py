class Glass:
    ...


if __name__ == "__main__":
    glass = Glass()

    print(type(glass))
    print(glass.__class__)

    print(type(glass) == glass.__class__)
