---
layout: base
---

# Tender Spring 分析

## 設計背景

目前彈簧姿態限制以 $roll = 2^\circ$、$pitch = 1.5^\circ$ 作為設計目標，但其中約 $0.5^\circ$ roll 與 $0.35^\circ$ pitch 會由輪胎變形提供，因此實際由懸吊壓縮造成的姿態角不需要吃完整個角度需求。若將總行程完全用於姿態變化，最大約可造成 $2.26^\circ$ roll 或 $1.87^\circ$ pitch；也就是說在不考慮空力下壓的情況下，目前允許的極限 full roll / full pitch 約使用總行程的 $60\%$。

由於輪胎剛性會與懸吊剛性串聯，實際 ride stiffness 會低於單純彈簧剛性，因此彈簧本體剛性必須比姿態限制直接推得的值更高。同時仍需確認簧上與簧下自然頻率之間保有足夠間隔，目前目標設定下兩者差距超過 3 倍，可避免輪胎 hop mode 與車身模態過度接近。

## [雙彈簧串聯剛性分析](2_spring/2_spring.md)

> 計算 main spring 與 tender spring 串聯後的等效剛性，並觀察 tender 剛性比例對初段總剛性的影響。

此分析用於建立 tender spring 選型的基本概念。當 tender spring 與 main spring 串聯時，初段等效剛性會低於任一單獨彈簧剛性，因此 tender 的剛性比例會直接影響懸吊初段支撐、低載荷行程與彈簧切換前的車身姿態。以目前偏保守的設定來看，tender spring 採用 main spring 的 $70\%$ 剛性時，串聯後 heave 剛性約為原 main spring 的 $40\%$，因此剛性切換前後會有明顯差距。

## [Tender Heave 與 Pitch 行程分析](tender/tender.md)

> 建立 tender + main spring 的分段剛性模型，估算不同下壓力與煞車加速度下的前後行程、heave 與 pitch 角。

此工具將 tender 彈簧壓縮到底前的串聯剛性，以及 tender bind 後只剩 main spring 的分段特性納入計算。透過掃描空力下壓力比例與煞車加速度，可以觀察懸吊行程是否過早吃完、pitch 姿態是否過大，以及 tender 設定對空力平台穩定性的影響。

目前的設計思路偏向讓 tender 主要服務 heave，而不是直接降低所有單輪 ride rate。原因是單輪衝擊會同時受到 heave 與 roll 剛性的平均影響，但空力下壓主要作用於 heave；因此將 tender 加入 heave 可以保留低速路面吸收能力，同時避免整體單輪 ride stiffness 被過度降低。
