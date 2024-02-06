
import numpy as np
import matplotlib.pyplot as plt

def generate_simulated_eeg_data(length=1000, sampling_rate=256, noise_level=0.1):
    time = np.arange(0, length) / sampling_rate
    alpha_freq = np.random.uniform(8, 12)  # Alpha wave frequency (8-12 Hz)
    beta_freq = np.random.uniform(12, 30)  # Beta wave frequency (12-30 Hz)
    theta_freq = np.random.uniform(4, 8)  # Theta wave frequency (4-8 Hz)
    delta_freq = np.random.uniform(1, 4)  # Delta wave frequency (1-4 Hz)
    alpha_wave = np.sin(alpha_freq * 2 * np.pi * time)
    beta_wave = np.sin(beta_freq * 2 * np.pi * time)
    theta_wave = np.sin(theta_freq * 2 * np.pi * time)
    delta_wave = np.sin(delta_freq * 2 * np.pi * time)
    simulated_data = (
        2 * alpha_wave
        + 1 * beta_wave
        + 0.5 * theta_wave
        + 0.2 * delta_wave
        + noise_level * np.random.normal(size=length)
    )
    return simulated_data

def plot_eeg_data(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data, label='Simulated EEG Data')
    plt.title('Simulated EEG Data Visualization')
    plt.xlabel('Time (ms)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)
    plt.savefig('eeg_plot.png')  
    plt.show()

def interpret_eeg_data(data):
    mean_value = np.mean(data)
    std_deviation = np.std(data)
    fft_result = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(data))
    dominant_freq = np.abs(freqs[np.argmax(np.abs(fft_result))]) * 256  
    print("Mean Value:", mean_value)
    print("Standard Deviation:", std_deviation)
    print("Dominant Frequency Component (Hz):", dominant_freq)

def main():

    simulated_data = generate_simulated_eeg_data()

    plot_eeg_data(simulated_data)

    interpret_eeg_data(simulated_data)

if __name__ == "__main__":
    main()
