from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score,roc_curve, auc
from sklearn import metrics
from sklearn.preprocessing import label_binarize
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.feature_selection import RFE

filename = 'fish.csv'
data = pd.read_csv(filename)
n_classes = 2

columns = ['having_IP_Address','URL_Length','Shortining_Service','having_At_Symbol','double_slash_redirecting','Prefix_Suffix','having_Sub_Domain','SSLfinal_State','Domain_registeration_length','Favicon','port','HTTPS_token','Request_URL','URL_of_Anchor','Links_in_tags','SFH','Submitting_to_email','Abnormal_URL','Redirect','on_mouseover','RightClick','popUpWidnow','Iframe','age_of_domain','DNSRecord','web_traffic','Page_Rank','Google_Index','Links_pointing_to_page','Statistical_report']
clf = svm.SVC(kernel = 'poly', probability=True)

X = pd.DataFrame(data, columns=columns)
y = data['label']

for i in range(1,31):
#estimator = SVR(kernel="linear")
    estimator = LinearSVC()
    selector = RFE(estimator, i , step=1)
    selector = selector.fit(X, y)
    #print(selector.support_)
    #print(selector.ranking_)
    mask = selector.get_support() #list of booleans
    new_features = [] # The list of your K best features

    for bool, feature in zip(mask, columns):
        if bool:
            new_features.append(feature)

    #print(new_features)

#columns = ['having_IP_Address','URL_Length','Shortining_Service','having_At_Symbol','double_slash_redirecting','Prefix_Suffix','having_Sub_Domain','SSLfinal_State','Domain_registeration_length','Favicon','port','HTTPS_token','Request_URL','URL_of_Anchor','Links_in_tags','SFH','Submitting_to_email','Abnormal_URL','Redirect','on_mouseover','RightClick','popUpWidnow','Iframe','age_of_domain','DNSRecord','web_traffic','Page_Rank','Google_Index','Links_pointing_to_page','Statistical_report']
#columns = ['having_IP_Address', 'URL_Length', 'Shortining_Service', 'having_At_Symbol', 'double_slash_redirecting', 'Prefix_Suffix', 'having_Sub_Domain', 'SSLfinal_State', 'Domain_registeration_length', 'Favicon', 'port', 'HTTPS_token', 'Request_URL', 'URL_of_Anchor', 'Links_in_tags', 'SFH', 'Submitting_to_email', 'Abnormal_URL', 'Redirect', 'on_mouseover', 'RightClick', 'popUpWidnow', 'Iframe', 'age_of_domain', 'DNSRecord', 'web_traffic', 'Page_Rank', 'Google_Index', 'Links_pointing_to_page', 'Statistical_report']
#clf = svm.SVC(kernel = 'poly', probability=True)

    X1 = pd.DataFrame(data, columns=new_features)
    #print("SVM Score for Features", i )
    #X = data.iloc[:,1:i]
    #print(X)
    #y = data['label']
    x_train_original,x_test_original,y_train_original,y_test_original=train_test_split(X1,y,test_size=0.25,random_state = 0)
    clf.fit(x_train_original,y_train_original)
    predictions=clf.predict(x_test_original)
    print("Accuracy Score =", accuracy_score(y_test_original, predictions))
    print("AUC Score =", roc_auc_score(y_test_original, predictions))
    #print(roc_auc_score(y_test_original, predictions))
    print(",")
