# Spaceship Titanic - Kaggle Competition

Binary classification solution predicting which passengers were transported to an alternate dimension during the Spaceship Titanic's collision with a spacetime anomaly.


## Approach

### Data Preprocessing
- Handled missing values: booleans with `False`, numeric with median, categorical with mode
- Engineered 55 features including cabin attributes, spending metrics, age categories, and group-based statistics
- Selected 47 features using Random Forest importance (threshold > 0.005)

### Feature Engineering Highlights
- **Cabin decomposition**: Extracted Deck, CabinNum, and Side
- **Spending analysis**: Total spending, service usage counts, luxury vs necessity ratios
- **Group dynamics**: Group size, group-level means/stds for spending and age
- **Interaction features**: CryoSleep × Age, VIP × Spending, Deck × Side

### Model Development
| Model | Validation AUC |
|-------|---------------|
| CatBoost | 0.9076 |
| LightGBM | 0.9072 |
| Gradient Boosting | 0.9051 |
| XGBoost | 0.9046 |
| Random Forest | 0.8876 |

### Final Ensemble
- **Model**: Voting Classifier (CatBoost + LightGBM + Gradient Boosting)
- **Validation AUC**: 0.9084
- **CV Accuracy**: 0.7883 ± 0.0246
- **Threshold**: Optimized to 0.430 for maximum F1 score

### Key Insights
- `CabinNum` was the single strongest predictor
- Spending behavior (services used, total spend) strongly correlated with transport status
- CryoSleep passengers exhibited distinct spending and transport patterns
