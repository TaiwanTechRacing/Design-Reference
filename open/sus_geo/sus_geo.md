---
layout: base
---

# 懸吊幾何分析

## [Roll Center 最小負載轉移速率分析](roll_center_min_load/roll_center_min_load.md)

> 掃描 roll center 高度，尋找可降低第一波總負載轉移速率峰值的幾何設定。

此分析用於觀察 roll center 高度如何改變側向負載轉移在懸吊彈簧與幾何力路徑之間的分配。透過比較懸吊彈簧造成的轉移速率、車架幾何造成的轉移速率，以及兩者相加後的總轉移速率，可以評估 roll center 是否能降低轉移峰值，讓負載轉移更平順地進入輪胎。

## [前後軸負載轉移速率匹配](roll_center_same_load/roll_center_same_load.md)

> 以前軸負載轉移速率作為基準，掃描後軸 roll center 高度，使前後軸第一波負載轉移速率盡可能接近。

此分析用於補償前後軸 roll stiffness 不同造成的負載轉移速度差異。若後軸懸吊剛性較低，可以透過提高後軸 roll center，使幾何力路徑分擔更多負載轉移，讓前後軸在 transient 狀態下的負載建立速度更接近。
