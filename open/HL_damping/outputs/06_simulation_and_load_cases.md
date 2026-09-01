---
layout: base
---

# 工況與 ODE 時域模擬

## 參數

| 變數名稱 | 物理意義 | 單位 |
| --- | --- | --- |
| $W$ | 車輛重量 | $N$ |
| $W_s$ | 簧上重量 | $N$ |
| $a_x$ | 縱向加速度，以 $g$ 為單位 | 無因次 |
| $a_y$ | 側向加速度，以 $g$ 為單位 | 無因次 |
| $h_{cg}$ | 重心高度 | $m$ |
| $h_{ra}$ | 重心到 roll axis 的距離 | $m$ |
| $L$ | 軸距 | $m$ |
| $t$ | 輪距 | $m$ |
| $k_s$ | 彈簧本體剛性 | $N/m$ |
| $k_w$ | Heave wheel rate | $N/m$ |
| $k_{ride}$ | 輪胎串聯後 ride rate | $N/m$ |
| $MR_h$ | Heave motion ratio | 無因次 |
| $MR_r$ | Roll motion ratio | 無因次 |
| $K_{\phi}$ | 實際 roll stiffness | $N \cdot m/rad$ |
| $K_{\phi,s}$ | 懸吊 roll stiffness | $N \cdot m/rad$ |
| $z_s,z_u$ | 簧上與簧下位移 | $m$ |
| $F_d$ | 阻尼器力 | $N$ |

## 計算

### 1. 縱向載重轉移

加速與煞車會因重心高度產生前後軸載重轉移：

$$
\Delta F_x
=
\frac{W a_x h_{cg}}{L}
$$

若 $a_x>0$ 代表加速，前軸減載、後軸增載；若 $a_x<0$ 代表煞車，前軸增載、後軸減載。以前軸為例，可寫為：

$$
F_{s,f}
=
F_{s,f,0}
-
\Delta F_x
$$

後軸則為：

$$
F_{s,r}
=
F_{s,r,0}
+
\Delta F_x
$$

### 2. Heave spring stroke 與 spring force

彈簧作動量由整軸簧上載重與 heave wheel rate 得到：

$$
x_{spring}
=
\frac{F_s}{k_w}MR_h
$$

彈簧力為：

$$
F_{spring}
=
k_s x_{spring}
$$

此處 $x_{spring}$ 是彈簧本體位移，不是輪端位移，因此需要乘上 motion ratio。

### 3. Pitch 角

Pitch 角使用前後軸 ride rate 計算由載重轉移造成的前後車高變化：

$$
\Delta z_f
=
\frac{-\Delta F_x}{k_{ride,f}}
$$

$$
\Delta z_r
=
\frac{\Delta F_x}{k_{ride,r}}
$$

因此 pitch 角為：

$$
\theta
=
\tan^{-1}
\left(
\frac{\Delta z_f-\Delta z_r}{L}
\right)
$$

### 4. 側向 roll 角

側向加速度造成 roll moment：

$$
M_{\phi}=Wa_yh_{ra}
$$

全車 roll angle：

$$
\phi
=
\frac{M_{\phi}}{K_{\phi,total}}
$$

因輪胎與懸吊串聯，懸吊彈簧實際承擔的相對 roll angle 為：

$$
\phi_{rel}
=
\frac{K_{\phi}}{K_{\phi,s}}\phi
$$

Roll spring stroke：

$$
x_{roll}
=
MR_r t\phi_{rel}
$$

Roll spring force：

$$
F_{roll}
=
k_{s,r}x_{roll}
$$

### 5. ODE 時域模型

每一個 heave 軸或單輪模型使用狀態：

$$
\mathbf{x}
=
\begin{bmatrix}
z_s & \dot{z}_s & z_u & \dot{z}_u
\end{bmatrix}^T
$$

運動方程為：

$$
m_s\ddot{z}_s
=
F_{ext}
-
k_w(z_s-z_u)
-
F_dMR
$$

$$
m_u\ddot{z}_u
=
k_w(z_s-z_u)
+
F_dMR
-
k_tz_u
$$

阻尼器速度由相對速度與 motion ratio 換算：

$$
v_d
=
(\dot{z}_s-\dot{z}_u)MR
$$

再將 $v_d$ 帶入 bilinear damper curve 得到 $F_d$。

## 結果

<div style="text-align: center;">
<img src="ode_acceleration_1p2g.png" alt="image" width="800">
</div>

加速 ODE 圖顯示前後軸簧上位移與 pitch angle 的暫態變化，可用於判斷 squat 反應與收斂速度。

<div style="text-align: center;">
<img src="ode_braking_1p7g.png" alt="image" width="800">
</div>

煞車 ODE 圖顯示 dive 反應的暫態變化，重點是 pitch 峰值、穩態角度與前後軸位移方向。

<div style="text-align: center;">
<img src="nonlinear_acceleration_1p2g_comparison.png" alt="image" width="800">
</div>

此圖比較 decoupled model 與 independent model 在加速工況下的時域反應。

<div style="text-align: center;">
<img src="nonlinear_braking_1p7g_comparison.png" alt="image" width="800">
</div>

此圖比較 decoupled model 與 independent model 在煞車工況下的時域反應。

<div style="text-align: center;">
<img src="ode_braking_tire_fz.png" alt="image" width="800">
</div>

輪胎法向力圖可用於檢查煞車時前後輪載重轉移建立的暫態過程。

<div style="text-align: center;">
<img src="fig_decoupled_longitudinal_accel_brake_ode45.png" alt="image" width="800">
</div>

此圖將 decoupled model 的煞車與加速反應放在同一張圖中，方便比較 pitch 方向、峰值與收斂。

## 歷史輸出

以下圖片為資料夾中保留的舊工況輸出，主要用於和新設定做差異比對。

<div style="text-align: center;">
<img src="ode_braking_1p6g.png" alt="image" width="800">
</div>

<div style="text-align: center;">
<img src="nonlinear_braking_1p6g_comparison.png" alt="image" width="800">
</div>
