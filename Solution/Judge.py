import matplotlib as plt
import numpy as np
import pandas as pd
import csv

all_data = {}
year_data = {}
artist_data = {}

def read_data():
    with open("full_music_data.csv", "r", encoding="UTF-8") as fmd:
        all_reader = csv.reader(fmd)
        for line in all_reader:
            if all_reader.line_num == 1:
                continue
            else:
                if line[1] in all_data:
                    all_data[line[1]][line[18]] = {"danceability":line[2], "energy":line[3], "valence":line[4], "tempo":line[5], "loudness":line[6], "mode":line[7], "key":line[8], "acousticness":line[9], "instumentalness":line[10], "liveness":line[11], "speechiness":line[12], "explicit":line[13], "duration_ms":line[14], "popularity":line[15], "year":line[16]}
                else:
                    all_data[line[1]] = {line[18]:{"danceability":line[2], "energy":line[3], "valence":line[4], "tempo":line[5], "loudness":line[6], "mode":line[7], "key":line[8], "acousticness":line[9], "instumentalness":line[10], "liveness":line[11], "speechiness":line[12], "explicit":line[13], "duration_ms":line[14], "popularity":line[15], "year":line[16]}}
    with open("data_by_artist.csv", "r", encoding="UTF-8") as dba:
        artist_reader = csv.reader(dba)
        for line in artist_reader:
            if artist_reader.line_num == 1:
                continue
            else:
                artist_data[line[1]] = {"danceability":line[2], "energy":line[3], "valence":line[4], "tempo":line[5], "loudness":line[6], "mode":line[7], "key":line[8], "acousticness":line[9], "instumentalness":line[10], "liveness":line[11], "speechiness":line[12], "duration_ms":line[13], "popularity":line[14], "count":line[15]}
    with open("data_by_year.csv", "r", encoding="UTF-8") as dby:
        year_reader = csv.reader(dby)
        for line in year_reader:
            if year_reader.line_num == 1:
                continue
            else:
                year_data[line[0]] = {"danceability":line[1], "energy":line[2], "valence":line[3], "tempo":line[4], "loudness":line[5], "mode":line[6], "key":line[7], "acousticness":line[8], "instumentalness":line[9], "liveness":line[10], "speechiness":line[11], "duration_ms":line[12], "popularity":line[13]}

if __name__ == '__main__':
    