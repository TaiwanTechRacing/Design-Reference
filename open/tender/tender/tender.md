---
layout: base
---

# Tender Heave 與 Pitch 行程分析

[Download Code](tender.py)

## 簡介

本分析建立 main spring 與 tender spring 串聯後的分段剛性模型，用於估算不同空力下壓力與煞車加速度下的前後懸吊行程、車輛 heave 位移與 pitch 角。Tender 在未壓到底前會與 main spring 串聯，使初段剛性降低；當 tender bind 後，系統則切換為 main spring 主導。

此工具適合用於評估 tender spring 是否會在空力下壓力或煞車負載轉移下過早壓滿，以及切換到 main spring 後是否造成 heave / pitch 梯度突變。對於需要穩定空力平台的車輛，這類分析可作為 tender 行程與剛性選型的初步依據。

## 參數

以下為計算中所採用的物理量與符號說明：

| 變數名稱 | 物理意義 | 單位 |
| --- | --- | --- |
| `m_car` | 車輛總質量 ($m$) | $kg$ |
| `g` | 重力加速度 ($g$) | $m/s^2$ |
| `W_total` | 車輛總重量 ($W$) | $N$ |
| `k_main_heave` | Main heave 彈簧剛性 ($k_{main}$) | $N/mm$ |
| `k_tender_heave` | Tender heave 彈簧剛性 ($k_{tender}$) | $N/mm$ |
| `k_total_heave` | Tender 與 main 串聯後初段等效剛性 | $N/mm$ |
| `wheelbase` | 車輛軸距 ($L$) | $m$ |
| `h_cg` | 重心高度 ($h_{CG}$) | $m$ |
| `front_weight_dist` | 前軸重分配比例 | 無因次 |
| `anti_dive` | 抗俯仰幾何比例 | 無因次 |
| `tender_max_stroke` | Tender 可壓縮最大行程 | $mm$ |
| `downforce_ratios` | 掃描的下壓力比例 | 無因次 |
| `a_x_list` | 掃描的煞車加速度 | $g$ |

## 計算

### 1. 初段串聯剛性

Tender 未壓滿前，main spring 與 tender spring 為串聯關係，heave 初段等效剛性為：

$$k_{total} = \frac{k_{main} k_{tender}}{k_{main} + k_{tender}}$$

程式先以 $10\%$ 車重的下壓力量估算初段會吃掉的 heave 行程：

$$F_{down,10\%} = 0.1 W_{total}$$

$$x_{heave,10\%} = \frac{F_{down,10\%}}{k_{total}}$$

此行程被用作 tender 的最大可壓縮行程估計值。

### 2. Tender bind 前後的分段力模型

當總彈簧位移 $x$ 尚未使 tender 壓到底時，彈簧力由串聯等效剛性決定：

$$F = k_{eq} x$$

Tender 達到最大行程時，對應的 bind force 為：

$$F_{bind} = k_{tender} x_{tender,max}$$

當總位移超過 bind 位移後，後續行程由 main spring 主導，系統進入較高剛性的第二階段。

### 3. 煞車負載轉移

煞車加速度造成前後軸負載轉移，程式以重心高度與軸距計算：

$$\Delta W = \frac{m a_x g h_{CG}}{L}$$

若有 anti-dive 幾何，負載轉移再乘上修正係數：

$$\Delta W_{eff} = \Delta W(1 - anti\_dive)$$

### 4. 前後懸吊平衡求解

在指定下壓力與煞車加速度下，程式求解前後行程 $x_f, x_r$，使垂直力與 pitch moment 同時平衡：

$$F_f + F_r = F_{total}$$

$$F_f - F_r = 2\Delta W_{eff}$$

求解後，車輛 heave 由前後行程平均得到：

$$heave = \frac{x_f + x_r}{2}$$

Pitch 角由前後行程差與軸距換算：

$$\theta_{pitch} = \tan^{-1}\left(\frac{x_f - x_r}{L \cdot 1000}\right)$$

### 5. Pitch gradient

程式最後對 pitch 角相對煞車加速度取數值梯度，用來觀察車輛 pitch 對煞車加速度的敏感度：

$$\frac{d\theta}{da_x}$$

## 結果

程式會顯示兩組圖：

1. 前懸吊行程、後懸吊行程、整車 heave 與 pitch 角，並比較不同下壓力比例下隨煞車加速度變化的趨勢。
2. Pitch gradient 對煞車加速度的關係，用於觀察 tender bind 前後是否造成 pitch 響應斜率改變。

結果可用來檢查 tender 設定是否在目標下壓力或煞車狀態下過早壓滿，也可評估懸吊平台在空力負載與縱向負載轉移下是否維持穩定。由於程式目前未儲存圖片檔，若需要將結果放入文件頁面，可先輸出圖檔後再於此段落加入置中圖片。
