# Code Citations

## License: unknown
https://github.com/josephsolway/GeneralAssembly/blob/b3acb1b331fe94aee46fa7dabc102c91ba76d52a/lab04.ipynb

```
Now I have the cell IDs. I'll fix both affected cells — remove `fetch_openml` from imports and replace the load cell with a direct CSV read:
<!-- filepath: /Users/adhyapak/ai-machine-learning-codes/notebooks/115_real_world_project/real_world_project_starter.ipynb -->
<VSCode.Cell id="#VSC-ccd3285e" language="python">
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA

# Classifiers (topics 01-07, 24)
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

# Evaluation (topics 29, 63, 108)
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    roc_auc_score, roc_curve, ConfusionMatrixDisplay
)

# Class imbalance (topic 28)
from imblearn.over_sampling import SMOTE

print('All imports successful!')
</VSCode.Cell>

<VSCode.Cell id="#VSC-eb4d066e" language="python">
# Load UCI Heart Disease (Cleveland subset) directly — no external API required
COLS = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
        'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']

URL = ('https://archive.ics.uci.edu
```


## License: unknown
https://github.com/josephsolway/GeneralAssembly/blob/b3acb1b331fe94aee46fa7dabc102c91ba76d52a/lab04.ipynb

```
Now I have the cell IDs. I'll fix both affected cells — remove `fetch_openml` from imports and replace the load cell with a direct CSV read:
<!-- filepath: /Users/adhyapak/ai-machine-learning-codes/notebooks/115_real_world_project/real_world_project_starter.ipynb -->
<VSCode.Cell id="#VSC-ccd3285e" language="python">
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA

# Classifiers (topics 01-07, 24)
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

# Evaluation (topics 29, 63, 108)
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    roc_auc_score, roc_curve, ConfusionMatrixDisplay
)

# Class imbalance (topic 28)
from imblearn.over_sampling import SMOTE

print('All imports successful!')
</VSCode.Cell>

<VSCode.Cell id="#VSC-eb4d066e" language="python">
# Load UCI Heart Disease (Cleveland subset) directly — no external API required
COLS = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
        'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']

URL = ('https://archive.ics.uci.edu
```


## License: unknown
https://github.com/josephsolway/GeneralAssembly/blob/b3acb1b331fe94aee46fa7dabc102c91ba76d52a/lab04.ipynb

```
Now I have the cell IDs. I'll fix both affected cells — remove `fetch_openml` from imports and replace the load cell with a direct CSV read:
<!-- filepath: /Users/adhyapak/ai-machine-learning-codes/notebooks/115_real_world_project/real_world_project_starter.ipynb -->
<VSCode.Cell id="#VSC-ccd3285e" language="python">
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA

# Classifiers (topics 01-07, 24)
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

# Evaluation (topics 29, 63, 108)
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    roc_auc_score, roc_curve, ConfusionMatrixDisplay
)

# Class imbalance (topic 28)
from imblearn.over_sampling import SMOTE

print('All imports successful!')
</VSCode.Cell>

<VSCode.Cell id="#VSC-eb4d066e" language="python">
# Load UCI Heart Disease (Cleveland subset) directly — no external API required
COLS = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
        'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']

URL = ('https://archive.ics.uci.edu
```


## License: unknown
https://github.com/josephsolway/GeneralAssembly/blob/b3acb1b331fe94aee46fa7dabc102c91ba76d52a/lab04.ipynb

```
Now I have the cell IDs. I'll fix both affected cells — remove `fetch_openml` from imports and replace the load cell with a direct CSV read:
<!-- filepath: /Users/adhyapak/ai-machine-learning-codes/notebooks/115_real_world_project/real_world_project_starter.ipynb -->
<VSCode.Cell id="#VSC-ccd3285e" language="python">
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA

# Classifiers (topics 01-07, 24)
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

# Evaluation (topics 29, 63, 108)
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    roc_auc_score, roc_curve, ConfusionMatrixDisplay
)

# Class imbalance (topic 28)
from imblearn.over_sampling import SMOTE

print('All imports successful!')
</VSCode.Cell>

<VSCode.Cell id="#VSC-eb4d066e" language="python">
# Load UCI Heart Disease (Cleveland subset) directly — no external API required
COLS = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
        'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']

URL = ('https://archive.ics.uci.edu
```


## License: unknown
https://github.com/josephsolway/GeneralAssembly/blob/b3acb1b331fe94aee46fa7dabc102c91ba76d52a/lab04.ipynb

```
Now I have the cell IDs. I'll fix both affected cells — remove `fetch_openml` from imports and replace the load cell with a direct CSV read:
<!-- filepath: /Users/adhyapak/ai-machine-learning-codes/notebooks/115_real_world_project/real_world_project_starter.ipynb -->
<VSCode.Cell id="#VSC-ccd3285e" language="python">
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA

# Classifiers (topics 01-07, 24)
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

# Evaluation (topics 29, 63, 108)
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    roc_auc_score, roc_curve, ConfusionMatrixDisplay
)

# Class imbalance (topic 28)
from imblearn.over_sampling import SMOTE

print('All imports successful!')
</VSCode.Cell>

<VSCode.Cell id="#VSC-eb4d066e" language="python">
# Load UCI Heart Disease (Cleveland subset) directly — no external API required
COLS = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
        'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']

URL = ('https://archive.ics.uci.edu
```


## License: unknown
https://github.com/josephsolway/GeneralAssembly/blob/b3acb1b331fe94aee46fa7dabc102c91ba76d52a/lab04.ipynb

```
Now I have the cell IDs. I'll fix both affected cells — remove `fetch_openml` from imports and replace the load cell with a direct CSV read:
<!-- filepath: /Users/adhyapak/ai-machine-learning-codes/notebooks/115_real_world_project/real_world_project_starter.ipynb -->
<VSCode.Cell id="#VSC-ccd3285e" language="python">
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA

# Classifiers (topics 01-07, 24)
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

# Evaluation (topics 29, 63, 108)
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    roc_auc_score, roc_curve, ConfusionMatrixDisplay
)

# Class imbalance (topic 28)
from imblearn.over_sampling import SMOTE

print('All imports successful!')
</VSCode.Cell>

<VSCode.Cell id="#VSC-eb4d066e" language="python">
# Load UCI Heart Disease (Cleveland subset) directly — no external API required
COLS = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
        'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']

URL = ('https://archive.ics.uci.edu
```


## License: unknown
https://github.com/josephsolway/GeneralAssembly/blob/b3acb1b331fe94aee46fa7dabc102c91ba76d52a/lab04.ipynb

```
Now I have the cell IDs. I'll fix both affected cells — remove `fetch_openml` from imports and replace the load cell with a direct CSV read:
<!-- filepath: /Users/adhyapak/ai-machine-learning-codes/notebooks/115_real_world_project/real_world_project_starter.ipynb -->
<VSCode.Cell id="#VSC-ccd3285e" language="python">
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA

# Classifiers (topics 01-07, 24)
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

# Evaluation (topics 29, 63, 108)
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    roc_auc_score, roc_curve, ConfusionMatrixDisplay
)

# Class imbalance (topic 28)
from imblearn.over_sampling import SMOTE

print('All imports successful!')
</VSCode.Cell>

<VSCode.Cell id="#VSC-eb4d066e" language="python">
# Load UCI Heart Disease (Cleveland subset) directly — no external API required
COLS = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
        'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']

URL = ('https://archive.ics.uci.edu
```


## License: unknown
https://github.com/josephsolway/GeneralAssembly/blob/b3acb1b331fe94aee46fa7dabc102c91ba76d52a/lab04.ipynb

```
Now I have the cell IDs. I'll fix both affected cells — remove `fetch_openml` from imports and replace the load cell with a direct CSV read:
<!-- filepath: /Users/adhyapak/ai-machine-learning-codes/notebooks/115_real_world_project/real_world_project_starter.ipynb -->
<VSCode.Cell id="#VSC-ccd3285e" language="python">
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA

# Classifiers (topics 01-07, 24)
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

# Evaluation (topics 29, 63, 108)
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    roc_auc_score, roc_curve, ConfusionMatrixDisplay
)

# Class imbalance (topic 28)
from imblearn.over_sampling import SMOTE

print('All imports successful!')
</VSCode.Cell>

<VSCode.Cell id="#VSC-eb4d066e" language="python">
# Load UCI Heart Disease (Cleveland subset) directly — no external API required
COLS = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
        'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']

URL = ('https://archive.ics.uci.edu
```


## License: unknown
https://github.com/josephsolway/GeneralAssembly/blob/b3acb1b331fe94aee46fa7dabc102c91ba76d52a/lab04.ipynb

```
Now I have the cell IDs. I'll fix both affected cells — remove `fetch_openml` from imports and replace the load cell with a direct CSV read:
<!-- filepath: /Users/adhyapak/ai-machine-learning-codes/notebooks/115_real_world_project/real_world_project_starter.ipynb -->
<VSCode.Cell id="#VSC-ccd3285e" language="python">
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA

# Classifiers (topics 01-07, 24)
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

# Evaluation (topics 29, 63, 108)
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    roc_auc_score, roc_curve, ConfusionMatrixDisplay
)

# Class imbalance (topic 28)
from imblearn.over_sampling import SMOTE

print('All imports successful!')
</VSCode.Cell>

<VSCode.Cell id="#VSC-eb4d066e" language="python">
# Load UCI Heart Disease (Cleveland subset) directly — no external API required
COLS = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
        'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']

URL = ('https://archive.ics.uci.edu
```

