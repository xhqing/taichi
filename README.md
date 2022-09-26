# taichi
Taichi usage example. More detail about [taichi](https://github.com/taichi-dev/taichi).

## primes count

```sh
python count_primes_without_taichi.py

78498
time cost: 3.318950891494751s
# =============================

python count_primes_with_taichi.py

[Taichi] version 1.1.3, llvm 10.0.0, commit 1262a70a, osx, python 3.9.12
[Taichi] Starting on arch=arm64
78498
time cost: 0.08886313438415527s
```

## longest commom sequence

```sh
python lcs_without_taichi.py

2687
time cost: 229.79690885543823s
# ============================

python lcs_with_taichi.py

[Taichi] version 1.1.3, llvm 10.0.0, commit 1262a70a, osx, python 3.9.12
[Taichi] Starting on arch=arm64
2701
time cost: 1.5659801959991455s
```
