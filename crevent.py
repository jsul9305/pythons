events = [
    {'date': '2024-11-01', 'event': 'Jeju Marathon', 'location': 'Jeju', 'url': 'https://jejumarathon.com'},
    {'date': '2024-11-15', 'event': 'Seoul Marathon', 'location': 'Seoul', 'url': 'https://seoulmarathon.com'},
]

html = "<h1>Upcoming Marathon Events</h1>\n"
html += "<table border='1'>\n<tr><th>Date</th><th>Event</th><th>Location</th><th>Link</th></tr>\n"

for event in events:
    html += f"<tr><td>{event['date']}</td><td>{event['event']}</td><td>{event['location']}</td>"
    html += f"<td><a href='{event['url']}' target='_blank'>Visit</a></td></tr>\n"

html += "</table>"

# 결과 HTML 출력
print(html)
