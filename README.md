## Breath Classifier

### 프로젝트 기간
2019-05-01 ~ 2019-05-10

### 프로젝트 설명
호흡수 체크를 위한 파이썬 코드

1. breath_data 폴더 내에 존재하는 wav 파일을 읽어들임
```python
sample_frequency, signalData = wavfile.read('breath_data/breath_' + str(i)+ '.wav')
```

2. 데이터 프레임의 값들을 이용한 이동평균 계산
```python
sample_frequency, signalData = wavfile.read('breath_data/breath_' + str(i)+ '.wav')
```

3. 피크 속성을 기준으로 피크점 찾기
인접 피크 사이의 샘플에서 필요한 최소 수평 거리 속성 
```python
from scipy.signal import find_peaks
max = np.max(rolling_mean[samplerate * 1:samplerate * 60])
max = int(max)
peaks2, properties = find_peaks(rolling_mean, distance=samplerate, prominence=(mean / 7, max))    
```
