# Setup

From the root of this repo, do:
```
python3.10 -m venv .venv
source .venv/bin/activate
pip install -e .
pip install -r requirements.txt
```

# Exercise Discussions

For discussions of specific exercises, see their respective folders:

| Chapter | Exercise | Topic | Notes |
|---------|----------|-------|-------|
| 2       | [2.5](./docs/ch02_ex02-05/README.md) | Non-stationary bandit | Random walk on values $\rarr$ noisier, slower convergence |
| 2       | [2.6](./docs/ch02_ex02-06/README.md) | Mysterious Spikes | &uarr; initial optimism $\implies$ &uarr; initial determinism in greedy policy |
|2 |[2.7](./docs/ch02_ex02-07/README.md) | Unbiased Constant-Step-Size Trick | Divide $\alpha$ by a function $f: \N \rarr [0, 1) $ which tends to 1 from below. Offsets bias of $Q_1$ by permitting larger-than-$\alpha$ updates at first, converging to $\alpha$-sized updates in the limit. |
|2|[2.8](./docs/ch02_ex02-08/README.md)|UCB Spikes| &uarr; exploration budget $\implies$ larger initial spike since bandit is 'forced off' the action with highest empirical mean |