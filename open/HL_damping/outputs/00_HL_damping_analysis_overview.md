---
layout: base
---

# 高低速阻尼設定分析

由於整個分析項目很大所以不支援獨立code下載，請上github翻。

## [Heave 分析](02_heave_analysis.md)
> Heave 分析使用 sprung/unsprung 兩自由度模型。

Heave 分析用來描述車輛受到垂直路面輸入時，簧上與簧下系統的等效剛性、自然頻率與阻尼特性。此分析採用前後軸分開的整軸模型，因此每一個 axle 都包含該軸左右輪的輪胎剛性與簧下質量。

## [Roll 分析](03_roll_analysis.md)
> roll 分析使用 sprung roll 與前後簧下 roll 的三自由度模型。模態分析用於確認自然頻率與阻尼比，並作為 state-space response 的基礎。

Roll 分析用來描述車輛受到側向加速度時的側傾剛性、roll gradient、模態頻率與暫態反應。此分析將懸吊 roll stiffness 與輪胎 roll stiffness 串聯處理，因此可以區分彈簧本身提供的剛性與輪胎柔度造成的實際車身側傾。

## [阻尼器與 Shock Dyno 分析](04_damper_analysis.md)
> 阻尼器分析將目標阻尼比轉換為 damper force-velocity 曲線。Heave 使用非對稱壓縮/回彈曲線；roll damper 則比較 physical fit 與 1DOF sizing 兩種定尺寸邏輯。

阻尼器分析的目的，是將 heave 與 roll 模型中的目標阻尼比轉換成 damper force-velocity 曲線。Heave damper 採用壓縮與回彈分開的非對稱 bilinear curve；roll damper 則使用對稱 bilinear curve，比較 1DOF sizing 與 physical 6-state fit 的差異。

## [獨立懸吊等效分析](05_independent_equivalent.md)
> 將roll heave 等效變成單輪懸吊設定用於分析單輪阻尼設定架構。

獨立懸吊等效分析用來將 decoupled heave / roll 的設計目標轉換成一般單輪獨立懸吊可理解的彈簧、ARB 與阻尼器需求。這個轉換不代表實際結構完全相同，而是讓 heave frequency、roll stiffness 與 damping target 可以在另一種懸吊架構下被比較。

## [工況與 ODE 時域模擬](06_simulation_and_load_cases.md)
> 工況分析包含縱向加速、縱向煞車與側向過彎。準靜態計算用於檢查彈簧作動量與姿態角；ODE 模擬則用於觀察暫態收斂、峰值與輪胎法向力變化。

工況分析用於檢查車輛在加速、煞車與過彎時的彈簧作動量、車身姿態與輪胎法向力變化。準靜態部分著重於力與位移平衡；ODE 時域模擬則用於觀察阻尼器造成的暫態響應、峰值與收斂特性。

## [所有輸出圖片索引](07_all_generated_figures.md)
> 檢索圖片用於驗證確認

## 分析圖表參考
除了以下項目還有很多其他分析，詳細說明請點上面連結。

<div style="text-align: center;">
<img src="roll_response_modal_physical_1dof.png" alt="image" width="800">
</div>

上圖比較 modal damping、physical damper fit 與 1DOF sizing 對 roll step response 的影響。

<div style="text-align: center;">
<img src="fig_decoupled_longitudinal_accel_brake_ode45.png" alt="image" width="800">
</div>

上圖整合縱向煞車與加速時的 decoupled heave 暫態反應，可用來檢查 pitch 姿態是否快速收斂，以及前後軸 heave 位移是否符合預期方向。
