"""
Peach Head Man - PNG Image Generator (using only built-in libraries)
Creates a PNG image without requiring any external installations
"""

import struct
import zlib

def create_png_image(filename="peach_head_man.png", width=400, height=600):
    """
    Generate a PNG image of the Peach Head Man character using only built-in libraries
    """
    
    # Create pixel data (RGB, 3 bytes per pixel)
    pixels = []
    
    # Define colors (RGB tuples)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    PEACH = (255, 218, 185)
    DARK_PEACH = (205, 140, 100)
    YELLOW = (255, 223, 0)
    BLUE = (65, 105, 225)
    
    # Create a white background
    for y in range(height):
        row = []
        for x in range(width):
            # Head circle (center at 200, 80, radius 50)
            dx, dy = x - 200, y - 80
            dist_head = (dx*dx + dy*dy) ** 0.5
            
            if dist_head <= 50:
                # Check if outline or fill
                if dist_head >= 48:
                    row.extend(DARK_PEACH)
                else:
                    row.extend(PEACH)
            # Eyes
            elif (180 <= x <= 186 and 64 <= y <= 76):  # Left eye area
                if ((x-183)**2 + (y-70)**2) <= 36:
                    if ((x-183)**2 + (y-70)**2) <= 9:
                        row.extend(WHITE)
                    else:
                        row.extend(BLACK)
                else:
                    row.extend(WHITE)
            elif (214 <= x <= 226 and 64 <= y <= 76):  # Right eye area
                if ((x-220)**2 + (y-70)**2) <= 36:
                    if ((x-220)**2 + (y-70)**2) <= 9:
                        row.extend(WHITE)
                    else:
                        row.extend(BLACK)
                else:
                    row.extend(WHITE)
            # Body (yellow rectangle)
            elif 160 <= x <= 240 and 135 <= y <= 215:
                if x == 160 or x == 240 or y == 135 or y == 215:
                    row.extend(BLACK)
                else:
                    row.extend(YELLOW)
            # Left arm
            elif 90 <= x <= 160 and 155 <= y <= 175:
                if y == 155 or y == 175 or x == 90 or x == 160:
                    row.extend(DARK_PEACH)
                else:
                    row.extend(PEACH)
            # Right arm
            elif 240 <= x <= 310 and 155 <= y <= 175:
                if y == 155 or y == 175 or x == 240 or x == 310:
                    row.extend(DARK_PEACH)
                else:
                    row.extend(PEACH)
            # Left leg
            elif 175 <= x <= 200 and 215 <= y <= 315:
                if x == 175 or x == 200 or y == 215:
                    row.extend(BLACK)
                elif y == 315:
                    row.extend(BLACK)
                else:
                    row.extend(BLUE)
            # Right leg
            elif 200 <= x <= 225 and 215 <= y <= 315:
                if x == 200 or x == 225 or y == 215:
                    row.extend(BLACK)
                elif y == 315:
                    row.extend(BLACK)
                else:
                    row.extend(BLUE)
            else:
                row.extend(WHITE)
        
        pixels.append(bytes(row))
    
    # Write PNG file
    write_png(filename, width, height, pixels)
    print(f"✅ PNG Image created: {filename}")
    print(f"You can now view {filename} with any image viewer!")


def write_png(filename, width, height, pixels):
    """Write PNG file with minimal PNG format implementation"""
    
    def png_chunk(chunk_type, data):
        """Create a PNG chunk"""
        chunk_len = struct.pack('>I', len(data))
        chunk_data = chunk_type + data
        chunk_crc = struct.pack('>I', zlib.crc32(chunk_data) & 0xffffffff)
        return chunk_len + chunk_data + chunk_crc
    
    # PNG signature
    png_signature = b'\x89PNG\r\n\x1a\n'
    
    # IHDR chunk (image header)
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)  # 8-bit RGB
    ihdr = png_chunk(b'IHDR', ihdr_data)
    
    # IDAT chunk (image data)
    raw_data = b''
    for row in pixels:
        raw_data += b'\x00' + row  # Filter type 0 (None) for each row
    
    compressed_data = zlib.compress(raw_data, 9)
    idat = png_chunk(b'IDAT', compressed_data)
    
    # IEND chunk (image end)
    iend = png_chunk(b'IEND', b'')
    
    # Write to file
    with open(filename, 'wb') as f:
        f.write(png_signature)
        f.write(ihdr)
        f.write(idat)
        f.write(iend)


if __name__ == "__main__":
    create_png_image()
