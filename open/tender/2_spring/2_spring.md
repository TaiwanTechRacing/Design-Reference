---
layout: base
---

# 雙彈簧串聯剛性分析

[Download Code](2_spring.py)

## 簡介

本分析用於計算 main spring 與 tender spring 串聯時的等效剛性。程式固定 main spring 剛性，並讓 tender spring 剛性在 main spring 的 30% 到 70% 之間掃描，觀察 tender 選型對初段總剛性的影響。

Tender spring 與 main spring 串聯時，等效剛性會明顯低於 main spring。本工具可用於快速評估 tender 比例是否會讓初段懸吊過軟，或是否能提供預期的低載荷 compliance。

## 參數

以下為計算中所採用的物理量與符號說明：

| 變數名稱 | 物理意義 | 單位 |
| --- | --- | --- |
| `k_main` | 主彈簧剛性 ($k_{main}$) | $N/m$ |
| `ratio` | Tender 剛性相對於主彈簧剛性的比例 | 無因次 |
| `k_tender` | Tender 彈簧剛性 ($k_{tender}$) | $N/m$ |
| `k_eq` | 串聯後等效剛性 ($k_{eq}$) | $N/m$ |

## 計算

### 1. Tender 剛性掃描

程式將 tender spring 剛性設定為 main spring 的固定比例：

$$k_{tender} = ratio \cdot k_{main}$$

其中 `ratio` 掃描範圍為 $0.3 \sim 0.7$。

### 2. 串聯彈簧等效剛性

兩個彈簧串聯時，在相同受力 $F$ 下總位移為兩個彈簧位移相加：

$$x_{total} = \frac{F}{k_{main}} + \frac{F}{k_{tender}}$$

因此等效剛性為：

$$k_{eq} = \frac{k_{main} k_{tender}}{k_{main} + k_{tender}}$$

等效剛性也可與 main spring 剛性相比，用來觀察初段剛性降低比例：

$$\frac{k_{eq}}{k_{main}} \times 100\%$$

### 3. 設計策略

Tender spring 的切換點可依照車輛需求分成三種策略：

1. **常態作法**：車重下壓後就幾乎切換至 main spring，tender 主要用於吸收低速路面震動。
2. **平衡作法**：在工作行程約一半處切換，平衡路面吸收與空力平台控制。
3. **空力作法**：高下壓或大姿態變化時才切換，讓高速時具備更高 heave 剛性與防觸底能力。

不論採用哪一種策略，因為 tender 與 main spring 串聯的物理機制，切換前後通常會產生兩倍以上的剛性差距。因此切換點不只影響行程使用量，也會影響車手對車輛支撐性的感受。

## 結果

程式會顯示兩張圖：

1. Tender spring 剛性與串聯等效剛性的關係。
2. Tender 剛性比例與等效剛性比例的關係。

結果可用來判斷 tender spring 若設定為 main spring 的 30% 到 70%，初段懸吊總剛性會降低到什麼程度。
