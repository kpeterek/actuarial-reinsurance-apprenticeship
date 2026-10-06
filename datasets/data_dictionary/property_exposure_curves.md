# `property_exposure_curves`: Property exposure curves

**File:** `datasets/raw/reinsurance/property_exposure_curves.csv` | **Rows:** 1,530 | **SQLite table:** `property_exposure_curves`

**Grain:** One row per occupancy x insured-value band x damage ratio (0.00 to 1.00 in steps of 0.02).  
**Key:** `occupancy` + `tiv_band_low` + `damage_ratio`

## Notes

- MBBEFD exposure curves (Bernegger, S. (1997), "The Swiss Re Exposure Curves and the MBBEFD Distribution Class", ASTIN Bulletin 27(1), 99-111), one-parameter `c` family: b = exp(3.1 - 0.15(1 + c)c), g = exp((0.78 + 0.12c)c), G(x) = ln[((g - 1)b + (1 - gb)b^x) / (1 - b)] / ln(gb).
- G(x) is the share of expected loss below a deductible equal to x times the insured value; the layer share between d and d + l is G((d + l)/TIV) - G(d/TIV).

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `occupancy` | text | Occupancy the curve applies to. | `Restaurant` | No | Same values as `locations.occupancy`. |
| `tiv_band_low` | integer | Lower bound of the total-insured-value band, $ (inclusive). | `0` | No |  |
| `tiv_band_high` | integer | Upper bound of the band, $ (exclusive). | `1000000` | No |  |
| `curve_c` | decimal | MBBEFD c parameter. | `2.0` | No |  |
| `curve_b` | decimal | MBBEFD b parameter derived from c. | `9.025013` | No |  |
| `curve_g` | decimal | MBBEFD g parameter derived from c. | `7.690609` | No |  |
| `damage_ratio` | decimal | Deductible as a share of insured value, x. | `0.00` | No |  |
| `exposure_curve_value` | decimal | G(x), share of expected loss below x. | `0.000000` | No |  |

Back to the [data dictionary overview](README.md).
