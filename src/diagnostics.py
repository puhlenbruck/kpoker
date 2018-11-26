from collections import deque


class DiagnosticOutput:
    def __init__(self, frame_times=False):
        self._frame_times = frame_times
        self._rolling_window_size = 10
        self._rolling_render_time_window = deque(maxlen=self._rolling_window_size)

    def record_frame_time(self, render_time):
        if self._frame_times:
            self._rolling_render_time_window.append(render_time)
            print(
                "Current frame rendered in {}ms. Average render time (last {} frames): {}ms".format(
                    render_time,
                    self._rolling_window_size,
                    _average(self._rolling_render_time_window),
                )
            )


def _average(items):
    total = 0
    for x in items:
        total += x
    return total / len(items)
