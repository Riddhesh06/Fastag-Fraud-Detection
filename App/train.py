FEATURE_COLUMNS = X.columns.tolist()

import joblib
joblib.dump(FEATURE_COLUMNS, "feature_columns.pkl")
