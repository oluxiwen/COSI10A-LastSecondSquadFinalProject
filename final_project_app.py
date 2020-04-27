import csv

vgsalesinfo = []
platforms = []
years = []
publishers = []
genres = []

with open('data/vgsales.csv') as csvfile:
    vgsalesinfo = [{k: v for k, v in row.items()}
                   for row in csv.DictReader(csvfile, skipinitialspace=True)]

platforms = list(set([b['Platform'] for b in vgsalesinfo]))
platforms.sort()
years = list(set([b['Year'] for b in vgsalesinfo]))
years.sort()
publishers = list(set([b['Publisher'] for b in vgsalesinfo]))
publishers.sort()
genres = list(set([b['Genre'] for b in vgsalesinfo]))
genres.sort()


def games_by_platform(games, platform):
    return [b for b in games if b['Platform'] == platform]


def games_by_year(games, year):
    return [b for b in games if b['Year'] == year]


def games_by_publisher(games, publisher):
    return [b for b in games if b['Publisher'] == publisher]


def games_by_genre(games, genre):
    return [b for b in games if b['Genre'] == genre]


def games_with_limit(games, limit):
    return games[:limit]
