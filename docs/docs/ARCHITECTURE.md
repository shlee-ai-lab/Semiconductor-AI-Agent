# SERA v1.0 Architecture

## 1. Project Goal

SERA는 반도체 연구 데이터를 읽고, 정리하고, 분석 계획을 세우고, AI 추론에 필요한 Research Context를 생성하는 개인 연구용 AI Agent이다.

최종 목표는 다음 흐름을 자동화하는 것이다.

Experiment Data  
→ Data Profiling  
→ Analysis Planning  
→ Python Analysis  
→ Figure Generation  
→ Research Context  
→ AI Reasoning  
→ Report / Paper / PPT

---

## 2. Core Principle

Python은 데이터 처리와 구조화를 담당한다.

AI는 과학적 해석, 가설 생성, 논문화 문장 작성을 담당한다.

---

## 3. System Layers

### Layer 1. Data Input

- CSV
- Excel
- XPS data
- XRD data
- TEM / SEM image metadata
- CV / IV data
- Literature summary
- Patent summary

### Layer 2. Data Profiler

역할:

- 데이터 컬럼 인식
- 데이터 종류 판단
- 공정 / 조성 / 전기 / 구조 데이터 분류

파일:

```text
src/profiler.py