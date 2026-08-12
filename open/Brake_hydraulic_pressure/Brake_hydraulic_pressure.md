---

## layout: base

# 煞車油管高低膨脹特性二階多項式擬合與評估（Brake Line Expansion Characteristics & Polynomial Fitting）計算與分析說明

## 簡介

本分析旨在探討 **煞車軟管（Brake Line / Hose）** 在不同內部油壓作用下的**體積膨脹特性（Volumetric Expansion）**。在煞車系統設計中，軟管在受壓時的體積膨脹會吸收部份煞車油量，導致踏板行程變長與腳感變軟（Pedal Sponginess）。

本程式讀取實驗量測數據（`brake_line_data.csv`），針對**低膨脹率軟管（Low Expansion Tube）**與**高膨脹率軟管（High Expansion Tube）**分別進行**二階多項式迴歸擬合（2nd-Order Polynomial Fitting）**，並計算在目標工作壓力（$5.67\text{ MPa}$，約為典型煞車工作點）下軟管的每米體積膨脹量（$\text{mm}^3/\text{m}$），作為液壓系統容積效率評估之依據。

## 參數

以下為計算中所採用的物理量與符號說明：

| 變數名稱 | 物理意義 | 單位 |
| --- | --- | --- |
| `pressure_target` | 評估目標管路壓力 ($P_{target} = 5.67$) | $MPa$ |
| `pl`, `ph` | 低膨脹與高膨脹軟管之實驗油壓數據點 ($P$) | $MPa$ |
| `cl`, `ch` | 低膨脹與高膨脹軟管之實驗膨脹係數數據點 ($C$) | $mm^3/m$ |
| `nl`, `nh` | 二階多項式擬合係數向量 ($[a, b, c]$) | - |
| `cl_target`, `ch_target` | 目標壓力下推算之軟管每米膨脹量 ($C_{target}$) | $mm^3/m$ |

## 計算

> 參考汽車煞車系統標準 : SAE J1401 / ISO 3996 *Road vehicles — Brake hose assemblies for hydraulic braking systems*

### 1. 二階多項式最小二乘擬合 (2nd-Order Polynomial Fitting)

橡膠與複合纖維煞車軟管的體積膨脹與內部油壓呈非線性關係，選用二階多項式進行擬合：

$$C(P) = a \cdot P^2 + b \cdot P + c$$

利用 `numpy.polyfit(P, C, 2)` 進行過度確定方程組之最小二乘求解，導出拟合係數 $a, b, c$。

### 2. 特徵點計算與內插評估

將擬合多項式在工作壓力區間 $0 \sim 20\text{ MPa}$（時間步長 $0.1\text{ MPa}$）進行連續插值，並在指定目標點 $P_{target} = 5.67\text{ MPa}$ 處帶入多項式估算單位長度膨脹量：

$$C_{target} = \text{polyval}(n, P_{target}) = a \cdot (5.67)^2 + b \cdot (5.67) + c$$

此數據可用於後續計算總煞車油耗量與主缸行程容積需求。

## 結果

由此圖與計算結果可以觀察到：

1. **二次曲線適應性**：實線展示了二階多項式能夠極佳地擬合實測數據點（Measured Data），精準呈現油壓越高時管路變形剛度與膨脹速率的變化規律。
2. **高低膨脹管對比**：在 $5.67\text{ MPa}$ 目標壓力下，標註點清晰呈現了低膨脹管（Low Expansion）與高膨脹管（High Expansion）的體積膨脹差異。選用低膨脹金屬編織軟管（Metal Braided Line）可顯著降低油路容積損失，提升煞車踏板的剛性與響應速度。