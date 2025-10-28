a, *b = (1, 2, 3, 4, 5, 6, 7)
print(a, b, type(b))

a, *b = [1, 2, 3, 4, 5, 6, 7]
print(a, b, type(b))

name = "akbar"


def testfunc(a, *args, name="ali", **kwargs):
    print(
        a,
        type(a),
        "\n",
        args,
        type(args),
        "\n",
        name,
        type(name),
        "\n",
        kwargs,
        type(kwargs),
        "\n",
    )


testfunc(26, 23, 15, 67, 9, 23, "90", name="reza", loc="tehran", country="germany")
