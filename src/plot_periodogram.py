import matplotlib.pyplot as plt
import numpy as np

def plot_periodogram(
    frequency,
    power
):

    period = 1 / frequency

    mask = np.isfinite(
        period
    )

    plt.figure(
        figsize=(10,5)
    )

    plt.plot(
        period[mask],
        power[mask]
    )

    plt.xlabel(
        "Period (days)"
    )

    plt.ylabel(
        "Power"
    )

    plt.title(
        "Lomb–Scargle Periodogram"
    )

    plt.xlim(
        0,
        2
    )

    plt.grid(
        alpha=0.3
    )

    plt.tight_layout()

    plt.savefig(
        "periodogram.png",
        dpi=300
    )

    plt.show()
