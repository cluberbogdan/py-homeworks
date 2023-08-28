import csv
import random


players = ["Josh", "Luke", "Kate", "Mark", "Mary"]


with open ("game_score.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Player name", "Score"])


    for player in players:
        for _ in range(100):
            score = random.randint(0, 1000)
            writer.writerow([player, score])
