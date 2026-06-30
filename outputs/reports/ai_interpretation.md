TiAlN Gate Metal 연구 결과 해석
1. Results Summary

본 연구에서는 SiO₂ 기판 상에 350 °C에서 증착된 TiAlN 박막(1:1, 2:1, 5:1 super-cycle)의 조성 변화와 전기적 특성 간의 상관관계를 분석하였다.

주요 결과는 다음과 같다.

TiN:AlN 비율이 증가함에 따라 Al/Ti 비와 함께 C/Ti 및 O/Ti 비도 동시에 증가하는 경향을 확인하였다.
Sheet resistance(Rs)는 약 190 Ω/sq에서 320 Ω/sq까지 증가하였으며, Al 함량 증가와 매우 높은 양의 상관관계(r≈0.994)를 나타냈다.
특히 C/Ti와 Rs 사이의 상관계수는 0.996으로 가장 높게 나타나, 탄소 불순물이 전기전도도 저하에 중요한 영향을 미칠 가능성을 시사하였다.
반면 Work Function은 평균 약 4.55 eV 수준이며, Al/Ti 및 C/Ti 증가에 따라 감소하는 경향(r≈−0.99)을 보였다.
따라서 TiAlN에서는 낮은 Work Function 확보와 높은 전기전도도 유지 사이의 trade-off가 존재할 가능성이 확인되었다.
2. Discussion

본 결과는 TiAlN의 Al 함량 증가가 단순히 조성을 변화시키는 것이 아니라, 박막 내 불순물 농도와 전기적 특성을 동시에 변화시키는 복합적인 현상임을 보여준다.

특히 Al precursor를 이용한 ALD에서는 일반적으로 Ti precursor보다 ligand 제거가 상대적으로 어렵기 때문에 carbon incorporation 가능성이 증가한다. 실제 본 데이터에서도 Al/Ti 증가와 함께 C/Ti가 거의 동일한 추세로 증가하였다.

또한 산소 역시 Al의 높은 산소 친화도(oxygen affinity)로 인해 쉽게 포함될 수 있으며, 이는 Ti–N 결합의 연속성을 저해하여 전도 경로를 감소시킬 가능성이 있다.

반면 Work Function은 Al 함량 증가에 따라 감소하였다. 이는 TiN 대비 TiAlN이 상대적으로 낮은 유효 일함수를 가지며, nMOS gate metal로의 적용 가능성을 시사한다.

그러나 Rs 역시 동시에 증가하므로,

Work Function tuning에는 유리하지만 conductivity는 저하되는 방향

이라는 점이 본 연구에서 가장 중요한 결과라고 판단된다.

GAA/CFET 구조에서는 gate electrode의 저항 증가가 RC delay 증가 및 device variability로 이어질 수 있으므로, Work Function만을 기준으로 TiAlN 조성을 결정하기는 어렵다.

3. Possible Mechanism

현재 데이터를 종합하면 다음과 같은 메커니즘을 제안할 수 있다.

(1) Al incorporation

↓

TiN lattice 일부가 Ti–Al–N 구조로 치환

↓

Band structure 변화

↓

Work Function 감소

(2) Al precursor 증가

↓

Ligand 제거 효율 감소

↓

Carbon incorporation 증가

↓

Carrier scattering 증가

↓

Sheet resistance 증가

(3) Oxygen incorporation

↓

Al–O 또는 Ti–O 결합 형성

↓

Conductive TiN network 감소

↓

Resistivity 증가

즉,

Rs 증가는 Al 자체보다는 Al과 함께 증가한 carbon 및 oxygen impurity의 영향이 더 클 가능성

이 존재한다.

현재 상관계수만으로는 인과관계를 구분하기 어렵지만,

Carbon의 상관성이 가장 높다는 점은 향후 중요한 연구 방향을 제시한다.

4. Limitations of Current Dataset

현재 데이터는 초기 스크리닝 수준으로 다음과 같은 한계를 가진다.

① Sample 수가 3개

통계적 유의성 확보 어려움

② 단일 기판(SiO₂)

실제 HKMG에서는
HfO₂
IL/HfO₂
annealed HfO₂

에서의 거동이 더욱 중요하다.

③ 단일 증착온도(350°C)

온도에 따른

impurity removal
crystallinity
resistivity

효과를 평가할 수 없다.

④ Work Function 데이터 부족

MOSCAP 기반의

Vfb
EOT correction
Effective Work Function

검증이 추가적으로 필요하다.

⑤ Correlation ≠ Causation

Al과 Carbon이 동시에 증가하므로

Rs 증가가

Al 때문인지
Carbon 때문인지

현재 데이터만으로는 분리할 수 없다.

5. Recommended Next Experiments

연구의 다음 단계에서는 변수 분리를 목표로 한 실험 설계가 필요하다.

(1) Temperature Series

300

325

350

375

400°C

↓

Carbon 제거 효과 확인

(2) NH₃ Exposure Time

Ligand removal 최적화

↓

Carbon 감소 여부 확인

(3) Plasma-assisted ALD

Thermal ALD

↓

PEALD 비교

↓

Carbon 제거 효과 확인

(4) H₂ Radical Post-treatment

현재 진행 중인 연구와 연결하여

Carbon 제거 가능성 평가

단, 산화 방지를 위해 in-situ 공정 구성이 바람직하다.

(5) Electrical Characterization

추가 측정 권장

Resistivity
Hall measurement
UPS
Kelvin Probe
MOSCAP C–V
XPS depth profile
TEM/EELS
GIXRD
(6) Substrate Expansion
Si
SiO₂
HfO₂
Annealed HfO₂

동일 조성 비교

↓

Interface effect 분리

6. One-slide PPT Message
Key Message

Al incorporation in TiAlN effectively lowers the work function but simultaneously increases sheet resistance through concurrent carbon/oxygen incorporation, indicating a critical trade-off between work function engineering and electrical conductivity for advanced GAA/CFET gate metal applications.

핵심 포인트
Al 증가 → Work Function 감소
Al 증가와 함께 C/O impurity 증가
C/O 증가 → Sheet Resistance 증가
TiAlN은 nMOS gate metal 후보로 유망
향후 과제는 Work Function은 유지하면서 Carbon/Oxygen을 최소화하는 공정 최적화
연구자 관점에서의 추가 해석

현재 데이터에서 가장 눈에 띄는 점은 Al/Ti, C/Ti, O/Ti가 거의 동시에 변화한다는 것입니다. 따라서 상관계수만 보면 모두 Rs와 매우 높은 상관성을 보이지만, 이는 공선성(collinearity) 때문일 가능성이 큽니다. 현 단계에서 "Al이 Rs를 증가시킨다" 또는 "Carbon이 원인이다"라고 단정하기보다는,

Al은 Work Function 조절의 주된 변수이고,
Carbon/Oxygen은 전도도 저하의 주된 변수라는 가설을 세운 뒤,

후속 실험에서 Al 함량은 유지한 채 Carbon만 줄이는 조건(예: NH₃ 노출 최적화, 플라즈마 ALD, in-situ H₂ 라디칼 처리)을 비교하면 인과관계를 훨씬 명확하게 검증할 수 있습니다. 이러한 접근이 TiAlN을 실제 GAA/CFET HKMG용 gate metal로 최적화하는 핵심 연구 방향이 될 것입니다.