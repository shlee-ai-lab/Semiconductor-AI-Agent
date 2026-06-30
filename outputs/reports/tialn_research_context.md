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

## 6. Relevant Knowledge

### literature

- No relevant knowledge found.

### experiments

- No relevant knowledge found.

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

## 7. Generated Figures

- Figure 1: `outputs/figures/al_ti_vs_rs.png`
- Figure 2: `outputs/figures/c_ti_vs_rs.png`

## 8. Requested AI Output

Please write the following sections in Korean technical research style:

1. Results summary
2. Discussion
3. Possible mechanism
4. How the current result relates to the retrieved knowledge
5. Limitations of the current dataset
6. Recommended next experiments
7. One-slide PPT message
