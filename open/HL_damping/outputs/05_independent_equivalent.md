---
layout: base
---

# 獨立懸吊等效分析

## 參數

| 變數名稱 | 物理意義 | 單位 |
| --- | --- | --- |
| $k_{w,h}$ | 解耦 heave 整軸輪端剛性 | $N/m$ |
| $k_{w,ind}$ | 獨立懸吊單輪輪端剛性 | $N/m$ |
| $MR_{ind}$ | 獨立懸吊 motion ratio | 無因次 |
| $k_{s,ind}$ | 獨立懸吊彈簧本體剛性 | $N/m$ |
| $t$ | 輪距 | $m$ |
| $K_{\phi,base}$ | 獨立彈簧自然提供的 roll stiffness | $N \cdot m/rad$ |
| $K_{\phi,target}$ | 目標懸吊 roll stiffness | $N \cdot m/rad$ |
| $K_{\phi,ARB}$ | ARB 需補足的 roll stiffness | $N \cdot m/rad$ |
| $c_{heave}$ | 解耦 heave 阻尼 | $N \cdot s/m$ |
| $c_{ind}$ | 獨立懸吊等效阻尼 | $N \cdot s/m$ |

## 計算

### 1. Heave wheel rate 轉換

Decoupled heave 模型以整軸為單位，包含左右兩輪共同作動。轉為 independent suspension 時，單輪 wheel rate 為整軸 heave wheel rate 的一半：

$$
k_{w,ind}
=
\frac{k_{w,h}}{2}
$$

### 2. 彈簧本體剛性

單輪 wheel rate 再透過 independent motion ratio 轉回彈簧本體剛性：

$$
k_{s,ind}
=
\frac{k_{w,ind}}{MR_{ind}^2}
$$

此公式與 heave 分析相同，只是方向從輪端回推到彈簧本體。

### 3. 獨立彈簧提供的 roll stiffness

獨立懸吊左右輪在 roll 時一邊壓縮、一邊伸張，因此彈簧本身會提供基礎 roll stiffness：

$$
K_{\phi,base}
=
\frac{1}{2}k_{w,ind}t^2
$$

其中 $\frac{1}{2}$ 來自左右輪相對位移與 roll angle 的幾何關係。

### 4. ARB 補償剛性

若目標是匹配 decoupled suspension 的 roll stiffness，ARB 需要補足的剛性為：

$$
K_{\phi,ARB}
=
K_{\phi,target}
-
K_{\phi,base}
$$

若 $K_{\phi,base}$ 已高於目標，則代表單靠獨立彈簧已超過原本 roll target，此時 ARB 需求可能為零或需要重新調整彈簧策略。

### 5. 阻尼器等效

整軸 heave 阻尼轉為單輪 independent damper 時，阻尼需求分配到單輪並透過 motion ratio 回推：

$$
c_{ind}
=
\frac{c_{heave}}{2MR_{ind}^2}
$$

## 結果

<div style="text-align: center;">
<img src="shock_dyno_independent.png" alt="image" width="800">
</div>

此圖顯示轉換為 independent equivalent 後的 shock dyno 曲線。它可用來檢查單輪 damper 需求與原本 decoupled heave 需求之間的差異。

<div style="text-align: center;">
<img src="shock_dyno_decoupled_heave.png" alt="image" width="800">
</div>

此圖為原 decoupled heave shock dyno，可與 independent equivalent 互相比較。
