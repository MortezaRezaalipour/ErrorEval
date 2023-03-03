import numpy as np
from src.result import Result
from src.specs import Specs
from src.argument import Arguments
from src.config.config import *


def main():

    spec_wae = Specs(metric=WAE)
    spec_wre = Specs(metric=WRE)
    spec_whd = Specs(metric=WHD)
    results_wae = Result(spec_wae)
    results_wre = Result(spec_wre)
    results_whd = Result(spec_whd)
    # print(f'{results_wae = }')
    # print(f'{results_wre = }')
    # print(f'{results_whd = }')

    results_wae.draw_scatter_plot_all(TOTAL_RUNTIME)
    results_wre.draw_scatter_plot_all(TOTAL_RUNTIME)
    # results_whd.draw_scatter_plot_all(TOTAL_RUNTIME)

    results_wae.avg_runtime(TOTAL_RUNTIME)

    results_wae.draw_avg_plot_all(N_SATS)


if __name__ == "__main__":
    main()