---
layout: base
---

# Tender Spring 分析

## [雙彈簧串聯剛性分析](2_spring/2_spring.md)

> 計算 main spring 與 tender spring 串聯後的等效剛性，並觀察 tender 剛性比例對初段總剛性的影響。

建立 tender spring 選型的基本概念。當 tender spring 與 main spring 串聯時，初段等效剛性會低於任一單獨彈簧剛性，因此 tender 的剛性比例會直接影響懸吊初段支撐、低載荷行程與彈簧切換前的車身姿態。
## [Tender Heave 與 Pitch 行程分析](tender/tender.md)

> 建立 tender + main spring 的分段剛性模型，估算不同下壓力與煞車加速度下的前後行程、heave 與 pitch 角。

將 tender 彈簧壓縮到底前的串聯剛性，以及 tender bind 後只剩 main spring 的分段特性納入計算。透過掃描空力下壓力比例與煞車加速度，可以觀察懸吊行程是否過早吃完、pitch 姿態是否過大，以及 tender 設定對空力平台穩定性的影響。

設計思路偏向讓 tender 服務 heave，而不是直接降低所有單輪 ride rate。原因是單輪衝擊會同時受到 heave 與 roll 剛性的平均影響，但空力下壓主要作用於 heave；因此將 tender 加入 heave 可以保留低速路面吸收能力，同時達到使用空力控制剛性的目的。
