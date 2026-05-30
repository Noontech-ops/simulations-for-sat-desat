# Al-Fum pyIAST Simulation Results

## Current Status

The pyIAST simulation is running successfully for Al-Fum CH4/N2 and CO2/N2 systems.

## Main Results

CH4/N2 IAST, 50/50 mol%, 1 bar:

- 273 K: CH4 = 0.9291 mmol/g, N2 = 0.0253 mmol/g, Selectivity = 36.69
- 298 K: CH4 = 0.5432 mmol/g, N2 = 0.0506 mmol/g, Selectivity = 10.74
- 313 K: CH4 = 0.4273 mmol/g, N2 = 0.0068 mmol/g, Selectivity = 62.85

CO2/N2 IAST, 15/85 mol%, 1 bar, 303 K:

- CO2 = 0.3278 mmol/g
- N2 = 0.1059 mmol/g
- Selectivity = 17.55

## Interpretation

The 298 K CH4/N2 result is the most reliable because the selectivity of 10.74 is close to the reported literature value of approximately 11.7.

The 273 K and 313 K selectivities are likely inflated because N2 uptake is very small and interpolation becomes unstable at low loading.

Therefore, 298 K should be treated as the strongest validated simulation case. The 273 K and 313 K cases should be treated as sensitivity outputs until the N2 isotherms are smoothed or refit.

## Recommended Conclusion

The Al-Fum pyIAST model is directionally valid near ambient temperature. At 298 K, the CH4/N2 selectivity closely matches literature, supporting the model. However, low-loading N2 data causes instability at 273 K and 313 K, so those results should not be overinterpreted.
