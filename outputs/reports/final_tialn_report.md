# Final TiAlN Research Report

## Part 1. Research Context

# SERA Research Context Package

## 1. Project Information

Project: TiAlN gate metal for advanced GAA/CFET devices

Research Goal:
- Evaluate TiAlN as a gate metal candidate for advanced GAA/CFET devices.
- Understand the relationship between process variables, composition, structure, and electrical properties.

## 2. Dataset Summary

- **sample_count**: 3
- **columns**: ['Sample_ID', 'Substrate', 'TiN_AlN_Ratio', 'Temperature_C', 'Thickness_nm', 'Al_Ti', 'C_Ti', 'N_Ti', 'O_Ti', 'Rs_ohm_sq', 'Work_Function_eV', 'Note']
- **missing_values**: 3
- **substrates**: ['SiO2']
- **temperatures_C**: [350]
- **ratios**: ['1:1', '2:1', '5:1']
- **average_rs_ohm_sq**: 253.33
- **min_rs_ohm_sq**: 190
- **max_rs_ohm_sq**: 320
- **average_al_ti**: 0.247
- **average_c_ti**: 0.203
- **average_n_ti**: 1.037
- **average_o_ti**: 0.077
- **average_work_function_eV**: 4.55

## 3. Data Profile

- **process**
  - Detected: True
  - Matched columns: ['Temperature_C', 'TiN_AlN_Ratio', 'Thickness_nm']
- **composition_xps**
  - Detected: True
  - Matched columns: ['Al_Ti', 'C_Ti', 'N_Ti', 'O_Ti']
- **electrical**
  - Detected: True
  - Matched columns: ['Rs_ohm_sq', 'Work_Function_eV']
- **structure**
  - Detected: False
  - Matched columns: []

## 4. Correlation Summary

- **Al_Ti_vs_Rs_ohm_sq**: 0.994
- **C_Ti_vs_Rs_ohm_sq**: 0.996
- **N_Ti_vs_Rs_ohm_sq**: 0.916
- **O_Ti_vs_Rs_ohm_sq**: 0.987
- **Al_Ti_vs_Work_Function_eV**: -0.988
- **C_Ti_vs_Work_Function_eV**: -0.999
- **N_Ti_vs_Work_Function_eV**: -0.897
- **O_Ti_vs_Work_Function_eV**: -0.993

## 5. Research Planner Output

- **Analysis**: Composition vs Electrical Property Analysis
  - Priority: High
  - Reason: XPS-derived composition and electrical data are both available.
  - Methods:
    - Al/Ti vs Rs correlation
    - C/Ti vs Rs correlation
    - O/Ti vs Rs correlation
    - N/Ti vs Rs correlation
- **Analysis**: Al incorporation effect
  - Priority: High
  - Reason: Al/Ti ratio and Rs data are available.
  - Methods:
    - Check whether Al incorporation improves or degrades conductivity.
    - Evaluate trade-off between work function tuning and resistance.
- **Analysis**: Carbon impurity effect
  - Priority: High
  - Reason: C/Ti ratio and Rs data are available.
  - Methods:
    - Assess whether carbon impurity increases resistance.
    - Connect precursor chemistry to electrical degradation.

## 6. Electrical Agent Report

- **Status**: Electrical data analyzed
- **Available electrical columns**: ['Rs_ohm_sq', 'Work_Function_eV']

### Electrical Summary

- **Rs_ohm_sq**
  - mean: 253.3333
  - min: 190
  - max: 320
  - std: 65.0641
- **Work_Function_eV**
  - mean: 4.55
  - min: 4.45
  - max: 4.65
  - std: 0.1

### Questions for Other Agents

- Material Agent: Check whether composition or impurity changes explain sheet resistance variation.
- Structure Agent: Check whether crystallinity, thickness, or interface quality explains sheet resistance variation.
- Material Agent: Check whether Al incorporation or interface dipole can explain work function shift.

## 7. Relevant Knowledge

### literature

- No relevant knowledge found.

### experiments

#### EXP-0001_TiAlN_Supercycle.md
- Path: `knowledge\experiments\EXP-0001_TiAlN_Supercycle.md`
- Match Score: 10

# EXP-0001

## Title
TiAlN supercycle ratio split experiment

## Project
TiAlN gate metal for advanced GAA/CFET devices

## Experiment Summary
TiAlN films were prepared using different TiN:AlN supercycle ratios to investigate the relationship between Al incorporation, impurity level, and sheet resistance.

## Key Variables
- TiN:AlN supercycle ratio
- Al/Ti ratio
- C/Ti ratio
- O/Ti ratio
- Sheet resistance

## Key Observation
Al incorporation changed the electrical properties of TiAlN. Carbon and oxygen impurities should be considered when interpreting sheet resistance trends.

## Related Metrics
- Al_Ti
- C_Ti
- O_Ti
- Rs_ohm_sq
- Work_Function_eV

## Tags
TiAlN, supercycle, XPS, sheet resistance, impurity, gate metal

### mechanisms

#### MECH-0001_TiAlN_WF_Rs_Tradeoff.md
- Path: `knowledge\mechanisms\MECH-0001_TiAlN_WF_Rs_Tradeoff.md`
- Match Score: 9

# MECH-0001

## Mechanism
TiAlN work function and sheet resistance may show a trade-off depending on Al incorporation.

## Explanation
Al incorporation can reduce effective work function, which may be beneficial for n-FET gate metal tuning. However, excessive Al precursor exposure may increase oxygen or carbon incorporation, leading to increased sheet resistance or degraded interface quality.

## Related Metrics
- Al/Ti ratio
- C/Ti ratio
- O/Ti ratio
- Sheet resistance
- Work function

## Suggested Experiments
- TiN:AlN supercycle ratio split
- XPS depth profiling
- UPS work function measurement
- HfO2/TiAlN MOSCAP C-V analysis

### failure_cases

#### FAIL-0001_TiAlN_Impurity_Rs.md
- Path: `knowledge\failure_cases\FAIL-0001_TiAlN_Impurity_Rs.md`
- Match Score: 8

# FAIL-0001

## Title
Possible sheet resistance degradation due to impurity incorporation in TiAlN

## Problem
TiAlN films may show increased sheet resistance when impurity incorporation becomes significant.

## Possible Causes
- Excess Al precursor exposure
- Carbon incorporation from metal-organic precursor
- Oxygen incorporation during or after deposition
- Interfacial reaction with HfO2 or SiO2
- Degraded crystallinity

## Warning Signs
- High C/Ti ratio
- High O/Ti ratio
- Increased Rs
- Poor reproducibility
- Strong substrate dependence

## Suggested Checks
- XPS composition and chemical state
- SIMS depth profile
- GIXRD crystallinity
- TEM interface analysis
- Repeat deposition for reproducibility

## Tags
TiAlN, impurity, carbon, oxygen, sheet resistance, failure case

### best_practices

#### BP-0001_TiAlN_Data_Interpretation.md
- Path: `knowledge\best_practices\BP-0001_TiAlN_Data_Interpretation.md`
- Match Score: 8

# BP-0001

## Title
Best practice for interpreting TiAlN gate metal data

## Guideline
TiAlN gate metal data should not be interpreted from a single metric. Composition, impurity, crystallinity, interface quality, and electrical properties should be interpreted together.

## Recommended Interpretation Flow
1. Confirm film thickness and uniformity.
2. Check Al/Ti ratio.
3. Check C/Ti and O/Ti impurity ratios.
4. Compare sheet resistance.
5. Compare work function or flat-band voltage.
6. Examine crystallinity by GIXRD.
7. Check interface quality by TEM or XPS depth profile.

## Important Caution
A lower work function is not always beneficial if sheet resistance or interface quality is significantly degraded.

## Tags
TiAlN, interpretation, gate metal, work function, sheet resistance, best practice

### writing_templates

- No relevant knowledge found.

## 8. Generated Figures

- Figure 1: `outputs\figures\al_ti_vs_rs.png`
- Figure 2: `outputs\figures\c_ti_vs_rs.png`

## 9. Requested AI Output

Please write the following sections in Korean technical research style:

1. Results summary
2. Discussion
3. Possible mechanism
4. How the current result relates to the retrieved knowledge
5. Limitations of the current dataset
6. Recommended next experiments
7. One-slide PPT message


---

## Part 2. AI Scientist Interpretation

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