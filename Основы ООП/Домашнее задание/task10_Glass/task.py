class Glass:
    def __init__(self, material: str):
        self.material = material

    def get_material(self):
        return self.material


if __name__ == "__main__":
    glass = Glass("glass")
    print(glass.get_material())


