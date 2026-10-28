# Prime Movies

Searchable catalogue of the movies included with David Comstock's Amazon Prime membership, as listed in Amazon's Prime Video search on the build date.

Live site: https://comstocd.github.io/prime-movies/

- `index.html`: the page
- `collection.js`: the data (`window.PRIME.rows`: title, rating, reviews, genre indexes, director, stars, ASIN)
- `build.py`: rebuilds `collection.js` from a fresh CSV export; bump BUILD in `sw.js` to the same number so devices see the update
