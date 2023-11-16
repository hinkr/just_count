import click

import just_count.square


@click.command()
# @click.argument("number")
@click.option(
    "-n",
    "--number",
    default=5,
    help="Number to calcultate the square of",
    show_default=True,
)
def main(number):
    print(f"The square of {number} is {just_count.square.square(int(number))}")


if __name__ == "__main__":
    main()
