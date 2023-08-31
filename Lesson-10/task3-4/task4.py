import csv


highest_scores = {}

with open("game_score.csv", mode="r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader, None)


    for player_name, score in reader:
        score = int(score)
        highest_scores[player_name] = max(score, highest_scores.get(player_name, 0))


sorted_scores = sorted(highest_scores.items(), key=lambda x: x[1], reverse=True)


with open("high_scores.csv", mode="w", newline="") as new_file:
    writer = csv.writer(new_file)
    writer.writerow(["Player name", "Highest Score"])
    writer.writerows(sorted_scores)