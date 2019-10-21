import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.io.wavfile import write
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks

file_path = 'breath_data/breath_'





for i in range(23) :

    sample_frequency, signalData = wavfile.read('breath_data/breath_' + str(i)+ '.wav')

    # plt.plot(signalData)
    # plt.show()


    df = pd.DataFrame(signalData)
    df = df.abs()
    # print(df)
    # plt.plot(df)
    # plt.show()

    rolling_mean = df.rolling(window=10000).mean()
    rolling_mean2 = df.rolling(window=50).mean()

    # plt.plot(df, label='11')
    # plt.show()
    # plt.plot(rolling_mean, label='22', color='orange')
    # plt.show()
    # plt.plot(rolling_mean2, label='33', color='magenta')
    #
    # plt.show()

    samplerate = 44100
    # write('breath_test_0' + '.wav', samplerate, rolling_mean)


    rolling_mean = rolling_mean.values.flatten()
    # arr1 = np.delete(rolling_mean, [0,1], axis=0)
    # arr1 = arr1.ravel()

    # x = electrocardiogram()[2000:4000]

    # print(np.mean(rolling_mean[samplerate*1:samplerate*60]))
    #
    # print(rolling_mean)


    t = 1 / samplerate
    te = 60
    t = np.arange(0, te, t)  # Time vector

    plt.subplot(311)
    plt.plot(t, signalData)

    # plt.subplot(412)
    # peaks, _ = find_peaks(rolling_mean, distance=samplerate*2, height=0)
    # plt.plot(rolling_mean)
    # plt.plot(peaks, rolling_mean[peaks], "x")
    # plt.plot(np.zeros_like(rolling_mean), "--", color="gray")
    #
    # plt.subplot(413)
    # peaks1, properties = find_peaks(rolling_mean, prominence=(104, samplerate))
    # properties["prominences"].max()
    # plt.plot(rolling_mean)
    # plt.plot(peaks1, rolling_mean[peaks1], "x")
    # # plt.show()
    plt.subplot(312)
    mean = np.mean(rolling_mean[samplerate * 1:samplerate * 60])

    mean = int(mean)
    max = np.max(rolling_mean[samplerate * 1:samplerate * 60])
    max = int(max)
    peaks2, properties = find_peaks(rolling_mean, distance=samplerate, prominence=(mean / 7, max))
    properties["prominences"].max()
    plt.plot(t, rolling_mean)
    # plt.plot(peaks2, rolling_mean[peaks2], "x")

    plt.subplot(313)
    # print(mean)
    # mean = int(mean)
    # max = int(max(rolling_mean[samplerate*1:samplerate*60]))
    plt.plot(rolling_mean)
    plt.plot(peaks2, rolling_mean[peaks2], "x")

    print('index = ', i, ', mean = ', mean, ', breath_num = ', len(peaks2))
    plt.show()
    # print(len(peaks2))
