# Load california housing data, split intro train and test, fit linear regression, and measure R-squared

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

housing = fetch_california_housing()

x_train, x_test, y_train, y_test = train_test_split(housing.data, 
                                                    housing.target, 
                                                    train_size = 0.6, 
                                                    random_state=314)

reg = LinearRegression().fit(x_train, y_train)

y_test_pred = reg.predict(x_test)

r2 = r2_score(y_test, y_test_pred)
print('R-squared:', r2)