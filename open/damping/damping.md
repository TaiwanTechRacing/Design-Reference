---
layout: base
---

# 阻尼分析

## [臨界阻尼與自然頻率分析](Critical_Damping_Analysis/Critical_Damping_Analysis.md)

> 掃描不同彈簧剛性，計算 quarter-car 等效質量下的自然頻率與臨界阻尼係數。

此分析用於建立阻尼器設計的基準量級。透過彈簧剛性與四分之一車質量，可以快速得到對應的自然頻率與 critical damping，進一步換算不同阻尼比下所需的阻尼係數。

## [Quarter-Car 阻尼比掃描](Damped_oscillation_analysis/Damped_oscillation_analysis.md)

> 使用二自由度 quarter-car 模型，比較不同阻尼比對簧上位移與輪胎動態載荷變化的影響。

此工具可用於觀察阻尼比增加時，車身振盪收斂速度與輪胎正向力波動之間的取捨。結果能輔助懸吊阻尼初始設定，避免只追求車身穩定而忽略輪胎接地負載變化。

## [Euler 質量彈簧阻尼積分](damping_int/damping_int.md)

> 以顯式 Euler 方法模擬單自由度質量-彈簧-阻尼系統的位移響應。

此範例用來示範如何將阻尼系統的微分方程離散化，並用固定時間步長逐步更新速度與位移。適合作為數值積分、時間步長與阻尼振盪概念的入門驗算。

## [單自由度阻尼 ODE 模擬](damping_ode/damping_ode.md)

> 使用 `solve_ivp` 求解單自由度阻尼振盪器，並輸出時間響應與相平面圖。

此分析用於比較欠阻尼、臨界阻尼與過阻尼的基本行為。透過質量、剛性與阻尼係數可計算自然頻率與阻尼比，並檢查系統是否仍會振盪。

## [Quarter-Car 路面階躍響應](quarter_suspension/quarter_suspension.md)

> 使用含輪胎剛性的 quarter-car 模型，模擬路面階躍輸入下的簧上與簧下響應。

此工具以二自由度懸吊模型模擬車輪遇到高度階躍後，車身與輪胎端的位移、速度、加速度與能量變化。可用於觀察阻尼如何耗散系統能量，以及簧上/簧下質量如何互相耦合。

## [Quarter-Car Euler 積分模擬](quarter_suspension_int/quarter_suspension_int.md)

> 以顯式 Euler 方法模擬 quarter-car 在路面階躍輸入下的簧上位移與加速度。

此工具從靜態平衡位置開始，逐步更新簧上與簧下質量的速度及位置。相較 ODE solver 版本，此版本更適合檢查力平衡、積分流程與簡化懸吊模型的基本數值行為。
