import pygame

# Function to clip a portion of an image
def clip(img, x, y, x_size, y_size):
    # Copy the image
    handle_img = img.copy()
    # Create a rectangular clip region
    clipR = pygame.Rect(x, y, x_size, y_size)
    # Set the clip region
    handle_img.set_clip(clipR)
    # Extract the clipped portion of the image
    image = img.subsurface(handle_img.get_clip())
    # Return the clipped portion as a separate image
    return image.copy()

# Class for handling fonts
class Font():
    def __init__(self, path, size):
        # Space between letters
        self.spacing = 1
        # List of characters in the image ordered in the order they appear in the image
        self.character_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', '-', ',', ':', '+', '\'', '!', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '/', '_', '=', '\\', '[', ']', '*', '"', '<', '>', ';']
        # Load font image
        font_img = pygame.image.load(path).convert()
        font_img.set_colorkey((0,0,0))
        current_char_width = 0
        self.characters = {}
        character_count = 0
        # Check for letter borders which are grey and have a red value of 127
        for x in range(font_img.get_width()):
            c = font_img.get_at((x, 0))
            if c[0] == 127:
                # Clip the image and add it to the dictionary
                char_img = clip(font_img, x - current_char_width, 0, current_char_width, font_img.get_height())
                self.characters[self.character_order[character_count]] = char_img.copy()
                character_count += 1
                current_char_width = 0
            else:
                current_char_width += 1
        # Set the space character's width to the width of the letter A
        self.space_width = self.characters['A'].get_width()
        self.size = size
        
    # Render text on the screen
    def render(self, surf, text, loc,custom_border=None):
        x_offset = 0
        y_offset = 0
        for char in text:
            if char != ' ' and char != '*' and char != '\n':
                # If close to the edge of the screen, move to the next line
                if custom_border == None:
                    if x_offset + loc[0] >= surf.get_width() - 50:
                        x_offset = 0
                        y_offset += (self.characters[char].get_height() * self.size) + 5
                else:
                    if x_offset + loc[0] >= custom_border:
                        x_offset = 0
                        y_offset += (self.characters[char].get_height() * self.size) + 5
                # Render character at specified location
                surf.blit(pygame.transform.scale(self.characters[char], (self.characters[char].get_width() * self.size, self.characters[char].get_height() * self.size)), (loc[0] + x_offset, loc[1] + y_offset))
                # Update x offset for next character
                x_offset += self.characters[char].get_width() * self.size + self.spacing * self.size
            # For space character, update x offset accordingly
            elif char == ' ':
                x_offset += self.space_width * self.size + self.spacing
            # '*' acts as enter to skip to the next line
            elif char == '*' or char == '\n':
                x_offset = 0
                y_offset += (self.characters['A'].get_height() * self.size) + 5
    
    # Get the rect of rendered text
    def rect(self, surf, text, loc):
        x_offset = 0
        y_offset = 0
        for char in text:
            if char != ' ' and char != '*':
                if x_offset + loc[0] >= surf.get_width() - 50:
                    x_offset = 0
                    y_offset += (self.characters[char].get_height() * self.size) + 5  
                # Update x offset for next character
                x_offset += self.characters[char].get_width() * self.size + self.spacing
            elif char == ' ':
                # For space character, update x offset accordingly
                x_offset += self.space_width * self.size + self.spacing
            elif char == '*' or char == '\n':
                x_offset = 0
                y_offset += (self.characters['A'].get_height() * self.size) + 5                
        # Return rect of rendered text
        return pygame.Rect(loc[0], loc[1], x_offset + self.characters['A'].get_width() * self.size, y_offset + self.characters['A'].get_height() * self.size)
