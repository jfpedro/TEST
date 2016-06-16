# from pylab import*
from numpy import*
import matplotlib.pyplot as plt

def Main():

    time = arange(0, 6, 0.01) # dominio do tempo

    # x is the original signal
    x = []
    
    for t in time:
        x.append(0.5*sin(15.0*t)+0.33*cos(20.0*t)+1.0*cos(50*t + 2.0) +5.0*sin(1.5*t)+3.0*cos(2.0*t + 0.3))

    fft_x = fft.fft(x)
    freq = 2*pi*fft.fftfreq(len(fft_x), d = 0.01) # frequency domain is symmetric

    #find maxima of the spectrum

    freq_max = []

    for i in range(1, len(fft_x) - 1):
        
        if fft_x[i] > fft_x[i+1] and fft_x[i] > fft_x[i-1]:
            freq_max.append(freq[i])
    
    #generate filter
    filter1 = [1.0 if abs(freq[n]) < freq_max[1] - 0.25*freq_max[1] else 0.0 for n in range(0, len(freq)) ] # this filter was generated roughly

    new_fft_x = fft_x * filter1
    plt.subplot(211)
    plt.plot(freq, fft_x)
    plt.plot(freq, new_fft_x)

    new_x = fft.ifft(new_fft_x)

    plt.subplot(212)
    plt.plot(time, new_x)  
    plt.plot(time, x)

    plt.show()

    return 'OK'

if __name__ == '__main__':
    
    Main()