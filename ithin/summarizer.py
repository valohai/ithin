from base64 import b64encode
from io import StringIO, BytesIO

CSS = """
body {
    font: 12pt sans-serif;
    background: #f8f8f8;
}
ol {
    list-style-type: none;
    margin: 0;
    padding: 0;
}
ol li {
    display: inline;
}
section {
    background: #fff;
    box-shadow: 0px 10px 5px -5px rgba(0,0,0,0.46);
    padding: 1em;
    margin-bottom: 1em;
}
"""

def make_summary_html(groups):
    buf = StringIO()
    buf.write('<!DOCTYPE html><html><head><style>{css}</style></head><body>'.format(css=CSS))
    for n, group in enumerate(groups, 1):
        buf.write('<section>')
        buf.write('<h1>Group {n}</h1>'.format(n=n))
        buf.write('<ol>')

        for image in group:
            ibuf = BytesIO()
            image['image'].save(ibuf, format='JPEG', quality=70)
            img_data_uri = 'data:image/jpeg;base64,%s' % b64encode(ibuf.getvalue()).decode()
            buf.write('<li>')
            buf.write('<img src=\"{uri}\" title=\"{name}\">'.format(
                uri=img_data_uri,
                name=image['name'],
            ))
            buf.write('</li>\n')
        buf.write('</ol>\n')
        buf.write('</section>\n')
    buf.write('</body></html>')
    return buf.getvalue()
