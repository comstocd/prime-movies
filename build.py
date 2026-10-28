# Convert the Prime CSV export into collection.js. Usage: python3 build.py prime_movies.csv BUILD DATE
import csv, json, sys, re
src, build, date = sys.argv[1], int(sys.argv[2]), sys.argv[3]
def num(s):
    s = (s or '').replace(',', '').strip()
    m = re.match(r'([\d.]+)([KM]?)$', s)
    if not m: return 0
    return int(round(float(m.group(1)) * {'': 1, 'K': 1000, 'M': 1000000}[m.group(2)]))
rows, genres = [], []
for r in csv.DictReader(open(src, encoding='utf-8-sig')):
    gi = []
    for g in [x.strip() for x in r['Genres'].split(';') if x.strip()]:
        if g not in genres: genres.append(g)
        gi.append(genres.index(g))
    rows.append([r['Title'], float(r['Rating'] or 0), num(r['Reviews']), gi, r['Director'], r['Stars'], r['Link'].rsplit('/', 1)[-1]])
order = sorted(range(len(genres)), key=lambda i: genres[i])
remap = {old: new for new, old in enumerate(order)}
for row in rows: row[3] = sorted(remap[i] for i in row[3])
out = {'build': build, 'updated': date, 'genres': [genres[i] for i in order], 'rows': rows}
open('collection.js', 'w', encoding='utf-8').write('window.PRIME=' + json.dumps(out, ensure_ascii=False, separators=(',', ':')) + ';\n')
print(len(rows), 'movies,', len(genres), 'genres')
