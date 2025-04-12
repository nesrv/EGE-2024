# (𝒙 > 𝟖) ∨ (𝟐𝒙 < 𝒚) ∨ (𝒙 ∗ 𝒚 < 𝑨)
# 129

for A in range(200):
    k = 0
    for x in range(1, 201):
        for y in range(1, 201):
            if (x > 8) or (2*x < y) or (x*y < A):
                k += 1
    if k == 40_000:
        print(A)
        break