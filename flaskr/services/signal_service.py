from blinker import signal
from flaskr.services.spell_check import SpellCheckService


class SignalService:
    all_signals = {}

    def __init__(self):
        self.all_signals['file_written'] = signal('file_written')
        self.all_signals['file_written'].connect(SpellCheckService.createDictionaryFromDatabase)

    def register_signal(self, name):
        self.all_signals[name] = signal(name)

    def get_signal(self, name):
        return self.all_signals[name]


signalService = SignalService()
