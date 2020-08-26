#%% 
# 参考url：https://www.cnblogs.com/LXP-Never/p/10918590.html
# 信息读取
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
from scipy.fftpack import dct

# 读取声音波形
sample_rate, signal = wavfile.read('demo.wav')
signal = signal[0:int(3.5 * sample_rate)]

# 显示图片
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.plot(signal)

# %%
# 预加重 Pre-Emphasis 
# 高通滤波器
pre_emphasis =0.97

emphasized_signal = np.append(0,signal[1:] - pre_emphasis * signal[:-1])
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.plot(emphasized_signal)


# %%
# Framing 分帧
frame_size = 0.025 # 采样率是8000，那么这一帧有200个采样
frame_stride = 0.01 # 步长是80个采样点
overlap=0.015 # 重叠120个采样点

# time -> sample point
frame_length, frame_step = frame_size * sample_rate, frame_stride * sample_rate  
signal_length = len(emphasized_signal)
frame_length = int(round(frame_length))
frame_step = int(round(frame_step))

# 保证有一帧
num_frames = int(np.ceil(float(np.abs(signal_length - frame_length)) / frame_step))  
# num_frames = 210

# 增加一个完整的整帧周期，使其能够整除frame_length
pad_signal_length = num_frames * frame_step + frame_length

# 创建剩余空容器
z = np.zeros((pad_signal_length - signal_length))

# 拼接完整的信号
pad_signal = np.append(emphasized_signal, z) 

# 左半部分，bias,创建 210 行的帧，其中每帧 200 个sample
# 右半部分，起点,创建 200 行的，起始采样点[0 80 160 ..]
indices = np.tile(np.arange(0, frame_length),(num_frames, 1)) + \
    np.tile(np.arange(0, num_frames * frame_step, frame_step), (frame_length, 1)).T

# 过滤
frames = pad_signal[indices.astype(np.int32, copy=False)]


# %%
# Window 加窗

frames *= np.hamming(frame_length)

# hamming window 例子
# ham = lambda n,N:0.54 - 0.46 * np.cos((2 * np.pi * n) / (N - 1))
# for i in range(10): print(ham(i,10))

# %%
# Fourier-Transform
NFFT = 512
mag_frames = np.absolute(np.fft.rfft(frames, NFFT))

# plt.imshow(mag_frames)

# %%
# Power Spectrum 功率谱
pow_frames = ((1.0 / NFFT) * ((mag_frames) ** 2))

# %%
# Filter Banks 滤波器组

nfilt = 40 # 滤波器组数
low_freq_mel = 0
high_freq_mel = (2595 * np.log10(1 + (sample_rate / 2) / 700)) # 确定mel频率

# 40个滤波器组，需要42个点，意味着在low_freq_mel和high_freq_mel之间间隔40个点
mel_points = np.linspace(low_freq_mel, high_freq_mel, nfilt + 2)
# 将Mel转换回-Hz
hz_points = (700 * (10 ** (mel_points / 2595) - 1))

# 本段较难，有之后需要分析的，再回来
# 计算每个hz点，有多少个frequ bin
bins = np.floor((NFFT + 1) * hz_points / sample_rate)

fbank = np.zeros((nfilt, int(np.floor(NFFT / 2 + 1))))
for m in range(1, nfilt + 1):
    f_m_minus = int(bins[m - 1])  # 左
    f_m = int(bins[m])  # 中
    f_m_plus = int(bins[m + 1])  # 右

    for k in range(f_m_minus, f_m):
        fbank[m - 1, k] = (k - bins[m - 1]) / (bins[m] - bins[m - 1])
    for k in range(f_m, f_m_plus):
        fbank[m - 1, k] = (bins[m + 1] - k) / (bins[m + 1] - bins[m])
filter_banks = np.dot(pow_frames, fbank.T)
filter_banks = np.where(filter_banks == 0, np.finfo(float).eps, filter_banks)  # 数值稳定性
filter_banks = 20 * np.log10(filter_banks)  # dB

plt.imshow(filter_banks.T)
# %%
# 离散余弦变换（DCT）
num_ceps = 12
mfcc = dct(filter_banks, type=2, axis=1, norm='ortho')[:, 1 : (num_ceps + 1)] 
(nframes, ncoeff) = mfcc.shape
n = np.arange(ncoeff)
cep_lifter = 12
lift = 1 + (cep_lifter / 2) * np.sin(np.pi * n / cep_lifter)
mfcc *= lift

plt.figure(figsize = (20,2))
plt.imshow(mfcc.T)

# %%
