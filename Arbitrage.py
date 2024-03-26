liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

def swapToken(tokenIn: str, tokenOut: str, amountIn: float) -> float:
    x, y = liquidity[(tokenIn, tokenOut)] if tokenIn < tokenOut else liquidity[(tokenOut, tokenIn)][::-1]
    return y / (x / (amountIn * 0.997) + 1.0)

target = "tokenB"
tokens = ["tokenA", "tokenB", "tokenC", "tokenD", "tokenE"]

ans = 0.0
ansPath = ""

def dfs(mask: int, path: list, arbitrage: float):
    global ans, ansPath
    if len(path) >= 4 and path[-1] == target and arbitrage > ans:
        ans = arbitrage
        ansPath = "->".join(path)
    for i in range(5):
        if mask >> i & 1 or path[-1] == tokens[i]: continue
        newMask = mask | 1 << i
        newArbitrage = swapToken(path[-1], tokens[i], arbitrage)
        path.append(tokens[i])
        dfs(newMask, path, newArbitrage)
        path.pop()
    
curPath = [target]
dfs(0, curPath, 5.0)

print("path:", ansPath, end = ", ")
print("tokenB balance=", ans, sep = "")