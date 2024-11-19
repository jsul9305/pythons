# List of names and values for 100K and 50K runners
runners_100k = [
    ("신용문", 132), ("양정모", 157), ("장지호", 247), 
    ("송상윤", 212), ("정혜원", 294), ("이영규", 221), 
    ("성하동", 182), ("정유미", 298)
]

runners_50k = [
    ("서민혜", 1259), ("김성욱", 1123), ("황경원", 1118), 
    ("이순진", 1243), ("이지윤", 1250), ("문형준", 1010), 
    ("이종국", 1039)
]

# Base URL with placeholder
base_url = 'https://seoul100k.livetrail.run/coureur.php?rech={}#tab'

# HTML template with Table of Contents
html_template = '''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Iframes with Runner Names</title>
    <style>
        iframe {{
            width: 90%;
            height: 600px;
            margin-bottom: 20px;
        }}
        h2 {{
            font-size: 1.2em;
            margin-top: 20px;
            margin-bottom: 5px;
        }}
        .toc {{
            font-size: 1.2em;
            margin-bottom: 30px;
        }}
        .toc a {{
            display: block;
            margin-bottom: 10px;
        }}
    </style>
</head>
<body>
    <h1>Table of Contents</h1>
    <div class="toc">
        <h2>100K Runners</h2>
        {}
        <h2>50K Runners</h2>
        {}
    </div>

    <h1 id="100k-runners">100K Runners</h1>
    {}
    <h1 id="50k-runners">50K Runners</h1>
    {}
</body>
</html>
'''

# Generate table of contents and iframe elements with runner names for 100K runners
toc_100k = ''
iframes_100k = ''
for name, value in runners_100k:
    toc_100k += f'<a href="#runner-{value}">{name}</a>\n'
    iframes_100k += f'<h2 id="runner-{value}">{name}</h2>\n<iframe src="{base_url.format(value)}" frameborder="0"></iframe>\n'

# Generate table of contents and iframe elements with runner names for 50K runners
toc_50k = ''
iframes_50k = ''
for name, value in runners_50k:
    toc_50k += f'<a href="#runner-{value}">{name}</a>\n'
    iframes_50k += f'<h2 id="runner-{value}">{name}</h2>\n<iframe src="{base_url.format(value)}" frameborder="0"></iframe>\n'

# Combine the template with the generated TOC and iframes
html_content = html_template.format(toc_100k, toc_50k, iframes_100k, iframes_50k)

# Save to an HTML file
with open('index.html', 'w') as f:
    f.write(html_content)

print("HTML file generated: index.html")