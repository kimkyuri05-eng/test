"""
Peach Head Man - SVG Image Generator
Creates an SVG image of the LEGO-like Peach Head Man (no external libraries needed!)
"""

def create_peach_head_man_svg(filename="peach_head_man.svg"):
    """
    Generate an SVG image of the Peach Head Man character
    """
    svg_content = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="400" height="600" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="400" height="600" fill="white"/>
  
  <!-- HEAD (Peach Circle) -->
  <circle cx="200" cy="80" r="50" fill="#FFDAB9" stroke="#8B6F47" stroke-width="3"/>
  
  <!-- LEFT EYE -->
  <circle cx="180" cy="70" r="6" fill="black"/>
  <circle cx="182" cy="68" r="3" fill="white"/>
  
  <!-- RIGHT EYE -->
  <circle cx="220" cy="70" r="6" fill="black"/>
  <circle cx="222" cy="68" r="3" fill="white"/>
  
  <!-- SMILE (Arc) -->
  <path d="M 175 85 Q 200 100 225 85" stroke="black" stroke-width="3" fill="none" stroke-linecap="round"/>
  
  <!-- BODY (Yellow Rectangle) -->
  <rect x="160" y="135" width="80" height="80" fill="#FFDF00" stroke="black" stroke-width="3"/>
  
  <!-- BUTTON 1 -->
  <circle cx="200" cy="155" r="5" fill="black"/>
  
  <!-- BUTTON 2 -->
  <circle cx="200" cy="185" r="5" fill="black"/>
  
  <!-- LEFT ARM (Peach) -->
  <rect x="90" y="155" width="70" height="20" fill="#FFDAB9" stroke="#8B6F47" stroke-width="2" rx="5"/>
  
  <!-- RIGHT ARM (Peach) -->
  <rect x="240" y="155" width="70" height="20" fill="#FFDAB9" stroke="#8B6F47" stroke-width="2" rx="5"/>
  
  <!-- LEFT LEG (Blue) -->
  <rect x="175" y="215" width="25" height="100" fill="#4169E1" stroke="black" stroke-width="2"/>
  
  <!-- RIGHT LEG (Blue) -->
  <rect x="200" y="215" width="25" height="100" fill="#4169E1" stroke="black" stroke-width="2"/>
  
  <!-- LEFT SHOE (Black) -->
  <rect x="175" y="315" width="25" height="15" fill="black"/>
  
  <!-- RIGHT SHOE (Black) -->
  <rect x="200" y="315" width="25" height="15" fill="black"/>
  
  <!-- TITLE -->
  <text x="200" y="560" font-size="24" font-weight="bold" text-anchor="middle" fill="black">PEACH HEAD MAN</text>
</svg>
'''
    
    with open(filename, 'w') as f:
        f.write(svg_content)
    
    print(f"✅ SVG Image created: {filename}")
    print(f"Open {filename} in any web browser to view your Peach Head Man!")


if __name__ == "__main__":
    create_peach_head_man_svg()
