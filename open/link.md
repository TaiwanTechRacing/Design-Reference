---
layout: base
---

# link


### 計算式整理

程式中的計算其實就是：

$$
F_x = m a g
$$

$$
M = F_x h
$$

$$
F=\frac{M}{L/2}
$$

$$
s=\frac{L}{2}\theta
$$

$$
K=\frac{F}{2s}
$$

因此可以直接合併為

$$
K=\frac{m a g h}{L\left(\frac{L}{2}\theta\right)}
=\frac{2m a g h}{L^2\theta}
$$

所以你甚至可以直接寫成

```python
K = (2 * m * a * g * h) / (L**2 * theta)
```
