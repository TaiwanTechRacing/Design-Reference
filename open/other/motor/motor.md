---
layout: base
---

# 馬達轉速-扭矩與分段擬合

[Download Code (資料小工具)](data_tool.py)

[Download Code (motor_curve_fitter)](motor_curve_fitter.py)

## 參數與區間設定

以下為系統採用的分段轉速臨界值與模型配置說明：

| 變數名稱 | 物理意義與數值 | 擬合/外推模型 | 最小資料點需求 |
| --- | --- | --- | --- |
| `SPLINE_END_RPM` | 三次樣條區間上限 | `CubicSpline` | $\ge 4$ 個數據點 |
| `QUAD_END_RPM` | 二次多項式區間上限 | `np.polyfit(deg=2)` | $\ge 3$ 個數據點 |
| `LINEAR_END_RPM` | 線性外推區間上限 | `LinearRegression` | $\ge 2$ 個數據點 |
| `ZERO_TORQUE_START_RPM` | 零扭矩強制截斷轉速 | 邊界條件截斷 ($T = 0.0\text{ N}\cdot\text{m}$) | - |

---

## 計算與數學模型

### 1. 低轉速區：三次樣條插值

在相鄰採樣點 $[x_i, x_{i+1}]$ 之間，構造三次多項式 $S_i(x)$：

$$S_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3$$

確保節點處的一階導數 $S_i'(x)$ 與二階導數 $S_i''(x)$ 完全連續，精準平滑捕捉低轉速下的額定扭矩與過渡區。

### 2. 中轉速弱磁區：二次多項式擬合

使用最小平方法（Least Squares Method）擬合二次曲線：

$$T(N) = c_2 \cdot N^2 + c_1 \cdot N + c_0$$

求得最小化殘差平方和的係數向量 $\mathbf{c} = [c_2, c_1, c_0]^T$：

$$\min_{\mathbf{c}} \sum_{i} \left( T_i - (c_2 N_i^2 + c_1 N_i + c_0) \right)^2$$

### 3. 高轉速極限區：線性迴歸外推

對高轉速數據建立線性預測模型：

$$T(N) = w \cdot N + b$$

## 結果

<div style="text-align: center;">
<img src="Motor%20Speed%20vs%20Torque%20(After%20Fiting).png" alt="image" width="800">
</div>

