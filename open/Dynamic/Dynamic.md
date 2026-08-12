---
layout: base
---

# 懸吊動態分析

## 解析解與顯式歐拉數值解比較

[Analytical Numerical Simulation](Analytical_Numerical_Simulation/Analytical_Numerical_Simulation.md) : 由於整個懸吊分析越做越龐大之後不可能永遠都使用解析解，所以比需進行解析解與數值解誤差分析。

## 時間解析度與精確度敏感性

[Time sensitivity](Time_sensitivity/Time_sensitivity.md) : 使用積分器的時候提高時間解析度可以大幅提高精度但是會投入更多時間，所以必須要進行取捨。

## ODE 方法求解精確度評估

[ode spring](ode_spring/ode_spring.md) : 比較一下RK45方法求解與直接使用積分器的效果差異確定一下差多少。如果差不多其實會考慮直接用積分器比較直覺快速好操作。

