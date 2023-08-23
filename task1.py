def cats_hats(num_cats):
    cats = [False] * num_cats
    for round in range(1, 101):
        for cat in range(round - 1, num_cats, round):
            cats[cat] = not cats[cat]
    cats_hats = [i + 1 for i, has_hat in enumerate(cats) if has_hat]
    return cats_hats


num_cats = 100
hats_on_cats = cats_hats(num_cats)
print("Cats with hats: ", hats_on_cats)