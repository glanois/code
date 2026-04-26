r"""
usage: lorem.py [-h] bytes

Generate lorem ipsum text of exactly the specified byte length.

positional arguments:
  bytes       desired length of the output in bytes

options:
  -h, --help  show this help message and exit
"""

import argparse
import random
import sys

# Classic lorem ipsum words (kept small for simplicity)
LOREM_WORDS = [
    'lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing',
    'elit', 'sed', 'do', 'eiusmod', 'tempor', 'incididunt', 'ut', 'labore',
    'et', 'dolore', 'magna', 'aliqua', 'enim', 'ad', 'minim', 'veniam',
    'quis', 'nostrud', 'exercitation', 'ullamco', 'laboris', 'nisi',
    'aliquip', 'ex', 'ea', 'commodo', 'consequat'
]

def generate_lorem_bytes(target_bytes: int) -> str:
    if target_bytes <= 0:
        return ''

    result = []
    current_bytes = 0
    used_newline = False

    while current_bytes < target_bytes:
        word = random.choice(LOREM_WORDS)
        
        # Decide separator: mostly space, sometimes newline (but not too many)
        if random.random() < 0.08 and used_newline < 3 and current_bytes > 20:
            separator = '\n'
            used_newline += 1
        else:
            separator = ' '

        candidate = word + separator
        candidate_bytes = len(candidate.encode('utf-8'))

        if current_bytes + candidate_bytes <= target_bytes:
            result.append(candidate)
            current_bytes += candidate_bytes
        else:
            # Last piece — fill remaining bytes (may cut word)
            remaining = target_bytes - current_bytes
            if remaining >= 1:
                # Try to take as much of the word as possible
                partial = ''
                for char in word:
                    if len((partial + char).encode('utf-8')) <= remaining:
                        partial += char
                    else:
                        break
                result.append(partial)
            break

    text = ''.join(result).rstrip(' \n')

    # Make sure we didn't undershoot too much — pad with spaces if needed
    final_bytes = len(text.encode('utf-8'))
    if final_bytes < target_bytes:
        text += ' ' * (target_bytes - final_bytes)

    return text


def main(bytes):
    # Generate the text.
    text = generate_lorem_bytes(bytes)

    # Output the result.
    print(text, end='')  # no extra newline at end

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate lorem ipsum text of exactly the specified byte length.')
    parser.add_argument(
        'bytes',
        type=int,
        help='desired length of the output in bytes')

    args = parser.parse_args()

    if args.bytes < 0:
        parser.error('number of bytes cannot be negative')

    if args.bytes == 0:
        print('', end='')
        sys.exit(0)

    sys.exit(main(args.bytes))
