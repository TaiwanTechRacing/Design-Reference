---
layout: base
---

# Roll 分析


## 簡介

State-space 模型包含 sprung roll、front unsprung roll 與 rear unsprung roll 三個自由度，可比較理想 modal damping、實體前後 roll damper 拓樸，以及 1DOF 簡化模型之間的差異。

## 參數

| 變數名稱 | 物理意義 | 單位 |
| --- | --- | --- |
| $W$ | 車輛重量 | $N$ |
| $a_y$ | 側向加速度，以 $g$ 為單位 | 無因次 |
| $h_{cg}$ | 重心高度 | $m$ |
| $h_{rc,f}, h_{rc,r}$ | 前、後 roll center 高度 | $m$ |
| $h_{ra}$ | 重心到 roll axis 的距離 | $m$ |
| $t_f, t_r$ | 前、後輪距 | $m$ |
| $k_t$ | 單輪輪胎垂直剛性 | $N/m$ |
| $k_{s,r}$ | Roll 彈簧本體剛性 | $N/m$ |
| $MR_r$ | Roll motion ratio | 無因次 |
| $k_{w,r}$ | Roll 輪端剛性 | $N/m$ |
| $K_{\phi,s}$ | 懸吊側傾剛性 | $N \cdot m/rad$ |
| $K_{\phi,t}$ | 輪胎側傾剛性 | $N \cdot m/rad$ |
| $K_{\phi}$ | 串聯後實際側傾剛性 | $N \cdot m/rad$ |
| $I_{xx}$ | 簧上 roll 慣量 | $kg \cdot m^2$ |
| $J_u$ | 簧下 roll 等效慣量 | $kg \cdot m^2$ |

## 計算

### 1. Roll axis 力臂

前後 roll center 連成 roll axis。重心所在縱向位置的 roll axis 高度可用前後 roll center 線性內插：

$$
h_{ra,line}
=
h_{rc,f}
+
\lambda_r
\left(h_{rc,r}-h_{rc,f}\right)
$$

重心到 roll axis 的有效力臂為：

$$
h_{ra}
=
h_{cg}-h_{ra,line}
$$

側向加速度造成的 roll moment 為：

$$
M_{\phi}
=
W a_y h_{ra}
$$

### 2. 懸吊 roll stiffness

Roll 彈簧先轉換為輪端剛性：

$$
k_{w,r}=k_{s,r}MR_r^2
$$

由於 roll 是左右輪反向作動，輪距會成為力臂。懸吊側傾剛性可寫為：

$$
K_{\phi,s}
=
k_{w,r}t^2
$$

### 3. 輪胎 roll stiffness

輪胎垂直剛性也會提供側傾支撐。對單軸左右兩輪而言：

$$
K_{\phi,t}
=
\frac{k_t t^2}{2}
$$

### 4. 串聯後實際 roll stiffness

懸吊與輪胎會共同分擔側傾位移，因此可視為串聯彈簧：

$$
\frac{1}{K_{\phi}}
=
\frac{1}{K_{\phi,s}}
+
\frac{1}{K_{\phi,t}}
$$

整理後：

$$
K_{\phi}
=
\frac{K_{\phi,s}K_{\phi,t}}
{K_{\phi,s}+K_{\phi,t}}
$$

全車總側傾剛性為前後軸加總：

$$
K_{\phi,total}
=
K_{\phi,f}+K_{\phi,r}
$$

Roll gradient 則為：

$$
RG
=
\frac{180}{\pi}
\frac{W h_{ra}}{K_{\phi,total}}
$$

### 5. Roll modal analysis

三自由度 roll 模型定義為：

$$
\mathbf{q}
=
\begin{bmatrix}
\phi_s & \phi_{u,f} & \phi_{u,r}
\end{bmatrix}^T
$$

質量矩陣：

$$
\mathbf{M}
=
\begin{bmatrix}
I_{xx} & 0 & 0 \\
0 & J_{u,f} & 0 \\
0 & 0 & J_{u,r}
\end{bmatrix}
$$

剛性矩陣：

$$
\mathbf{K}
=
\begin{bmatrix}
K_{\phi,s,f}+K_{\phi,s,r} & -K_{\phi,s,f} & -K_{\phi,s,r} \\
-K_{\phi,s,f} & K_{\phi,s,f}+K_{\phi,t,f} & 0 \\
-K_{\phi,s,r} & 0 & K_{\phi,s,r}+K_{\phi,t,r}
\end{bmatrix}
$$

自然頻率由廣義特徵值問題求得：

$$
\mathbf{K}\mathbf{\Phi}
=
\mathbf{M}\mathbf{\Phi}\mathbf{\Lambda}
$$

$$
\omega_i=\sqrt{\lambda_i},
\qquad
f_i=\frac{\omega_i}{2\pi}
$$

Modal damping matrix 由目標阻尼比轉回物理座標：

$$
\mathbf{C}
=
\mathbf{M}\mathbf{\Phi}
\operatorname{diag}\left(2\zeta_i\omega_i\right)
\mathbf{\Phi}^{T}\mathbf{M}
$$

### 6. State-space response

狀態向量為：

$$
\mathbf{x}
=
\begin{bmatrix}
\mathbf{q} & \dot{\mathbf{q}}
\end{bmatrix}^T
$$

狀態方程：

$$
\dot{\mathbf{x}}
=
\begin{bmatrix}
\mathbf{0} & \mathbf{I} \\
-\mathbf{M}^{-1}\mathbf{K} & -\mathbf{M}^{-1}\mathbf{C}
\end{bmatrix}
\mathbf{x}
+
\mathbf{B}a_y
$$

輸出為 sprung roll angle：

$$
y=\phi_s
$$

## 結果

<div style="text-align: center;">
<img src="roll_step_response.png" alt="image" width="800">
</div>

此圖顯示不同阻尼模型在 roll step input 下的響應。若最終 roll angle 接近，但峰值與收斂時間不同，代表剛性設定一致，但阻尼拓樸改變了暫態行為。

<div style="text-align: center;">
<img src="roll_step_low_speed.png" alt="image" width="800">
</div>

低速阻尼 step response 用於觀察車身 roll 在較高阻尼設定下的收斂特性。

<div style="text-align: center;">
<img src="roll_step_high_speed.png" alt="image" width="800">
</div>

高速阻尼 step response 用於檢查阻尼降低時，是否出現較大的 overshoot 或較明顯的振盪。

<div style="text-align: center;">
<img src="roll_bode_modal.png" alt="image" width="800">
</div>

Modal Bode plot 用來觀察側向加速度輸入到 sprung roll angle 的頻率響應。

<div style="text-align: center;">
<img src="roll_bode_low_speed.png" alt="image" width="800">
</div>

低速阻尼 Bode plot 可用於檢查高阻尼設定下的 roll response 頻率放大。

<div style="text-align: center;">
<img src="roll_bode_high_speed.png" alt="image" width="800">
</div>

高速阻尼 Bode plot 可用於檢查較低阻尼設定是否讓 roll mode 的峰值更明顯。

<div style="text-align: center;">
<img src="roll_tire_fz_transient.png" alt="image" width="800">
</div>

輪胎法向力暫態圖可檢查過彎時內外輪載重轉移的建立過程，以及前後軸載重轉移是否平衡。

<div style="text-align: center;">
<img src="roll_1dof_step.png" alt="image" width="800">
</div>

1DOF roll step response 是較簡化的車身側傾模型，可作為阻尼器初步定尺寸的參考。

<div style="text-align: center;">
<img src="roll_1dof_bode.png" alt="image" width="800">
</div>

1DOF roll Bode plot 使用線性增益描述側向加速度到 roll angle 的關係，適合與靜態 roll gradient 共同判讀。

<div style="text-align: center;">
<img src="fig3_13_roll_step_1dof.png" alt="image" width="800">
</div>

此圖為 1DOF roll step response 的報告輸出版本。

<div style="text-align: center;">
<img src="fig3_14_roll_bode_1dof.png" alt="image" width="800">
</div>

此圖為 1DOF roll frequency response 的報告輸出版本。

<div style="text-align: center;">
<img src="roll_response_modal_physical_1dof.png" alt="image" width="800">
</div>

此圖比較理想 modal damping、實體 roll damper fit 與 1DOF sizing，可用於判斷簡化模型與可實作阻尼器拓樸之間的差異。
