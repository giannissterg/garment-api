import jsonlines


def main():
    with jsonlines.open("./assets/garments.jl") as reader:
        for obj in reader:
            print(obj)


if __name__ == "__main__":
    main()
