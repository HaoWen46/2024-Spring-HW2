# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution
> 
> path: tokenB->tokenA->tokenD->tokenC->tokenB
> 
> tokenB->tokenA: amountIn=5.0               , amountOut=5.655321988655322
> tokenA->tokenD: amountIn=5.655321988655322 , amountOut=2.4587813170979333
> tokenD->tokenC: amountIn=2.4587813170979333, amountOut=5.0889272933015155
> tokenC->tokenB: amountIn=5.0889272933015155, amountOut=20.129888944077447
> 
> final reward: tokenB balance=20.129888944077447

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution
> 
> The difference between the expected price of a trade and the actual executed price.
>
> Uniswap V2 addresses slippage by liquidity providers.
> Liquidity Providers receives fees by providing liquidity to a liquidity pool, and higher liquidity will lead to less slippage.
>
> (x - dx)(y + dy) = xy
> => dy = y / (1 + x / dx) 
>
> When x and y are significantly larger, they are less prone to fluctuations, hence increase the stability of slippage.
 
## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution
> 
> To prevent users from creating very small liquidity, which wastes quite a lot of resource.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution 
> 
> To ensure that the deposited tokens are added to the liquidity pool in the correct proortion.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution
> 
> When the victim is about to make a large purchase, the attacker first monitors the victim's transaction, and then purchases at a higher price before the victim actually trades. This will raise the price and will increase the slippage. Therefore the victim will have to pay at a higher price for a large quantity, and the attacker benefits from this sandwhich attack.
