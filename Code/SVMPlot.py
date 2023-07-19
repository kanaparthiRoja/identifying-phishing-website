import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
columns = ['having_IP_Address','URL_Length','Shortining_Service','having_At_Symbol','double_slash_redirecting','Prefix_Suffix','having_Sub_Domain','SSLfinal_State','Domain_registeration_length','Favicon','port','HTTPS_token','Request_URL','URL_of_Anchor','Links_in_tags','SFH','Submitting_to_email','Abnormal_URL','Redirect','on_mouseover','RightClick','popUpWidnow','Iframe','age_of_domain','DNSRecord','web_traffic','Page_Rank','Google_Index','Links_pointing_to_page','Statistical_report']
#objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(columns))
performance = [0.541236949956
,
0.5
,
0.5
,
0.5
,
0.5
,
0.619471947195
,
0.563306354655
,
0.882073843894
,
0.603570645295
,
0.5
,
0.5
,
0.5
,
0.630432002368
,
0.837631953748
,
0.603402590059
,
0.5
,
0.5
,
0.5
,
0.5
,
0.5
,
0.5
,
0.5
,
0.5
,
0.561781966828
,
0.5
,
0.595732031169
,
0.5
,
0.550602594287
,
0.5
,
0.530320758257]
 
plt.bar(y_pos, performance, align ='center', alpha=1)
plt.xticks(y_pos, columns)
plt.xticks(rotation='vertical')
plt.ylabel('AUC')
plt.title('SVM Based on Individual Features')
 
plt.show()