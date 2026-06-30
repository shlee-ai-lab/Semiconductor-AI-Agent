import pandas as pd

print("=" * 50)
print("Semiconductor AI Agent v0.1")
print("=" * 50)

# CSV 읽기
df = pd.read_csv("data/tialn_dataset.csv")

print("\n데이터를 성공적으로 읽었습니다.\n")

print(df)

print("\n총 Sample 개수 :", len(df))