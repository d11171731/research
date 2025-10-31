#!/usr/bin/env python3
import re
import sys

def markdown_to_html(md_content):
    """Convert markdown to HTML with basic formatting"""
    html = md_content

    # Escape HTML special characters in code blocks first
    code_blocks = []
    def save_code_block(match):
        code_blocks.append(match.group(0))
        return f"___CODE_BLOCK_{len(code_blocks)-1}___"

    html = re.sub(r'```[\s\S]*?```', save_code_block, html)

    # Headers (with IDs for TOC linking)
    html = re.sub(r'^# (.*?)$', lambda m: f'<h1 id="{slugify(m.group(1))}">{m.group(1)}</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', lambda m: f'<h2 id="{slugify(m.group(1))}">{m.group(1)}</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.*?)$', lambda m: f'<h3 id="{slugify(m.group(1))}">{m.group(1)}</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.*?)$', lambda m: f'<h4 id="{slugify(m.group(1))}">{m.group(1)}</h4>', html, flags=re.MULTILINE)
    html = re.sub(r'^##### (.*?)$', lambda m: f'<h5 id="{slugify(m.group(1))}">{m.group(1)}</h5>', html, flags=re.MULTILINE)

    # Bold
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)

    # Italic
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)

    # Inline code
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)

    # Links
    html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank">\1</a>', html)

    # Unordered lists
    html = re.sub(r'^\- (.*?)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'(<li>.*?</li>\n?)+', r'<ul>\g<0></ul>', html, flags=re.DOTALL)

    # Restore code blocks with proper formatting for Prism.js
    for i, block in enumerate(code_blocks):
        # Extract language and code
        match = re.match(r'```(\w*)\n?([\s\S]*?)```', block)
        if match:
            lang = match.group(1) or 'plaintext'
            # Map common language aliases
            lang_map = {
                'sh': 'bash',
                'shell': 'bash',
                'yml': 'yaml',
                'properties': 'properties',
                'conf': 'bash'
            }
            lang = lang_map.get(lang, lang)
            code = match.group(2).strip()
            code = code.replace('<', '&lt;').replace('>', '&gt;')
            html = html.replace(f'___CODE_BLOCK_{i}___',
                f'<pre class="line-numbers"><code class="language-{lang}">{code}</code></pre>')

    # Paragraphs (lines not already in HTML tags)
    lines = html.split('\n')
    result = []
    in_tag = False
    paragraph = []

    for line in lines:
        if re.match(r'^\s*<', line) or line.strip() == '':
            if paragraph:
                result.append(f'<p>{" ".join(paragraph)}</p>')
                paragraph = []
            result.append(line)
        else:
            paragraph.append(line.strip())

    if paragraph:
        result.append(f'<p>{" ".join(paragraph)}</p>')

    return '\n'.join(result)

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def extract_toc(md_content):
    """Extract table of contents from markdown headers"""
    toc = []
    for line in md_content.split('\n'):
        if line.startswith('#'):
            level = len(re.match(r'^#+', line).group(0))
            title = re.sub(r'^#+\s*', '', line).strip()
            slug = slugify(title)
            toc.append((level, title, slug))
    return toc

def generate_toc_html(toc):
    """Generate HTML for table of contents"""
    html = ['<nav class="toc">', '<h2>Table of Contents</h2>', '<ul>']
    current_level = 1

    for level, title, slug in toc:
        if level > current_level:
            html.append('<ul>' * (level - current_level))
        elif level < current_level:
            html.append('</ul>' * (current_level - level))

        html.append(f'<li><a href="#{slug}">{title}</a></li>')
        current_level = level

    html.append('</ul>' * current_level)
    html.append('</nav>')
    return '\n'.join(html)

# Read markdown file
with open('/Users/a./workspace/git/personal/research/dma3/TECHNICAL_PLAN.md', 'r') as f:
    md_content = f.read()

# Generate TOC
toc = extract_toc(md_content)
toc_html = generate_toc_html(toc)

# Convert markdown to HTML
content_html = markdown_to_html(md_content)

# Create full HTML document
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DMA Trading System - Technical Plan</title>

    <!-- Prism.js for syntax highlighting -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet" />
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/line-numbers/prism-line-numbers.min.css" rel="stylesheet" />
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/toolbar/prism-toolbar.min.css" rel="stylesheet" />

    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
        }}

        .container {{
            display: flex;
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            min-height: 100vh;
        }}

        .toc {{
            width: 300px;
            position: sticky;
            top: 0;
            height: 100vh;
            overflow-y: auto;
            background: #2c3e50;
            color: white;
            padding: 20px;
            border-right: 1px solid #ddd;
        }}

        .toc h2 {{
            color: #ecf0f1;
            margin-bottom: 15px;
            font-size: 1.2em;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }}

        .toc ul {{
            list-style: none;
            margin-left: 0;
        }}

        .toc ul ul {{
            margin-left: 15px;
            margin-top: 5px;
        }}

        .toc li {{
            margin: 8px 0;
        }}

        .toc a {{
            color: #ecf0f1;
            text-decoration: none;
            transition: color 0.2s;
            display: block;
            padding: 3px 0;
        }}

        .toc a:hover {{
            color: #3498db;
            padding-left: 5px;
        }}

        .content {{
            flex: 1;
            padding: 40px 60px;
            max-width: 900px;
        }}

        h1 {{
            color: #2c3e50;
            font-size: 2.5em;
            margin: 30px 0 20px 0;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}

        h2 {{
            color: #34495e;
            font-size: 2em;
            margin: 25px 0 15px 0;
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 8px;
        }}

        h3 {{
            color: #34495e;
            font-size: 1.5em;
            margin: 20px 0 12px 0;
        }}

        h4 {{
            color: #555;
            font-size: 1.2em;
            margin: 15px 0 10px 0;
        }}

        h5 {{
            color: #666;
            font-size: 1.1em;
            margin: 12px 0 8px 0;
        }}

        p {{
            margin: 12px 0;
            color: #444;
        }}

        ul {{
            margin: 12px 0;
            padding-left: 25px;
        }}

        li {{
            margin: 6px 0;
            color: #444;
        }}

        code {{
            background: #f0f0f0;
            padding: 3px 7px;
            border-radius: 4px;
            font-family: 'SF Mono', Monaco, 'Cascadia Code', 'Roboto Mono', Consolas, 'Courier New', monospace;
            color: #d73a49;
            font-size: 0.92em;
            border: 1px solid #e1e4e8;
        }}

        /* Prism.js custom styling */
        pre[class*="language-"] {{
            border-radius: 6px;
            margin: 20px 0;
            border-left: 4px solid #0969da;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            max-height: 600px;
            overflow: auto;
        }}

        code[class*="language-"],
        pre[class*="language-"] {{
            font-size: 14px;
            line-height: 1.6;
            font-family: 'SF Mono', Monaco, 'Cascadia Code', 'Roboto Mono', Consolas, 'Courier New', monospace;
            text-shadow: none;
        }}

        .line-numbers .line-numbers-rows {{
            border-right: 1px solid #444 !important;
        }}

        /* Scrollbar styling for code blocks */
        pre[class*="language-"]::-webkit-scrollbar {{
            width: 10px;
            height: 10px;
        }}

        pre[class*="language-"]::-webkit-scrollbar-track {{
            background: #1d1f21;
            border-radius: 5px;
        }}

        pre[class*="language-"]::-webkit-scrollbar-thumb {{
            background: #0969da;
            border-radius: 5px;
        }}

        pre[class*="language-"]::-webkit-scrollbar-thumb:hover {{
            background: #0550ae;
        }}

        /* Toolbar styling */
        div.code-toolbar > .toolbar {{
            opacity: 1;
        }}

        div.code-toolbar > .toolbar > .toolbar-item > button {{
            background: #0969da;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 4px 10px;
            font-size: 12px;
            cursor: pointer;
        }}

        div.code-toolbar > .toolbar > .toolbar-item > button:hover {{
            background: #0550ae;
        }}

        a {{
            color: #3498db;
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}

        strong {{
            color: #2c3e50;
            font-weight: 600;
        }}

        em {{
            color: #555;
        }}

        @media (max-width: 768px) {{
            .container {{
                flex-direction: column;
            }}

            .toc {{
                width: 100%;
                height: auto;
                position: relative;
            }}

            .content {{
                padding: 20px;
            }}
        }}

        /* Smooth scroll */
        html {{
            scroll-behavior: smooth;
        }}

        /* Back to top button */
        .back-to-top {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: #3498db;
            color: white;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            opacity: 0;
            transition: opacity 0.3s;
            font-size: 24px;
            text-decoration: none;
        }}

        .back-to-top.show {{
            opacity: 1;
        }}

        .back-to-top:hover {{
            background: #2980b9;
        }}
    </style>
</head>
<body>
    <div class="container">
        {toc_html}
        <div class="content">
            {content_html}
        </div>
    </div>

    <a href="#" class="back-to-top" id="backToTop">↑</a>

    <!-- Prism.js Scripts -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/line-numbers/prism-line-numbers.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/toolbar/prism-toolbar.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/copy-to-clipboard/prism-copy-to-clipboard.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-java.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-yaml.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-xml-doc.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-properties.min.js"></script>

    <script>
        // Back to top button
        window.addEventListener('scroll', function() {{
            const backToTop = document.getElementById('backToTop');
            if (window.pageYOffset > 300) {{
                backToTop.classList.add('show');
            }} else {{
                backToTop.classList.remove('show');
            }}
        }});

        // Add line-numbers class to all pre elements
        document.addEventListener('DOMContentLoaded', function() {{
            document.querySelectorAll('pre').forEach(function(pre) {{
                pre.classList.add('line-numbers');
            }});
        }});
    </script>
</body>
</html>
"""

# Write HTML file
with open('/Users/a./workspace/git/personal/research/dma3/TECHNICAL_PLAN.html', 'w') as f:
    f.write(html_template)

print("✓ Converted TECHNICAL_PLAN.md to TECHNICAL_PLAN.html")
