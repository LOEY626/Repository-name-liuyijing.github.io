with open("C:/Users/Kyrie/Documents/2.0/portfolio/project-5.html", "r", encoding="utf-8") as f:
    content = f.read()

sections = content.split('<div class="project-section')
print("Found %d project sections" % (len(sections)-1))

for i, sec in enumerate(sections[1:], 1):
    h2_start = sec.find("<h2>") + 4
    h2_end = sec.find("</h2>", h2_start)
    h2_text = sec[h2_start:h2_end] if h2_start > 3 else "?"
    
    img_count = sec.count("<img ")
    o_count = sec.count("p5-o")
    g_count = sec.count("p5-g")
    
    print("  Section %d: [%s] -> %d images" % (i, h2_text, img_count))
    has_new_gallery = "grid-column:1/3;grid-row:span 2" in sec
    has_rotated = "rotate" in sec and "p5-o" in sec
    print("    New gallery: %s, Rotated VR: %s" % (has_new_gallery, has_rotated))
