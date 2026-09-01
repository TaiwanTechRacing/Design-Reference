---
layout: base
---

# 阻尼器與 Shock Dyno 分析



## 參數

| 變數名稱 | 物理意義 | 單位 |
| --- | --- | --- |
| $c_c$ | 臨界阻尼 | $N \cdot s/m$ |
| $\zeta$ | 目標阻尼比 | 無因次 |
| $MR$ | damper 對應 motion ratio | 無因次 |
| $v$ | damper shaft velocity | $mm/s$ |
| $v_k$ | knee velocity | $mm/s$ |
| $c_{LS}$ | low-speed 阻尼斜率 | $N/(mm/s)$ |
| $c_{HS}$ | high-speed 阻尼斜率 | $N/(mm/s)$ |
| $F_d$ | 阻尼器力 | $N$ |
| $C_{\phi}$ | 側傾扭轉阻尼 | $N \cdot m/(rad/s)$ |

## 計算

### 1. Heave 阻尼係數

臨界阻尼由 heave wheel rate 與 sprung mass 取得：

$$
c_c=2\sqrt{k_wm_s}
$$

目標線性阻尼為：

$$
c=\zeta c_c
$$

阻尼器本體速度與輪端速度之間受 motion ratio 影響，因此阻尼器本體係數為：

$$
c_d=\frac{c}{MR^2}
$$

若模型由整軸轉為單輪 independent equivalent，阻尼需求需分配到單輪：

$$
c_{d,ind}
=
\frac{\zeta c_c}{2MR_{ind}^2}
$$

### 2. 非對稱 bilinear force curve

Heave damper 分成 bump 與 rebound，並在 knee velocity 前後切換斜率。壓縮側可寫為：

$$
F_d(v)=
\begin{cases}
c_{LS,b}v, & 0\le v\le v_k \\
c_{LS,b}v_k+c_{HS,b}(v-v_k), & v>v_k
\end{cases}
$$

回彈側可寫為：

$$
F_d(v)=
\begin{cases}
c_{LS,r}v, & -v_k\le v<0 \\
-c_{LS,r}v_k+c_{HS,r}(v+v_k), & v<-v_k
\end{cases}
$$

此設定能讓低速區域保有姿態控制，高速區域則降低路面衝擊傳遞。

### 3. Roll physical damper fit

3DOF roll modal damping matrix 通常不能由前後兩支實體 roll damper 完全重現，因此使用 least-squares fit 找出最接近的前後阻尼係數。若前後 roll damper basis matrix 為 $\mathbf{B}_f$、$\mathbf{B}_r$，目標 modal damping matrix 為 $\mathbf{C}_{target}$，則可寫成：

$$
\mathbf{C}_{fit}
=
c_f\mathbf{B}_f+c_r\mathbf{B}_r
$$

係數由下式求得：

$$
\min_{c_f,c_r}
\left\|
\mathbf{C}_{target}
-
\left(c_f\mathbf{B}_f+c_r\mathbf{B}_r\right)
\right\|_F
$$

### 4. Roll 1DOF sizing

1DOF roll 模型使用總側傾剛性與簧上 roll inertia 計算扭轉阻尼：

$$
C_{\phi,total}
=
2\zeta\sqrt{K_{\phi,total}I_{xx}}
$$

前後分配可依 roll stiffness distribution：

$$
C_{\phi,f}=D_fC_{\phi,total},
\qquad
C_{\phi,r}=D_rC_{\phi,total}
$$

再由 roll damper arm 轉為線性阻尼：

$$
c_{d}
=
\frac{C_{\phi}}{(MR_rt)^2}
$$

## 結果

<div style="text-align: center;">
<img src="shock_dyno_decoupled_heave.png" alt="image" width="800">
</div>

解耦 heave shock dyno 顯示前後軸 heave damper 在壓縮與回彈方向的阻尼力變化。

<div style="text-align: center;">
<img src="shock_dyno_independent.png" alt="image" width="800">
</div>

Independent equivalent shock dyno 顯示轉成單輪模型後的阻尼器需求。

<div style="text-align: center;">
<img src="shock_dyno_roll_physical.png" alt="image" width="800">
</div>

Roll physical shock dyno 顯示由 6-state modal damping matrix 近似出的前後 roll damper 需求。

<div style="text-align: center;">
<img src="shock_dyno_roll_solution_compare.png" alt="image" width="800">
</div>

此圖比較 1DOF sizing 與 physical 6-state fit。若兩者差異明顯，代表簡化模型雖可用於初步定尺寸，但實體 damper 拓樸仍可能造成不同暫態反應。
