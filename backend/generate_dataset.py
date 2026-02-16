import csv
import random


def generate_dataset(num_samples=5000):

    rows = []

    for _ in range(num_samples):

        passes_attempted = random.randint(10, 80)
        passes_completed = int(passes_attempted * random.uniform(0.6, 0.95))
        pass_accuracy = passes_completed / passes_attempted

        goals = random.choices([0, 1, 2, 3], weights=[60, 25, 10, 5])[0]
        assists = random.choices([0, 1, 2], weights=[65, 25, 10])[0]
        shots_on_target = random.randint(0, 5)
        key_passes = random.randint(0, 6)

        tackles = random.randint(0, 5)
        interceptions = random.randint(0, 4)
        clearances = random.randint(0, 4)
        blocks = random.randint(0, 3)

        yellow_cards = random.choices([0, 1], weights=[85, 15])[0]

        activity_rate = random.uniform(0.5, 3)

        features = {
            "pass_accuracy": pass_accuracy,
            "goals": goals,
            "assists": assists,
            "shots_on_target": shots_on_target,
            "key_passes": key_passes,
            "tackles": tackles,
            "interceptions": interceptions,
            "clearances": clearances,
            "blocks": blocks,
            "yellow_cards": yellow_cards,
            "activity_rate": activity_rate
        }

        target = (
            pass_accuracy * 20 +
            goals * 15 +
            assists * 10 +
            shots_on_target * 4 +
            key_passes * 3 +
            tackles * 2 +
            interceptions * 2 -
            yellow_cards * 5
        )

        target = max(0, min(100, int(target)))

        row = list(features.values()) + [target]
        rows.append(row)

    header = list(features.keys()) + ["performance_score"]

    with open("training_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

    print(f"Dataset generated with {num_samples} samples.")


if __name__ == "__main__":
    generate_dataset()
    