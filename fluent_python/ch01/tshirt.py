colors = ["black", "red", "white", "yellow"]
sizes = ["xs", "s", "m", "l", "xl"]
materials = ["cotton", "plastic"]

tshirts = [(color, size, material) for color in colors for size in sizes for material in materials]
print(tshirts)
