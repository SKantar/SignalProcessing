from ssignal import Signal
from filter import NotchFilter, ButterFilter
import sounddevice as sd

if __name__ == '__main__':
    signal = Signal(Signal.read('signal.wav'))
    signal.display('RAW Signal')
    signal.display_fft('RAW Signal')

    notch = NotchFilter(fs=signal.Fs, f0=20000.0)
    notch.display()

    butt = ButterFilter(fs=signal.Fs, f0=20000.0)
    butt.display()

    filtered_signal = Signal(notch.filter(signal))
    filtered_signal.display('Filtered(Notch)')
    filtered_signal.display_fft('Filtered(Notch)')

    filtered_signal.store('notch.wav')

    # PlaySound
    Fs, data = Signal.read('signal.wav')
    sd.play(data, Fs)

    filtered_signal = Signal(butt.filter(signal))
    filtered_signal.display('Filtered(Butter)')
    filtered_signal.display_fft('Filtered(Butter)')

    filtered_signal.store('butter.wav')

    # PlaySound
    Fs, data = Signal.read('butter.wav')
    sd.play(data, Fs)
