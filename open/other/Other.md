# 空力與電力

## [電池](Battery_capacity/Battery_capacity.md)

> 利用單圈累積能量消耗**計算，並以此導出耐久賽的**電池包總容量需求。

在 FSAE 電動賽車（EV）的動力系統設計中，估算單圈及全場耐久賽的能量需求是電池包（Accumulator Container）容量選型與輕量化設計的核心關鍵。本分析透過兩個工具：

1. **功率時域分析**：計算車輛驅動力與車速之乘積 $P = F \cdot v$，繪製功率與時間關係圖，並導出峰值功率（Maximum Power）與平均功率（Average Power）。
2. **能量數值積分與電池容量估算**：利用梯形積分法（Trapezoidal Rule）對位移區間內的正向驅動力進行功（Work）的數值積分 $\int F \, dx$，計算單圈累積能量，並結合安全係數（Safety Factor, SF）導出全場賽事所需的總電池容量（$\text{kWh}$ / 度）。

## [馬達](motor/motor.md)

> 本分析程式旨在針對實驗量測或規格書中非連續、有限採樣點的**馬達轉速-扭矩原始數據**進行高精度的**分段曲線擬合與高轉速區間外推**。

在馬達動力學（Motor Dynamics）中，馬達在不同轉速區間（低轉速恆扭矩區、中轉速恆功率衰減區、高轉速弱磁弱功率區）表現出高度非線性的物理特性。為避免單一迴歸模型產生的 Runge 現象或高轉速失真，本程式採用**三階段混合擬合架構**：

1. **低轉速區**：採用 **三次樣條插值（Cubic Spline）**，完美還原低轉速與額定轉速區間的平滑扭矩輸出。
2. **中轉速區**：採用 **二次多項式擬合（Quadratic Polynomial Fit）**，模擬弱磁區（Field Weakening Region）扭矩隨轉速呈二次曲線衰減的物理行為。
3. **高轉速極限區**：採用 **線性迴歸（Linear Regression）** 進行外推，並於臨界轉速設置**零扭矩截斷（Zero-Torque Cutoff）**，模擬馬達達到反電動勢限制與極限轉速時扭矩歸零的物理邊界。

## 空力

還沒加入

## 其他小工具 (點擊下載)

1. [刪除所有png](tools/clear_pngs.py)
1. [資料小工具](tools/data_tool.py)
1. [強制資料夾刪除工具](tools/file_delete_tool.py)
1. [翻譯機(簡體>>繁體)](tools/Translator.py)