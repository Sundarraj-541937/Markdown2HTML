from pathlib import Path
import markdown
import shutil

DOCS_DIR = Path("docs")
SITE_DIR = Path("site")

# Remove old site folder
if SITE_DIR.exists():
    shutil.rmtree(SITE_DIR)

SITE_DIR.mkdir()

# Simple CSS
css = """
body {
    font-family: Arial, sans-serif;
    max-width: 900px;
    margin: auto;
    padding: 40px;
    line-height: 1.6;
    background-color: #f4f4f4;
}

h1, h2, h3 {
    color: #333;
}

a {
    color: #0066cc;
    text-decoration: none;
}

code {
    background: #eee;
    padding: 2px 4px;
}
"""

# Write CSS file
(SITE_DIR / "style.css").write_text(css)

index_links = []

# Convert markdown files
for md_file in DOCS_DIR.glob("*.md"):
    html_content = markdown.markdown(md_file.read_text())

    title = md_file.stem.capitalize()
    output_file = SITE_DIR / f"{md_file.stem}.html"

    full_html = f"""
    <html>
    <head>
        <title>{title}</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <h1>{title}</h1>
        {html_content}
    </body>
    </html>
    """

    output_file.write_text(full_html)

    index_links.append(
        f'<li><a href="{md_file.stem}.html">{title}</a></li>'
    )

# Generate index.html
index_html = f"""
<html>
<head>
    <title>Documentation</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Documentation</h1>
    <ul>
        {''.join(index_links)}
    </ul>
</body>
</html>
"""

(SITE_DIR / "index.html").write_text(index_html)

print("Site generated successfully!")
print("Testing PR workflow")