```python
import pandas as pd
import numpy as np

```


```python
df = pd.read_csv('D:/Swapnil/Swapnil/Work/Python_Projects/AD_Click_Agency/ad_click_dataset.csv')
```


```python
# Dropping 'id' and 'full_name' as they are not relevant for prediction
df.drop(['id', 'full_name'], axis=1, inplace=True)

```


```python
# Checking for duplicates
duplicate_count = df.duplicated().sum()
print(f"Number of duplicates: {duplicate_count}")
```

    Number of duplicates: 4589
    


```python
# Removing duplicates if any
df = df.drop_duplicates()
```


```python
# Checking for missing values
missing_values = df.isnull().sum()
print(f"Missing values per column:\n{missing_values}")
```

    Missing values per column:
    age                 1845
    gender              2366
    device_type         1315
    ad_position         1318
    browsing_history    2249
    time_of_day         1257
    click                  0
    dtype: int64
    


```python
# Imputing numerical values (age) with median
df['age'] = df['age'].fillna(df['age'].median())

# Imputing categorical values with mode
df['gender'] = df['gender'].fillna(df['gender'].mode()[0])
df['device_type'] = df['device_type'].fillna(df['device_type'].mode()[0])
df['ad_position'] = df['ad_position'].fillna(df['ad_position'].mode()[0])
df['browsing_history'] = df['browsing_history'].fillna(df['browsing_history'].mode()[0])
df['time_of_day'] = df['time_of_day'].fillna(df['time_of_day'].mode()[0])


```


```python
# Checking for missing values
missing_values = df.isnull().sum()
print(f"Missing values per column:\n{missing_values}")
```

    Missing values per column:
    age                 0
    gender              0
    device_type         0
    ad_position         0
    browsing_history    0
    time_of_day         0
    click               0
    dtype: int64
    


```python
import matplotlib.pyplot as plt
import seaborn as sns

# Age distribution
plt.figure(figsize=(8, 6))
sns.histplot(df['age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.show()

```


    

    



```python
# Gender vs Clicks
plt.figure(figsize=(8, 6))
sns.countplot(x='gender', hue='click', data=df)
plt.title('Gender vs Clicks')
plt.show()

```


    

    



```python
# Device Type vs Clicks
plt.figure(figsize=(8, 6))
sns.countplot(x='device_type', hue='click', data=df)
plt.title('Device Type vs Clicks')
plt.show()

```


    

    



```python
# Checking and ensuring correct data types
print(df.dtypes)

# Convert categorical columns to the correct data type if needed
df['gender'] = df['gender'].astype('category')
df['device_type'] = df['device_type'].astype('category')
df['ad_position'] = df['ad_position'].astype('category')
df['browsing_history'] = df['browsing_history'].astype('category')
df['time_of_day'] = df['time_of_day'].astype('category')

```

    age                 float64
    gender               object
    device_type          object
    ad_position          object
    browsing_history     object
    time_of_day          object
    click                 int64
    dtype: object
    


```python
from sklearn.preprocessing import StandardScaler

# Scaling 'age' feature
scaler = StandardScaler()
df['age'] = scaler.fit_transform(df[['age']])

```


```python
df = pd.get_dummies(df, drop_first=True)

```


```python
from sklearn.model_selection import train_test_split

# Define features and target
X = df.drop('click', axis=1)
y = df['click']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

```


```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Initialize and train logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate the model
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))

```

    Accuracy: 0.5548029556650246
                  precision    recall  f1-score   support
    
               0       0.54      0.60      0.57       801
               1       0.57      0.51      0.54       823
    
        accuracy                           0.55      1624
       macro avg       0.56      0.56      0.55      1624
    weighted avg       0.56      0.55      0.55      1624
    
    


```python
from sklearn.ensemble import RandomForestClassifier

# Initialize and train Random Forest
rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)

# Predict and evaluate
y_rf_pred = rf_model.predict(X_test)
print(f"Random Forest Accuracy: {accuracy_score(y_test, y_rf_pred)}")

```

    Random Forest Accuracy: 0.5474137931034483
    


```python
from xgboost import XGBClassifier

# Initialize and train XGBoost
xgb_model = XGBClassifier(use_label_encoder=False)
xgb_model.fit(X_train, y_train)

# Predict and evaluate
y_xgb_pred = xgb_model.predict(X_test)
print(f"XGBoost Accuracy: {accuracy_score(y_test, y_xgb_pred)}")


```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    Cell In[20], line 1
    ----> 1 from xgboost import XGBClassifier
          3 # Initialize and train XGBoost
          4 xgb_model = XGBClassifier(use_label_encoder=False)
    

    ModuleNotFoundError: No module named 'xgboost'



```python
!pip install xgboost

```

    Collecting xgboost
      Downloading xgboost-2.1.1-py3-none-win_amd64.whl.metadata (2.1 kB)
    Requirement already satisfied: numpy in c:\users\swapn\appdata\local\programs\python\python312\lib\site-packages (from xgboost) (2.1.1)
    Requirement already satisfied: scipy in c:\users\swapn\appdata\local\programs\python\python312\lib\site-packages (from xgboost) (1.14.1)
    Downloading xgboost-2.1.1-py3-none-win_amd64.whl (124.9 MB)
       ---------------------------------------- 0.0/124.9 MB ? eta -:--:--
       ---------------------------------------- 0.8/124.9 MB 5.6 MB/s eta 0:00:23
       - -------------------------------------- 3.9/124.9 MB 12.4 MB/s eta 0:00:10
       -- ------------------------------------- 7.1/124.9 MB 13.6 MB/s eta 0:00:09
       --- ------------------------------------ 10.0/124.9 MB 13.5 MB/s eta 0:00:09
       ---- ----------------------------------- 12.6/124.9 MB 13.4 MB/s eta 0:00:09
       ----- ---------------------------------- 15.7/124.9 MB 13.6 MB/s eta 0:00:09
       ------ --------------------------------- 21.5/124.9 MB 15.6 MB/s eta 0:00:07
       -------- ------------------------------- 26.2/124.9 MB 16.4 MB/s eta 0:00:07
       --------- ------------------------------ 30.9/124.9 MB 17.2 MB/s eta 0:00:06
       ----------- ---------------------------- 36.7/124.9 MB 18.5 MB/s eta 0:00:05
       -------------- ------------------------- 43.8/124.9 MB 19.9 MB/s eta 0:00:05
       ---------------- ----------------------- 50.3/124.9 MB 20.7 MB/s eta 0:00:04
       ------------------ --------------------- 57.4/124.9 MB 21.8 MB/s eta 0:00:04
       -------------------- ------------------- 62.9/124.9 MB 22.3 MB/s eta 0:00:03
       ---------------------- ----------------- 69.2/124.9 MB 22.6 MB/s eta 0:00:03
       ------------------------ --------------- 76.5/124.9 MB 23.4 MB/s eta 0:00:03
       -------------------------- ------------- 81.5/124.9 MB 23.4 MB/s eta 0:00:02
       ---------------------------- ----------- 87.8/124.9 MB 23.7 MB/s eta 0:00:02
       ------------------------------ --------- 94.1/124.9 MB 24.0 MB/s eta 0:00:02
       -------------------------------- ------ 103.3/124.9 MB 25.0 MB/s eta 0:00:01
       ---------------------------------- ---- 109.6/124.9 MB 25.3 MB/s eta 0:00:01
       ------------------------------------ -- 117.2/124.9 MB 25.7 MB/s eta 0:00:01
       --------------------------------------  124.8/124.9 MB 26.2 MB/s eta 0:00:01
       --------------------------------------  124.8/124.9 MB 26.2 MB/s eta 0:00:01
       --------------------------------------  124.8/124.9 MB 26.2 MB/s eta 0:00:01
       --------------------------------------- 124.9/124.9 MB 23.5 MB/s eta 0:00:00
    Installing collected packages: xgboost
    Successfully installed xgboost-2.1.1
    


```python
from xgboost import XGBClassifier

# Initialize and train XGBoost
xgb_model = XGBClassifier(use_label_encoder=False)
xgb_model.fit(X_train, y_train)

# Predict and evaluate
y_xgb_pred = xgb_model.predict(X_test)
print(f"XGBoost Accuracy: {accuracy_score(y_test, y_xgb_pred)}")
```

    XGBoost Accuracy: 0.6231527093596059
    

    C:\Users\swapn\AppData\Local\Programs\Python\Python312\Lib\site-packages\xgboost\core.py:158: UserWarning: [15:43:19] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0015a694724fa8361-1\xgboost\xgboost-ci-windows\src\learner.cc:740: 
    Parameters: { "use_label_encoder" } are not used.
    
      warnings.warn(smsg, UserWarning)
    


```python
from xgboost import XGBClassifier

# Initialize and train XGBoost without use_label_encoder
xgb_model = XGBClassifier()
xgb_model.fit(X_train, y_train)

# Predict and evaluate
y_xgb_pred = xgb_model.predict(X_test)
print(f"XGBoost Accuracy: {accuracy_score(y_test, y_xgb_pred)}")

```

    XGBoost Accuracy: 0.6231527093596059
    


```python
#OPTIMIZING

# Create interaction terms between 'device_type' and 'time_of_day'
df['device_time_interaction'] = (
    (df['device_type_Mobile'].astype(str) + "_Mobile_" + df['time_of_day'].astype(str)).replace('0_Mobile_', '') +
    (df['device_type_Tablet'].astype(str) + "_Tablet_" + df['time_of_day'].astype(str)).replace('0_Tablet_', '')
)

# Create interaction terms between 'ad_position' and 'browsing_history'
df['ad_browsing_interaction'] = (
    (df['ad_position_Side'].astype(str) + "_Side_" + df['browsing_history'].astype(str)).replace('0_Side_', '')
)

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    File ~\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\indexes\base.py:3805, in Index.get_loc(self, key)
       3804 try:
    -> 3805     return self._engine.get_loc(casted_key)
       3806 except KeyError as err:
    

    File index.pyx:167, in pandas._libs.index.IndexEngine.get_loc()
    

    File index.pyx:196, in pandas._libs.index.IndexEngine.get_loc()
    

    File pandas\\_libs\\hashtable_class_helper.pxi:7081, in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    File pandas\\_libs\\hashtable_class_helper.pxi:7089, in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    KeyError: 'time_of_day'

    
    The above exception was the direct cause of the following exception:
    

    KeyError                                  Traceback (most recent call last)

    Cell In[27], line 5
          1 #OPTIMIZING
          2 
          3 # Create interaction terms between 'device_type' and 'time_of_day'
          4 df['device_time_interaction'] = (
    ----> 5     (df['device_type_Mobile'].astype(str) + "_Mobile_" + df['time_of_day'].astype(str)).replace('0_Mobile_', '') +
          6     (df['device_type_Tablet'].astype(str) + "_Tablet_" + df['time_of_day'].astype(str)).replace('0_Tablet_', '')
          7 )
          9 # Create interaction terms between 'ad_position' and 'browsing_history'
         10 df['ad_browsing_interaction'] = (
         11     (df['ad_position_Side'].astype(str) + "_Side_" + df['browsing_history'].astype(str)).replace('0_Side_', '')
         12 )
    

    File ~\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\frame.py:4102, in DataFrame.__getitem__(self, key)
       4100 if self.columns.nlevels > 1:
       4101     return self._getitem_multilevel(key)
    -> 4102 indexer = self.columns.get_loc(key)
       4103 if is_integer(indexer):
       4104     indexer = [indexer]
    

    File ~\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\indexes\base.py:3812, in Index.get_loc(self, key)
       3807     if isinstance(casted_key, slice) or (
       3808         isinstance(casted_key, abc.Iterable)
       3809         and any(isinstance(x, slice) for x in casted_key)
       3810     ):
       3811         raise InvalidIndexError(key)
    -> 3812     raise KeyError(key) from err
       3813 except TypeError:
       3814     # If we have a listlike key, _check_indexing_error will raise
       3815     #  InvalidIndexError. Otherwise we fall through and re-raise
       3816     #  the TypeError.
       3817     self._check_indexing_error(key)
    

    KeyError: 'time_of_day'



```python
print(df.columns)

```

    Index(['age', 'click', 'gender_Male', 'gender_Non-Binary',
           'device_type_Mobile', 'device_type_Tablet', 'ad_position_Side',
           'ad_position_Top', 'browsing_history_Entertainment',
           'browsing_history_News', 'browsing_history_Shopping',
           'browsing_history_Social Media', 'time_of_day_Evening',
           'time_of_day_Morning', 'time_of_day_Night'],
          dtype='object')
    


```python
# Combine device type and time of day columns to create interaction terms
df['device_time_interaction'] = (
    (df['device_type_Mobile'] * df['time_of_day_Morning']).astype(str) + "_Mobile_Morning_" +
    (df['device_type_Mobile'] * df['time_of_day_Evening']).astype(str) + "_Mobile_Evening_" +
    (df['device_type_Tablet'] * df['time_of_day_Morning']).astype(str) + "_Tablet_Morning_" +
    (df['device_type_Tablet'] * df['time_of_day_Night']).astype(str) + "_Tablet_Night_"
).replace('0', '')  # Remove 0 interactions


```


```python
# Combine ad position and browsing history to create interaction terms
df['ad_browsing_interaction'] = (
    (df['ad_position_Side'] * df['browsing_history_Shopping']).astype(str) + "_Side_Shopping_" +
    (df['ad_position_Top'] * df['browsing_history_Social Media']).astype(str) + "_Top_Social_Media_" +
    (df['ad_position_Side'] * df['browsing_history_News']).astype(str) + "_Side_News_"
).replace('0', '')  # Remove 0 interactions


```


```python
# Binning the 'age' column
df['age_group'] = pd.cut(df['age'], bins=[0, 20, 30, 40, 50, 100], labels=['Teen', 'Young Adult', 'Adult', 'Middle Aged', 'Senior'])

```


```python



!pip install imbalanced-learn


from imblearn.over_sampling import SMOTE

# Define features and target
X = df.drop('click', axis=1)
y = df['click']

# Initialize SMOTE and resample
smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X, y)

# Check class distribution after SMOTE
print(pd.Series(y_res).value_counts())

```

    Collecting imbalanced-learn
      Downloading imbalanced_learn-0.12.3-py3-none-any.whl.metadata (8.3 kB)
    Requirement already satisfied: numpy>=1.17.3 in c:\users\swapn\appdata\local\programs\python\python312\lib\site-packages (from imbalanced-learn) (2.1.1)
    Requirement already satisfied: scipy>=1.5.0 in c:\users\swapn\appdata\local\programs\python\python312\lib\site-packages (from imbalanced-learn) (1.14.1)
    Requirement already satisfied: scikit-learn>=1.0.2 in c:\users\swapn\appdata\local\programs\python\python312\lib\site-packages (from imbalanced-learn) (1.5.2)
    Requirement already satisfied: joblib>=1.1.1 in c:\users\swapn\appdata\local\programs\python\python312\lib\site-packages (from imbalanced-learn) (1.4.2)
    Requirement already satisfied: threadpoolctl>=2.0.0 in c:\users\swapn\appdata\local\programs\python\python312\lib\site-packages (from imbalanced-learn) (3.5.0)
    Downloading imbalanced_learn-0.12.3-py3-none-any.whl (258 kB)
    Installing collected packages: imbalanced-learn
    Successfully installed imbalanced-learn-0.12.3
    


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[35], line 12
         10 # Initialize SMOTE and resample
         11 smote = SMOTE(random_state=42)
    ---> 12 X_res, y_res = smote.fit_resample(X, y)
         14 # Check class distribution after SMOTE
         15 print(pd.Series(y_res).value_counts())
    

    File ~\AppData\Local\Programs\Python\Python312\Lib\site-packages\imblearn\base.py:208, in BaseSampler.fit_resample(self, X, y)
        187 """Resample the dataset.
        188 
        189 Parameters
       (...)
        205     The corresponding label of `X_resampled`.
        206 """
        207 self._validate_params()
    --> 208 return super().fit_resample(X, y)
    

    File ~\AppData\Local\Programs\Python\Python312\Lib\site-packages\imblearn\base.py:106, in SamplerMixin.fit_resample(self, X, y)
        104 check_classification_targets(y)
        105 arrays_transformer = ArraysTransformer(X, y)
    --> 106 X, y, binarize_y = self._check_X_y(X, y)
        108 self.sampling_strategy_ = check_sampling_strategy(
        109     self.sampling_strategy, y, self._sampling_type
        110 )
        112 output = self._fit_resample(X, y)
    

    File ~\AppData\Local\Programs\Python\Python312\Lib\site-packages\imblearn\base.py:161, in BaseSampler._check_X_y(self, X, y, accept_sparse)
        159     accept_sparse = ["csr", "csc"]
        160 y, binarize_y = check_target_type(y, indicate_one_vs_all=True)
    --> 161 X, y = self._validate_data(X, y, reset=True, accept_sparse=accept_sparse)
        162 return X, y, binarize_y
    

    File ~\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\base.py:650, in BaseEstimator._validate_data(self, X, y, reset, validate_separately, cast_to_ndarray, **check_params)
        648         y = check_array(y, input_name="y", **check_y_params)
        649     else:
    --> 650         X, y = check_X_y(X, y, **check_params)
        651     out = X, y
        653 if not no_val_X and check_params.get("ensure_2d", True):
    

    File ~\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\validation.py:1301, in check_X_y(X, y, accept_sparse, accept_large_sparse, dtype, order, copy, force_writeable, force_all_finite, ensure_2d, allow_nd, multi_output, ensure_min_samples, ensure_min_features, y_numeric, estimator)
       1296         estimator_name = _check_estimator_name(estimator)
       1297     raise ValueError(
       1298         f"{estimator_name} requires y to be passed, but the target y is None"
       1299     )
    -> 1301 X = check_array(
       1302     X,
       1303     accept_sparse=accept_sparse,
       1304     accept_large_sparse=accept_large_sparse,
       1305     dtype=dtype,
       1306     order=order,
       1307     copy=copy,
       1308     force_writeable=force_writeable,
       1309     force_all_finite=force_all_finite,
       1310     ensure_2d=ensure_2d,
       1311     allow_nd=allow_nd,
       1312     ensure_min_samples=ensure_min_samples,
       1313     ensure_min_features=ensure_min_features,
       1314     estimator=estimator,
       1315     input_name="X",
       1316 )
       1318 y = _check_y(y, multi_output=multi_output, y_numeric=y_numeric, estimator=estimator)
       1320 check_consistent_length(X, y)
    

    File ~\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\validation.py:1064, in check_array(array, accept_sparse, accept_large_sparse, dtype, order, copy, force_writeable, force_all_finite, ensure_2d, allow_nd, ensure_min_samples, ensure_min_features, estimator, input_name)
       1058     raise ValueError(
       1059         "Found array with dim %d. %s expected <= 2."
       1060         % (array.ndim, estimator_name)
       1061     )
       1063 if force_all_finite:
    -> 1064     _assert_all_finite(
       1065         array,
       1066         input_name=input_name,
       1067         estimator_name=estimator_name,
       1068         allow_nan=force_all_finite == "allow-nan",
       1069     )
       1071 if copy:
       1072     if _is_numpy_namespace(xp):
       1073         # only make a copy if `array` and `array_orig` may share memory`
    

    File ~\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\validation.py:108, in _assert_all_finite(X, allow_nan, msg_dtype, estimator_name, input_name)
        106 if not is_array_api and X.dtype == np.dtype("object") and not allow_nan:
        107     if _object_dtype_isnan(X).any():
    --> 108         raise ValueError("Input contains NaN")
        110 # We need only consider float arrays, hence can early return for all else.
        111 if not xp.isdtype(X.dtype, ("real floating", "complex floating")):
    

    ValueError: Input contains NaN



```python
# Fill missing values in the 'age_group' column by re-binning the 'age' column
df['age_group'] = pd.cut(df['age'], bins=[0, 20, 30, 40, 50, 100], labels=['Teen', 'Young Adult', 'Adult', 'Middle Aged', 'Senior'])

# Verify missing values again
print(df.isnull().sum())



```

    age                                  0
    click                                0
    gender_Male                          0
    gender_Non-Binary                    0
    device_type_Mobile                   0
    device_type_Tablet                   0
    ad_position_Side                     0
    ad_position_Top                      0
    browsing_history_Entertainment       0
    browsing_history_News                0
    browsing_history_Shopping            0
    browsing_history_Social Media        0
    time_of_day_Evening                  0
    time_of_day_Morning                  0
    time_of_day_Night                    0
    device_time_interaction              0
    ad_browsing_interaction              0
    age_group                         3686
    dtype: int64
    


```python
# Drop the 'age_group' column
df.drop('age_group', axis=1, inplace=True)

# Verify that the column is dropped
print(df.columns)

```

    Index(['age', 'click', 'gender_Male', 'gender_Non-Binary',
           'device_type_Mobile', 'device_type_Tablet', 'ad_position_Side',
           'ad_position_Top', 'browsing_history_Entertainment',
           'browsing_history_News', 'browsing_history_Shopping',
           'browsing_history_Social Media', 'time_of_day_Evening',
           'time_of_day_Morning', 'time_of_day_Night', 'device_time_interaction',
           'ad_browsing_interaction'],
          dtype='object')
    


```python
# Drop the interaction columns that contain strings
df.drop(['device_time_interaction', 'ad_browsing_interaction'], axis=1, inplace=True)



from imblearn.over_sampling import SMOTE

# Define features and target
X = df.drop('click', axis=1)
y = df['click']

# Initialize SMOTE and resample
smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X, y)

# Check class distribution after SMOTE
print(pd.Series(y_res).value_counts())

```

    click
    1    2735
    0    2735
    Name: count, dtype: int64
    


```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Initialize and train logistic regression model
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_res, y_res)

# Predict on test data
y_log_pred = log_model.predict(X_test)

# Evaluate the model
print(f"Logistic Regression Accuracy: {accuracy_score(y_test, y_log_pred)}")
print(classification_report(y_test, y_log_pred))

```

    Logistic Regression Accuracy: 0.5634236453201971
                  precision    recall  f1-score   support
    
               0       0.56      0.55      0.55       801
               1       0.57      0.57      0.57       823
    
        accuracy                           0.56      1624
       macro avg       0.56      0.56      0.56      1624
    weighted avg       0.56      0.56      0.56      1624
    
    


```python
from sklearn.ensemble import RandomForestClassifier

# Initialize and train Random Forest
rf_model = RandomForestClassifier()
rf_model.fit(X_res, y_res)

# Predict on test data
y_rf_pred = rf_model.predict(X_test)
print(f"Random Forest Accuracy: {accuracy_score(y_test, y_rf_pred)}")

```

    Random Forest Accuracy: 0.8300492610837439
    


```python
from xgboost import XGBClassifier
from sklearn.model_selection import RandomizedSearchCV

# Define parameter grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 6, 10],
    'learning_rate': [0.001, 0.01, 0.1],
    'subsample': [0.6, 0.8, 1.0],
    'colsample_bytree': [0.6, 0.8, 1.0]
}

# Initialize XGBoost model
xgb_model = XGBClassifier()

# Randomized search
random_search = RandomizedSearchCV(xgb_model, param_grid, n_iter=10, scoring='accuracy', cv=5, random_state=42, n_jobs=-1)
random_search.fit(X_res, y_res)

# Best parameters
print(f"Best parameters: {random_search.best_params_}")

# Predict using the best model
y_xgb_pred = random_search.best_estimator_.predict(X_test)
print(f"Optimized XGBoost Accuracy: {accuracy_score(y_test, y_xgb_pred)}")

```

    Best parameters: {'subsample': 1.0, 'n_estimators': 200, 'max_depth': 6, 'learning_rate': 0.1, 'colsample_bytree': 0.8}
    Optimized XGBoost Accuracy: 0.7561576354679803
    


```python
import matplotlib.pyplot as plt
import seaborn as sns

# Class distribution before SMOTE
plt.figure(figsize=(6,4))
sns.countplot(x=df['click'])
plt.title("Class Distribution Before SMOTE")
plt.show()

# Class distribution after SMOTE
plt.figure(figsize=(6,4))
sns.countplot(x=y_res)
plt.title("Class Distribution After SMOTE")
plt.show()

```


    

    



    

    



```python
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Predictions for logistic regression
y_log_pred = log_model.predict(X_test)

# Calculate metrics for logistic regression
log_accuracy = accuracy_score(y_test, y_log_pred)
log_precision = precision_score(y_test, y_log_pred)
log_recall = recall_score(y_test, y_log_pred)

print(f"Logistic Regression - Accuracy: {log_accuracy}, Precision: {log_precision}, Recall: {log_recall}")



# Predictions for random forest
y_rf_pred = rf_model.predict(X_test)

# Calculate metrics for random forest
rf_accuracy = accuracy_score(y_test, y_rf_pred)
rf_precision = precision_score(y_test, y_rf_pred)
rf_recall = recall_score(y_test, y_rf_pred)

print(f"Random Forest - Accuracy: {rf_accuracy}, Precision: {rf_precision}, Recall: {rf_recall}")



# Predictions for XGBoost
y_xgb_pred = random_search.best_estimator_.predict(X_test)

# Calculate metrics for XGBoost
xgb_accuracy = accuracy_score(y_test, y_xgb_pred)
xgb_precision = precision_score(y_test, y_xgb_pred)
xgb_recall = recall_score(y_test, y_xgb_pred)

print(f"XGBoost - Accuracy: {xgb_accuracy}, Precision: {xgb_precision}, Recall: {xgb_recall}")




# Define the metrics for each model
model_names = ['Logistic Regression', 'Random Forest', 'XGBoost']
accuracies = [log_accuracy, rf_accuracy, xgb_accuracy]
precisions = [log_precision, rf_precision, xgb_precision]
recalls = [log_recall, rf_recall, xgb_recall]

# Plot accuracy comparison
plt.figure(figsize=(8, 6))
plt.bar(model_names, accuracies, color='skyblue')
plt.title('Model Accuracy Comparison')
plt.ylabel('Accuracy')
plt.show()

# Plot precision comparison
plt.figure(figsize=(8, 6))
plt.bar(model_names, precisions, color='lightgreen')
plt.title('Model Precision Comparison')
plt.ylabel('Precision')
plt.show()

# Plot recall comparison
plt.figure(figsize=(8, 6))
plt.bar(model_names, recalls, color='salmon')
plt.title('Model Recall Comparison')
plt.ylabel('Recall')
plt.show()




```

    Logistic Regression - Accuracy: 0.5634236453201971, Precision: 0.5685096153846154, Recall: 0.574726609963548
    Random Forest - Accuracy: 0.8300492610837439, Precision: 0.8132875143184422, Recall: 0.8626974483596598
    XGBoost - Accuracy: 0.7561576354679803, Precision: 0.7217030114226376, Recall: 0.8444714459295262
    


    

    




    



    

    



```python
from sklearn.metrics import plot_confusion_matrix

# Assuming you have the models already trained and tested
plt.figure(figsize=(8, 6))
plot_confusion_matrix(log_model, X_test, y_test)
plt.title('Confusion Matrix for Logistic Regression')
plt.show()

plt.figure(figsize=(8, 6))
plot_confusion_matrix(rf_model, X_test, y_test)
plt.title('Confusion Matrix for Random Forest')
plt.show()

plt.figure(figsize=(8, 6))
plot_confusion_matrix(random_search.best_estimator_, X_test, y_test)
plt.title('Confusion Matrix for XGBoost')
plt.show()

```


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    Cell In[47], line 1
    ----> 1 from sklearn.metrics import plot_confusion_matrix
          3 # Assuming you have the models already trained and tested
          4 plt.figure(figsize=(8, 6))
    

    ImportError: cannot import name 'plot_confusion_matrix' from 'sklearn.metrics' (C:\Users\swapn\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\__init__.py)



```python
from sklearn.metrics import ConfusionMatrixDisplay

# Logistic Regression
plt.figure(figsize=(8, 6))
ConfusionMatrixDisplay.from_estimator(log_model, X_test, y_test)
plt.title('Confusion Matrix for Logistic Regression')
plt.show()

# Random Forest
plt.figure(figsize=(8, 6))
ConfusionMatrixDisplay.from_estimator(rf_model, X_test, y_test)
plt.title('Confusion Matrix for Random Forest')
plt.show()

# XGBoost
plt.figure(figsize=(8, 6))
ConfusionMatrixDisplay.from_estimator(random_search.best_estimator_, X_test, y_test)
plt.title('Confusion Matrix for XGBoost')
plt.show()

```


    <Figure size 800x600 with 0 Axes>



    

    



    <Figure size 800x600 with 0 Axes>



    

    



    <Figure size 800x600 with 0 Axes>



    

    



```python
from sklearn.metrics import roc_curve, auc

# For Logistic Regression
log_fpr, log_tpr, _ = roc_curve(y_test, log_model.predict_proba(X_test)[:,1])
log_auc = auc(log_fpr, log_tpr)

# For Random Forest
rf_fpr, rf_tpr, _ = roc_curve(y_test, rf_model.predict_proba(X_test)[:,1])
rf_auc = auc(rf_fpr, rf_tpr)

# For XGBoost
xgb_fpr, xgb_tpr, _ = roc_curve(y_test, random_search.best_estimator_.predict_proba(X_test)[:,1])
xgb_auc = auc(xgb_fpr, xgb_tpr)

# Plot ROC curve
plt.figure(figsize=(8,6))
plt.plot(log_fpr, log_tpr, label=f'Logistic Regression (AUC = {log_auc:.2f})')
plt.plot(rf_fpr, rf_tpr, label=f'Random Forest (AUC = {rf_auc:.2f})')
plt.plot(xgb_fpr, xgb_tpr, label=f'XGBoost (AUC = {xgb_auc:.2f})')
plt.plot([0, 1], [0, 1], 'k--')  # Diagonal line
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()

```


    

    



```python

```
