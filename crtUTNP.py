# List of names and values for 100K and 50K runners
runners_9peak = [
    ("안준설", 9071), ("신형수", 9221), ("김상훈", 9150), ("지민호", 9051), ("송두환", 9037)
]
runners_APTRC80 = [
    ("장동국", 8058), ("구교정", 8065)
]
runners_APTRC40 = [
    ("오완목", 5010), ("이새별", 5019), ("김순민", 5241)
]

# Base URL with placeholder
base_url = 'https://smartchip.co.kr/Expectedrecord_data.asp?usedata=202450000176&nameorbibno={}'

# HTML template with Table of Contents
html_template = '''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>저스트레일 UTNP 참가자 모니러링</title>
    <style>
        body {{
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            margin: 0;
            padding: 0;
        }}
        iframe {{
            width: 100%; /* 페이지의 너비를 설정 */
            height: 1000px; /* 각 iframe의 높이를 설정 */
            border: 1px solid #000; /* 테두리 설정 */
            margin: 10px; /* iframes 간의 여백 */
        }}

        h1, h2 {{
            text-align: center;
            width: 100%;
            position: relative;
            animation: blink-text 2s infinite; /* 글자 반짝임 효과 추가 */
            color: white;
            background: linear-gradient(90deg, #ffcc00, #ff3399, #6699ff, #cc33ff, #ffcc00);
            background-size: 200% 200%;
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            animation: shimmer 3s infinite; /* 별 반짝이는 효과 */
        }}

        /* 텍스트 반짝임 애니메이션 */
        @keyframes shimmer {{
            0% {{
                background-position: 0% 50%;
            }}
            50% {{
                background-position: 100% 50%;
            }}
            100% {{
                background-position: 0% 50%;
            }}
        }}

        .male-header {{
            background-color: red;
            color: white;
            animation: blink-stars 2s infinite; /* 반짝이는 효과 */
        }}

        .female-header {{
            background-color: yellow;
            color: black;
            animation: blink-stars 2s infinite;
        }}

        /* 텍스트에서 반짝이는 효과 추가 */
        @keyframes blink-stars {{
            0% {{
                text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 20px #ff3399, 0 0 30px #ff3399, 0 0 40px #ff3399;
            }}
            50% {{
                text-shadow: 0 0 10px #fff, 0 0 20px #ff3399, 0 0 30px #ff3399, 0 0 40px #ff3399, 0 0 50px #ff3399;
            }}
            100% {{
                text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 20px #ff3399, 0 0 30px #ff3399, 0 0 40px #ff3399;
            }}
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
    <script>
        let seconds = 60;  // Set initial countdown seconds

        window.onload = function() {{
            let countdownElement = document.getElementById('countdown');

            // Scroll to the stored hash after reload
            let savedHash = localStorage.getItem('scrollPosition');
            if (savedHash) {{
                window.location.hash = savedHash;
                localStorage.removeItem('scrollPosition');  // Clean up storage after use
            }}

            function updateCountdown() {{
                countdownElement.innerText = "Page will reload in " + seconds + " seconds";
                seconds--;

                if (seconds < 0) {{
                    window.location.reload();  // Reload the page when timer reaches 0
                }}
            }}

            // Update the countdown every 1 second
            setInterval(updateCountdown, 1000);
        }};

        // Save the current hash before reloading
        window.onhashchange = function() {{
            localStorage.setItem('scrollPosition', window.location.hash);
        }};
    </script>
</head>
<body>
    <div id="countdown" style="float:right;">Page will reload in 60 seconds</div>
    <h1 id="header">목록</h1>
    <div class="toc">
        <h2>9 Peak Runners</h2>
        {}
        <h2>UTNP Long trail 80 Runners</h2>
        {}
        <h2>UTNP Short trail 40 Runners</h2>
        {}
    </div>

    <h2 id="9p-runners">9 Peak Runners</h1>
    {}
    <h2 id="L8-runners">Long trail 80 Runners</h1>
    {}
    <h2 id="S4-runners">Short trail 40 Runners</h1>
    {}
    <div style="position: fixed; bottom: 5px; right: 5px;">
        <a href="#header">▲TOP</a>
    </div>
</body>
</html>
'''

# Generate table of contents and iframe elements with runner names for 9 Peak runners
toc_9p = ''
iframes_9p = ''
for name, value in runners_9peak:
    toc_9p += f'<a href="#runner-{value}">{name}</a>\n'
    iframes_9p += f'<h3 id="runner-{value}">{name}</h2>\n<iframe src="{base_url.format(value)}" frameborder="0"></iframe>\n'

# Generate table of contents and iframe elements with runner names for 50K runners
toc_L8 = ''
iframes_L8 = ''
for name, value in runners_APTRC80:
    toc_L8 += f'<a href="#runner-{value}">{name}</a>\n'
    iframes_L8 += f'<h3 id="runner-{value}">{name}</h2>\n<iframe src="{base_url.format(value)}" frameborder="0"></iframe>\n'


# Generate table of contents and iframe elements with runner names for 50K runners
toc_S4 = ''
iframes_S4 = ''
for name, value in runners_APTRC40:
    toc_S4 += f'<a href="#runner-{value}">{name}</a>\n'
    iframes_S4 += f'<h3 id="runner-{value}">{name}</h2>\n<iframe src="{base_url.format(value)}" frameborder="0"></iframe>\n'


# Combine the template with the generated TOC and iframes
html_content = html_template.format(toc_9p, toc_L8, toc_S4, iframes_9p, iframes_L8, iframes_S4)

# Save to an HTML file
with open('index.html', 'w') as f:
    f.write(html_content)

print("HTML file generated: index.html")