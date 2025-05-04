import argparse
import os
from typing import Dict, List


class ASCIIArtGenerator:
    def __init__(self):
        self.fonts = {
            'standard': {
                'A': ["  A  ", " A A ", "AAAAA", "A   A", "A   A"],
                'B': ["BBBB ", "B   B", "BBBB ", "B   B", "BBBB "],
                'C': [" CCC ", "C   C", "C    ", "C   C", " CCC "],
                'D': ["DDD  ", "D  D ", "D   D", "D  D ", "DDD  "],
                'E': ["EEEEE", "E    ", "EEE  ", "E    ", "EEEEE"],
                'F': ["FFFFF", "F    ", "FFF  ", "F    ", "F    "],
                'G': [" GGG ", "G   G", "G GGG", "G   G", " GGG "],
                'H': ["H   H", "H   H", "HHHHH", "H   H", "H   H"],
                'I': ["IIIII", "  I  ", "  I  ", "  I  ", "IIIII"],
                'J': ["JJJJJ", "   J ", "   J ", "J  J ", " JJ  "],
                'K': ["K   K", "K  K ", "KKK  ", "K  K ", "K   K"],
                'L': ["L    ", "L    ", "L    ", "L    ", "LLLLL"],
                'M': ["M   M", "MM MM", "M M M", "M   M", "M   M"],
                'N': ["N   N", "NN  N", "N N N", "N  NN", "N   N"],
                'O': [" OOO ", "O   O", "O   O", "O   O", " OOO "],
                'P': ["PPPP ", "P   P", "PPPP ", "P    ", "P    "],
                'Q': [" QQQ ", "Q   Q", "Q   Q", "Q  QQ", " QQQQ"],
                'R': ["RRRR ", "R   R", "RRRR ", "R  R ", "R   R"],
                'S': [" SSS ", "S   S", " SSS ", "    S", " SSS "],
                'T': ["TTTTT", "  T  ", "  T  ", "  T  ", "  T  "],
                'U': ["U   U", "U   U", "U   U", "U   U", " UUU "],
                'V': ["V   V", "V   V", "V   V", " V V ", "  V  "],
                'W': ["W   W", "W   W", "W W W", "WW WW", "W   W"],
                'X': ["X   X", " X X ", "  X  ", " X X ", "X   X"],
                'Y': ["Y   Y", " Y Y ", "  Y  ", "  Y  ", "  Y  "],
                'Z': ["ZZZZZ", "   Z ", "  Z  ", " Z   ", "ZZZZZ"],
                ' ': ["     ", "     ", "     ", "     ", "     "],
                '0': [" 000 ", "0  90", "0 9 0", "09  0", " 000 "],
                '1': ["  1  ", " 11  ", "  1  ", "  1  ", "11111"],
                '2': [" 222 ", "2   2", "   2 ", "  2  ", "22222"],
                '3': [" 333 ", "3   3", "  33 ", "3   3", " 333 "],
                '4': ["   4 ", "  44 ", " 4 4 ", "44444", "   4 "],
                '5': ["55555", "5    ", "5555 ", "    5", "5555 "],
                '6': [" 666 ", "6    ", "6666 ", "6   6", " 666 "],
                '7': ["77777", "   7 ", "  7  ", " 7   ", "7    "],
                '8': [" 888 ", "8   8", " 888 ", "8   8", " 888 "],
                '9': [" 999 ", "9   9", " 9999", "    9", " 999 "],
            },
            'banner': {
                'A': ["  #  ", " # # ", "#   #", "#####", "#   #"],
                'B': ["#### ", "#   #", "#### ", "#   #", "#### "],
                'C': [" ### ", "#   #", "#    ", "#   #", " ### "],
                'D': ["### ", "#  #", "#   #", "#  #", "### "],
                'E': ["#####", "#    ", "###  ", "#    ", "#####"],
                ' ': ["     ", "     ", "     ", "     ", "     "],
            },
            'small': {
                'A': [" _ ", "/_\\", "   "],
                'B': ["_  ", "|_)", "/_ "],
                'C': [" _ ", "|  ", "\\_/"],
                ' ': ["   ", "   ", "   "],
            }
        }
        
        self.borders = {
            'plain': {
                'horizontal': '-',
                'vertical': '|',
                'top_left': '+',
                'top_right': '+',
                'bottom_left': '+',
                'bottom_right': '+'
            },
            'fancy': {
                'horizontal': '═',
                'vertical': '║',
                'top_left': '╔',
                'top_right': '╗',
                'bottom_left': '╚',
                'bottom_right': '╝'
            },
            'round': {
                'horizontal': '─',
                'vertical': '│',
                'top_left': '╭',
                'top_right': '╮',
                'bottom_left': '╰',
                'bottom_right': '╯'
            }
        }

    def generate(self, text: str, font: str = 'standard', border: str = None, 
                shadow: bool = False, center: bool = False) -> str:
        """Generate ASCII art from text"""
        text = text.upper()
        font_data = self.fonts.get(font, self.fonts['standard'])
        
        # Handle unsupported characters
        result = []
        for char in text:
            if char not in font_data:
                char = ' '
            result.append(font_data[char])
        
        # Create the ASCII art line by line
        art_lines = []
        height = max(len(char_lines) for char_lines in result)
        
        for i in range(height):
            line = []
            for char_lines in result:
                if i < len(char_lines):
                    line.append(char_lines[i])
                else:
                    line.append(' ' * len(char_lines[0]))
            art_lines.append(' '.join(line))
        
        # Add shadow if requested
        if shadow:
            shadow_lines = []
            for line in art_lines:
                shadow_lines.append(' ' + line)
            art_lines = shadow_lines
        
        # Add border if requested
        if border and border in self.borders:
            art_lines = self._add_border(art_lines, self.borders[border])
        
        # Center text if requested
        if center:
            max_width = max(len(line) for line in art_lines)
            art_lines = [line.center(max_width) for line in art_lines]
        
        return '\n'.join(art_lines)

    def _add_border(self, lines: List[str], border_chars: Dict[str, str]) -> List[str]:
        """Add border around ASCII art"""
        max_width = max(len(line) for line in lines)
        bordered_lines = []
        
        # Top border
        top_border = border_chars['top_left'] + border_chars['horizontal'] * max_width + border_chars['top_right']
        bordered_lines.append(top_border)
        
        # Content with side borders
        for line in lines:
            bordered_line = border_chars['vertical'] + line.ljust(max_width) + border_chars['vertical']
            bordered_lines.append(bordered_line)
        
        # Bottom border
        bottom_border = border_chars['bottom_left'] + border_chars['horizontal'] * max_width + border_chars['bottom_right']
        bordered_lines.append(bottom_border)
        
        return bordered_lines

    def save_to_file(self, text: str, filename: str, **kwargs):
        """Save ASCII art to file"""
        ascii_art = self.generate(text, **kwargs)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(ascii_art)
        return filename


def main():
    parser = argparse.ArgumentParser(description='ASCII Art Text Generator')
    parser.add_argument('text', help='Text to convert to ASCII art')
    parser.add_argument('-f', '--font', choices=['standard', 'banner', 'small'], 
                        default='standard', help='Font style to use')
    parser.add_argument('-b', '--border', choices=['plain', 'fancy', 'round'], 
                        help='Add border around the text')
    parser.add_argument('-s', '--shadow', action='store_true', help='Add shadow effect')
    parser.add_argument('-c', '--center', action='store_true', help='Center the text')
    parser.add_argument('-o', '--output', help='Save to file instead of printing to console')
    parser.add_argument('--list-fonts', action='store_true', help='List available fonts')
    parser.add_argument('--demo', action='store_true', help='Show examples of all fonts')
    
    args = parser.parse_args()
    
    generator = ASCIIArtGenerator()
    
    if args.list_fonts:
        print("Available fonts:")
        for font in generator.fonts.keys():
            print(f"  - {font}")
        return
    
    if args.demo:
        print("ASCII Art Font Demo\n")
        for font in generator.fonts.keys():
            print(f"Font: {font}")
            print(generator.generate('HELLO', font=font, border='plain'))
            print()
        return
    
    try:
        if args.output:
            filename = generator.save_to_file(
                args.text,
                args.output,
                font=args.font,
                border=args.border,
                shadow=args.shadow,
                center=args.center
            )
            print(f"ASCII art saved to: {filename}")
        else:
            art = generator.generate(
                args.text,
                font=args.font,
                border=args.border,
                shadow=args.shadow,
                center=args.center
            )
            print(art)
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()
