from blinker import signal


class SignalService:
    all_signals = {}

    def __init__(self):
        self.all_signals['file_written'] = signal('file_written')

    def register_signal(self, name):
        self.all_signals[name] = signal(name)

    def get_signal(self, name):
        return self.all_signals[name]


signalService = SignalService()
