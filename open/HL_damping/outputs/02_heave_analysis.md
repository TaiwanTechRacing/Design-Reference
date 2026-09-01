---
layout: base
---

# Heave 分析

## 簡介

用於檢查 ride rate、heave natural frequency、step response 與頻率響應，並作為阻尼器初步定尺寸的基礎。

## 參數

| 變數名稱 | 物理意義 | 單位 |
| --- | --- | --- |
| $m_s$ | 該軸簧上質量 | $kg$ |
| $m_u$ | 該軸簧下質量 | $kg$ |
| $k_s$ | Heave 彈簧本體剛性 | $N/m$ |
| $MR_h$ | Heave motion ratio | 無因次 |
| $k_w$ | Heave 輪端剛性 | $N/m$ |
| $k_t$ | 單輪輪胎垂直剛性 | $N/m$ |
| $k_{t,a}$ | 整軸輪胎等效剛性 | $N/m$ |
| $k_{ride}$ | 輪胎串聯後的 ride rate | $N/m$ |
| $c_c$ | 臨界阻尼係數 | $N \cdot s/m$ |
| $\zeta$ | 目標阻尼比 | 無因次 |

## 計算

### 1. 彈簧本體剛性轉換為輪端剛性

懸吊彈簧安裝位置通常不在輪心，因此彈簧本體位移與輪端位移之間存在 motion ratio。若輪端位移為 $x_w$，彈簧位移可表示為：

$$
x_s = MR_h x_w
$$

由虛功關係，彈簧力與輪端力也會經由相同幾何轉換，因此輪端剛性為：

$$
k_w = k_s MR_h^2
$$

### 2. 輪胎與懸吊串聯

路面輸入會先經過輪胎，再傳到懸吊彈簧，因此輪胎與懸吊在垂直方向可視為串聯彈簧。整軸模型包含左右兩輪，因此整軸輪胎等效剛性為：

$$
k_{t,a}=2k_t
$$

串聯剛性滿足：

$$
\frac{1}{k_{ride}}
=
\frac{1}{k_w}
+
\frac{1}{k_{t,a}}
$$

整理後：

$$
k_{ride}
=
\frac{k_w k_{t,a}}{k_w+k_{t,a}}
$$

此結果會低於單純懸吊輪端剛性，因為輪胎柔度會消耗部分路面輸入位移。

### 3. Heave 自然頻率

對簧上 heave 主模態，可用 ride rate 與簧上質量估算自然頻率：

$$
\omega_n
=
\sqrt{\frac{k_{ride}}{m_s}}
$$

$$
f_n
=
\frac{\omega_n}{2\pi}
$$

此頻率可用於檢查前後軸 ride balance，也可作為阻尼比設定的參考。

### 4. 臨界阻尼與目標阻尼

臨界阻尼定義為：

$$
c_c=2\sqrt{k_wm_s}
$$

給定目標阻尼比 $\zeta$ 後，線性阻尼係數為：

$$
c=\zeta c_c
$$

若低速與高速阻尼使用不同阻尼比，則可分別得到 $c_{LS}$ 與 $c_{HS}$，並在 damper curve 中形成不同速度區段的斜率。

### 5. Heave state-space

Heave 模型使用兩自由度狀態：

$$
\mathbf{x}
=
\begin{bmatrix}
z_s & \dot{z}_s & z_u & \dot{z}_u
\end{bmatrix}^T
$$

其中 $z_s$ 為簧上位移，$z_u$ 為簧下位移。運動方程為：

$$
m_s\ddot{z}_s
=
-k_w(z_s-z_u)
-c(\dot{z}_s-\dot{z}_u)
$$

$$
m_u\ddot{z}_u
=
k_w(z_s-z_u)
+c(\dot{z}_s-\dot{z}_u)
-k_{t,a}(z_u-z_r)
$$

其中 $z_r$ 是路面輸入。整理為 state-space 後，可分析 step response 與 Bode plot。

## 結果

<div style="text-align: center;">
<img src="heave_front_step.png" alt="image" width="800">
</div>

前軸 step response 顯示路面階躍輸入後簧上位移的暫態收斂狀態，可用於檢查阻尼是否過低造成振盪，或過高造成反應過慢。

<div style="text-align: center;">
<img src="heave_front_bode.png" alt="image" width="800">
</div>

前軸 Bode plot 顯示路面位移到簧上位移的頻率響應，可用於辨識車體模態與輪胎/簧下模態。

<div style="text-align: center;">
<img src="heave_rear_step.png" alt="image" width="800">
</div>

後軸 step response 可與前軸比較，用於檢查前後 heave 阻尼設定是否造成明顯不同的暫態特性。

<div style="text-align: center;">
<img src="heave_rear_bode.png" alt="image" width="800">
</div>

後軸 Bode plot 可用於確認後軸 ride frequency 與簧下模態是否落在合理範圍。
