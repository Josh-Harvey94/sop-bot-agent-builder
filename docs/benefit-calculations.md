# Capacity and payback

The source guide's calculation estimates potential staff capacity. These are planning estimates until measured in a pilot; they are not automatically cash savings.

## Define the units first

Gross hours per active week = gross minutes saved per case per staff member × cases per active week × staff who each save those minutes ÷ 60.

If minutes already represent total staff effort per case, use staff multiplier **1**. A five-minute team activity observed by three people is not automatically fifteen minutes saved. Use the measured effort of each participant. Do not count reduced waiting time as staff working time unless someone was actively occupied by it.

## Convert and adjust

1. Realised annual hours = gross hours per active week × active weeks per year × realisation fraction.
2. Net annual hours = realised annual hours − annual maintenance/support hours.
3. Average monthly net hours = net annual hours ÷ 12.
4. Build-only payback months = technical build hours ÷ positive average monthly net hours.

Realisation covers retained checks, exceptions and incomplete adoption. If the minutes already include those adjustments, use 100% realisation. The guide deducts annual maintenance separately, so do not include it again in the realisation factor. A negative result means extra workload and must remain visible. If the net monthly benefit is zero or negative, there is no positive payback.

The interactive calculator labels weekly output **per active week** and shows it before the separate annual maintenance deduction. Annual and average monthly figures are net of maintenance. This avoids spreading annual maintenance ambiguously across inactive weeks.

## Worked estimate

| Input | Illustrative value |
| --- | ---: |
| Gross minutes per case per staff member | 5 |
| Cases per active week | 40 |
| Staff multiplier | 1 |
| Active weeks | 46 |
| Realisation | 70% |
| Annual maintenance/support | 12 hours |
| Technical build | 16 hours |

Gross active-week hours = 5 × 40 × 1 ÷ 60 = 3.333.

Realised active-week hours = 3.333 × 0.70 = 2.333.

Realised annual hours = 2.333 × 46 = 107.333.

Net annual hours = 107.333 − 12 = **95.333**.

Average monthly net hours = 95.333 ÷ 12 = **7.944**.

Build-only payback = 16 ÷ 7.944 = **2.014 months**.

## Scenarios and exclusions

For the same volume and minutes, 40%, 70% and 90% realisation yield 49.333, 95.333 and 126 net annual hours after 12 maintenance hours. With 16 build hours, payback is approximately 3.9, 2.0 and 1.5 months respectively. These scenarios are illustrative, not probability estimates.

Build-only payback excludes discovery, permissions, reviews, testing, training and other one-off work unless included in the input. For full implementation payback, include those hours in the numerator and label that choice. Monetary licensing or procurement costs need a separate business case; do not combine money and hours in the same ratio.

Effort bands in the guide are source-derived heuristics: Simple 2–8 hours; Small 1–3 days; Medium 3–10 days; Complex 2–8 weeks or longer. State working hours per day/week before converting. They are not delivery commitments.

When opportunities overlap, assess a combined option using the final end-state process and count shared build work once. Do not add separate “capture”, “copying” and “tracker” savings if they replace the same minutes.
