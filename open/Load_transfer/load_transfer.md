---
layout: base
---

# 四輪負載

## [車輛四輪載荷轉移](Four_wheel_load/FWL.md)

>評估車輛在動態加速、煞車與過彎過轉過程中，四輪正向載荷（Wheel Normal Loads）的動態轉移與分佈情況。

利用重心法（CG Distribution Method）計算縱向（$a_x$）與側向（$a_y$）加速度下的靜態重力分佈及慣性動態載荷轉移量，並支援外部力與力矩（如空氣動力學下壓力與阻力）的額外貢獻。

分析輸出兩組視圖，協助工程師判斷車輛在各動態工況下（$g\text{-}g$ 圖）的四輪受力包絡面（Envelope），並明確識別輪胎抬昇脫離地面（Wheel Lift-off, 輪胎載荷為零）的極限邊界。

## [車輛四輪正向載荷靜不定系統零空間分析](Four_wheel_load/solver_compar.md)

>四輪車輛屬於超靜定系統（Indeterminate System），僅憑三個靜力平衡方程式（垂直力平衡 $F_z$、側滾力矩平衡 $M_x$、俯仰力矩平衡 $M_y$）無法唯一確定四個輪胎的正向載荷，因此我們進行了一點奛玩的小研究。

對比兩種常見求解策略：
1. **最小作用量法（Least Action Principle / LSM Method）**：利用偽逆矩陣（Pseudo-inverse）求解最小範數解（Minimum-norm solution），對應剛性幾何下最省能量的力分布。
2. **重心比例分配法（CG Distribution Method）**：按靜態 CG 分配幾何比例進行載荷轉移。

同時，本分析透過線性代數中的零空間（Null Space Vector）推導，定量分析兩方法之差異向量，並求得保持四輪正向載荷皆非負（$N_i \ge 0$）的可行參數區間（Feasible Region）。


## [車輛懸吊剛度載荷轉移分析](sus_load/sus_load.md)

>本分析採用**懸吊系統剛度模型**，計算車輛在穩態縱向加速度與側向加速度下的四輪正向載荷

與幾何重心法不同，本方法考量了前後軸的**跳動剛度（Heave Stiffness）**與**側滾剛度（Roll Stiffness）**分佈，能更精準地評估懸吊彈簧與防傾桿調校對前後軸載荷轉移量（Pitch & Roll Load Transfer）的影響。分析結果輸出四輪受力包絡圖（Wheel Load Envelope），並透過**紅色實線**標示輪胎正向力降為零的極限抬輪邊界（Wheel Lift-off Threshold）。


## [極限負荷分析](sus_load/max_load.md)

> 分析極限的工作力量，用在輪端設計的ansys力量設定

結合懸吊剛度模型求解動態下車輛四輪的正向載荷（Normal Forces, $F_z$），評估特定極限工況（如高 $g$ 加速過彎）下各輪能提供之最大縱向驅動/煞車力（$F_{x,max}$）與最大側向抓地力（$F_{y,max}$）。
