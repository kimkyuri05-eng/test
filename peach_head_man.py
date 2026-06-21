"""
Peach Head Man - A LEGO-like character creation script
"""

class PeachHeadMan:
    """A simple LEGO-style Peach Head Man character"""
    
    def __init__(self, name="Peach Head", color="peach"):
        self.name = name
        self.color = color
        self.head = self.create_head()
        self.body = self.create_body()
        self.arms = self.create_arms()
        self.legs = self.create_legs()
    
    def create_head(self):
        """Create the peach-colored head"""
        return {
            "shape": "sphere",
            "color": self.color,
            "size": "small",
            "features": ["eyes", "smile"]
        }
    
    def create_body(self):
        """Create the torso"""
        return {
            "shape": "cylinder",
            "color": "yellow",
            "size": "medium",
            "parts": ["chest", "waist"]
        }
    
    def create_arms(self):
        """Create the arms"""
        return {
            "left": {"shape": "cylinder", "color": "peach", "size": "small"},
            "right": {"shape": "cylinder", "color": "peach", "size": "small"}
        }
    
    def create_legs(self):
        """Create the legs"""
        return {
            "left": {"shape": "cylinder", "color": "blue", "size": "small"},
            "right": {"shape": "cylinder", "color": "blue", "size": "small"}
        }
    
    def display(self):
        """Display the LEGO figure as ASCII art"""
        ascii_art = f"""
        ╔═══════════════╗
        ║      😊      ║  ← Peach Head
        ╚═══════════════╝
             │ │ │
           ──┼─┼─┼──     ← Arms
             │ │ │
        ┌────┴─┴─┴────┐
        │   YELLOW    │  ← Body
        │   TORSO     │
        └────┬─┬─┬────┘
           ││││││││││
           ││││││││││  ← Blue Legs
           ││││││││││
        """
        return ascii_art
    
    def __str__(self):
        return f"{self.name} - {self.color.upper()} HEAD MAN\n{self.display()}"


# Create a peach head man
if __name__ == "__main__":
    peach_man = PeachHeadMan(name="Peachy", color="peach")
    print(peach_man)
    print("\nCharacter Details:")
    print(f"Head: {peach_man.head}")
    print(f"Body: {peach_man.body}")
    print(f"Arms: {peach_man.arms}")
    print(f"Legs: {peach_man.legs}")
