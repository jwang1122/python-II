from rx import of, operators as op

source = of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")

composed = source.pipe(
    op.filter(lambda i: len(i) > 5)
)
composed.subscribe(lambda value: print(f"Received: {value}"))