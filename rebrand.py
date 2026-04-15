"""
GyanUday University — Rebranding Script
Run this to rename the project for a different college.

Usage:
    python rebrand.py "Sunrise Institute of Technology" "SI"
    python rebrand.py "DY Patil College" "DYP"
"""

import sys
import os

def rebrand(college_name, initials):
    files_to_update = [
        'templates/base.html',
        'templates/accounts/login.html',
    ]

    replacements = [
        ('GyanUday University', college_name),
        ('>GU<',               f'>{initials}<'),
        ('GU</div>',           f'{initials}</div>'),
    ]

    for filepath in files_to_update:
        if not os.path.exists(filepath):
            print(f'  SKIP (not found): {filepath}')
            continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        original = content
        for old, new in replacements:
            content = content.replace(old, new)
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'  Updated: {filepath}')
        else:
            print(f'  No changes: {filepath}')

    # Also update the page title in base.html
    base_path = 'templates/base.html'
    if os.path.exists(base_path):
        with open(base_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace('GyanUday University', college_name)
        with open(base_path, 'w', encoding='utf-8') as f:
            f.write(content)

    print(f'\nDone! Project rebranded to: {college_name} ({initials})')
    print('Restart the server to see changes.')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python rebrand.py "College Name" "INITIALS"')
        print('Example: python rebrand.py "Sunrise Institute" "SI"')
        sys.exit(1)
    rebrand(sys.argv[1], sys.argv[2])
