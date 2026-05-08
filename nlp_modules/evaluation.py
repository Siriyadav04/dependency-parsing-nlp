def evaluate(predicted, gold):
    correct_head = 0
    correct_label = 0
    total = len(gold)

    for p, g in zip(predicted, gold):
        if p["head"] == g["head"]:
            correct_head += 1
            if p["dep"] == g["dep"]:
                correct_label += 1

    uas = correct_head / total if total > 0 else 0
    las = correct_label / total if total > 0 else 0

    return uas, las