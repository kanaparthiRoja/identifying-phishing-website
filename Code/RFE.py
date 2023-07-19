from sklearn import svm
from sklearn.svm import SVR
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score,roc_curve, auc
from sklearn import metrics
from sklearn.preprocessing import label_binarize
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE

columns = ['having_IP_Address','URL_Length','Shortining_Service','having_At_Symbol','double_slash_redirecting','Prefix_Suffix','having_Sub_Domain','SSLfinal_State','Domain_registeration_length','Favicon','port','HTTPS_token','Request_URL','URL_of_Anchor','Links_in_tags','SFH','Submitting_to_email','Abnormal_URL','Redirect','on_mouseover','RightClick','popUpWidnow','Iframe','age_of_domain','DNSRecord','web_traffic','Page_Rank','Google_Index','Links_pointing_to_page','Statistical_report']

filename = 'fish.csv'
data = pd.read_csv(filename)
n_classes = 2
X = pd.DataFrame(data, columns=columns)
y = data['label']

#estimator = SVR(kernel="linear")
estimator = LinearSVC()
selector = RFE(estimator, 2, step=1)
selector = selector.fit(X, y)
print(selector.support_)
print(selector.ranking_)
mask = selector.get_support() #list of booleans
new_features = [] # The list of your K best features

for bool, feature in zip(mask, columns):
    if bool:
        new_features.append(feature)

print(new_features)
