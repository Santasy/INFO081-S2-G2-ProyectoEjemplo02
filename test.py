import datetime as dt
from ppdc_timed_generator import GeneradorUniforme

gen = GeneradorUniforme(
    100000,
)


def dummy_factory(id: int, hora_creacion: dt.datetime):
    return (id, hora_creacion)


res = gen.generar_clientes(10, dummy_factory)
print(len(res))
