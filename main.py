import lightkurve as lk

from src.find_period import find_period
from src.plot_periodogram import plot_periodogram

target = "AB Dor"

search = lk.search_lightcurve(
    target,
    mission="TESS"
)

lc = search.download()

time = lc.time.value
flux = lc.flux.value

period, frequency, power = find_period(
    time,
    flux
)

print(
    "Recovered period:",
    period
)

plot_periodogram(
    frequency,
    power
)
