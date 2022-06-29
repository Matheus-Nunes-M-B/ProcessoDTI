from cmath import inf
from datetime import datetime
import sys

petshops = [
    {
        "name": "Meu Canino Feliz",
        "distance": 2000,
        "price_s": 20,
        "price_b": 40,
        "weekend": lambda x: x * 1.2,
    },
    {
        "name": "Vai Rex",
        "distance": 1700,
        "price_s": 15,
        "price_b": 50,
        "weekend": lambda x: x + 5,
    },
    {
        "name": "ChowChawgas",
        "distance": 800,
        "price_s": 30,
        "price_b": 45,
        "weekend": lambda x: x,
    },
]


def bath_price(petshop, n_small, n_big, weekend):
    if weekend:
        return (
            petshop["weekend"](petshop["price_s"]) * n_small
            + petshop["weekend"](petshop["price_b"]) * n_big
        )
    else:
        return petshop["price_s"] * n_small + petshop["price_b"] * n_big


def main(date=None, n_small=None, n_big=None):
    try:
        date = date.split("/")
        n_small = int(n_small)
        n_big = int(n_big)
        d = datetime(int(date[2]), int(date[1]), int(date[0]))
    except Exception:
        print(
            "Favor inserir os dados no padrão <data> <quantidade de cães pequenos> <quantidade cães grandes>"
        )
        sys.exit(0)

    best_price = inf
    best_petshop = petshops[0]

    for curr_petshop in petshops:
        curr_price = bath_price(curr_petshop, n_small, n_big, d.weekday() > 4)
        if (curr_price < best_price) or (
            curr_price == best_price
            and curr_petshop["distance"] < best_petshop["distance"]
        ):
            best_price = curr_price
            best_petshop = curr_petshop

    print(best_petshop["name"])
    print(best_price)


if __name__ == "__main__":
    main(*sys.argv[1:])
