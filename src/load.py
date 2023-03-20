from utils.data.load import get_signal
from utils.dvc.params import get_params
from utils.data.write import write_signal

params = get_params()

signal = get_signal(decimation_factor=params["decimation_factor"],
                    moving_average_win_size=params["moving_average_"
                    + "win_size"])

write_signal(signal)
