import os, glob

pattern = b'project-hero-overlay"></div>'
replacement = b'project-hero-overlay"></div>\n  <div class="project-hero-halftone"></div>'

for f in sorted(glob.glob('C:/Users/Kyrie/Documents/2.0/portfolio/project-*.html')):
    basename = os.path.basename(f)
    if basename == 'project-1.html':
        continue
    with open(f, 'rb') as fh:
        content = fh.read()
    if replacement in content:
        print(f'Skipping {basename} (already has halftone)')
        continue
    if pattern not in content:
        print(f'WARNING: pattern not found in {basename}')
        continue
    content = content.replace(pattern, replacement, 1)
    with open(f, 'wb') as fh:
        fh.write(content)
    print(f'Updated {basename}')
