"""
Peach Head Man - Image Generator
Creates a visual representation of the LEGO-like Peach Head Man
"""

from PIL import Image, ImageDraw

def create_peach_head_man_image(filename="peach_head_man.png", size=(400, 600)):
    """
    Generate an image of the Peach Head Man character
    """
    # Create image with white background
    img = Image.new('RGB', size, color='white')
    draw = ImageDraw.Draw(img)
    
    # Define colors
    peach = (255, 218, 185)
    dark_peach = (205, 140, 100)
    yellow = (255, 223, 0)
    blue = (65, 105, 225)
    black = (0, 0, 0)
    white = (255, 255, 255)
    
    # Center X
    center_x = size[0] // 2
    
    # Draw HEAD (peach colored sphere/circle)
    head_y = 80
    head_radius = 50
    draw.ellipse(
        [center_x - head_radius, head_y - head_radius, 
         center_x + head_radius, head_y + head_radius],
        fill=peach,
        outline=dark_peach,
        width=3
    )
    
    # Draw eyes
    eye_y = head_y - 10
    left_eye_x = center_x - 20
    right_eye_x = center_x + 20
    eye_radius = 6
    
    draw.ellipse([left_eye_x - eye_radius, eye_y - eye_radius,
                  left_eye_x + eye_radius, eye_y + eye_radius],
                 fill=black)
    draw.ellipse([right_eye_x - eye_radius, eye_y - eye_radius,
                  right_eye_x + eye_radius, eye_y + eye_radius],
                 fill=black)
    
    # Draw pupils (white)
    pupil_radius = 3
    draw.ellipse([left_eye_x - pupil_radius + 2, eye_y - pupil_radius + 1,
                  left_eye_x + pupil_radius + 2, eye_y + pupil_radius + 1],
                 fill=white)
    draw.ellipse([right_eye_x - pupil_radius + 2, eye_y - pupil_radius + 1,
                  right_eye_x + pupil_radius + 2, eye_y + pupil_radius + 1],
                 fill=white)
    
    # Draw smile (arc)
    smile_box = [center_x - 25, head_y + 5, center_x + 25, head_y + 25]
    draw.arc(smile_box, start=0, end=180, fill=black, width=3)
    
    # Draw BODY (yellow rectangle)
    body_top = head_y + head_radius + 5
    body_left = center_x - 40
    body_right = center_x + 40
    body_bottom = body_top + 80
    
    draw.rectangle([body_left, body_top, body_right, body_bottom],
                   fill=yellow,
                   outline=black,
                   width=3)
    
    # Draw body details (buttons)
    button_radius = 5
    button_y1 = body_top + 20
    button_y2 = body_top + 50
    
    draw.ellipse([center_x - button_radius, button_y1 - button_radius,
                  center_x + button_radius, button_y1 + button_radius],
                 fill=black)
    draw.ellipse([center_x - button_radius, button_y2 - button_radius,
                  center_x + button_radius, button_y2 + button_radius],
                 fill=black)
    
    # Draw LEFT ARM (peach)
    arm_y = body_top + 20
    arm_width = 30
    arm_height = 20
    
    # Left arm
    left_arm_x = body_left - arm_width
    draw.rectangle([left_arm_x - arm_width, arm_y - arm_height // 2,
                    left_arm_x, arm_y + arm_height // 2],
                   fill=peach,
                   outline=dark_peach,
                   width=2)
    
    # Right arm
    right_arm_x = body_right + arm_width
    draw.rectangle([right_arm_x, arm_y - arm_height // 2,
                    right_arm_x + arm_width, arm_y + arm_height // 2],
                   fill=peach,
                   outline=dark_peach,
                   width=2)
    
    # Draw LEFT LEG (blue)
    leg_width = 25
    leg_height = 100
    left_leg_x = center_x - 25
    
    draw.rectangle([left_leg_x - leg_width // 2, body_bottom,
                    left_leg_x + leg_width // 2, body_bottom + leg_height],
                   fill=blue,
                   outline=black,
                   width=2)
    
    # Draw RIGHT LEG (blue)
    right_leg_x = center_x + 25
    
    draw.rectangle([right_leg_x - leg_width // 2, body_bottom,
                    right_leg_x + leg_width // 2, body_bottom + leg_height],
                   fill=blue,
                   outline=black,
                   width=2)
    
    # Draw shoes (black)
    shoe_height = 15
    draw.rectangle([left_leg_x - leg_width // 2, body_bottom + leg_height,
                    left_leg_x + leg_width // 2, body_bottom + leg_height + shoe_height],
                   fill=black)
    draw.rectangle([right_leg_x - leg_width // 2, body_bottom + leg_height,
                    right_leg_x + leg_width // 2, body_bottom + leg_height + shoe_height],
                   fill=black)
    
    # Add title
    draw.text((center_x - 60, size[1] - 40), "PEACH HEAD MAN", fill=black)
    
    # Save image
    img.save(filename)
    print(f"✅ Image created: {filename}")
    return img


if __name__ == "__main__":
    create_peach_head_man_image()
